def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()
    for ch in sorted(chars_dict, key=chars_dict.get, reverse=True):
        if ch.isalpha():
            print(f"The {ch} character was found {chars_dict[ch]} times.")
    
    print(f"--- End report ---")

#Converts each character to lowercase where applicable and returns the count of each    
def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

#Gets the word count
def get_num_words(text):
    words = text.split()
    return len(words)

#Find the book and parse the text
def get_book_text(path):
    with open(path) as f:
        return f.read() 
    
def sort_on(chars_dict):
    return chars_dict["num"]


main()