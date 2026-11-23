# Three tabs open — the honest count, written as one number and nothing else.
import os

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write("3")
