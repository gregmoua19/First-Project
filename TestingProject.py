import re
from tqdm import tqdm
import pandas as pd

filename = "names.txt"  # replace with the name of your file
names_list = [] 
with open(filename, "r") as file:
    for line in file:
        words = line.split()
        if len(words) > 4 and not words[0] == "MP" and not words[0] == "MPs":
            names_list.append(words[1] + ", " + words[0])
#print(names_list)
off = "Abbott, Ms Diane (Hackney North and Stoke Newington)  3. Gifts, benefits and hospitality from UK sources  Name of donor: The Premier League  Address of donor: Brunel Building, 57 North Wharf Road, London W2 1HQ  Amount of donation or nature and value if donation in kind: Two box tickets with hospitality for Arsenal v Everton, value \u00a3500  Date received: 22 May 2022  Date accepted: 22 May 2022  Donor  status: company, registration 02719699  (Registered 14 June 2022)  4. Visits outside the UK  Name of donor: PNP Women\u2019s Movement  Address of donor: 89 Old Hope Road, St. Andrew, Jamaica  Estimate of the probable value (or amount of any donation): Flights \u00a31,73 7.81, accommodation \u00a3802.01 and use of the airport Lounge \u00a334.75, total value \u00a32,574.57  Destination of visit: Kingston, Jamaica  Dates of visit: 7 -12 July 2022  Purpose of visit: Guest speaker at the PNP Women\u2019s Movement\u2019s 48th Annual Conference.  (Registered  05 September 2022)  8. Miscellaneous  Since December 2015, a trustee of the Diane Abbott Foundation, which works to excel and improve education. (Registered 26 October 2016)   Abrahams, Debbie (Oldham East and Saddleworth)  Nil   Adams, Nigel (Selby and Ainsty)  4. Visits outside the UK  Name of donor: Jamaica Tourist Board  Address of donor: 1 -2 Prince Consort Rd, London SW7 2BZ  Estimate of the probable value (or amount of any donation): Air travel and 2 accommodation for me and a family member, value \u00a33,950  Destination of visit: Kingston and St Elizabeth Parish, Jamaica  Dates of visit: 1 -8 August 2022  Purpose of visit: Lords and Commons Cricket delegation for the 60th Anniversary of Jamaican Independence, including UK High Commission event with ministers and parliamentarians and presenting a donation to the BREDS Cricket Academy.  (Registered 31 August 2022)  Name of donor: Embassy of the State of Qatar  Address of donor: 1 South Audley Street, London W1K 1NB  Estimate of the probable value (or amount of any donat ion): Flights, accommodation and match tickets for the FIFA World Cup, value \u00a32,880  Destination of visit: Doha, Qatar  Dates of visit: 29 November - 1 December 2022  Purpose of visit: Part of a parliamentary delegation attending the World Cup and to attend a  dinner with UK and Welsh Government Ministers hosted by the British Embassy to mark the participation of England and Wales in the tournament.  (Registered 23 December 2022)  6. Land and property portfolio: (i) value over \u00a3100,000 and/or (ii) giving rental i ncome of over \u00a310,000 a year  One mixed use commercial and residential property in Selby, North Yorkshire, co -owned with my wife: (i) and (ii).  Three residential properties in York co -owned with my wife, the second of which was acquired in September 2017, a nd the third on 1 October 2021: (i) and (ii). (Registered 13 May 2015; updated 10 October 2017 and 02 November 2021)  From 18 March 2016, one residential property in Leeds co -owned with my wife: (i) and from 10 May 2016 (ii). (Registered 18 March 2016; upda ted 10 May 2016)  9. Family members employed and paid from parliamentary expenses  I employ my spouse, Claire Adams, as part -time Office Manager.   "
#off1 = " 3sa4sa0a8sa7qaw5esayau2isoai1:named2yasdas4a6xscav0b7m9m5hsgad1:names8s3l2w1:nameh3r0tsy4uso9k8k7h0g5f6w2q1:namer8pp3ss2d4g6h07u9i5o1:namef6kajsg3dsa0ff5g4h9jak7l2k"
#labels = ["1:named","1:names","1:namer","1:namef","1:nameh","1:namet"]

# Basically How this works is it seperates the String into a list of Strings whenever there is a "1"
#In our case "1" will be the name of the politicians

#After that we further seperate for each politician based off the Key Words.
#I decided to replace the String with something that I can manipulate easily.
#"8.Miscellaneious" = #@#8.Miscellaneious Dont ask me why
# The first index of every list will be '' or ' ' which was an issue so I have a hack to address it. 

#Finally and most importantly I place the entire contents of the substring excluding the begining in the corresponding index
# For example "8.MiscellaneousSmexy pants" ->"#@#8Smexy Pants" -> "8Smexy Pants" ->"Smexy Pants"(Gets placed in the 8th element of the row)
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

def splitting(allWords,names_list):
    separator_regex = "|".join(re.escape(name) for name in names_list)
    split_1 = re.split(separator_regex,allWords)
    #print(split_1)
    huff = []
    for sub in split_1:
        
        # Here we will need to replace the "0" to "9" with the income types ex:8.Miscellanious
        l = sub.replace("1. Employment and earnings", "#@#0")
        l = l.replace("2. (a) Support linked to an MP but received by a local party organisation or indirectly via a central party organisation", "#@#1")
        l = l.replace("2. (b) Any other support not included in Category 2(a)", "#@#2")
        l = l.replace("3. Gifts, benefits and hospitality from UK sources", "#@#3")
        l = l.replace("4. Visits outside the UK", "#@#4")
        l = l.replace("5. Gifts and benefits from sources outside the UK", "#@#5")
        l = l.replace("6. Land and property portfolio: (i) value over £100,000 and/or (ii) giving rental income of over £10,000 a year", "#@#6")
        l = l.replace("7. (i) Shareholdings: over 15% of issued share capital", "#@#7")
        l = l.replace("7. (ii) Other shareholdings, valued at more than £70,000", "#@#8")
        l = l.replace("8. Miscellaneous", "#@#9")
        l = l.replace("9. Family members employed and paid from parliamentary expenses", "#@#10")
        l = l.replace("10. Family members engaged in lobbying the public sector on behalf of a third party or client", "#@#11")
        l = l.replace("Nil", "#@#12")
        k = re.split("#@#",l)
        print(k)
        itr = 0
        
        
        
        huff.append(organize(k,itr))
               
    return huff


def organize(lst,tick):
    xs = [None] * 1

    for element_k in lst:

    #This is the hack so we dont die
        if element_k == ' 'or  element_k == '':
            element_k = "9aaaaa"
        #print(element_k)

        #Fill an empty list with the values based on the first number and current row. then we append to a super list
        #xs[int(element_k[0])] = element_k[1:]

        if(tick == len(lst)-1):
            return xs
            #huff.append(xs)
        tick += 1
        
        
for i in tqdm (range (1), desc="Loading..."):
    
    final_lst = splitting(off,names_list)
#print(final_lst)
    
    

#What needs to be done:
#Update the replaces to include relavant strings
#Make the code work with politician names. I didnt know how we had the names so i didnt know how to proceed.¯\_(ツ)_/¯
#It should work after that.
