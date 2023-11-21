def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    letter_count = get_letter_count(text)
    generate_book_report(book_path, word_count, letter_count)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    return len(words)

def get_letter_count(text):
    letter_count = {}
    for letter in text:
        lc_letter = letter.lower()
        if lc_letter in letter_count:
            letter_count[lc_letter] += 1
        else:
            letter_count[lc_letter] = 1
    return letter_count

def generate_book_report(path, word_count, letter_dict):
    print(f"-- Report for {path} --")
    print(f"{word_count} words found in the document")
    print()
    letter_list = list(letter_dict.keys())
    letter_list.sort()
    for letter in letter_list:
        if letter.isalpha():
            print(f"The '{letter}' character was found {letter_dict[letter]} times")
    print()
    print("-- END --")

main()
