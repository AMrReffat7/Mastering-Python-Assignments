my_ranks = {
    'Math': 'A',
    'Science': 'B',
    'Drawing': 'A',
    'Sports': 'C'
}

my_points = {
    "A": 100,
    "B": 80,
    "C": 40
}

total_points = 0

for subject, rank in my_ranks.items():
    points = my_points.get(rank)
    if points is not None:
        total_points += points
        print(f"My Rank in {subject} Is '{rank}' And This Equals {points} Points.")

print(f"Total Points Is: {total_points}")
