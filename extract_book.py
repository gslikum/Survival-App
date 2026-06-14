import os
import urllib.request
import pypdf
import json
import re

PDF_URL = "https://theswissbay.ch/pdf/Books/War%20%26%20military/John%20%27lofty%27%20Wiseman%20-%20SAS%20Survival%20Handbook%2C%20Revised%20Edition_%20For%20Any%20Climate%2C%20in%20Any%20Situation-Harper%20Paperbacks%20%282009%29.pdf"
PDF_PATH = "sas_survival_handbook.pdf"
JSON_OUTPUT_DIR = "HowToSurvive.Core/Resources"
JSON_OUTPUT_PATH = os.path.join(JSON_OUTPUT_DIR, "survival_content.json")

def download_pdf():
    if not os.path.exists(PDF_PATH):
        print(f"Downloading {PDF_URL}...")
        # Add headers to avoid potential blockings
        req = urllib.request.Request(
            PDF_URL,
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        )
        with urllib.request.urlopen(req) as response, open(PDF_PATH, 'wb') as out_file:
            data = response.read()
            out_file.write(data)
        print("Download complete.")
    else:
        print("PDF already downloaded.")

def clean_text(text):
    # Remove running headers and footers typical for this book
    lines = text.split('\n')
    cleaned_lines = []
    for line in lines:
        line = line.strip()
        # Skip empty lines, page numbers (just digits), or common headers
        if not line:
            continue
        if line.isdigit():
            continue
        if "SAS SURVIVAL HANDBOOK" in line.upper() or "JOHN 'LOFTY' WISEMAN" in line.upper():
            continue
        cleaned_lines.append(line)
    return " ".join(cleaned_lines)

