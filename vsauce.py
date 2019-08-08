import random
attemptResults = []

for _ in range(1000):
    eggs = random.sample(range(100), k=100)
    choosers = random.sample(range(100), k=100)

    hasFailedOnce = False
    for i in choosers:
        foundItself = False
        attempts = 1
        currentNumber = i
        while attempts < 50:
            if eggs[currentNumber] == i:
                foundItself = True
                break
            else:
                attempts += 1
                currentNumber = eggs[currentNumber]
        if not foundItself:
            hasFailedOnce = True
    attemptResults.append(hasFailedOnce)
print("Youtubers got demonetized in " + str(attemptResults.count(True)) + " out of 1000 attempts.")