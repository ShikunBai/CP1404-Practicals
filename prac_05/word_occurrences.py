"""
Word Occurrences
Estimate: 10 minutes
Actual:   40 minutes
"""
word_counts = {}
text = input("Text: ").strip()
words = text.split()

for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1
sorted_words = sorted(word_counts.keys())

word_length = max(len(word) for word in sorted_words)
for word in sorted_words:
    print(f"{word:{word_length}} : {word_counts[word]}")