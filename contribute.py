from datetime import datetime

# Replace this with your commit messages or tasks
contributions = [
    "Added new feature",
    "Fixed a bug",
    "Updated README",
]

# Append contributions to a file with timestamps
with open("contributions.log", "a") as f:
    for c in contributions:
        f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {c}\n")

print("Contributions logged!")

