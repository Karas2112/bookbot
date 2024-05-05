
def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents
        
def count_words(book):
    words = book.split()
    count = len(words)
    return count

def lower_letter(string):
    lower_letters = string.lower()
    return lower_letters

def count_letters(string):
    lowered_text = lower_letter(string)
    counted_letters = {"": 0}
    for letter in lowered_text:
        counted_letters[letter] = counted_letters.get(letter, 0) + 1
    print(counted_letters)


def main():
    book_path = "books/Frankenstein.txt"
    text = get_book_text(book_path)
    #print(text)
    print(count_words(text))
    count_letters(text)
    
    
    
main()