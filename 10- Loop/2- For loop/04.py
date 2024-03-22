Here's your code with comments added to explain each part:

```python
# Define the students' grades for different subjects
students = {
    "Ahmed": {
        "Math": "A",
        "Science": "D",
        "Draw": "B",
        "Sports": "C",
        "Thinking": "A"
    },
    "Sayed": {
        "Math": "B",
        "Science": "B",
        "Draw": "B",
        "Sports": "D",
        "Thinking": "A"
    },
    "Mahmoud": {
        "Math": "D",
        "Science": "A",
        "Draw": "A",
        "Sports": "B",
        "Thinking": "B"
    }
}

# Define the points corresponding to each grade
my_points = {
    "A": 100,
    "B": 80,
    "C": 40,
    "D": 20
}

# Initialize variables to store the total points for each student
sum1 = 0
sum2 = 0
sum3 = 0

# Iterate through each student in the students dictionary
for student in students:
    # Print a separator for each student
    print("-" * 30)
    # Print the student's name
    print(f"Student Name => {student}")
    # Print a separator for each student
    print("-" * 30)

    # Iterate through each subject and grade for the current student
    for subjects in students[student]:
        # Iterate through each grade and its corresponding points
        for points in my_points:
            # Check if the current grade matches a grade in the my_points dictionary
            if students[student][subjects] == points:
                # Add the corresponding points to the total points for the current student
                if student == "Ahmed":
                    sum1 += my_points[points]
                elif student == "Sayed":
                    sum2 += my_points[points]
                elif student == "Mahmoud":
                    sum3 += my_points[points]

                # Print the subject and the points earned
                print(f"- {subjects} => {my_points[points]} Points")

    # Print the total points for the current student
    print(f"= Total Points For {student} Is: {sum1 if student == 'Ahmed' else sum2 if student == 'Sayed' else sum3}")
```

With these comments, it should be clearer what each part of the code is doing.