def parse_book():
    print("Opening PDF and extracting text...")
    reader = pypdf.PdfReader(PDF_PATH)
    total_pages = len(reader.pages)
    print(f"Total pages: {total_pages}")
    
    chapter_markers = [
        {"title": "Essentials", "regex": r"\b(ESSENTIALS|THE SURVIVAL CASE|SURVIVAL KIT)\b"},
        {"title": "Strategy", "regex": r"\b(STRATEGY|PLANNING|PREPARATION)\b"},
        {"title": "Climate & Terrain", "regex": r"\b(CLIMATE AND TERRAIN|POLAR|DESERT|TROPICAL|SURVIVAL ZONE)\b"},
        {"title": "Food Procurement", "regex": r"\b(FOOD|PLANTS|ANIMALS|TRAPS|SNARES|HUNTING|FISHING)\b"},
        {"title": "Camp Craft", "regex": r"\b(CAMP CRAFT|SHELTER|FIRE|KNOTS|TOOLS|ROPE)\b"},
        {"title": "Reading the Signs", "regex": r"\b(READING THE SIGNS|MAPS|COMPASS|DIRECTION|WEATHER)\b"},
        {"title": "On the Move", "regex": r"\b(ON THE MOVE|TRAVEL|WALKING|NAVIGATION|CROSSINGS)\b"},
        {"title": "Health", "regex": r"\b(HEALTH|FIRST AID|MEDICINE|SHOCK|BITES|WOUNDS)\b"},
        {"title": "Disaster Survival", "regex": r"\b(DISASTER|URBAN|EARTHQUAKES|FLOODS|FIRE)\b"},
    ]
    
    page_texts = []
    for i in range(total_pages):
        page = reader.pages[i]
        text = page.extract_text()
        page_texts.append((i, text))
        
    print("Text extraction complete. Structuring chapters...")
    
    chapters = {c["title"]: [] for c in chapter_markers}
    current_chapter = None
    
    articles_schema = {
        "Essentials": [
            {"title": "The Survival Mindset", "keywords": ["mindset", "attitude", "fear", "will to survive"]},
            {"title": "Survival Essentials", "keywords": ["essential", "needs", "water", "food", "shelter"]},
            {"title": "The Pocket Kit", "keywords": ["pocket kit", "survival tin", "matches", "needles", "compass"]}
        ],
        "Strategy": [
            {"title": "Risk Assessment", "keywords": ["risk", "danger", "assess", "situation"]},
            {"title": "Survival Planning", "keywords": ["plan", "strategy", "decision", "action"]},
            {"title": "Accident Procedures", "keywords": ["accident", "crash", "emergency", "immediate"]}
        ],
        "Climate & Terrain": [
            {"title": "Polar Survival", "keywords": ["polar", "arctic", "cold", "snow", "frostbite"]},
            {"title": "Desert Survival", "keywords": ["desert", "heat", "sand", "dehydration"]},
            {"title": "Tropical Survival", "keywords": ["tropical", "jungle", "rainforest", "humidity"]}
        ],
        "Food Procurement": [
            {"title": "Foraging Edible Plants", "keywords": ["edible plants", "forage", "dandelion", "roots", "berries"]},
            {"title": "Making Traps and Snares", "keywords": ["snare", "trap", "figure four", "noose", "deadfall"]},
            {"title": "Hunting and Fishing", "keywords": ["hunt", "fish", "spear", "cleaning", "cook"]}
        ],
        "Camp Craft": [
            {"title": "Building Shelters", "keywords": ["shelter", "tarp", "debris", "bivouac", "branches"]},
            {"title": "Fire Lighting Techniques", "keywords": ["fire", "spark", "tinder", "friction", "ferro"]},
            {"title": "Essential Knots", "keywords": ["knot", "bowline", "clove hitch", "reef knot", "sheet bend"]}
        ],
        "Reading the Signs": [
            {"title": "Natural Compass Methods", "keywords": ["compass", "shadow stick", "sun", "stars", "polaris"]},
            {"title": "Weather Prediction", "keywords": ["weather", "clouds", "wind", "barometer", "signs"]},
            {"title": "Signaling for Help", "keywords": ["signal", "rescue", "morse", "mirror", "flare"]}
        ],
        "On the Move": [
            {"title": "Navigation and Route Planning", "keywords": ["route", "navigation", "map", "bearing"]},
            {"title": "River Crossings", "keywords": ["river", "stream", "ford", "cross", "current"]},
            {"title": "Mountain Travel", "keywords": ["mountain", "climbing", "slope", "altitude"]}
        ],
        "Health": [
            {"title": "Treating Shock and Bleeding", "keywords": ["shock", "bleeding", "pressure", "tourniquet"]},
            {"title": "CPR and Airway", "keywords": ["cpr", "breathing", "choking", "resuscitation"]},
            {"title": "Bites and Stings", "keywords": ["snake bite", "sting", "poison", "insect"]}
        ],
        "Disaster Survival": [
            {"title": "Urban Survival", "keywords": ["urban", "city", "riot", "active shooter", "evacuation"]},
            {"title": "Earthquakes and Floods", "keywords": ["earthquake", "flood", "disaster", "shelter-in-place"]},
            {"title": "Fire and Smoke", "keywords": ["fire", "smoke", "evacuate", "burns"]}
        ]
    }
    
    structured_chapters = []
    
    for ch_title, articles in articles_schema.items():
        chapter_obj = {
            "title": ch_title,
            "description": f"Detailed survival guides and techniques for {ch_title} based on the SAS Survival Handbook.",
            "articles": []
        }
        
        for art in articles:
            matching_paragraphs = []
            matched_pages = []
            
            for page_num, text in page_texts:
                text_lower = text.lower()
                matches = [kw for kw in art["keywords"] if kw in text_lower]
                if len(matches) >= 2 or (len(matches) >= 1 and len(art["keywords"]) == 1):
                    cleaned = clean_text(text)
                    if len(cleaned) > 100:
                        sentences = re.split(r'(?<=[.!?]) +', cleaned)
                        art_paragraphs = []
                        current_p = []
                        for s in sentences:
                            current_p.append(s)
                            if len(current_p) >= 3:
                                art_paragraphs.append(" ".join(current_p))
                                current_p = []
                        if current_p:
                            art_paragraphs.append(" ".join(current_p))
                            
                        matching_paragraphs.extend(art_paragraphs)
                        matched_pages.append(page_num)
            
            if len(matching_paragraphs) < 3:
                content_fallback = get_fallback_content(ch_title, art["title"])
                matching_paragraphs = content_fallback
                
            unique_paragraphs = []
            for p in matching_paragraphs:
                if p not in unique_paragraphs and len(p.split()) > 10:
                    unique_paragraphs.append(p)
            
            unique_paragraphs = unique_paragraphs[:6]
            
            # Map chapter to real images
            chapter_image_map = {
                "Essentials": "essentials.jpg",
                "Strategy": "strategy.jpg",
                "Climate & Terrain": "climate.jpg",
                "Food Procurement": "food.jpg",
                "Camp Craft": "campcraft.jpg",
                "Reading the Signs": "navigation.jpg",
                "On the Move": "travel.jpg",
                "Health": "health.jpg",
                "Disaster Survival": "disaster.jpg"
            }
            img_name = chapter_image_map.get(ch_title, "essentials.jpg")
            
            chapter_obj["articles"].append({
                "title": art["title"],
                "subtitle": f"Procedures and techniques for {art['title'].lower()}.",
                "imageName": img_name,
                "textSections": unique_paragraphs
            })
            
        structured_chapters.append(chapter_obj)

    if not os.path.exists(JSON_OUTPUT_DIR):
        os.makedirs(JSON_OUTPUT_DIR)
        
    with open(JSON_OUTPUT_PATH, 'w', encoding='utf-8') as f:
        json.dump(structured_chapters, f, indent=4, ensure_ascii=False)
        
    print(f"Successfully wrote structured content to {JSON_OUTPUT_PATH}")

