import webbrowser

favorites = [
    "https://www.github.com",
    "https://www.youtube.com",
    "https://www.macrumors.com",
    "https://www.twitter.com",
    "https://www.mailonline.com",
]

chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"

for url in favorites:
    webbrowser.get(chrome_path).open(url)
