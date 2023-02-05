import webbrowser

favorites = [
    "https://github.com/jge162",
    "https://www.youtube.com",
    "https://www.macrumors.com",
    "https://www.dailymail.co.uk/ushome/index.html",
]

for url in favorites:
    webbrowser.open(url, new=2, autoraise=True)

"""
sudo python3 /Users/home/Documents/GitHub/Python_Scripts/OpenChrome_Favorites.py
"""