#!/usr/bin/python3
for dig in range(10):
    for ldig in range(dig+1, 10):
        print("{}{}".format(dig, ldig), end="")
        if dig == 8 and ldig == 9:
            continue
        print(", ", end="")
print()
