import subprocess
import os
import string
def get_drives():
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    no = 0
    while bitmask > 0:
        if bitmask & 1:
            drives.append(string.ascii_uppercase[no])
        bitmask >>= 1
        no+=1
    return drives

def clear_dns_cache():
    try:
        subprocess.call(["dscacheutil", "-flushcache"] if os.name != 'nt' else ["ipconfig","/flushdns"])
        print("DNS cache cleared successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")


def empty_trash():
    try:
        if os.name != 'nt':
            home = os.path.expanduser("~")
            trash = os.path.join(home, ".Trash")
            subprocess.call(["rm", "-rf", trash + "/*"])
         else:
            from ctypes import windll
            sid = subprocess.check_output("wmic useraccount where name=\"" + os.getlogin() + "\" get sid", shell=True)[4:].strip().decode('utf8')
            for i in get_drives():
                shutil.rmtree(shutil.rmtree(i + ":\\$Recycle.Bin\\" + sid + "\\", onerror=lambda str, path, err: print("Error deleting "+path + ' ('+ type(err[0]).__name__ +')')))
            
            
        print("Trash bin emptied successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    clear_dns_cache()
    empty_trash()

"""
sudo python3 ClearDNS_EmptyTrashBin.py
"""

"""
output below
sudo python3 ClearDNS_EmptyTrashBin.py

DNS cache cleared successfully.
Trash bin emptied successfully.
"""
