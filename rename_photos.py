import os

# Folder containing the images
folder_path = r"C:\Users\le\Downloads\New folder (2)\vee"

# Supported image extensions
extensions = [".jpg", ".jpeg", ".png"]

count = 1

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    file_ext = os.path.splitext(filename)[1].lower()

    # Check if file is an image
    if file_ext in extensions:
        old_path = os.path.join(folder_path, filename)

        # New file name
        new_name = f"photo{count}{file_ext}"
        new_path = os.path.join(folder_path, new_name)

        # Rename file
        os.rename(old_path, new_path)

        print(f"Renamed: {filename} -> {new_name}")

        count += 1

print("Done renaming files.")