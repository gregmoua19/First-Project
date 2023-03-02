import re

from tqdm import tqdm

off = " 3sa4sa0a8sa7qaw5esayau2isoai12yasdas4a6xscav0b7m9m5hsgad18s3l2w13r0tsy4uso9k8k7h0g5f6w2q18pp3ss2d4g6h07u9i5o16kajsg3dsa0ff5g4h9jak7l2k"

names = "1"

# Basically How this works is it seperates the String into a list of Strings whenever there is a "1"
#In our case "1" will be the name of the politicians
#After that we further seperate for each politician based off the Key Words.
#I decided to replace the String with something that I can manipulate easily.
#"8.Miscellaneious" = #@#8.Miscellaneious Dont ask me why
# The first index of every list will be '' or ' ' which was an issue so I have a hack to address it.
#Finally and most importantly I place the entire contents of the substring excluding the begining in the corresponding index
# For example "8.MiscellaneousSmexy pants" ->"#@#8Smexy Pants" -> "8Smexy Pants" ->"Smexy Pants"(Gets placed in the 8th element of the row)

def splitting(allWords,first_seperator):
    split_1 = re.split(first_seperator,allWords)
    place = 0
    xs = [None] * 11
    huff = []
    for sub in split_1:
        xs = [None] * 11
        # Here we will need to replace the "0" to "9" with the income types ex:8.Miscellanious
        l = sub.replace("0", "#@#0")
        l = l.replace("1", "#@#1")
        l = l.replace("2", "#@#2")
        l = l.replace("3", "#@#3")
        l = l.replace("4", "#@#4")
        l = l.replace("5", "#@#5")
        l = l.replace("6", "#@#6")
        l = l.replace("7", "#@#7")
        l = l.replace("8", "#@#8")
        l = l.replace("9", "#@#9")
        k = re.split("#@#",l)
        print(k)
        itr = 0
        for element_k in k:
    #This is the hack so we dont die
            if element_k == ' 'or element_k == '':
                element_k = "9aaaaa"
    #Fill an empty list with the values based on the first number and current row. then we append to a super list
                xs[int(element_k[0])] = element_k[1:]
            if(itr == len(k)-1):
                huff.append(xs)
            itr += 1
    return huff

for i in tqdm (range (1), desc="Loading..."):
    final_lst = splitting(off,names)
    final_lst

#What needs to be done:
#Update the replaces to include relavant strings
#Make the code work with politician names. I didnt know how we had the names so i didnt know how to proceed.¯\_(ツ)_/¯
#It should work after that