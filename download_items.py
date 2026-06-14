import os
import re
import urllib.request
import urllib.parse
import time

# List of items with search queries and output filenames
ITEMS = [
    # Tin items
    ("matches", "waterproof matches"),
    ("candle", "wax candle burning"),
    ("flint", "ferrocerium rod fire steel"),
    ("compass", "button compass pocket"),
    ("snare", "brass wire coil"),
    ("sewing", "sewing kit needles thread"),
    ("fishing", "fishing hooks line tackle"),
    ("wiresaw", "wire pocket saw camping"),
    ("scalpel", "scalpel blade surgical"),
    ("plasters", "adhesive bandages plaster"),
    ("sterilizer", "water purification tablets"),
    ("condom", "latex condom sealed"),
    # Pouch items
    ("mirror", "signal mirror heliograph"),
    ("whistle", "survival whistle outdoor"),
    ("torch", "led headlamp torch"),
    ("purifier", "water filter straw survival"),
    ("bivy", "emergency bivy bag thermal"),
    ("tinder", "tinder cotton fire starter"),
    ("rations", "emergency food bar ration")
]

MAUI_IMG_DIR = "HowToSurvive.Maui/Resources/Images"
WEB_IMG_DIR = "HowToSurvive.Web/wwwroot/images"

def setup_directories():
    os.makedirs(MAUI_IMG_DIR, exist_ok=True)
    os.makedirs(WEB_IMG_DIR, exist_ok=True)

def find_and_download_image(name, query):
    search_url = f"https://unsplash.com/s/photos/{urllib.parse.quote(query)}"
    print(f"Searching Unsplash for '{query}'...")
    
    try:
        req = urllib.request.Request(
            search_url,
            headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
        )
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8')
            
        # Unsplash photo URLs format: https://images.unsplash.com/photo-154...
        # Let's search for matches in the HTML source code
        matches = re.findall(r'https://images.unsplash.com/(photo-[a-zA-Z0-9\-_]+)', html)
        
        if not matches:
            # Try a broader regex search
            matches = re.findall(r'photo-([a-zA-Z0-9\-_]+)\?auto', html)
            if matches:
                matches = [f"photo-{m}" for m in matches]
                
        if matches:
            # Get the first unique match
            photo_id = None
            for m in matches:
                # Filter out generic profile images or tracking pixels if any
                if len(m) > 15:
                    photo_id = m
                    break
            
            if not photo_id:
                photo_id = matches[0]
                
            download_url = f"https://images.unsplash.com/{photo_id}?auto=format&fit=crop&w=400&q=80"
            print(f"Found photo ID: {photo_id}. Downloading image for '{name}'...")
            
            # Paths to save
            maui_path = os.path.join(MAUI_IMG_DIR, f"{name}.jpg")
            web_path = os.path.join(WEB_IMG_DIR, f"{name}.jpg")
            
            img_req = urllib.request.Request(
                download_url,
                headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'}
            )
            with urllib.request.urlopen(img_req) as img_resp:
                data = img_resp.read()
                
                with open(maui_path, 'wb') as f:
                    f.write(data)
                with open(web_path, 'wb') as f:
                    f.write(data)
                    
            print(f"Successfully downloaded '{name}.jpg'")
            return True
        else:
            print(f"No photos found on Unsplash for '{query}'")
            return False
            
    except Exception as e:
        print(f"Error downloading image for '{query}': {e}")
        return False

def main():
    setup_directories()
    success_count = 0
    
    for name, query in ITEMS:
        success = find_and_download_image(name, query)
        if success:
            success_count += 1
        # Brief sleep to avoid rate limits
        time.sleep(1.5)
        
    print(f"\nDownload completed. Successfully downloaded {success_count}/{len(ITEMS)} images.")

if __name__ == "__main__":
    main()
