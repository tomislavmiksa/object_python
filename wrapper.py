import time

def log_calls(func):
    def wrapper(*args, **kwargs):
        now = time.time()
        print("Calling function: {0}\n with: {1}\n and {2}".format(func.__name__, args, kwargs))
        return_value = func(*args, **kwargs)
        print("Executed function {0} in {1}ms...".format(func.__name__, time.time() - now))
        return return_value
    return wrapper

def test1(a,b,c):
    print("\ttest1 function called")

def test2(a,b):
    print("\ttest2 function called")

def test3(a,b):
    print("\ttest3 function called")
    time.sleep(1)

test1 = log_calls(test1)
test2 = log_calls(test2)
test3 = log_calls(test3)
