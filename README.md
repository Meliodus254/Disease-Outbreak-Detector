🌍 Disease Outbreak Detection App

This app monitors global news websites to detect potential disease outbreaks using natural language processing (NLP) and geolocation mapping. It scrapes headlines, extracts disease and location mentions using an AI model, and displays outbreaks on an interactive map.


🔧 Features

📰 Scrapes headlines from global and African news/health sources

🧠 Detects diseases and locations using ScispaCy NLP

📍 Geocodes detected locations to coordinates

🗺️ Maps outbreak reports on an interactive world map

💾 Saves results to timestamped CSV logs for historical tracking

⏱️ Displays progress for scraping, NLP, and geolocation steps

🚀 Getting Started

1. Clone the Repository

   
       git clone https://github.com/your-username/disease-outbreak-detector.git
       cd disease-outbreak-detector
2. Create and Activate a Virtual Environment
   
# Windows
       python -m venv venv
       venv\Scripts\activate

# macOS/Linux
      python3 -m venv venv
      source venv/bin/activate
3. Install Dependencies
   
       pip install -r requirements.txt
Make sure to have spaCy and ScispaCy installed.

4. Download the ScispaCy Model

        pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.5.1/en_ner_bc5cdr_md-0.5.1.tar.gz
   
🏃 Run the App

        streamlit run app.py
        
📂 Project Structure


├── app.py                     # Main Streamlit app

├── scraper.py                # Web scrapers for various news sites

├── nlp_utils.py              # NLP logic using ScispaCy

├── geocode_utils.py          # Geolocation using geopy

├── requirements.txt          # Python dependencies

└── logs/                     # Saved CSV logs of each run



🗞️ Supported News Sources

Includes global health authorities and over 20 news websites from:

🌐 WHO, CDC, NHS

🇬🇧 The Guardian, BBC

🇺🇸 NPR, NYTimes

🌍 Africa: The East African, News24, SABC News, Premium Times, GhanaWeb, and more


🧠 Technologies Used

Streamlit – for web UI

BeautifulSoup – for web scraping

ScispaCy – for biomedical NLP

geopy – for geocoding locations

Folium – for interactive maps

pandas – for data management


📈 Future Improvements

Trend charts of outbreak frequency

SMS or email alerts for high-risk locations

Admin dashboard with filters

Integration with health APIs (e.g. HealthMap, Outbreak.info)

🛡️ Disclaimer
This app is a prototype for research and demo purposes only. It does not provide medical or official outbreak alerts.

📬 Contact
Developer: Collins
Email: collinskimani254@gmail.com
