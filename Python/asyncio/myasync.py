""" ----- Implementation of asynchronous workflow using purely generators / iterator protocol -----

    The event loop 'run' takes a 'main' function (coroutine) as an entrypoint argument, and handles all 
    asynchronous operations. The asynchronous functions have to be generator objects, from which they
    inherit the functionality of temporarily returning (pausing) and saving their state crucial for 
    asynchronous operations. The functions can give signals (with 'yield' keyword) with specific commands 
    and arguments so that the event loop can understand what to do and handle accrodingly.
    
"""

from json import dumps
from copy import deepcopy

__all__ = [
    "event_loop",
]


#* Signal Command Handling functions
def await_time(**kwargs):
    #SPEC The keyword arguments supported are (time: int, )
    time = kwargs["time"]
    import time as t
    t.sleep(time)
    return None

def await_coroutine(**kwargs):
    #SPEC The keyword arguments supported are (target: function_object, )
    target = kwargs["target"]
    result = target()
    return result

def create_task(**kwargs):
    pass
    return None

def await_all_tasks(**kwargs):
    pass

def await_task(**kwargs):
    pass

def none(**kwargs):
    return None

#* Protocol dictionary contains all signals reference
protocol = {
    "await_time" : await_time,
    "await_coroutine": await_coroutine,
    "none": none,
    "create_task": create_task,
    "await_all_tasks": await_all,
    "await_task": await_task,
}

#* Task_queue used by the event loop
class task_queue:
    def __init__(self):
        pass
    def enqueue(self):
        pass
    def dequeue(self):
        pass
    

#* Custom event loop
class event_loop:
    f"""
        Signal SPEC --> tuple(<command>, dict(param1: arg1, param2, arg2, ...))
        Protocol SPEC --> 
        {dumps(protocol, sort_keys=True, indent=4)}
    """

    def run(main_generator):
        generator_sending_value = None
        while True:
            # Drive the generator
            try:
                yielded = main_generator.send(generator_sending_value)
                try:
            # Read the signal
                    command = yielded[0]
                    kwargs = dict(yielded[1])
                except ValueError as e:
                    raise ValueError("\nTHE EVENT LOOP CANNOT RECOGNIZE SUCH SYNTAX OF SIGNAL\n PLEASE OBEY THE 'SIGNAL SPEC'!")
            # Handle the signal
                if command in protocol:
                    try:
                        returned_value = protocol[command](**kwargs) # Calling the handling function
                        generator_sending_value = deepcopy(returned_value) # An arbitrary check just in case any bugs come
                    except Exception as e:
                        if command == "func":
                            print(f"======= ERROR : {kwargs['target']}() failed to run with the following exception")
                            print(Exception)
                        else:
                            raise Exception
                else:
                    raise Exception("\nTHIS COMMAND IS NOT IN THE PROTOCOL\n PLEASE OBEY THE 'PROTOCOL'!")
            # Until generator returns
            except StopIteration as e:
                return e.value

