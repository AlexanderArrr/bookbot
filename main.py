def main():
    dict_count = {}
    li_count = []
    
    print("--- Begin report of books/frankenstein.txt ---")
    text = get_book_text("books/frankenstein.txt")
    count = get_words_count(text)
    dict_count = get_characters_count(text)
    li_count = conv_charcount_to_list(dict_count)
    li_count.sort(reverse=True, key=sort_on)
    print_char_report(li_count)
 

def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_words_count(text):
    words = text.split()
    print(f"{len(words)} words found in the document\n")


def get_characters_count(text):
    chars = {}
    for char in text:
        if char.isalpha():
            char = char.lower()
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1       
    return chars


def conv_charcount_to_list(dict):
    li_dicts = []
    for k in dict:
        fresh_dict = {}
        fresh_dict["char"] = k
        fresh_dict["num"] = dict[k]
        li_dicts.append(fresh_dict)
    return li_dicts


def sort_on(dict):
    return dict["num"]


def print_char_report(list):
    for di in list:
        print(f"The '{di['char']}' character was found {di['num']} times")


main()