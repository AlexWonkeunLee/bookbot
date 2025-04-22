import sys
from stats import wordCount
from stats import characterCount
from stats import sortedList

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def printReport(listDict, path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {wordCount(get_book_text(path))} total words")
    print("--------- Character Count -------")
    for entry in listDict:
        print(f"{entry["alpha"]}:", entry["count"])
    print("============= END ===============")
    

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_book = sys.argv[1]
    printReport(sortedList(characterCount(get_book_text(path_to_book))), path_to_book)


main()



