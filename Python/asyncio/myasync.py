"""Implementation of asynchronous workflow using purely generators / iterator protocol"""
import time

#* Protocol dict
protocol = {
    "wait" : "Timevalue"
}

#* Custom event loop
# Can only run a single generator rn
def run(gen_obj):
    while True:
        try:
            yielded = next(gen_obj)
            if yielded[0] == "wait":
                time.sleep(yielded[1])
            elif yielded[0] == "function":
                yielded[1]()
        except StopIteration as e:
            return e.value
