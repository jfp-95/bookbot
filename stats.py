

def accept_text(words):
    words_ls = words.split()
    word_count = len(words_ls)

    print(f'{word_count} words found in the document')

def num_of_chars(words):
    words = words.lower()
    char_counts = {}
    for char in text:
        if char in char_counts: 
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    print(char_counts)

