#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print("{}".format(0))
    elif len(sys.argv) == 2:
        print("{}".format(sys.argv[1]))
    else:
        sum = int(sys.argv[1])
        for i in range(2, len(sys.argv)):
            sum += int(sys.argv[i])
        print("{}".format(sum))
