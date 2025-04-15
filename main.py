def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def accept_text(words):
    words_ls = words.split()
    word_count = len(words_ls)

    print(f'{word_count} words found in the document')

def main():
    text = get_book_text("books/frankenstein.txt")
    accept_text(text)




main()
