
import sys

# Import functions from stats.py
from stats import accept_text, num_of_chars, sorted_list

#get book from filepath
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    text = get_book_text(path)
    print("=========BOOKBOT=========")
    print("---------Word Count------------")
    accept_text(text)
    print("---------Character Count-------------")
    char_counts = num_of_chars(text)
    sorted_chars = sorted_list(char_counts)
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["count"]

        if char.isalpha():
            print(f"{char}: {count}")


    print("=============END=============")

if __name__ == "__main__":
    main()

