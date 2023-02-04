import subprocess

# List of scripts to run
scripts = ['script1.py', 'script2.py', 'script3.py']

# Run each script
for script in scripts:
    subprocess.call(['python', script])

# You can run this master script using the terminal by navigating to the directory containing the script and 
# running python master_script.py.
