import os

def rename_files_in_folder(folder):
    for count, filename in enumerate(os.listdir(folder), start=1):
        file_ext = os.path.splitext(filename)[1]
        new_name = f"file_{count}{file_ext}"
        os.rename(os.path.join(folder, filename), os.path.join(folder, new_name))
