import itertools
import string

def generate_wordlist(filename, min_length, max_length):
    chars = string.ascii_lowercase + string.digits
    with open(filename, 'w') as file:
        for length in range(min_length, max_length + 1):
            for combo in itertools.product(chars, repeat=length):
                file.write(''.join(combo) + '\n')
    print(f"Wordlist {filename} generated successfully.")

if __name__ == "__main__":
    filename = input("Enter wordlist filename: ")
    min_length = int(input("Enter minimum password length: "))
    max_length = int(input("Enter maximum password length: "))
    generate_wordlist(filename, min_length, max_length)
