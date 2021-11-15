def main():
    with open('input.txt', 'r') as f:
        for line in f:
            numbers = list(map(int, line.split()))
            print('   '.join(map(str, numbers)))
            print('min =', min(numbers))


if __name__ == '__main__':

    main()