import os
import re

# Define the folder where the mp4 files are located
folder_path = r"C:\Users\thinkpad\Downloads\10D"

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    print(f"Processing: {filename}")  # Print each file being processed

    # Check if the file is an mp4 file and contains the pattern
    if filename.endswith(".mp3") and "[SPOTIFY-DOWNLOADER.COM]" in filename:
        print(f"Match found: {filename}")  # Print when a match is found
        
        # Create the new filename by removing the unwanted part
        new_filename = re.sub(r"\[SPOTIFY-DOWNLOADER\.COM\]\s*", "", filename)
        
        # Get full paths for the old and new file names
        old_file = os.path.join(folder_path, filename)
        new_file = os.path.join(folder_path, new_filename)
        
        # Print old and new filenames for verification
        print(f"Old filename: {old_file}")
        print(f"New filename: {new_file}")
        
        # Rename the file
        os.rename(old_file, new_file)
        print(f"Renamed: {filename} -> {new_filename}")
    else:
        print(f"No match for: {filename}")

print("All applicable files have been renamed.")
