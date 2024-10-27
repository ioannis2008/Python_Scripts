import itertools
def generate_combinations(s):
    char_options = [(char.upper(), char.lower()) if char.isalpha() else (char,) for char in s]
    combinations = itertools.product(*char_options)
    for combo in combinations:
        print(''.join(combo))
    return len(char_options)
def calculate_combinations_count(s):
    total_combinations = 1
    for char in s:
        if char.isalpha():
            total_combinations *= 2
        else:
            total_combinations *= 1
    return total_combinations
if __name__ == "__main__":
    input_string = input("Enter an alphanumerical string: ")
    count = calculate_combinations_count(input_string)
    print(f"Total combinations: {count}")
    generate_combinations(input_string)
