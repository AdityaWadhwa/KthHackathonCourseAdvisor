import json
import itertools
import re

regex_bachelor = r"bachelor|Bachelor|BACHELOR|BS|(B\.Sc)|(B\.E)|BE|Bacharel|Bac|bac|BSc|bsc"
regex_master = r"master|Master|MASTER|MS|(M\.Sc)|MS"

data = []

input_file = open('a-10.json')
raw_data = json.load(input_file)

#print(raw_data)

for obj in raw_data:
    # raw check if the object has the properties we need
    if "educations" in obj and "positions" in obj and "skills" in obj and len(obj["skills"]) >= 4:
        # new record creation
        record = []

        # education
        counter = 0
        for edu in obj["educations"]:
            if "field-of-study" in edu and "degree" in edu and counter < 2:
                print(edu)
                if re.match(regex_bachelor, edu["degree"]):
                    record.append(edu["field-of-study"])
                    counter += 1

                if re.match(regex_master, edu["degree"]):
                    record.append(edu["field-of-study"])
                    counter += 1
        print(record)

        # positions
        counter = 0
        for pos in obj["positions"]:
            if "title" in pos and counter < 2:
                record.append(pos["title"])
                counter+=1
        print(record)

        # skills
        skill_list = [] 
        for skill in obj["skills"]:
            skill_list.append(skill)
        
        if len(skill_list) > 4:
            skill_groups = list(itertools.combinations(skill_list, 5))
            for skill_group in skill_groups:
                record[-4:] = skill_group
                data.append(record)
        print(record)

print()
print()
print(data) 