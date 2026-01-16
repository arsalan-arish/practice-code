import myasync
#? import asyncio

def test():
    print("-- Currently Inside function 'test'")

def main():
    print("Starting async function main()")
    # Make the function wait for some time
    yield ("wait", 3)
    print("Successfully tested 'wait'")
    yield ("function", test)
    print("Successfully tested 'function'")
    print("Ending async function main()")
    return 0 # Success

print(myasync.run(main()))

