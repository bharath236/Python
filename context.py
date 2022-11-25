#context manger allow us to properly manage resources when we working with certain objects

class ContextManager:
    def __init__(self):
        print("init method called")
    def __enter__(self):
        print("enter method called")
    def __exit__(self, exc_type, exc_val, exc_traceback):
        print("exit method called")

with ContextManager() as manager:
    print("with statement block")