def print_file():
    with open("numbers.txt", 'r', encoding='utf-8') as ofile:
        line = ofile.read()
        nums = line.replace('\n', '').split(',')
        for num in nums:
            print(num)


if __name__ == '__main__':
    print_file()