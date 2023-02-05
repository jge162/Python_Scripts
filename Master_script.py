import subprocess

# List of scripts to run
scripts = ['/Users/home/Documents/GitHub/Python_Scripts/OpenChrome_Favorites.py',
           '/Users/home/Documents/GitHub/Python_Scripts/Organize_DocsFolder.py',
           '/Users/home/Documents/GitHub/Python_Scripts/Organize_downloadFolder.py']

# Run each script
for script in scripts:
    subprocess.call(['/usr/bin/python3', script])

print("All scripts have been completed, enjoy")
# You can run this master script using the terminal by navigating to the directory containing the script and 
# running python master_script.py.

"""
sudo python3 Master_script.py
"""