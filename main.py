number_of_occurences = [
    {},
    {},
    {},
    {},
    {}
]

words = []

with open("valid_solutions.txt", "r") as words_text:
    words = words_text.read().split("\n")

for w in words:
    for i in range(0, 5):
        try:
            number_of_occurences[i][w[i].lower()] += 1
        except:
            number_of_occurences[i][w[i].lower()] = 1

print("\n\n")
for dict in number_of_occurences:
    print(dict, end= "\n\n\n\n")