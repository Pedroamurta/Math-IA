from generate_probability import word_feedback_probability
from math import fsum, log2

word_entropy = {}

for word in word_feedback_probability:
    probability_list = word_feedback_probability[word]
    entropy = -fsum(p * log2(p) for p in probability_list)
    word_entropy[word] = entropy

best_words = sorted(word_entropy, key = word_entropy.get)[:5]
worst_words = sorted(word_entropy, key= word_entropy.get, reverse= True)[:5]
print(best_words)
for word in best_words:
    print(word, word_entropy[word])
print("\n\n")
for word in worst_words:
    print(word, word_entropy[word])
