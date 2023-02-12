import subprocess

# List of scripts to run
scripts = ['/Users/home/Documents/GitHub/Python_Scripts/OpenChrome_Favorites.py',
           '/Users/home/Documents/GitHub/Python_Scripts/Organize_DocsFolder.py',
           '/Users/home/Documents/GitHub/Python_Scripts/Stock_Scrapper.py',
           '/Users/home/Documents/GitHub/Python_Scripts/Organize_Downloads.py',
           '/Users/home/Documents/GitHub/Python_Scripts/ClearDNS_EmptyTrash.py',
           '/Users/home/Documents/GitHub/Python_Scripts/Password_Generator.py']

# Loop through all scripts 
for script in scripts:
    subprocess.call(['/usr/bin/python3', script])
print("=============================================")
print("= All scripts have run successfully, enjoy! =")
print("=============================================")

# You can run this master script using the terminal by navigating to the directory containing the script and 
# running python master_script.py.

"""
sudo python3 /Users/home/Documents/GitHub/Python_Scripts/Master_script.py
"""
