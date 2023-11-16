from bs4 import BeautifulSoup
import requests

def get_soup() -> BeautifulSoup:
    headers: dict = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0"
    }
    request = requests.get("https://www.bbc.com/news", headers=headers)
    html: bytes = request.content
    
    #create soup
    soup = BeautifulSoup(html, "html.parser")
    return soup

def get_headlines(soup: BeautifulSoup) -> [str]:
    headlines: set = set()
    
    for h in soup.findAll("h3", class_="gs-c-promo-heading__title"):
        headline: str = h.contents[0].lower()
        headlines.add(headline)
    
    return sorted(headlines)

def check_headlines(headlines: [str], term: str):
    term_list: [str] = []
    terms_found: int = 0
    
    for i, headline in enumerate(headlines, start=1):
        if term.lower() in headline:
            terms_found += 1
            term_list.append(headline)
            print(f"{i}: {headline.capitalize()} <-------------------------- {term}")
        else:
            print(f"{i}: {headline.capitalize()}")
    
    print("-----------------------------------------")
    if terms_found:
        print(f"{term} was mentioned {terms_found} times.")
        print("-----------------------------------------")
        
        for i, headline in enumerate(term_list, start=1):
            print(f"{i}: {headline.capitalize()}")
    
    else:
        print(f"No matches found for: {term}")
        print("-----------------------------------------")
    

def main():
    soup: BeautifulSoup = get_soup()
    headlines: list[str] = get_headlines(soup=soup)
    
    user_input: str = "Israel"
    check_headlines(headlines, user_input)


if __name__ == "__main__":
    main()