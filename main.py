
from stats import get_word_count, get_char_count, sort_char_count

def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()
    
def print_word_count(count):
    print("----------- Word Count ----------")
    print(f"Found {count} total words")

def print_char_count(char_count):
    print("--------- Character Count -------")
    for entry in char_count:
        if entry["char"].isalpha():
            print(f"{entry["char"]}: {entry["num"]}")

def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")

    book_text = get_book_text("books/frankenstein.txt")
    wordcount = get_word_count(book_text)

    print_word_count(wordcount)

    char_count = get_char_count(book_text)
    char_count_sorted = sort_char_count(char_count)

    print_char_count(char_count_sorted)

    print("============= END ===============")

main()