import subprocess
import os


def clear_dns_cache():
    try:
        subprocess.call(["dscacheutil", "-flushcache"])
        print("====================================")
        print("= DNS cache cleared: Successfully. =")
        print("====================================")
    except Exception as e:
        print(f"An error occurred: {e}")


def empty_trash():
    try:
        home = os.path.expanduser("~")
        trash = os.path.join(home, ".Trash")
        subprocess.call(["rm", "-rf", trash + "/*"])
        print("====================================")
        print("= Trash bin emptied: Successfully. =")
        print("====================================")

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
