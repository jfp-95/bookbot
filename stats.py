

def accept_text(words):
    words_ls = words.split()
    word_count = len(words_ls)

    print(f'Found {word_count} total words')

def num_of_chars(words):
    words = words.lower()
    char_counts = {}
    for char in words:
        if char in char_counts: 
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return char_counts

def sorted_list(char_dict):
    chars_list = []
    for char, count in char_dict.items():
        char_info = {
            "char": char,
            "count": count
        }
        chars_list.append(char_info)

    chars_list.sort(reverse=True, key=lambda d: d["count"])

    return chars_list

