#https://galaiko.rocks/posts/2018-07-08/
def f(num):
    return 1 if int(num) <= 26 else 0

def count_possibilites(enc):
    length = len(enc)
    if length == 1:
        return 1
    elif length == 2:
        return f(enc) + 1
    else:
        return f(enc[:1]) * count_possibilites(enc[1:]) + f(enc[:2]) * count_possibilites(enc[2:])

testCase = '221282229182918928192912195211191212192819813'
print(count_possibilites(testCase))