from stats import get_word_count

def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()
    


def main():
    book_text = get_book_text("books/frankenstein.txt")
    count = get_word_count(book_text)
    print(f"{count} words found in the document")

main()