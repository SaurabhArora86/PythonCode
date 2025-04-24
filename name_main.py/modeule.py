def my_func():
    print("I am running from module.py file")
    print(__name__)


if (__name__ == "__main__"):
    print("This is module.py file")
