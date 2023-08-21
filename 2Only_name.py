import os

folder_path = r"C:\Users\David Quirino\Documents\Musica\4K Video Downloader\Modificar\Ixchel"
prefix = "1 Ixchel - "

def rename_files_with_prefix(folder_path, prefix):
    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            new_filename = prefix + filename
            os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
            print(f'Renamed: {filename} -> {new_filename}')

rename_files_with_prefix(folder_path, prefix)