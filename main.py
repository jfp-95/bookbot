from stats import accept_text
from stats import num_of_chars

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    text = get_book_text("books/frankenstein.txt")
    accept_text(text)
    num_of_chars(text)




main()
