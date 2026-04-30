import random

def create_pairs(texts, labels):
    pairs = []
    pair_labels = []

    for i in range(len(texts)):
        j = random.randint(0, len(texts)-1)

        pairs.append((texts[i], texts[j]))
        pair_labels.append(int(labels[i] == labels[j]))

    return pairs, pair_labels
