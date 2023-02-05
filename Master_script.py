import subprocess
import sys.argv

# Run each script
for script in sys.argv[2:]:
    subprocess.call(['python', script])

# You can run this master script using the terminal by navigating to the directory containing the script and 
# running python master_script.py [script1] [script2] ...
