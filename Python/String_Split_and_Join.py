def split_and_join(line):
    line = line.split(" ")
    line1 = "-".join(line)
    return line1

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
