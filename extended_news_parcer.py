import requests
from bs4 import BeautifulSoup

def get_bbc_news():
    url = "https://www.bbc.com"
    response = requests.get(url)
    return response.text

def get_cnn_news():
    url = "https://edition.cnn.com"
    response = requests.get(url)
    return response.text

def get_custom_news(url):
    response = requests.get(url)
    return response.text

def parse_news(html):
    soup = BeautifulSoup(html, 'html.parser')
    headlines = soup.find_all(['h2', 'h3', 'h1' ])

    print("Last news: \n")
    for idx, headline in enumerate(headlines[:10], 1):
        print(f"{idx}. {headline.get_text(strip=True)}")


def main():
    print("Choose website for parsing:")
    print("1. BBC")
    print("2. CNN")
    print("3. Enter your choice")
    choice = input("Enter number (1, 2 or 3): ")

    if choice == "1":
        html = get_bbc_news()
    elif choice == "2":
        html = get_cnn_news()
    elif choice == "3":
        url = input("Enter URL for parsing: ")
        html = get_custom_news(url)
    else:
        print("Invalid choice, try again.")
        return
    parse_news(html)
if __name__ == "__main__":
    main()


