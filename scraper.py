import requests
from bs4 import BeautifulSoup

def scrape_news(url):
    headlines = []
    try:
        r = requests.get(url, timeout=30)  # Increased timeout from 10 to 30 seconds
        soup = BeautifulSoup(r.text, 'html.parser')
        for item in soup.find_all('h3'):
            if item.text:
                headlines.append(item.text.strip())
    except Exception as e:
        print(f"Error scraping {url}: {e}")
    return headlines

def scrape_multiple_sites():
    urls = [
        # Global health organizations
        'https://www.who.int/news',                          # World Health Organization
        'https://www.cdc.gov/media/index.html',              # Centers for Disease Control and Prevention (USA)

        # Popular and reliable health/news websites from individual countries
        'https://www.nhs.uk/news/',                          # National Health Service (UK)
        'https://www.smh.com.au/',                           # Sydney Morning Herald (Australia)
        'https://www.theguardian.com/world',                 # The Guardian (UK)
        'https://www.aljazeera.com/news/',                   # Al Jazeera (Middle East)
        'https://www.bbc.com/news',                          # BBC (UK)
        'https://www.npr.org/sections/health-shots/',         # NPR Health Shots (USA)
        'https://www.deccanherald.com/national/',             # Deccan Herald (India)
        'https://www.france24.com/en/',                      # France 24 (France)
        'https://www.dw.com/en/world/s-1598',                # Deutsche Welle (Germany)
        'https://www.abc.net.au/news/',                      # ABC News (Australia)
        'https://www.reuters.com/',                          # Reuters (Global)
        'https://www.euronews.com/en/world',                 # Euronews (Europe)
        'https://www.xinhuanet.com/english/',                # Xinhua News (China)
        'https://www.nytimes.com/',                          # New York Times (USA)

        # African news websites
        'https://www.theeastafrican.co.ke/',                 # The East African (East Africa)
        'https://www.africanews.com/',                       # Africa News (Pan-African)
        'https://www.enca.com/',                             # eNCA (South Africa)
        'https://www.sowetanlive.co.za/',                    # Sowetan Live (South Africa)
        'https://www.modernghana.com/',                      # Modern Ghana (Ghana)
        'https://www.vanguardngr.com/',                      # Vanguard (Nigeria)
        'https://www.news24.com/',                           # News24 (South Africa)
        'https://www.sabcnews.com/',                         # SABC News (South Africa)
        'https://www.nigerianmonitor.com/',                  # Nigerian Monitor (Nigeria)
        'https://www.dailytrust.com.ng/',                   # Daily Trust (Nigeria)
        'https://www.thetimes.co.za/',                       # The Times (South Africa)
        'https://www.ghanaweb.com/',                         # GhanaWeb (Ghana)
        'https://www.premiumtimesng.com/',                   # Premium Times (Nigeria)
        'https://www.mmegi.bw/',                             # Mmegi (Botswana)
        'https://www.newtimes.co.rw/',                       # The New Times (Rwanda)
        'https://www.standardmedia.co.ke/',                  # Standard Media (Kenya)
        'https://www.sundaytimes.co.za/',                    # Sunday Times (South Africa)
        'https://www.irishtimes.com/africa/',                # Irish Times Africa section
    ]

    all_headlines = []
    for url in urls:
        all_headlines.extend(scrape_news(url))
    return all_headlines
