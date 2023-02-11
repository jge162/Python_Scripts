import os
import shutil

# path to the directory containing the documents
src_dir = '/Users/home/Documents'

# dictionary to store file extensions and their corresponding folder names
extension_to_folder_map = {
    '.pdf': 'PDF Files',
    '.doc': 'Word Files',
    '.docx': 'Word Files',
    '.xls': 'Excel Files',
    '.xlsx': 'Excel Files',
    '.ppt': 'PowerPoint Files',
    '.pptx': 'PowerPoint Files',
    '.png': 'PNG Files',
    '.rtf': 'RTF Files'

}

for filename in os.listdir(src_dir):
    # split the filename into name and extension
    name, ext = os.path.splitext(filename)

    # get the target folder name for the file
    target_folder = extension_to_folder_map.get(ext, 'Document Files')

    # construct the path to the target folder
    target_path = os.path.join(src_dir, target_folder)

    # create the target folder if it does not exist
    if not os.path.exists(target_path):
        os.makedirs(target_path)

    # move the file to the target folders
    src_path = os.path.join(src_dir, filename)
    shutil.move(src_path, os.path.join(target_path, filename))
    print("=================================")
    print("= Files organized: successfully =")
    print("=================================")

"""
sudo python3 /Users/home/Documents/GitHub/Python_Scripts/Organize_DocsFolder.py
"""
