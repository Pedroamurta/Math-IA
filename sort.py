with open('words.txt', 'r') as text_file:
    words = []
    # this is to make sure two words on the same line don't get saved as one
    for line in text_file:
        listed_line = line.split()

        for word in listed_line:
            if word not in words:
                words.append(word)
            else:
                pass

    

words.sort()

with open('words.txt', 'w') as text_file:
    for word in words:
        text_file.writelines(f'{word.lower()}\n')



