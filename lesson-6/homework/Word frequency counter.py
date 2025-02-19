import os
import string
from collections import Counter

def create_sample_file():
    text = input("Enter a paragraph : ")
    with open("sample.txt", "w") as file:
        file.write(text)

def read_file():
    if not os.path.exists("sample.txt"):
        print("'sample.txt' not found. Creating a new file.")
        create_sample_file()
    with open("sample.txt", "r") as file:
        return file.read()

def count_word_frequency(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    word_count = Counter(words)
    return word_count

def save_report(word_count, total_words):
    with open("word_count_report.txt", "w") as file:
        file.write("Word Count Report\n")
        file.write(f"Total Words: {total_words}\n")
        file.write("Top 5 Words:\n")
        for word, count in word_count.most_common(5):
            file.write(f"{word} - {count}\n")

def main():
    text = read_file()
    word_count = count_word_frequency(text)
    total_words = sum(word_count.values())
    print(f"Total words: {total_words}")
    print("Top 5 most common words:")
    for word, count in word_count.most_common(5):
        print(f"{word} - {count} times")
    save_report(word_count, total_words)
    print("Word count report saved to 'word_count_report.txt'")

if __name__ == "__main__":
    main()
