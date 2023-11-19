path = "./books/frankenstein.txt"
with open(path) as f:
    file_contents = f.read()

words = file_contents.lower()
letter_count = {}
for letter in words:
    if not letter.isalpha():
        continue
    if letter in letter_count:
        letter_count[letter] += 1
    else:
        letter_count[letter] = 1

print(f"--- Begin report of {path} ---")
print(f"{len(words.split())} words found in the document")
sorted_letters = sorted(letter_count.items(), key = lambda x:x[1], reverse = True)
for item in sorted_letters:
    print(f"The '{item[0]}' character was found {item[1]} times")
print("--- End report ---")