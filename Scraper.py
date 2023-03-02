import re
from Reader import *
import json
from Beautiful import *
from tqdm import tqdm
from Project import *
text = full
newVar = dictionary
#print(newVar)
# initialize a dictionary to store the results
result = {}

# use regular expressions to extract the name
#match = re.match(r"^(.*), (.*?) \(", text)
#result['name'] = f"{match.group(2)} {match.group(1)}"

# use regular expressions to split the text into sections
#sections = re.split(r"\n(\d+)\. ", text)[1:]
name_pattern = re.compile(r"^(.*), (.*?) \(")
for i in tqdm (range (len(text)), desc="Loading..."):
    match = name_pattern.match(text)
    result['name'] = f"{match.group(2)} {match.group(1)}"
print(result)
# loop over the sections and extract the information
#for i in range(0, len(sections), 2):
    # section_num = int(sections[i])
    # section_text = sections[i+1]
    # section_dict = {}
    
    # # use regular expressions to extract the information in the section
    # matches = re.findall(r"^(.*?):\s+(.*)\n?", section_text, flags=re.MULTILINE)
    
    # # store the information in a nested dictionary
    # for k, v in matches:
    #     section_dict[k] = v.strip()
    
    # # update or add the section dictionary to the result dictionary
    # if section_num in result:
    #     result[section_num].update(section_dict)
    # else:
    #     result[section_num] = section_dict

# print the result
#print(result.keys())

# write the keys of the result dictionary to a file
with open('values.txt', 'w') as convert_file:
    convert_file.write(json.dumps(list(result.keys())))
