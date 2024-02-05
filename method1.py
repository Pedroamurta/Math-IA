#most likely solution not using conditional pobability, not a real word
ideal_word = 'saaee' 

with open('valid_solutions.txt', 'r') as solutions_text:
    solutions = solutions_text.read().split('\n')

best_words = []
for word in solutions:
    #number of 0 - 5 that counts how much of the word is similar to the ideal word, 5 being the same word
    similarity_counter = 0
    for index in range(len(word)):
        if word[index] == ideal_word[index]:
            similarity_counter += 1
    if similarity_counter >= 3:
        best_words.append(word)

print(best_words)