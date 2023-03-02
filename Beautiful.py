filename = "names.txt"  # replace with the name of your file
dictionary = []
incrementor = 0
with open(filename, "r") as file:
    for line in file:
        words = line.split()
        if len(words) > 4 and not words[0] == "MP" and not words[0] == "MPs":
            dictionary.append(words[1] + ", " + words[0])
            incrementor+=1

#print(dictionary)
#print(incrementor)