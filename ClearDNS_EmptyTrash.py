import os
import subprocess


def clear_dns_cache():
    try:
        subprocess.call(["dscacheutil", "-flushcache"])
        print("DNS cache cleared: Successfully! ")
    except Exception as e:
        print(f"An error occurred: {e}")


def empty_trash():
    try:
        # Run the osascript command to empty the trash bin
        subprocess.call(['osascript', '-e', 'tell application "Finder" to empty trash'])
        print("Trash bin has been emptied!")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    clear_dns_cache()
    empty_trash()

"""
sudo python3 /Users/home/Documents/GitHub/Python_Scripts/ClearDNS_EmptyTrash.py
DNS cache cleared successfully.
Trash bin emptied successfully.
"""
