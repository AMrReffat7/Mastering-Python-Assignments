skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")

# Reverse the skills tuple
reversed_skills = reversed(skills)

# Enumerate the reversed skills with a start value of 50
enumerated_skills = enumerate(reversed_skills, 50)

# Print the enumerated skills
for counter, skill in enumerated_skills:
    if not isinstance(skill, int):
        print(f"{counter} - {skill}")
