import os
import urllib.request

IMAGES = {
    "essentials.jpg": "photo-1501555088652-021faa106b9b",
    "strategy.jpg": "photo-1526772662000-3f88f10405ff",
    "climate.jpg": "photo-1464822759023-fed622ff2c3b",
    "food.jpg": "photo-1501747315-124a0eaca060",
    "campcraft.jpg": "photo-1510312305653-8ed496efae75",
    "navigation.jpg": "photo-1506318137071-a8e063b4bec0",
    "travel.jpg": "photo-1469474968028-56623f02e42e",
    "health.jpg": "photo-1603398938378-e54eab446dde",
    "disaster.jpg": "photo-1477959858617-67f85cf4f1df",
    "knife.jpg": "29R5-f0SgI8",
    "kit.jpg": "photo-1596755094514-f87e34085b2c"
}

MAUI_IMG_DIR = "HowToSurvive.Maui/Resources/Images"
WEB_IMG_DIR = "HowToSurvive.Web/wwwroot/images"

def setup_directories():
    os.makedirs(MAUI_IMG_DIR, exist_ok=True)
    os.makedirs(WEB_IMG_DIR, exist_ok=True)

def download_images():
    setup_directories()
    for filename, unsplash_id in IMAGES.items():
        url = f"https://images.unsplash.com/{unsplash_id}?auto=format&fit=crop&w=800&q=80"
        
        # Paths to save
        maui_path = os.path.join(MAUI_IMG_DIR, filename)
        web_path = os.path.join(WEB_IMG_DIR, filename)
        
        print(f"Downloading {filename} from Unsplash...")
        try:
            req = urllib.request.Request(
                url,
                headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
            )
            with urllib.request.urlopen(req) as response:
                data = response.read()
                
                # Save to MAUI
                with open(maui_path, 'wb') as f:
                    f.write(data)
                    
                # Save to Web
                with open(web_path, 'wb') as f:
                    f.write(data)
                    
            print(f"Successfully saved {filename} to both projects.")
        except Exception as e:
            print(f"Error downloading {filename}: {e}")

if __name__ == "__main__":
    download_images()
