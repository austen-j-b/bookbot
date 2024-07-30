def main():
    book_contents = get_book("books/frankenstein.txt")
    print(count_words(book_contents))
    print(count_characters(book_contents))
    create_report(book_contents)

def count_words(text):
    words = text.split();
    return len(words)

def count_characters(text):
    text = text.lower()
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] +=1
        else:
            char_count[char] = 1
    return char_count

def get_book(location):
    with open(location) as book:
        return book.read()

def sort_on(dict):
    return dict["count"]

def create_report(book_content):
    word_count = count_words(book_content)
    character_count = count_characters(book_content)
    character_count_list = []
    for char in character_count:
        if char.isalpha():
            character_count_list.append({"character":char, "count":character_count[char]})
    character_count_list.sort(reverse=True, key=sort_on)
    print(character_count_list)
    print("--- Begin report ---")
    print(f"{word_count} words found in document")
    for char_count in character_count_list:
        char = char_count["character"]
        count = char_count["count"]
        print(f"{char} was found {count} times")
    print("--- End report ---")

main()
