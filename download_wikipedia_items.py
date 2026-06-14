import os
import json
import urllib.request
import urllib.parse
import time

# List of items mapped to their corresponding Wikipedia page titles
ITEMS = [
    # Tin items
    ("matches", "Match"),
    ("candle", "Candle"),
    ("flint", "Ferrocerium"),
    ("compass", "Compass"),
    ("snare", "Snare_trap"),
    ("sewing", "Sewing_needle"),
    ("fishing", "Fishing_tackle"),
    ("wiresaw", "Pocket_3D_Wire_Saw"), # fallback to "Hand_saw" if not found
    ("scalpel", "Scalpel"),
    ("plasters", "Adhesive_bandage"),
    ("sterilizer", "Water_purification_tablet"),
    ("condom", "Condom"),
    # Pouch items
    ("mirror", "Heliograph"),
    ("whistle", "Whistle"),
    ("torch", "Headlamp_(outdoor)"),
    ("purifier", "Water_filter"),
    ("bivy", "Bivouac_sack"),
    ("tinder", "Tinder"),
    ("rations", "Field_ration")
]

# Alternate titles to try if primary fails
FALLBACKS = {
    "Pocket_3D_Wire_Saw": ["Hand_saw", "Saw"],
    "Sewing_needle": ["Sewing", "Needle"],
    "Headlamp_(outdoor)": ["Flashlight", "Tactical_light"],
    "Water_purification_tablet": ["Water_purification", "Chlorine_tablets"],
    "Snare_trap": ["Animal_trapping", "Trap_(device)"],
    "Field_ration": ["Survival_ration", "Rationing", "Packaged_food"]
}

MAUI_IMG_DIR = "HowToSurvive.Maui/Resources/Images"
WEB_IMG_DIR = "HowToSurvive.Web/wwwroot/images"

def setup_directories():
    os.makedirs(MAUI_IMG_DIR, exist_ok=True)
    os.makedirs(WEB_IMG_DIR, exist_ok=True)

def get_wikipedia_image_url(title):
    api_url = f"https://en.wikipedia.org/w/api.php?action=query&prop=pageimages&format=json&piprop=original&titles={urllib.parse.quote(title)}"
    try:
        req = urllib.request.Request(
            api_url,
            headers={'User-Agent': 'HowToSurviveApp/1.0 (contact: info@howtosurvive.app)'}
        )
        with urllib.request.urlopen(req) as response:
            res_data = json.loads(response.read().decode('utf-8'))
            
        pages = res_data.get("query", {}).get("pages", {})
        for page_id, page_data in pages.items():
            if "original" in page_data:
                return page_data["original"]["source"]
    except Exception as e:
        print(f"API Error for '{title}': {e}")
    return None

def download_image(name, url):
    maui_path = os.path.join(MAUI_IMG_DIR, f"{name}.jpg")
    web_path = os.path.join(WEB_IMG_DIR, f"{name}.jpg")
    
    try:
        req = urllib.request.Request(
            url,
            headers={'User-Agent': 'HowToSurviveApp/1.0 (contact: info@howtosurvive.app)'}
        )
        with urllib.request.urlopen(req) as response:
            data = response.read()
            
        with open(maui_path, 'wb') as f:
            f.write(data)
        with open(web_path, 'wb') as f:
            f.write(data)
            
        print(f"Successfully downloaded '{name}.jpg'")
        return True
    except Exception as e:
        print(f"Failed to download image from {url}: {e}")
        return False

def process_item(name, primary_title):
    print(f"Fetching image for '{name}' (wiki page: {primary_title})...")
    url = get_wikipedia_image_url(primary_title)
    
    # Try fallbacks if primary page does not have a page image
    if not url and primary_title in FALLBACKS:
        for fallback in FALLBACKS[primary_title]:
            print(f"Trying fallback '{fallback}' for '{name}'...")
            url = get_wikipedia_image_url(fallback)
            if url:
                break
                
    if url:
        return download_image(name, url)
    else:
        print(f"No image found for '{name}' on Wikipedia.")
        return False

def main():
    setup_directories()
    success_count = 0
    
    for name, title in ITEMS:
        success = process_item(name, title)
        if success:
            success_count += 1
        time.sleep(0.5) # rate limit politeness
        
    print(f"\nDownload completed. Successfully downloaded {success_count}/{len(ITEMS)} images.")

if __name__ == "__main__":
    main()
