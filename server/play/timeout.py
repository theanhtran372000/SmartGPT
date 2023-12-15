import func_timeout
 
 
def largeFunction():
    while True: pass
    return 'PythonPool.com'
 
 
def runFunction(f, max_wait, default_value):
    try:
        return func_timeout.func_timeout(max_wait, f)
    except func_timeout.FunctionTimedOut:
        pass
    return default_value
 
x = runFunction(largeFunction, 5, 'Python')
 
print(x)