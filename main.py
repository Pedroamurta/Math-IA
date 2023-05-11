number_of_occurences = [
    {},
    {},
    {},
    {},
    {}
]

words = []

with open("valid_guesses.txt", "r") as words_text:
    words = words_text.read().split("\n")

for w in words:
    for i in range(0, 5):
        try:
            number_of_occurences[i][w[i].lower()] += 1
        except:
            number_of_occurences[i][w[i].lower()] = 1

print("\n\n")
for i in number_of_occurences:
    print(i, end= "\n\n\n\n")
