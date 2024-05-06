
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
    return(counted_letters)

def sort_on(dict):
    return dict["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def report(text):
    counted_letters = count_letters(text)
    counted_letters_list = []
    for letter in counted_letters:
        counted_letters_list.append({"char": letter, "num": counted_letters[letter]})
    
    counted_letters_list.sort(reverse=True, key=sort_on)

        
        
    return(counted_letters_list)

def main():
    book_path = "books/Frankenstein.txt"
    text = get_book_text(book_path)
    counted_words = count_words(text)
    counted_letters = count_letters(text)
    chars_sorted_list = report(text)
    report(text)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{count_words(text)} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")
    
    
    
    
    
    
    
    
    
main()