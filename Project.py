from tqdm import tqdm
import re
filename = "names.txt"  # replace with the name of your file
dictionary = []
incrementor = 0
filetext = ""
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


#full_text = filetext
full_text = "Abbott, Ms Diane (Hackney North and Stoke Newington)  3. Gifts, benefits and hospitality from UK sources  Name of donor: The Premier League  Address of donor: Brunel Building, 57 North Wharf Road, London W2 1HQ  Amount of donation or nature and value if donation in kind: Two box tickets with hospitality for Arsenal v Everton, value \u00a3500  Date received: 22 May 2022  Date accepted: 22 May 2022  Donor  status: company, registration 02719699  (Registered 14 June 2022)  4. Visits outside the UK  Name of donor: PNP Women\u2019s Movement  Address of donor: 89 Old Hope Road, St. Andrew, Jamaica  Estimate of the probable value (or amount of any donation): Flights \u00a31,73 7.81, accommodation \u00a3802.01 and use of the airport Lounge \u00a334.75, total value \u00a32,574.57  Destination of visit: Kingston, Jamaica  Dates of visit: 7 -12 July 2022  Purpose of visit: Guest speaker at the PNP Women\u2019s Movement\u2019s 48th Annual Conference.  (Registered  05 September 2022)  8. Miscellaneous  Since December 2015, a trustee of the Diane Abbott Foundation, which works to excel and improve education. (Registered 26 October 2016)   Abrahams, Debbie (Oldham East and Saddleworth)  Nil   Adams, Nigel (Selby and Ainsty)  4. Visits outside the UK  Name of donor: Jamaica Tourist Board  Address of donor: 1 -2 Prince Consort Rd, London SW7 2BZ  Estimate of the probable value (or amount of any donation): Air travel and 2 accommodation for me and a family member, value \u00a33,950  Destination of visit: Kingston and St Elizabeth Parish, Jamaica  Dates of visit: 1 -8 August 2022  Purpose of visit: Lords and Commons Cricket delegation for the 60th Anniversary of Jamaican Independence, including UK High Commission event with ministers and parliamentarians and presenting a donation to the BREDS Cricket Academy.  (Registered 31 August 2022)  Name of donor: Embassy of the State of Qatar  Address of donor: 1 South Audley Street, London W1K 1NB  Estimate of the probable value (or amount of any donat ion): Flights, accommodation and match tickets for the FIFA World Cup, value \u00a32,880  Destination of visit: Doha, Qatar  Dates of visit: 29 November - 1 December 2022  Purpose of visit: Part of a parliamentary delegation attending the World Cup and to attend a  dinner with UK and Welsh Government Ministers hosted by the British Embassy to mark the participation of England and Wales in the tournament.  (Registered 23 December 2022)  6. Land and property portfolio: (i) value over \u00a3100,000 and/or (ii) giving rental i ncome of over \u00a310,000 a year  One mixed use commercial and residential property in Selby, North Yorkshire, co -owned with my wife: (i) and (ii).  Three residential properties in York co -owned with my wife, the second of which was acquired in September 2017, a nd the third on 1 October 2021: (i) and (ii). (Registered 13 May 2015; updated 10 October 2017 and 02 November 2021)  From 18 March 2016, one residential property in Leeds co -owned with my wife: (i) and from 10 May 2016 (ii). (Registered 18 March 2016; upda ted 10 May 2016)  9. Family members employed and paid from parliamentary expenses  I employ my spouse, Claire Adams, as part -time Office Manager."
full_text = re.sub('\s+', ' ', full_text).strip()
#print(full_text)
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
#with open(filename2, "r") as file:
#    for line in tqdm (file, desc="Loading..."):
        
#        words = line.split()
#print(names_dict)
#print(types_dict)
words = full_text.split()
name_temp = ''
string_temp = ''
for i in words:
    i = i.replace("Mr","").replace("Dr", "").replace("Ms", "")
    if i != "":
        name_temp += i + " "
        string_temp += i + " "
    if name_temp.strip() in names_dict:
        print("changing col")
        print(names_dict.get(name_temp))
        col_index = names_dict.get(name_temp)
        string_temp = ""
        name_temp = ""   
    if string_temp.strip() in types_dict:
        print("changing row")
        row_index = types_dict.get(string_temp)
        string_temp = ""
        name_temp = ""   
    my_array[row_index][col_index] = i 
#print(my_array)
#print(name_temp)
#loop to read file
#if name found (key match name dict, grab value [will be index])
#move to that index [0][key.value()]
#read until next name is found or EOF
#before next name is found perform similar operation on inner text
#read through text until one of the types are found
#if found read all data until next number type is found
#repeat until end of file

