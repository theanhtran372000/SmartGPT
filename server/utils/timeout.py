import func_timeout

def run_with_timeout(f, max_wait, default_value):
    try:
        return func_timeout.func_timeout(max_wait, f)
    except func_timeout.FunctionTimedOut:
        pass
    return default_value