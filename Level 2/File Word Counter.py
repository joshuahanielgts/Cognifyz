from collections import Counter

def word_counter(file_path):
    with open(file_path, 'r') as file:
        words = file.read().lower().split()
        counts = Counter(words)
    for word in sorted(counts):
        print(f"{word}: {counts[word]}")

# Example usage
word_counter('sample.txt')
