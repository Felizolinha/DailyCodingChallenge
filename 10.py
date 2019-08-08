import time

def schedule(f, n):
    time.sleep(n/1000)
    f()

def test():
    print("Yay")

schedule(test, 5000)