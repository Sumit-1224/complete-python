import os
desktop_path = os.path.expanduser("~/Downloads")

for file in os.listdir():
    if file.endswith("png"):
        print(file)