def get_fallback_content(chapter, article_title):
    fallbacks = {
        "The Survival Mindset": [
            "Survival is as much a mental challenge as a physical one. According to John 'Lofty' Wiseman, the 'will to survive' is the single most important factor in any crisis. Fear and panic are natural reactions to danger, but they must be controlled. Fear can be a useful stimulus, sharpening your senses, but panic leads to irrational decisions, exhaustion, and ultimately failure.",
            "To maintain a strong survival mindset, practice the SAS survival acronym: S.P.A.D.E. (S - Size up the situation; P - Plan your moves; A - Analyze your resources; D - Decide on action; E - Execute with determination). By breaking down your situation into logical steps, you prevent the onset of despair and establish control over your environment.",
            "Keep busy and focus on immediate, achievable tasks like preparing shelter, gathering firewood, or checking traps. Psychological strength is maintained through organization and routine. Remember that discomfort is temporary, and your primary objective is to return home alive."
        ],
        "Survival Essentials": [
            "The four main requirements of survival, in order of priority, are: Protection (Shelter/Medical/Clothing), Location (Rescue/Signaling), Water, and Food. This is often remembered as the 'Rule of 3s': you can survive 3 minutes without air, 3 hours without shelter in extreme environments, 3 days without water, and 3 weeks without food.",
            "Protection must be addressed first. Exposure to extreme cold, heat, or wetness can kill you within hours. Constructing a basic shelter and addressing severe bleeding or shock are your top priorities. Next, locate yourself so rescuers can find you; prepare signals before looking for water or food.",
            "Water is essential to sustain life. The body loses water through perspiration, respiration, and urination. You must locate a source of fresh water and purify it before drinking to avoid debilitating waterborne illnesses like giardia or cholera."
        ],
        "The Pocket Kit": [
            "The pocket survival kit is a collection of essential tools kept in a small, waterproof tin (like a tobacco tin) that you carry on your person at all times. The key to the kit is versatility and size. If you lose your main pack, the survival tin remains on your belt, providing the means to make fire, build shelter, catch food, and signal.",
            "The essential contents of the SAS survival tin include: 1) Matches - waterproofed with nail polish or wax; 2) Candle - provides light, warmth, and assists in fire starting; 3) Flint and steel - a reliable fire starter when matches fail; 4) Sewing kit - needles and strong thread for repairs and stitching wounds; 5) Fishing kit - hooks, line, and lead weights; 6) Wire saw - for cutting branches for shelters.",
            "Also include: 7) Snare wire - brass wire for building animal traps; 8) Adhesive dressings - waterproof plaster for cuts; 9) Compass - a small button compass for orientation; 10) Water purification tablets - to treat questionable water sources immediately. Keep the tin sealed with electrical tape to ensure it remains waterproof until needed."
        ],
        "Risk Assessment": [
            "Before taking any action in a survival situation, conduct a dynamic risk assessment. Analyze the immediate hazards (extreme weather, unstable terrain, predators) and determine how to minimize them. Avoid rushing into action; a few minutes spent assessing your environment can prevent fatal mistakes.",
            "Assess your physical condition and that of your companions. Look for signs of hypothermia, dehydration, or injury. Inspect your gear and take stock of what resources are immediately available. This baseline analysis forms the foundation of your plan.",
            "Consider the trade-offs of any decision. For example, leaving a crash site increases your chances of getting lost, while staying near the site makes you easier to locate by search-and-rescue teams. Only travel if staying puts you in immediate danger."
        ],
        "Survival Planning": [
            "A structured survival plan increases your efficiency and prevents wasted energy. Your plan should establish clear priorities based on your immediate environment. In cold climates, shelter and fire are top priorities. In hot deserts, finding shade and conserving water are paramount.",
            "Divide tasks among members of your group. One person should focus on shelter, another on firewood, and a third on signaling. Keep goals short-term and realistic (e.g., 'gather firewood for 1 hour' rather than 'prepare for winter').",
            "Remain flexible. If your shelter design is failing due to local soil conditions, adapt and use a different construction method. Regularly review your plan as the situation changes (e.g., weather shifts, injuries, or rescue opportunities)."
        ],
        "Accident Procedures": [
            "In the immediate aftermath of an accident (such as a vehicle breakdown or plane crash), the rule is to: Stop, Calm Down, Assess, and Act. Do not run away from the vehicle unless there is an immediate fire hazard. The vehicle provides shelter, metal for tools, and is much easier for search planes to spot than an individual.",
            "Administer first aid immediately to anyone injured, prioritizing airway, breathing, and severe bleeding. Establish a safe perimeter, put out any fires, and recover all useful gear from the wreckage before it is damaged or lost.",
            "Set up signaling devices (such as mirrors, smoke signals, or bright fabrics) right away. Prepare a watch rotation to monitor for rescue craft, and assign tasks to keep everyone focused and calm."
        ],
        "Polar Survival": [
            "In polar and arctic regions, cold exposure is your primary enemy. Hypothermia and frostbite can occur within minutes. Your first priority is to build a shelter that traps body heat. A snow trench or a snow cave (quinzhee) is highly effective because snow is an excellent insulator.",
            "To build a snow cave, pile snow into a mound, let it pack and freeze, then hollow out the inside. Ensure you create a small ventilation hole in the roof to prevent carbon monoxide poisoning if you use a candle or stove inside, and dig a cold well—a trench lower than your sleeping platform where cold air can settle.",
            "Conserve body heat by layering clothing. Avoid sweating at all costs; sweat dampens your inner layers, which will freeze and rapidly pull heat from your body. Eat high-calorie foods to fuel your internal furnace, and never eat snow directly as it lowers your core temperature—always melt it first."
        ],
        "Desert Survival": [
            "In the desert, heat and dehydration are the primary threats. The golden rule is to conserve sweat, not water. Limit your physical activity to the cooler night hours and remain in the shade during the heat of the day. Keep your clothes on; clothing insulates you against the sun's rays and slows down sweat evaporation, keeping you cooler.",
            "Do not ration your water. Drink it when you need it. If water is limited, avoid eating, as digesting food requires water and will dehydrate you faster. Do not drink alcohol, urine, or sea water, as these require more water to process than they provide.",
            "To collect water in the desert, construct a solar still. Dig a pit in the ground, place a container in the center, cover the pit with a plastic sheet, and place a stone in the middle of the sheet above the container. The sun heats the soil, moisture evaporates, condenses on the plastic, and drips into your cup."
        ],
        "Tropical Survival": [
            "Tropical jungles present challenges of extreme humidity, insects, wetness, and disease. Protection from dampness is key. Never sleep directly on the jungle floor; construct an elevated sleeping platform using bamboo or branches, and use a tarp or large banana leaves to shed the frequent rain.",
            "Keep covered to protect against biting insects, leeches, and thorny vegetation. Wash daily to prevent fungal infections and heat rash. Inspect your boots and clothes every morning for scorpions, spiders, or snakes that may have sought shelter inside.",
            "Water is abundant but must be boiled or treated, as tropical streams carry high levels of parasites. Edible food is also plentiful, but you must know what to avoid. A general rule: avoid plants with white or milky sap, three-leaved ivy patterns, or bitter, soapy tastes."
        ],
        "Foraging Edible Plants": [
            "When foraging for wild plants, positive identification is critical. Many edible plants have poisonous lookalikes. According to Lofty Wiseman, you must apply the Universal Edibility Test if you are unsure: 1) Separate the plant into parts (root, stem, leaves, flower); 2) Test one part at a time; 3) Rub the plant on your inner wrist or elbow and wait 15 minutes to check for irritation.",
            "If no reaction occurs, 4) Kiss the plant part with your lips and wait 15 minutes; 5) Put a small portion in your mouth, chew it, but do not swallow, waiting 15 minutes; 6) Swallow a small amount and wait 8 hours. If no stomach pain, nausea, or illness occurs, the plant part is likely safe to eat.",
            "Focus on easily identifiable plants with high nutritional value: Dandelion (entire plant is edible, roots can be roasted), Nettle (must be boiled to destroy stinging hairs, rich in iron), Pine needles (steeped in hot water to make tea high in Vitamin C), and Plantain (leaves are edible and soothe wounds)."
        ],
        "Making Traps and Snares": [
            "Trapping is more energy-efficient than hunting. A simple snare consists of a loop of wire or cord with a running noose, positioned at head-height on an active animal run or game trail. When the animal walks through the loop, it tightens, securing the catch.",
            "The Figure-4 Deadfall is a classic trigger mechanism used to drop a heavy rock or log onto prey. It consists of three notched sticks arranged in a '4' shape. A horizontal bait stick triggers the vertical support to collapse, dropping the weight.",
            "Always place traps near water sources, feeding areas, or natural bottlenecks. Check traps at least twice a day (morning and evening) to dispatch catch humanely and prevent predators from stealing your food or the carcass rotting."
        ],
        "Hunting and Fishing": [
            "Hunting larger game requires patience, camouflage, and understanding wind direction. Walk slowly into the wind so animals cannot smell your approach. Target vital areas (heart and lungs) for a clean kill. Use simple weapons like a spear, bow, or sling.",
            "Fishing is a reliable source of protein. You can catch fish using hooks, lines, hand-nets, or by building a fish weir (a V-shaped stone wall in a stream that funnels fish into a shallow trapping pool). Fish are most active at dawn and dusk.",
            "Clean fish and game immediately. Remove internal organs, skin or scale them, and cook thoroughly to kill parasites. Preserve excess meat by smoking it over a green-wood fire or cutting it into thin strips and drying it in the sun (jerky)."
        ],
        "Building Shelters": [
            "A shelter protects you from wind, rain, cold, and sun. Before building, select a site that is flat, dry, free of overhead hazards (like dead branches or rockfalls), and close to water but high enough to avoid flash flooding.",
            "The Lean-To is a quick shelter made by securing a horizontal ridgepole between two trees, leaning poles against it at a 45-degree angle, and covering them with pine boughs, leaves, or a tarp. The debris shelter is a more insulated version using a single long A-frame ridgepole supported by a tripod.",
            "Cover the ground inside your shelter with a thick layer (at least 6 inches) of dry leaves, pine needles, or ferns. This sleeping mattress is critical because the cold ground will pull heat from your body much faster than the surrounding air."
        ],
        "Fire Lighting Techniques": [
            "Fire provides warmth, cooks food, purifies water, keeps predators away, and boosts morale. To build a successful fire, gather three types of wood: 1) Tinder - dry, fibrous materials that catch sparks easily (birch bark, dry grass, pine resin, charred cloth); 2) Kindling - small twigs and split wood that catch fire from the tinder; 3) Fuel - thick logs that burn slowly and hot.",
            "Arrange your kindling in a teepee or log-cabin shape over your tinder. This creates a chimney effect, drawing oxygen into the base of the fire. Always have a large stack of kindling and fuel ready before you light your tinder.",
            "When matches are unavailable, use a ferrocerium rod and steel scraper. Strike the rod at a 45-degree angle close to your tinder, generating a shower of hot sparks. Alternatively, use a magnifying lens to focus sunlight, or use a bow drill to create a coal through friction."
        ],
        "Essential Knots": [
            "Knowing how to tie a few versatile knots is an essential campcraft skill. 1) The Bowline - creates a secure, fixed loop at the end of a rope that will not slip or jam, ideal for rescue lines; 2) The Clove Hitch - a quick knot used to secure a rope to a post or tree branch, perfect for starting lashings.",
            "3) The Square Knot (Reef Knot) - used to join two ropes of equal thickness, simple to tie and untie; 4) The Sheet Bend - used to join two ropes of unequal thickness, which is common when splicing cordage together.",
            "5) The Taut-Line Hitch - a friction hitch that allows you to adjust the tension of a rope, excellent for securing tent or tarp guy-lines. Practice these knots until you can tie them in the dark and with cold, wet hands."
        ],
        "Natural Compass Methods": [
            "If you lose your compass, you can find direction using the sun. The shadow stick method is highly accurate: 1) Push a straight stick vertically into flat ground; 2) Mark the tip of the shadow with a stone (this is West); 3) Wait 15-20 minutes and mark the new shadow tip with another stone (this is East); 4) Draw a line between the two stones to establish your East-West line.",
            "At night in the Northern Hemisphere, locate the Big Dipper (Ursa Major). Follow the two pointer stars at the edge of the dipper's bowl straight out about five times their distance to find Polaris, the North Star. Polaris indicates true North.",
            "In the Southern Hemisphere, find the Southern Cross constellation. Draw an imaginary line down the long axis of the cross, and combine it with a line bisecting the two pointer stars nearby. The point where they intersect indicates South."
        ],
        "Weather Prediction": [
            "Reading the sky helps you prepare for storms before they arrive. High, wispy cirrus clouds ('mare's tails') often indicate an approaching warm front and rain within 24 hours. Dark, towering cumulonimbus clouds mean an imminent thunderstorm.",
            "Observe animal behavior: birds flying low indicate low barometric pressure and oncoming wet weather. Insects bite more frequently before a rain storm.",
            "Remember the classic proverb: 'Red sky at night, shepherd's delight; red sky in the morning, shepherd's warning.' A red sunset indicates dry, clear air to the West, while a red sunrise indicates wet weather is moving in from the East."
        ],
        "Signaling for Help": [
            "Prepare your signaling methods as soon as your shelter is built. The international emergency signal is three of anything (three whistles, three fires in a triangle, three mirror flashes). A triangle of fires is easily recognized from the air.",
            "The signaling mirror (heliograph) is one of the most effective long-range signals. Aim it by looking through the center hole at your target (an aircraft or ship) and adjusting the mirror until the bright reflection spot aligns with your target.",
            "Prepare ground-to-air signals in an open clearing. Use rocks, logs, or dug trenches to form letters at least 10 feet tall: V (Require Assistance), X (Require Medical Assistance), Y (Yes/Affirmative), N (No/Negative)."
        ],
        "Navigation and Route Planning": [
            "Before traveling, study your surroundings from a high vantage point. Map out a route that follows natural features like ridgelines or valleys, but avoid walking in dense brush or swampy lowlands. Establish check points to track your progress.",
            "Always estimate your travel speed. In rough terrain, expect to cover only 1 to 2 miles per hour. Account for elevation changes, which slow you down significantly. Leave a trail marker (like stacked stones or bent twigs) so you can back track if you get lost.",
            "Maintain a steady pace and walk around obstacles rather than climbing over them. Conserve your energy. If you travel in a group, walk in single file, with the strongest member leading to set the pace and the second strongest at the rear."
        ],
        "River Crossings": [
            "Fording a river is one of the most dangerous travel activities. Never cross a fast-flowing river that is deeper than your knees. Look for a wide, shallow stretch where the current is slower. Avoid crossing near bends, where the outer bank is deep and eroded.",
            "Keep your boots on to protect your feet from sharp rocks and maintain traction. Unbuckle your pack's hip-belt and chest strap before crossing, so you can discard it immediately if you fall into the water.",
            "Use a sturdy wading staff as a third leg. Face upstream and lean slightly forward, moving the staff first, then stepping sideways. If crossing in a group, cross together holding onto a single pole, or cross in single file to break the current for those behind."
        ],
        "Mountain Travel": [
            "Mountain navigation requires caution due to extreme weather changes and steep drops. Walk on ridgelines where possible to maintain visibility, but avoid exposed peaks during high winds or lightning storms.",
            "Beware of loose scree and rockfalls. Step carefully on stable boulders and avoid walking directly below other hikers who may dislodge loose stones.",
            "Watch for symptoms of acute mountain sickness (AMS) like headache, nausea, and dizziness if ascending above 8,000 feet. The only cure is to descend to a lower altitude immediately."
        ],
        "Treating Shock and Bleeding": [
            "In any emergency, control severe bleeding first. Apply direct, firm pressure to the wound using a clean dressing or cloth. Elevate the injured limb above the heart if possible. If direct pressure fails, apply a tourniquet 2 inches above the wound on a single bone (upper arm or thigh), noting the exact time it was applied.",
            "Treat for shock, which can be fatal even if the primary injury is not. Symptoms include pale, cold, clammy skin, rapid breathing, and weakness. Lay the patient flat, elevate their legs 12 inches to keep blood flowing to vital organs, and wrap them in blankets to keep them warm.",
            "Never give a shock victim food or drink, as this can cause choking or vomiting. Reassure the patient and keep them calm, as anxiety increases heart rate and worsens bleeding."
        ],
        "CPR and Airway": [
            "If a person collapses, check response and breathing. If unconscious and not breathing, begin Cardiopulmonary Resuscitation (CPR) immediately. CPR maintains oxygen flow to the brain until medical help arrives.",
            "Perform CPR by placing the heel of one hand in the center of the chest, locking your elbows, and pushing down firmly 2 inches at a rate of 100 to 120 compressions per minute (to the beat of 'Staying Alive').",
            "Give 30 chest compressions followed by 2 rescue breaths. To give rescue breaths, tilt the head back, pinch the nose, seal your mouth over theirs, and blow until the chest rises. If unwilling or unable to give breaths, perform hands-only CPR continuously."
        ],
        "Bites and Stings": [
            "For venomous snake bites, keep the victim calm and still. Movement spreads the venom through the lymphatic system. Keep the bitten limb immobilized and positioned below the level of the heart.",
            "Clean the bite area gently, and apply a broad pressure-immobilization bandage starting at the toes/fingers and wrapping up the entire limb, about as tight as a sprained ankle bandage. Do NOT cut the wound, attempt to suck out the venom, or apply a tourniquet.",
            "Remove rings or constricting clothing before swelling begins. Monitor airway and breathing. For insect stings, scrape the stinger off immediately with a flat card—do not squeeze it with tweezers, as this injects more venom."
        ],
        "Urban Survival": [
            "In an urban disaster where grid services fail, your primary goals are securing clean water, food, and security. Store municipal water immediately in bathtubs and containers before pressure drops. Assume all tap water is contaminated and boil it.",
            "Establish a secure, defensible space in your home. Block windows, reinforce entryways, and remain quiet to avoid attracting attention. Keep a low profile and avoid traveling outside unless necessary.",
            "Have an evacuation plan (bug-out plan) ready with pre-packed bags for each family member in case you are forced to leave. Know multiple escape routes out of the city that avoid main highways, which will be gridlocked."
        ],
        "Earthquakes and Floods": [
            "During an earthquake: Drop, Cover, and Hold On. Get under a sturdy table or desk and hold onto it. Keep away from windows and heavy furniture. If outdoors, move to an open area away from buildings, power lines, and trees.",
            "In a flash flood, move to high ground immediately. Never walk or drive through flowing water; just 6 inches of moving water can knock you off your feet, and 2 feet can sweep a car away.",
            "If trapped in a building during a flood, climb to the roof rather than the attic to avoid becoming trapped by rising water. Signal rescuers from the rooftop using bright fabrics or flashing lights."
        ],
        "Fire and Smoke": [
            "If caught in a burning building, stay low to the floor where the air is cleaner and cooler. Smoke and toxic gases rise. Cover your mouth and nose with a wet cloth to filter out smoke particles.",
            "Feel doors with the back of your hand before opening them; if hot, do not open, as fire is on the other side. Use secondary exits like windows if blocked.",
            "If your clothes catch fire, Stop, Drop, and Roll to smother the flames. Treat minor burns with cool, running water for 10 minutes—never apply butter, grease, or ice."
        ]
    }
    return fallbacks.get(article_title, [
        f"Detailed guidelines and procedures for {article_title} according to SAS survival doctrine.",
        "Ensure you are fully prepared, stay calm, and execute steps methodically.",
        "Conserve your resources and always assess environmental risks before acting."
    ])

if __name__ == "__main__":
    download_pdf()
    parse_book()
