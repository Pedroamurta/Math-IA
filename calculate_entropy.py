from generate_probability import word_feedback_probability
from math import fsum, log2

word_entropy = {}

for word in word_feedback_probability:
    probability_list = word_feedback_probability[word]
    entropy = -fsum(p * log2(p) for p in probability_list)
    word_entropy[word] = entropy

best_word = min(word_entropy, key = word_entropy.get)
print(best_word, word_entropy[best_word])