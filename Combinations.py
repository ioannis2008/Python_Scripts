import itertools

def generate_combinations(s, filename):
    char_options = [(char.upper(), char.lower()) if char.isalpha() else (char,) for char in s]
    combinations = itertools.product(*char_options)
    with open(filename, 'w') as f:
        for combo in combinations:
            f.write(''.join(combo) + '\n')
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

    output_file = input("Enter output filename (default: combinations.txt): ") or "combinations.txt"
    
    if count > 1000000:
        print("Warning: The number of combinations is large, which may take a long time to compute.")
    
    generate_combinations(input_string, output_file)
    print(f"All combinations saved to {output_file}.")
