#!/bin/env python

def is_descending(values):
    flags = []
    for i in range(0, len(values)-1):
        if (values[i+1] < values[i]):
            if (values[i] - values[i+1] >= 1 and values[i] - values[i+1] <= 3):
                flags.append(True)
            else:
                flags.append(False)
        else:
            flags.append(False)
    
    for f in flags:
        if f == False:
            return False
        
    return True


def is_ascending(values):
    flags = []
    for i in range(0, len(values)-1):
        if (values[i+1] > values[i]):
            if (values[i+1] - values[i] >= 1 and values[i+1] - values[i] <= 3):
                flags.append(True)
            else:
                flags.append(False)
        else:
            flags.append(False)
    
    for f in flags:
        if f == False:
            return False
        
    return True


def is_safe(values):
    return (is_ascending(values) or is_descending(values))


def main():
    file = open("day2a-input.txt")

    safe_count = 0

    line = file.readline()
    while line != "":
        values = line.split(' ')
        num_values = []
        for v in values:
            num_values.append(int(v))

        #print(num_values)
        safe = is_safe(num_values)
        if (safe):
            safe_count += 1

        line = file.readline()

    print("Safe reports: ", safe_count)


if __name__ == "__main__":
    main()