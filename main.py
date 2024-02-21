def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    letters_dist = count_letters(text)
    letters_sorted = sort_letters(letters_dist)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in document")
    for item in letters_sorted:
        letter = item["letter"]
        count = item["count"]
        print(f"The '{letter}' character was found {count} times")
    print("--- End report ---")

# Helper functions
def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_words(text):
    return len(text.split())

def count_letters(text):
    letters = {}
    for s in text.lower():
        if not s in letters:
            letters[s] = 0
        letters[s] += 1
    return letters

def sort_on(dict):
    return dict["count"]

def sort_letters(dict):
    # reshape letters distribution into list of dictionaries
    list_of_dicts = []
    for key in dict:
        if key.isalpha():
            list_of_dicts.append({"letter": key, "count": dict[key]})
    list_of_dicts.sort(reverse=True, key = sort_on)
    return list_of_dicts

main()