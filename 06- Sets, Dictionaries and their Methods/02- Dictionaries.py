# ---------------(Assignment 1)---------------
# Dictionary representing skills and their progress
skills = {
    'Python': '80%',
    'HTML': '50%',
    'CSS': '20%'
}

# Update skills dictionary with a new skill and its progress
skills.update({'AI': '30%'})

# Print progress for each skill
for skill, progress in skills.items():
    print(f"{skill} Progress Is {progress}")
