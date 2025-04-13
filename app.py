import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from scraper import scrape_multiple_sites
from nlp_utils import extract_entities
from geocode_utils import get_coordinates
from time import sleep
from datetime import datetime
import os

st.set_page_config(page_title="🌍 Disease Outbreak Detection", layout="wide")

st.title("🌍 Disease Outbreak Detection")
st.write("This app scrapes news websites, extracts mentions of diseases and locations, and maps potential outbreaks.")

# Step 1: Scrape news
with st.spinner("🔍 Scraping news sites..."):
    headlines = scrape_multiple_sites()
    st.success(f"✅ Scraped {len(headlines)} headlines.")

# Step 2: Extract info and geocode
data = []
with st.spinner("📊 Analyzing headlines and mapping outbreaks..."):
    for i, headline in enumerate(headlines):
        st.write(f"📰 Processing headline {i+1}/{len(headlines)}: `{headline[:100]}...`")
        locations, diseases = extract_entities(headline)
        for loc in locations:
            coords = get_coordinates(loc)
            if coords:
                for disease in diseases:
                    data.append({
                        'headline': headline,
                        'location': loc,
                        'disease': disease,
                        'lat': coords[0],
                        'lon': coords[1],
                        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    })
        sleep(1)  # prevent hitting geocoding rate limit

# Step 3: Create DataFrame
df = pd.DataFrame(data)

# Step 4: Save to CSV with timestamp
os.makedirs("logs", exist_ok=True)
timestamp_str = datetime.now().strftime("%Y%m%d_%H%M%S")
csv_filename = f"logs/outbreak_log_{timestamp_str}.csv"
df.to_csv(csv_filename, index=False)
st.success(f"💾 Data saved to `{csv_filename}`")

# Step 5: Display DataFrame
st.subheader("🦠 Detected Outbreaks")
if not df.empty:
    st.dataframe(df)
else:
    st.warning("No disease outbreaks detected.")

# Step 6: Show map
st.subheader("🗺️ Map View of Outbreaks")
if not df.empty:
    m = folium.Map(location=[0, 20], zoom_start=2)
    for _, row in df.iterrows():
        folium.Marker(
            location=[row['lat'], row['lon']],
            popup=f"{row['disease'].title()} in {row['location']}",
            tooltip=row['headline'],
            icon=folium.Icon(color="red", icon="plus")
        ).add_to(m)
    st_folium(m, width=700, height=500)
else:
    st.info("No locations to map.")
