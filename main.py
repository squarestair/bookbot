from stats import get_num_words, get_char_count_lower, sort_dict
import sys


def get_books_text(filepath):
    with open(filepath) as f:
        # f is a file object
        file_contents = f.read()
    return file_contents


def sort_on(items):
    return items["num"]


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    bookpath = sys.argv[1]

    book = get_books_text(bookpath)
    charcount = get_char_count_lower(book)
    sorted_list = sort_dict(charcount)
    # print(sorted_list)
    print("============ BOOKBOT ============")
    print(F"Analyzing book found at {bookpath}...")
    print("----------- Word Count - ---------")
    print("Found", get_num_words(book), "total words")
    print("--------- Character Count - ------")

    for i in sorted_list:
        print(i["char"]+":", i["num"])
    print("============= END ===============")


main()
