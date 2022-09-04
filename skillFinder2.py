import json
import itertools
import re

regex_bachelor = r"bachelor|Bachelor|BACHELOR|BS|(B\.Sc)|(B\.E)|BE|Bacharel|Bac|bac|BSc|bsc"
regex_master = r"master|Master|MASTER|MS|(M\.Sc)|MS"

skills = []

def skillFinder(inEdu, inPos):
    input_file = open('a-10.json')
    raw_data = json.load(input_file)

    for obj in raw_data:
        # raw check if the object has the properties we need
        if "educations" in obj and "positions" in obj and "skills" in obj and len(obj["skills"]) >= 4:
            # education
            for edu in obj["educations"]:
                if "field-of-study" in edu and "degree" in edu:
                    print(edu)
                    if re.match(regex_bachelor, edu["degree"]) or re.match(regex_master, edu["degree"]):
                        if inEdu in edu["field-of-study"]:
                            # positions
                            for pos in obj["positions"]:
                                if "title" in pos:
                                    if inPos in pos:
                                        # skills
                                        skill_list = [] 
                                        for skill in obj["skills"]:
                                            skill_list.append(skill)

                                        if len(skill_list) > 4:
                                            skill_groups = list(itertools.combinations(skill_list, 5))
                                            for skill_group in skill_groups:
                                                skills.append(skill_group)
                                        
    print()
    print()
    print(skills) 
    return(skills)