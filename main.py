
number_of_occurs = [
    {},
    {},
    {},
    {},
    {}
]

words = []

with open("words.txt", "r") as words_text:
    words = words_text.read().split("\n")

for w in words:
    for i in range(0, 5):
        try:
            number_of_occurs[i][w[i].lower()] += 1
        except:
            number_of_occurs[i][w[i].lower()] = 1

for i in number_of_occurs:
    print(i, end= "\n\n\n\n")
