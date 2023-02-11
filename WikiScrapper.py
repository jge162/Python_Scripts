import requests


def get_wikipedia_content(page_title):
    # Define the URL for the Wikipedia page
    url = f"https://en.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&titles={page_title}"

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        pages = data["query"]["pages"]
        page_id = list(pages.keys())[0]
        if page_id != "-1":
            return pages[page_id]["extract"]
        else:
            return None
    else:
        return None


# Example usage
page_title = "Python (programming language)"
content = get_wikipedia_content(page_title)
if content:
    with open("wikipedia_content.txt", "w") as file:
        file.write(content)
    print("Content saved to wikipedia_content.txt")
else:
    print("Page not found.")
