import os
import zipfile
import fnmatch

def zip_matching_files(folder_path, extensions, output_zip):
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(folder_path):
            for ext in extensions:
                for filename in fnmatch.filter(files, f'*.{ext}'):
                    abs_filepath = os.path.join(root, filename)
                    rel_filepath = os.path.relpath(abs_filepath, start=folder_path)
                    zipf.write(abs_filepath, rel_filepath)
    print(f"Zip file created: {output_zip}")

if __name__ == "__main__":
    folder_path = input("Enter the folder path: ")
    extensions = input("Enter the file extensions (comma separated): ").split(',')
    extensions = [ext.strip() for ext in extensions]  # Remove any extra whitespace
    output_zip = input("Enter the output zip file path (e.g., output.zip): ")
    
    zip_matching_files(folder_path, extensions, output_zip)
