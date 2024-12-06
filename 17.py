# Write a program to count the words "to" and "the" present in the text file python.txt

def count_words(filename, words_to_count):
    """Counts occurrences of specific words in a text file.

    Args:
        filename: The name of the file to process.
        words_to_count: A list of words to count.

    Returns:
        A dictionary containing the count of each word.
    """

    word_counts = {}
    with open(filename, 'r') as file:
        for line in file:
            for word in line.split():
                if word.lower() in words_to_count:
                    word_counts[word.lower()] = word_counts.get(word.lower(), 0) + 1

    return word_counts

filename = "python.txt"
words_to_count = ["to", "the"]
word_counts = count_words(filename, words_to_count)

print("Word counts:")
for word, count in word_counts.items():
    print(f"{word}: {count}")