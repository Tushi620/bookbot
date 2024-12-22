def read_file():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents
    
def count_words(text):
    words = text.split()
    count = len(words)
    return count

book_text = read_file()
word_count = count_words(book_text)
print(word_count)

def count_char(text):
    lowered_string = text.lower()
    char_count = {}
    for char in lowered_string:
        if char in char_count:
            char_count[char] += 1
        else: 
            char_count[char] = 1
    return char_count

character_count = count_char(book_text)
print(character_count)

def sort_on(char_count):
    return char_count["num"]

char_counts = [{"char": char, "num": count} for char, count in character_count.items() if char.isalpha()]

char_counts.sort(reverse=True, key=sort_on)

print("--- Begin report of books/frankenstein.txt ---")
print(f"{word_count} words found in the document\n")

for item in char_counts:
    print(f"The '{item['char']}' character was found {item['num']} times")

print("--- End report ---")


