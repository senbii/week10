from collections import Counter


def q1():
    with open('out.txt', 'w') as file:
        file.write('Hard work beats talent!')


def q2():
    fullName = input('What is your full name?: ')
    age = input('How old are you?: ')
    land = input('Where are you from?: ')
    midterm = input('What did you get on midterm exam?: ')
    with open('out.txt', 'w') as file:
        file.write(fullName)
        file.write(age)
        file.write(land)
        file.write(midterm)


def q3():
    file_name = 'random-numbers.txt'
    try:
        with open(file_name, 'r') as file:
            numbers = []
            for line in file:
                for j in line.split():
                    try:
                        numbers.append(float(j))
                    except ValueError:
                        continue

        if numbers:
            average = sum(numbers) / len(numbers)
            print(
                f'The average of the numbers in {file_name} is {average:.2f}')

            with open('out.txt', 'w') as outfile:
                outfile.write(f'{average:.2f}')
        else:
            print(f'No numbers found in {file_name}')

    except FileNotFoundError:
        print(f'File not found: {file_name}')


def q4():
    file_name = 'random-numbers.txt'
    try:
        with open(file_name, 'r') as file:
            numbers = []
            for line in file:
                for j in line.split():
                    try:
                        numbers.append(float(j))
                    except ValueError:
                        continue

        if numbers:
            print(
                f'The sum of the numbers in {file_name} is {sum(numbers):.0f}')

            with open('out.txt', 'w') as outfile:
                outfile.write(f'{sum(numbers):.0f}')
        else:
            print(f'No numbers found in {file_name}')

    except FileNotFoundError:
        print(f'File not found: {file_name}')


def q5():
    file_name = 'scenes.txt'
    try:
        with open(file_name, 'r') as file:
            count = 0
            for line in file:
                count += 1
            print(f'The number of lines in {file_name} is {count}')
    except FileNotFoundError:
        print(f'File not found: {file_name}')


def q6():
    file_name = 'names.txt'
    try:
        with open(file_name, 'r') as file:
            names = {}
            for line in file:
                for name in line.split():
                    names[name] = names.get(name, 0) + 1

            print(f'Names: {names}')
    except FileNotFoundError:
        print(f'File not found: {file_name}')


def q7():
    category_counts = Counter()

    with open("folder-hierarchy.txt", "r") as file:
        for line in file:
            parts = line.strip().split("/")
            if len(parts) > 2:
                category = parts[2]
                category_counts[category] += 1

        for category, count in category_counts.items():
            print(f"{category}: {count}")


def load_numbers(file_name):
    with open(file_name, "r") as file:
        return set(int(line.strip()) for line in file if line.strip().isdigit())


def q8():
    primes = load_numbers("primes.txt")
    happy_numbers = load_numbers("happy-numbers.txt")

    overlapping_numbers = primes & happy_numbers

    print("Overlapping numbers:")
    print(sorted(overlapping_numbers))
