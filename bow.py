
"""
Write a function that accepts a list of strings and performs Bag of words and convert it to numerical vectors.

"""


def bag_of_words(texts):
    # Creating a set of unique words from the texts
    vocabulary = set()
    for text in texts:
        for word in text.split():
            vocabulary.add(word)
    
    vocabulary = sorted(list(vocabulary))

    # Creating numerical vectors for each text
    vectors = []
    for text in texts:
        vector = [0] * len(vocabulary)
        words = text.split()
        for word in words:
            if word in vocabulary:
                index = vocabulary.index(word)
                vector[index] += 1
        vectors.append(vector)
    
    return vectors, vocabulary

# Example usage:
texts = ["apple apple orange fruit", "banana apple fruit", "banana orange"]
vectors, vocabulary = bag_of_words(texts)

for i, text in enumerate(texts):
    print(f"'{text}' is represented as {vectors[i]} using the vocabulary {vocabulary}")
