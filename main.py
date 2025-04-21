from stats import num_words, char_count, char_sort
import sys
def get_book_text(filepath):
    with open(filepath) as book:
        text = book.read()
        return text

def print_results(book, text, char_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words(text)} total words")
    print("--------- Character Count -------")
    for i in char_list:
            if (i['character'].isalpha()):
                print(f"{i['character']}: {i["count"]}")
    print("============= END ===============")

def main():
    if len(sys.argv) < 2:
         print("Usage: python3 main.py <path_to_book>")
         sys.exit(1)
    book = sys.argv[1]
    text = get_book_text(book)
    char_list = (char_sort(char_count(text)))
    print_results(book, text, char_list)

main()