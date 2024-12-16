import os

folder = r"C:\Users\rapha\OneDrive\ZHAW\2024HS\PROG1\music_extension_example

for filename in os.listdir(folder):
    if filename.lower().endswith(".mp3"):
        os.rename(
            os.path.join(folder, filename),
            os.path.join(folder, filename.lower())
        )
