#!/usr/bin/env python3

# Created by Donggeun Lim
# Created on December 2020
# This is for loop program

def main():
    loop_counter = 0
    sum = 0

    positive_string = input("Enter the positive integer: ")
    print("")
    try:
        positive_number = int(positive_string)
        if positive_number > 0:

            for loop_counter in range(positive_number + 1):
                sum = loop_counter**2
                print("{}²={}".format(loop_counter, sum))
        else:
            print("This is negative number")
    except Exception:
        print("This was not an integer")


if __name__ == "__main__":
    main()
