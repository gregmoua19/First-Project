from Reader import *
from tqdm import tqdm

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
#print(dictionary)
#print(incrementor)

types = ["1. Employment and earnings",
         "2. (a) Support linked to an MP but received by a local party organisation or indirectly via a central party organisation",
         "2. (b) Any other support not included in Category 2(a)",
         "3. Gifts, benefits and hospitality from UK sources", 
         "4. Visits outside the UK",
         "5. Gifts and benefits from sources outside the UK",
         "6. Land and property portfolio: (i) value over £100,000 and/or (ii) giving rental income of over £10,000 a year",
         "7. (i) Shareholdings: over 15% of issued share capital",
         "7. (ii) Other shareholdings, valued at more than £70,000",
         "8. Miscellaneous",
         "9. Family members employed and paid from parliamentary expenses",
         "10. Family members engaged in lobbying the public sector on behalf of a third party or client",
         "Nil"]


full_text = full
names = dictionary
col = len(names)+1
rows = len(types)+1
counter = 0
names_dict = {}
types_dict = {}
my_array = [[0 for j in range(col)] for i in range(rows)]
for i in range(1,rows):
    my_array[i][0] = types[counter]
    types_dict[types[counter]] = i
    counter+=1
#    print(my_array[i][0])
counter = 0
for j in range(1,col):
    my_array[0][j] = names[counter]
    names_dict[names[counter]] = j
    counter+=1
#    print(my_array[0][j])

#for i in range(rows):
 #   for j in range(col):
  #      print(my_array[i][j], end=' ')
#    print()  # Add a newline after each row#
string_temp = ""
name_temp = ""
col_index = 0
row_index = 0
filename2 = "text.txt"
with open(filename2, "r") as file:
    for line in tqdm (file, desc="Loading..."):
        words = line.split()
        for i in words:
            name_temp += i
            string_temp += i
            name_temp = name_temp.replace("Mr","").replace("Dr", "").replace("Ms", "")
            if name_temp in names_dict:
                string_temp = ""   
                col_index = names_dict.get(name_temp)
            if string_temp in types_dict:
                row_index = types_dict.get(string_temp)
                string_temp = ""


                
            if string_temp not in types_dict:
                my_array[row_index][col_index] = string_temp    
#loop to read file
#if name found (key match name dict, grab value [will be index])
#move to that index [0][key.value()]
#read until next name is found or EOF
#before next name is found perform similar operation on inner text
#read through text until one of the types are found
#if found read all data until next number type is found
#repeat until end of file

