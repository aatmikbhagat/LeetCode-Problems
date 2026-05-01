import os
import subprocess

num = input("Problem number: ").zfill(4)
title = input("Problem title: ").lower().replace(" ", "_")
diff = input("Difficulty (easy/medium/hard): ").lower()

if diff not in ["easy", "medium", "hard"]:
    print("Invalid difficulty")
    exit()

filename = f"{diff}/{num}_{title}.py"

os.makedirs(diff, exist_ok=True)

print("Paste your code below. Press CTRL+D (Mac) or CTRL+Z + Enter (Windows):")

code = []
try:
    while True:
        line = input()
        code.append(line)
except EOFError:
    pass

with open(filename, "w") as f:
    f.write(f"# {num} {title.replace('_', ' ')}\n\n")
    f.write("\n".join(code))

readme_line = f"- [{num} {title.replace('_', ' ').title()}]({filename}) , {diff}, python\n"

with open("README.md", "a") as f:
    f.write(readme_line)

subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit", "-m", f"Add {num} {title}, {diff}, python"])
subprocess.run(["git", "push"])

print(f"Saved to {filename} and pushed 🚀")
