def get_feedbacks(word, solutions):
    feedbacks_list = []
    for solution in solutions:
        feedback = ""
        for i in range(len(word)):
            if word[i] == solution[i]:
                feedback += "G"
            elif word[i] != solution[i] and word[i] in solution:
                feedback += "Y"
            else:
                feedback += "B"
        feedbacks_list.append(feedback)
    return feedbacks_list


with open('valid_words.txt', 'r') as text_file:
    words = []
    # this is to make sure two words on the same line don't get saved as one
    for line in text_file:
        listed_line = line.split()

        for word in listed_line:
            if word not in words:
                words.append(word)
            else:
                pass

with open('valid_solutions.txt', 'r') as text_file:
    solutions = []
    # this is to make sure two words on the same line don't get saved as one
    for line in text_file:
        listed_line = line.split()

        for word in listed_line:
            if word not in solutions:
                solutions.append(word)
            else:
                pass

word_feedbacks = {}

for word in words:
    feedbacks = get_feedbacks(word, solutions)
    word_feedbacks[word] = feedbacks
