import json
import os

JSON_OUTPUT_DIR = "HowToSurvive.Core/Resources"
JSON_OUTPUT_PATH = os.path.join(JSON_OUTPUT_DIR, "survival_content.json")

structured_chapters = [
    {
        "title": "Essentials",
        "description": "The absolute foundation of survival: the PLAN doctrine, medical self-care, health checks, route planning, clothing, pack stowing, and off-grid communication.",
        "articles": [
            {
                "title": "The Will to Survive & PLAN",
                "subtitle": "Mindset, priorities, and emergency medical monitoring.",
                "imageName": "essentials.jpg",
                "textSections": [
                    """The human species has established itself in almost every corner of the Earth. Even in territories too inhospitable to provide a regular home, mankind has found a way to exploit its resources, whether by hunting or by taking wealth from the ground, and has often pitted its skills against nature simply for the satisfaction of doing so. Almost everywhere nature provides the necessities for survival. In some places the provision is abundant, in others very meagre and it takes common sense, knowledge and ingenuity to take advantage of the resources available. Even more important is the will to survive. Men and women have shown that they can survive in the most adverse situations, but they have done so because of their determination to do so - without that, the skills and knowledge in this book will be of little use if you find yourself really up against it.""",
                    """Survival is the art of staying alive. Any equipment you have must be considered a bonus. You must know how to take everything possible from nature and use it to the full, how to attract attention to yourself so that rescuers may find you, how to make your way across unknown territory back to civilization, if hope of rescue is not on the cards, navigating without map or compass. You must know how to maintain a healthy physical condition, or if sick or wounded heal yourself and others. You must be able to maintain your morale and that of others who share your situation.""",
                    """Lack of equipment should not mean that you are unequipped, for you will carry skills and experience with you, but those skills and experience must not be allowed to get rusty and you must extend your knowledge all the time. We are all used to surviving on our home ground - though we may not think of our lives in that way - but the true survivor must learn how to survive when taken from familiar surroundings or when those surroundings are drastically changed by man or nature.""",
                    """Anyone, young or old, from whatever walk of life, can find him- or herself in a survival situation. As more and more people fly the globe, sail small boats or cross the sea in large ones, walk the hills and climb mountains and take their holidays in ever more exotic places, the situations to which they could become exposed are increasingly diversified. But survival skills are not only concerned with the extremes of the air crash on a mountain peak, a shipwreck in the tropics or a vehicle breakdown in the middle of a desert. Every time you fasten a seat belt in a car you are giving yourself a greater chance of survival. Checking each way before crossing a road or ensuring that an open fire is safe before you go to bed are survival techniques that you carry out instinctively. It is these habits of mind that you must develop as much as acquiring skills.""",
                    """The main elements of survival are Food, Fire, Shelter, Water, Navigation and Medicine. To put these in order of priority we use the acronym PLAN. No matter where you are in the world this will never change be it the Arctic, desert, jungle, sea or seashore.\n\n• P - for Protection: You must ensure that you are protected from further danger, i.e. impending avalanche, forest fire or exploding fuel. Always stay on the scene of the incident as long as it is safe to do so and then make sure you are protected from the elements. This means making a shelter and often lighting a fire. There are several reasons why you should always stay at the scene: 1) You can utilize the wreckage for shelter, signaling etc. 2) It's a bigger signature on the ground, making it easier to find. 3) There are probably injured people that cannot be moved. 4) By staying where you are you conserve energy. 5) Because you have booked in and out and have stayed on the route, rescue time will be minimal.\n\n• L - for Location: The next step after building a shelter is to put out emergency signals. You must draw attention to your position. Do this as soon as possible to help the rescuers.\n\n• A - for Acquisition: While waiting to be rescued, look for water and food to help supplement your emergency supplies.\n\n• N - for Navigation: Good navigation will keep you on route and will often avert a survival situation. But if you find yourself stranded, always stay where you are.""",
                    """Medical: You must become your own doctor and carefully monitor yourself at all times. Treat blisters as they occur, don't let them become septic. Keep an eye on your companions and deal with any unusual problems as they arise. If they are limping, falling behind, or behaving strangely, stop and treat immediately."""
                ]
            },
            {
                "title": "Preparation, Planning & Research",
                "subtitle": "Health preparation, terrain research, and group organization.",
                "imageName": "essentials.jpg",
                "textSections": [
                    """BE PREPARED: The Boy Scouts' motto is the right one. Anyone setting out on a journey or planning an expedition should follow it by discovering as much as possible about the situations likely to be faced and the skills and equipment called for. It is the most basic common sense to prepare yourself, to take appropriate gear and to plan as carefully as possible.""",
                    """Your kit could make the difference between failure and success, but, especially when back-packing, many people initially take too much and have to learn from bitter experience what they really need and what they could have done without. There is no fun in struggling with a huge pack full of superfluous items while wishing that you had a torch or can opener with you. Getting the right balance is not easy.""",
                    """Before any journey or expedition make a check list and ask yourself the following questions:\n- How long will I be away? How much food do I need for this period and do I need to carry water?\n- Have I the right clothing for the climate and enough of it? Is one pair of boots enough or, because of the surface conditions and the amount of walking, should I take a standby pair?\n- What special equipment do I need for the terrain?\n- What medical kit is appropriate?\n\nMake sure that you are fit enough for what you plan to do. The fitter you are, the easier and more enjoyable it will be. If you are going hill-walking, for instance, take regular exercise beforehand and wear in your hiking boots. Walk to and from work with a bag weighted with sand and get your muscles in condition! Mental fitness is another factor. Are you sure that you are up to the task, have prepared enough and have the equipment to accomplish it? Eliminate any nagging doubts before you set out.""",
                    """Always prepare contingency plans in case anything goes wrong. Things rarely go quite according to plan. What will you do if you are prevented from achieving your objective? What will you do if a vehicle breaks down, or if weather or ground conditions prove more severe than anticipated? If in a party, how will you regroup if separated? What happens if someone becomes ill?""",
                    """Health checks: Have a thorough medical check and ensure that you have all the necessary injections for the territories through which you intend to travel. There are vaccinations against yellow fever, cholera, typhoid, hepatitis, smallpox, polio, diphtheria and tuberculosis, and an anti-tetanus injection is a must. Allow plenty of time for jabs - the full anti-typhoid protection requires three injections over the course of six months. If travelling through a malarial region take an adequate supply of anti-malaria tablets. You must start taking these two weeks before your journey, so that resistance is in the system before you arrive in the risk area, and should keep taking them for a month after your return.""",
                    """Go to the dentist and get your teeth inspected. Teeth that normally do not hurt can cause considerable pain in cold climates. At least start out in sound condition. Make up a medical kit that will cover all your likely needs and, if travelling with a group, ensure that any particular individual medical needs are covered. If a potential member of the group is not fit, should they be dropped from the party? A difficult decision among friends, but one that must be made for it is best in the long run. Consider, too, the ability of each member of the group to deal with the challenge of hardship, risk and endurance that you may meet. Stress often brings out the unknown side of a person, and in planning any group expedition some form of selection is needed when choosing your companions.""",
                    """RESEARCH: You can never have too much information about a place you are going to. Contact people who know it already, read books, study maps - and make sure that you have reliable and up-to-date maps to take with you. Find out about the local people. Are they likely to be friendly and helpful or are they wary of strangers? Are there local customs and taboos? The more detailed your knowledge of the way people live - particularly in non-westernized societies, where life is linked much more closely to the land - the more survival knowledge you will have if you come to need it. Local methods of shelter building and fire making, wild foods, herbal medicines and water sources will be based on an intimate understanding of the surroundings.""",
                    """Study your maps carefully, get a feel for the land even before you see it and gain as much knowledge of the terrain as possible: river directions and speed of flow, waterfalls, rapids and difficult currents. How high are hills and mountains, and what are their slopes like - are they snow covered? Which way do the ridges run? What kind of vegetation can you expect, what species of trees and where? What might temperatures be and how different at day and night? When are first and last light? What is the state of the moon, the time and height of tides, the prevailing wind direction and strength? The weather that can be expected?""",
                    """PLANNING: For a group expedition get the members together for frequent discussions of what you aim to achieve. Nominate people for particular responsibilities: medic, linguist, cook, special equipment, vehicle maintenance, driver, navigator and so forth. Ensure that everyone is familiar with the equipment and that there are spares where needed - batteries, fuel and bulbs especially. Divide the project into phases: entry phase, objective and recovery. Clearly state the aim of each phase and work out a time scale. Plan for emergency procedures such as vehicle breakdown, illness and casualty evacuation.""",
                    """In estimating the rate of progress, especially on foot, allow plenty of time. It is always better to underestimate and be pleasantly surprised by doing better. Pressure to keep up to an over-ambitious schedule not only produces tension and exhaustion but leads to errors of judgement and risk-taking that are frequently the reason for things going wrong. You cannot carry all your water requirement with you but must replenish supplies as you travel. Water sources will be a major factor in planning any route.""",
                    """When the route is planned and agreed make sure that others know about it so that you can have expectations of rescue if anything goes wrong. If you are hiking in the hills inform the police and local mountain rescue centre. Tell them your proposed plan and give times of departure and expected arrival. If touring by car, log the route with the respective motoring organization. If sailing, check with coastguard and port authorities. Always make sure that someone knows what you are planning to do and when, and keep them informed at prearranged stages so that failure to contact will set alarm bells ringing. Boats and aircraft are strictly controlled in this respect and, if overdue, a search is raised and the route checked out, effecting rescue. Get into the habit of telling people where you are going and what time you expect to return or reach your next destination."""
                ]
            },
            {
                "title": "Survival Equipment & Pack Stowing",
                "subtitle": "Clothing selection, sleeping bags, packs, and stowing layout.",
                "imageName": "kit.jpg",
                "textSections": [
                    """EQUIPMENT: Being prepared for any eventuality is a tall order if you are on foot and have to carry everything you need yourself. Whatever you carry, you must ensure that it is up to the job, versatile and robust. It's a fine balance between what you would like to carry and what you must carry. When preparing for any adventure, you must take into consideration what the dangers are and how you can overcome these. This is what is called contingency planning. The climate, weather and time of year will all help you to determine what to carry, but you must ensure that everyone with you knows how to use and maintain the specialist kit you decide to take with you. Armed with information from your research you will be able to select your equipment, matching it to objectives and conditions.""",
                    """Clothing: The correct choice of clothing is so important. If you start out right the chances are that you will succeed. Man is a tropical animal and can only survive as we are born in the tropics. The moment we leave this area we have to provide our bodies with this tropical environment, hence the need for clothes. There is no heat in clothing, it only traps what the body produces.""",
                    """The wind and rain are the most dangerous elements in a temperate climate and the cold in extreme areas like the polar regions. If the heat that is trapped in the layers of clothing you are wearing is continuously being replaced by wind and rain, you are in danger of hypothermia. In cold climates layering is the answer so pull on a jersey if it turns cold and waterproofs if it rains. However if you wear an anorak while carrying a heavy pack, there is a danger of wearing through the shoulders and lower lumbar region allowing the ingress of water to soak the body. You need a change of clothing and additional warm garments for when you stop.""",
                    """In hot climates it is very difficult to get the balance right between comfort and practicality. There has always been a danger of overheating in extreme conditions caused by wearing heavy clothing while carrying out physical activities. When on the move wear the least amount of clothing possible and avoid walking in waterproofs if you are too hot, as the condensation generated will soak the inner layers. Clothing should give good protection and be well-fitting without being restrictive. It must keep you warm and dry but have plenty of ways to keep the body ventilated so you don't overheat (if it gets colder you can always put on more.)""",
                    """With all the great breakthroughs in recent years in fabric technology it is worth understanding the pros and cons of the different materials on offer. Gore-tex is an excellent material because it is breathable and so keeps you warm and dry while ventilating the body, but it does have limitations. Breathable materials can only work if they are kept clean. Once they get covered in mud and accumulate grime they are less effective. Gore-tex is not robust or hard-wearing and must be looked after. The best way to use Gore-tex is to walk or climb in windproof garments and when at rest, put on the breathable kit.""",
                    """Synthetic materials such as fleece are very popular and in certain conditions outperform natural materials like wool, down or cotton. Having a zipped front makes a fleece easy to put on and take off and they are also comfortable to walk in. Choose one that is windproof as this is often all that is needed in most conditions. If it gets colder they can be worn under an outer waterproof giving good insulation. There are also garments which act like an animal's skin, using the buffalo system. They have a windproof outer with a man-made fibre pile inside. When wet they perform like a wetsuit. They are good for walking in cold/wet conditions, and are ideal for boating, canoeing and caving.""",
                    """As for natural fabrics, wool is still an excellent choice for jumpers as it retains its warmth even when wet. The downside is it stretches and becomes heavy, so it's not a good choice for socks. Down is the warmest and lightest of all natural insulating materials but loses all its heat-retaining qualities when wet. Cotton acts as a wick and draws up all the moisture. So it's good to wear in the tropics but not in the cold/wet regions.""",
                    """Footwear is an important consideration and for serious walking give your feet priority. Break in new boots gradually and harden up your skin with surgical spirit, starting two weeks before you set off.""",
                    """For the enthusiast the major consideration in choosing clothing is cost. Surplus stores are very popular for the younger adventurer who loves to parade in camouflage clothing. Although ex-military kit is good, and cheap, it is already obsolete. The big drawback of wearing camouflage or dark clothing is the risk of not being found when lost. The reason soldiers wear it is so they cannot be seen which contradicts what you are trying to do if you get into trouble. Most outdoor clothing is blue or orange, some is reversible, so a contrasting colour will always stand out wherever we find ourselves. Buy the best clothing you can afford, and take advice from a reputable outdoor shop. Remember: There is no such thing as bad weather, only bad clothing.""",
                    """Sleeping bags: Two types are generally available. One kind uses hollow fill, man-made fibre, the other (and more expensive) is filled with down. Down is very light and gives much better insulation - provided it stays dry. If it gets wet it loses all its insulating properties and is very difficult to dry out. For conditions that are likely to be wet the man-made fibre will therefore be the better choice. Avoid getting your sleeping bag wet, however, as sleep will be seriously affected. Excellent bivouac bags made of breathable material are also available that will keep you dry in place of a tent, but in the long term you cannot beat a tent which can also be used for cooking and communal activities. Keep your sleeping bag inside the bivy bag and stow it inside a compression sack to make it as small as possible. Keep the bag clean and use a kip mat or poncho to lie on.""",
                    """Packs: You need a strong and comfortable back-pack to carry all your clothing and equipment. Choose the very best you can afford. It should have tough and fully adjustable webbing, well secured to the pack's frame or fabric. Heavy loads can quickly loosen poorly made webbing. It must have a comfortable hip belt. The secret of wearing a pack is to take the weight securely on the hips - the body's strongest pivot - not on the shoulders and back, which quickly strain and tire. Do you want a pack with an external or an internal frame? Internal frames are lighter and make a pack more easy to stow, but external frames are stronger, ensure a more even distribution of the load and are especially useful for awkward or heavy equipment - including, in an emergency, a sick or injured person. A good external frame should carry the pack high up on your body, putting less strain on hips and shoulders, and it should be designed to allow an airspace between the pack and your back to minimise contact perspiration. A frame adds weight and is more prone to snag on rocky projections or branches, making progress through dense vegetation a little more difficult, but its advantages more than compensate. Finally, choose a pack made from a tough, waterproof fabric, preferably with a lace-up hood inside the main sack to prevent water leaking in and the contents falling out. Side pockets are always useful, but they must have secure zips rather than straps or drawstrings, which do not hold equipment safely.""",
                    """Stowing kit: If you expect to get wet, stow everything in polythene bags. Pack so that you know where everything is and so that the first things you need are not buried at the bottom. The sleeping bag is probably the last thing you need so that goes at the bottom. Your tent should be on the top, so should heavy kit such as radios, which are more easily carried there - though try not to make the pack too high, if you have to cope with strong winds, for a very high pack will be more difficult to balance and you will expend a lot of energy just keeping upright. Pack a stove and brew-kit in a side pocket so that you have easy access when you halt. Make sure that foodstuffs that can be easily squashed or melted are in suitable containers. In a warm climate you can carry food to eat cold and make plenty of hot drinks. In a cold climate make sure that you have plenty of fats and sugars. The exact rations depend on your taste, but they should be chosen to give a good balance of vitamins, minerals, fats, proteins and carbohydrates. Take into account the extent to which you will be able to live off the land and carry a supply of anything unlikely to be available locally."""
                ]
            },
            {
                "title": "Off-Grid Communications & Tech",
                "subtitle": "Operating GPS, radios, altimeters, and mobile devices in the wild.",
                "imageName": "essentials.jpg",
                "textSections": [
                    """G.P.S: A G.P.s (Global Positioning System) is an excellent piece of equipment and has taken a lot of skill away from the navigator. Basically these systems receive radio signals from satellites and can locate your current position, anywhere in the world, and are relatively easy to use. It is also useful to note that they are reported to have 95% accuracy rate. However, in order to work, the satellite transmission must not have any obstructions in its way, such as a tree branch or movement, so to receive a clear signal you need to be standing still and out in the open. However, if we depend solely on technology our basic skills will suffer and we will become unstuck if it becomes unserviceable or is lost. G.P.s is not effective unless you can identify where you are so stick to the basics. Map read and navigate normally and use the G.P.s to confirm your navigation or correct it.""",
                    """When looking to buy a G.P.s there are several considerations to think about: what you'll be using it for - if walking you will want the unit to be as light as possible and compact; where you'll be using it; and if you need it to be waterproof (this is usually a feature of the heavier models with extra gadgets). Battery life should also be taken into account. Some G.P.s are more complicated than others so choose the model that you're happy with. Most have the facility of being able to put in way points (at sea this means the eastern and northern coordinates and on land these can be campsites, rock formations etc) and there are many convenient hand-held versions and some are even featured on watches. There is always a danger with any battery-operated equipment that it lets you down when you need it most. Batteries always discharge faster in the cold and with age. Recharging facilities are difficult in the wilderness, and bad connections caused by constant abuse while on the move are a real menace. Carry the G.P.s around the neck tucked under the jacket. This will minimize the risk of damage and protect it from the weather. Don't place it in your pack or leave it lying around. When planning your route from the map, choose prominent points that can be used as emergency rendezvous. Have these at regular intervals, preferably every hour of walking. Enter these into the G.P.s and they will keep you on track. Once entered they will offer information as to where you are in relation to these points and tell you what direction to take to reach them.""",
                    """Radios: For a long expedition in remote territory a radio is a necessity. They tend to be expensive but are well worth the cost; if you cannot afford the radio, you cannot afford the expedition. Choose a model with the least amount of channels available to suit your particular needs. The trouble with multi-channeled sets is that people get confused and tend to use the wrong ones. Have a working channel that everyone uses at established schedules. Have a priority channel that you can switch to in an emergency so no one will break into your transmissions. If working with coastguards/forest rangers etc make sure that your radio is compatible and you know the emergency channel (channel 16); knowing the frequency of the World Service is also useful. Keep your radio in a safe place, ideally on a person and not in a pack. Prearrange a signals plan with scheduled calls morning and evening, especially when working in a large party. A signals plan entails people manning the radio at base and two-way communication is easily made. Make sure that the chosen frequencies will work in the areas you are going to, and that at least two people in the party are familiar with the working of the radio. Every group on the ground must be in radio contact with base. They should be allocated a call sign and frequency, and a schedule of calls to be made.""",
                    """Discourage groups from talking to each other without going through base. This will cause great confusion if not controlled. Listen out before transmitting otherwise you will interfere with other stations. Everyone has verbal diarrhoea when they talk on the radio so write down what you want to say before making contact and have pencil and paper ready to make notes and take instructions. This will help to keep transmissions to a minimum and preserve the batteries. RSVP Rules for clear transmissions:\n- Rhythm: Don't talk like a Dalek\n- Speed: Talk slowly\n- Volume: Speak softly\n- Pitch: Pitch voice higher than normal and use the phonetic alphabet when spelling out place names""",
                    """In the evening give a situation report to base with your location, what you have done and your future intentions. In the morning receive an update on weather conditions, a time check and other information that base can give you. A noon time call can be used to confirm your position. BE AWARE: Signals will be weak in gullies and valley bottoms; good signals will be received on top of high ground or across water. If you are tackling a dangerous aspect of the expedition you may want to arrange that base listen out for additional calls so that in an emergency you can call for help and get a response immediately. An emergency plan should always be put into operation if two consecutive calls are missed. Even if all is well, if you have not been able to make contact this will be treated by base as an emergency. You must return to or stay at the last reported location and await contact. If you are really in trouble base will know where you last were and where you planned to go to, and the rescue mission can follow.""",
                    """Mobiles: The mobile phone is one of the great inventions of the twentieth century. In an emergency situation it can be a real life-saver. On expeditions where the radios have failed due to bad weather or the location of the victims, a mobile phone has been used to raise the alarm. A group on Everest got into trouble as they started their descent after summitting. They tried many times to raise base camp but without success. The leader phoned his wife in Hong Kong on a mobile phone and reported their situation. She then alerted Kathmandu, who in turn alerted base camp, Everest and effected a rescue. Some phones are better than others so it's worth doing some homework; it's also essential to check the network coverage with the service provider before going abroad. Keep one in the car, they are priceless when help is required and a cigarette lighter is a convenient charger for the battery, providing you have an adaptor. Charging can be a problem in the wild so use your phone wisely, but small, hand-held manual chargers can now be bought to recharge batteries. With radios and phones it takes less power to listen than to transmit, so make your call and listen for a reply. If nothing is heard don't despair. With all electrical kit water/moisture is the enemy. The transmitting side may be working but not the receiving side. Make short calls on the hour. Someone may be picking up your signal so don't give up. Once you receive confirmation that the rescue is under way keep the radio/phone on listening watch.""",
                    """Altimeters & Improvisation: In mountainous areas an altimeter is a good idea. Relating the height recorded can help you determine what contour you are on, and how far it is to the ridge or summit. You never have enough kit in an emergency. It's nice to have G.P.s, phones etc but you can still manage without as long as you have the ability to improvise and adapt. Learn the basics and use technology for confirmation, rather than depending on them whole heartedly. Communication is of the highest importance and must be given priority. It is a safer place as long as you can communicate with the outside world. Many survival sagas begin because of bad navigation, with people getting lost. Always plan for the worst eventuality. BE AWARE: When things go wrong it's a series of events that compound the situation. The weather deteriorates, the radio is broken, the mobile phone is lost. Two people have multiple injuries and you are out of water. Never give in. Plan for these situations and you will come through, but always have a contingency plan. Imagine the worst possible scenario, and train for it."""
                ]
            },
            {
                "title": "The Survival Knife, Tin & Pouch",
                "subtitle": "Visual specifications and contents of your most critical gear.",
                "imageName": "knife.jpg",
                "textSections": [
                    """THE SURVIVAL KNIFE: The survival knife is your single most critical piece of equipment. It must be a fixed-blade knife with a robust, single-edged blade about 10-15 cm (4-6 inches) long, a thick spine (4-6 mm), and a full tang (meaning the steel of the blade extends all the way through the handle). Avoid folding pocket knives for primary survival tasks; the locking mechanism can easily fail or collapse on your hand under the impact of heavy chopping or batoning (using a log to hammer the knife through wood to split it). A single-edged blade is safer because it allows you to press your hand or a wooden baton against the spine for leverage. Keep it razor-sharp and lightly oiled to prevent rust.""",
                    """THE SURVIVAL TIN: A basic survival kit should be packed inside a small, flat metal container (such as a tobacco or mint tin). Seal the joint of the lid with a strip of waterproof adhesive tape; this keeps the contents dry and holds the lid secure. The tin itself is highly versatile: it can be polished to serve as a signal mirror, and its metal body can be used to boil small amounts of water or char wood/cloth. Pack the tin as tightly and logically as possible, placing cotton wool on top to prevent items from rattling and to act as instant tinder.
Essential Survival Tin contents:
1. Matches: Waterproofed by dipping the heads in melted paraffin wax.
2. Candle: Shaved down to fit; a source of fuel, fat/wax, and long-burning light.
3. Flint & Striker: A reliable spark-throwing ferrocerium rod.
4. Button Compass: A small, liquid-filled compass for navigation.
5. Snare Wire: Flexible brass wire (60-90 cm) for trapping small game.
6. Sewing Kit: Heavy needles and strong thread.
7. Fishing Tackle: Line, hooks, lead sinkers, and swivels.
8. Wire Saw: A flexible wire saw with finger rings for cutting shelter poles.
9. Scalpel Blades: Two scalpel blades of different sizes for skinning and fine work.
10. Adhesive Plasters: Waterproof dressings for cuts.
11. Water Sterilizer: Chlorine or iodine tablets.
12. Condom: A clean, durable water container holding up to 1 liter of water.""",
                    """THE SURVIVAL POUCH: For items too large to fit in a pocket tin, carry a durable canvas or nylon pouch threaded onto your belt. This pouch should never be detached from your person. It must contain:
1. Signal Mirror (Heliograph): A high-grade mirror with a central sighting hole for catching the sun and signaling aircraft or search parties.
2. Whistle: A pea-less survival whistle for signaling rescuers in thick cover or fog.
3. Headlamp or Torch: A compact LED light source with spare batteries.
4. Water Purification Straw: A portable filter straw to allow drinking directly from streams.
5. Emergency Bivouac Bag: A lightweight, heat-reflective plastic bag to shield your body from wind and hypothermia.
6. Tinder Bundle: Cotton balls soaked in petroleum jelly (Vaseline), kept in a waterproof film canister.
7. Rations: High-energy food bars, dextrose tablets, or salt packets."""
                ],
                "items": [
                    {
                        "name": "1. Matches",
                        "description": "Waterproofed by dipping the heads in melted paraffin wax.",
                        "imageName": "matches.jpg"
                    },
                    {
                        "name": "2. Candle",
                        "description": "Shaved down to fit; a source of fuel, fat/wax, and long-burning light.",
                        "imageName": "candle.jpg"
                    },
                    {
                        "name": "3. Flint & Striker",
                        "description": "A reliable spark-throwing ferrocerium rod.",
                        "imageName": "flint.jpg"
                    },
                    {
                        "name": "4. Button Compass",
                        "description": "A small, liquid-filled compass for navigation.",
                        "imageName": "compass.jpg"
                    },
                    {
                        "name": "5. Snare Wire",
                        "description": "Flexible brass wire (60-90 cm) for trapping small game.",
                        "imageName": "snare.jpg"
                    },
                    {
                        "name": "6. Sewing Kit",
                        "description": "Heavy needles and strong thread.",
                        "imageName": "sewing.jpg"
                    },
                    {
                        "name": "7. Fishing Tackle",
                        "description": "Line, hooks, lead sinkers, and swivels.",
                        "imageName": "fishing.jpg"
                    },
                    {
                        "name": "8. Wire Saw",
                        "description": "A flexible wire saw with finger rings for cutting shelter poles.",
                        "imageName": "wiresaw.jpg"
                    },
                    {
                        "name": "9. Scalpel Blades",
                        "description": "Two scalpel blades of different sizes for skinning and fine work.",
                        "imageName": "scalpel.jpg"
                    },
                    {
                        "name": "10. Adhesive Plasters",
                        "description": "Waterproof dressings for cuts.",
                        "imageName": "plasters.jpg"
                    },
                    {
                        "name": "11. Water Sterilizer",
                        "description": "Chlorine or iodine tablets.",
                        "imageName": "sterilizer.jpg"
                    },
                    {
                        "name": "12. Condom",
                        "description": "A clean, durable water container holding up to 1 liter of water.",
                        "imageName": "condom.jpg"
                    },
                    {
                        "name": "Signal Mirror (Heliograph)",
                        "description": "A high-grade mirror with a central sighting hole for catching the sun and signaling aircraft or search parties.",
                        "imageName": "mirror.jpg"
                    },
                    {
                        "name": "Whistle",
                        "description": "A pea-less survival whistle for signaling in thick cover or fog.",
                        "imageName": "whistle.jpg"
                    },
                    {
                        "name": "Headlamp or Torch",
                        "description": "A compact LED light source with spare batteries.",
                        "imageName": "torch.jpg"
                    },
                    {
                        "name": "Water Purification Straw",
                        "description": "A portable filter straw to allow drinking directly from streams.",
                        "imageName": "purifier.jpg"
                    },
                    {
                        "name": "Emergency Bivouac Bag",
                        "description": "A lightweight, heat-reflective plastic bag to shield your body from wind and hypothermia.",
                        "imageName": "bivy.jpg"
                    },
                    {
                        "name": "Tinder Bundle",
                        "description": "Cotton balls soaked in petroleum jelly, kept in a waterproof canister.",
                        "imageName": "tinder.jpg"
                    },
                    {
                        "name": "Rations",
                        "description": "High-energy food bars, dextrose tablets, or salt packets.",
                        "imageName": "rations.jpg"
                    }
                ]
            },
            {
                "title": "Transport Prep & The Unexpected",
                "subtitle": "Emergency procedures for vehicles, aircraft, boats, and the ultimate tool.",
                "imageName": "essentials.jpg",
                "textSections": [
                    """Vehicles: Motor vehicles need special adjustment and adaptation to deal with high altitudes and extreme conditions, as well as a thorough overhaul to make sure they are in tip-top working order. You will need tanks for extra fuel and water as well as spares and modifications. Boats and planes: Whether travelling privately or on a commercial service you must take note of the emergency procedures. Maritime and aviation authorities rule that passengers must be informed of them and remembering them could save your life. When you board an aircraft cabin staff point out the emergency exits and advise you on action to take in the event of an emergency. On board ship you will carry out lifeboat drills and be instructed on how to abandon ship if you have to. The safest place on an aircraft is as far back in the tail as possible. In a crash this frequently breaks off and most survivors are from this portion. If you are a passenger in a light aircraft ask the pilot about the trip: how long will it take and what sort of ground will you be flying over? Attend to details - they count in an emergency. Also, try to keep your kit with you at all times.""",
                    """THE UNEXPECTED: How can you prepare for what you do not expect? Preparing for expected difficulties and dangers is difficult enough, but what chance have you of equipping yourself for the totally unknown disaster? Yet these are the disasters that immediately spring to people's minds - the shipwreck and the plane crash or forced landing in unfamiliar and difficult terrain. This is the reason for this book's existence. Even more important, however, is to know about a whole range of skills which can be applied and adapted to all kinds of situations and to develop a way of thinking that enables you to draw upon them to find the solutions to particular problems. This is the preparation you can make for the unexpected. But this is not all. You can equip yourself with a few small items which will increase your chances many times over by helping you with some of the basic necessities of survival. This can tip the balance between failure and success. They will fit in a small container slipped into a pocket or bag and can be carried anywhere. They are your survival kit. If there is an emergency you will be glad you always carry it. More bulky, but still compact enough to carry on a belt whenever you are travelling, are a knife and the items which will fit in your survival pouch. Without the basics, which these two kits provide, you can still improvise but they will give you a head start.""",
                    """SURVIVAL SCENARIO: You're getting your kit together, what is the most important item to remember to take with you? Take your brain with you. You can't beat the combination of common sense and experience in high stress survival situations."""
                ]
            },
            {
                "title": "Facing Disaster & The Rule of 3s",
                "subtitle": "Coping with physical and mental stresses, fitness, warning signals, and the limits of survival.",
                "imageName": "disaster.jpg",
                "textSections": [
                    """When facing a disaster it is easy to let yourself go, to collapse and be consumed in self-pity. But it is no use giving up or burying your head in the sand and hoping that this is a bad dream that will soon pass. It won't, and with that kind of attitude it will rapidly become much worse. Only positive action can save you.

A healthy, well-nourished person can physically tolerate a great deal, provided that he or she has self-confidence. Even if sick or injured, a determined person can win through and recover from seemingly impossible situations. To do so there are many stresses that must be overcome.

The survival situation will put you under pressure, both physical and mental. You will have to overcome some or all of these stresses:
- Fear and anxiety
- Pain, illness and injury
- Cold and/or heat
- Thirst, hunger and fatigue
- Sleep deprivation
- Boredom
- Loneliness and isolation

Can you cope? You have to.""",
                    """Self-confidence is a product of good training and sound knowledge. These must be acquired before you have to face up to a survival situation.

Physical fitness plays an important part. The fitter you are the better you will survive. Initially you may have to go without sleep to ensure that you are in a safe location, or make a long march in dangerous conditions. Do not wait until you are forced to go without sleep to see whether you are capable of doing so. Prove it to yourself now by getting into training. Develop the resources to cope with fatigue and loss of sleep.""",
                    """You will be working hard to procure food and water. They will relieve hunger and thirst. But finding them will tire you and you will need an adequate shelter to enable you to rest and recover from your efforts. Don't overdo it. Rest frequently and assess the situation.

Pain and fever are warning signals that call attention to an injury or physical condition. They are not in themselves dangerous, however distressing and discomforting. Pain can be controlled and overcome. Its biological function is to protect an injured part, to prevent you using it, but this warning may have to be ignored to avoid the risk of further injury or death.""",
                    """How long can the body cope without the essentials?

In general the human body can survive for:
- 3 minutes without air
- 3 days without water
- 3 weeks without food

There are always exceptions to this and there are examples of people pushing these boundaries and surviving for longer periods. It is amazing what the human body can endure but such a survivor's health can suffer in the long term due to such trauma. For example, a person surviving for more than 9 days without water will undoubtedly suffer kidney damage or failure."""
                ]
            },
            {
                "title": "Water Sourcing & Sweat Conservation",
                "subtitle": "Prioritizing water over food, hydration rules, water loss, and sweat management.",
                "imageName": "purifier.jpg",
                "textSections": [
                    """BASIC NEEDS: To reiterate, the main elements required for survival are FOOD, FIRE, SHELTER and WATER. Use PLAN (Protection, Location, Acquisition, Navigation) to help you to prioritise your survival needs. If you don't have shelter in the desert, having 2 litres (3½ pts) of water is of little use to you in the longer term.

It takes a healthy person quite a long time to die of starvation, for the body can use up its stored resources, but exposure to wind, rain and cold can be fatal even in temperate climates and death comes in only minutes in the icy waters of the poles. Food is rarely the first priority. Even in those places where it is difficult to find there are usually other problems to face first. Shelter will often be the prime necessity in extremes of climate or temperature - not just in the frozen polar regions or the baking deserts, but for walkers trapped by mist on a hillside. The need for fire is closely linked. Water is something that most people in the modern world take for granted. They are so used to turning on a tap that until an extreme drought causes water rationing they scarcely think about it. Yet the survivor at sea, or after a flood, though surrounded by water, may be desperate for drinkable water - and there are many places where, unless it rains, no obvious water is available. Water is universally important.""",
                    """WATER: Water is essential to life. A person can survive for three weeks without food but for only three days without water, therefore its discovery and conservation should be prioritised over food. Don't wait until you have run out of water before you look for it. Conserve what you have and seek a source as soon as possible, preferably fresh running water, though all water can be sterilized by boiling or by using chemical purifiers. In a survival situation a 1 litre-jug (1¾ pt) can be made to last 4 days, but if necessary the last ¼ litre (½ pt) can be made to last 3 days. This is achieved by dividing the last ¼ litre into three, then drinking half of the day's ration at midday, and the balance at night, for 3 days.

Water is the coolant that keeps the body at an even temperature, it is needed to keep the kidneys functioning to eliminate wastes, is required for breathing, and for digestion. But the fluids contained in the body are limited. Lost water must be replaced or health and efficiency will suffer. The average human requires the minimum of ¼ litre (½ pt) of water per day to survive.""",
                    """WATER LOSS & SWEAT RATIONING:

The average person loses 2-3 litres (3½-5¼ pt) of water each day - even someone resting in shade loses about 1 litre (1¾ pt). Just breathing loses fluids, and loss through respiration and perspiration increases with work rate and temperature. Vomiting and diarrhoea increase loss further. This must all be replaced to preserve the critical water balance, either by actual water or water contained in food.

REMEMBER: RATION YOUR SWEAT, NOT YOUR WATER!
If you have to ration water, take it in sips. After going a long time without water, don't guzzle when you do find it. Take only sips at first. Large gulps will make a dehydrated person vomit, losing even more of the valuable liquid.

Rules to minimize water loss:
- Avoid exertion. Just rest.
- Don't smoke.
- Keep cool. Stay in shade. If there is none, erect a cover to provide it.
- Do not lie on hot ground or heated surfaces.
- Don't eat, or eat as little as possible. If there is no water available, fluid will be taken from the vital organs to digest food, further increasing dehydration. Fat is hardest to digest and takes a lot of fluid to break it down.
- Never drink alcohol.
- Don't talk - and breathe through the nose, not the mouth."""
                ]
            },
            {
                "title": "Finding Water, Birds & Insects",
                "subtitle": "Where to dig, coastal resources, warning signs of pollution, and wildlife indicators.",
                "imageName": "compass.jpg",
                "textSections": [
                    """FINDING WATER: The first place to look is in valley bottoms where water naturally drains. If there is no obvious stream or pool, look for patches of green vegetation and try digging there. There may be water just below the surface which will build up in the hole. Even digging in gullies and dry stream beds may reveal a spring beneath the surface, especially in gravelly areas. In mountains look for water trapped in crevices.

On the coast digging above the high water line, especially where there are sand dunes, has a good chance of producing about 5cm (2in) of fresh water that filters down and floats on the heavier salt water. It may be brackish but is still drinkable. Where cliffs fall into the sea look for lush growth of vegetation, even ferns and mosses, in a fault in the rock formation and you may find a soak or spring. If no freshwater can be found, saltwater can be distilled.""",
                    """WARNING: Be suspicious of any pool with no green vegetation growing around it, or animal bones present. It is likely to be polluted by chemicals in the ground close to the surface. Check the edge for minerals which might indicate alkaline conditions. ALWAYS BOIL WATER FROM POOLS. In deserts there are lakes with no outlets; these become salt lakes. Their water MUST be distilled before drinking.

Dew and rain collection: Rainwater everywhere is drinkable and only needs collecting. Use as big a catchment area as possible, running the water off into containers of every kind. A hole dug in the ground and lined with clay will hold water efficiently, but keep it covered. If you have no impermeable sheeting, metal sheets or bark can be used to catch water in. If you have any doubt about the water you have collected, boil it.

In climates where it is very hot during the day and cold at night, heavy dew can be expected. When it condenses on metal objects it can be sponged or licked off. You can use clothing to soak up water and then wring it out. One way is to tie clean cloths around the legs and ankles and walk through wet vegetation. These can be sucked or wrung out.""",
                    """ANIMAL INDICATORS:

• Mammals: Most animals require water regularly. Grazing animals are usually never far from water - though some kinds travel thousands of miles to avoid the dry season - as they need to drink at dawn and dusk. Converging game trails often lead to water; follow them downhill. Carnivores (meat eaters) can go for a long period between waterings. They get moisture from the animals on which they prey so are not a positive indication of local water.

• Birds: Grain eaters, such as finches and pigeons, are never far from water. They drink at dawn and dusk. When they fly straight and low they are heading for water. When returning from water they are loaded with it and fly from tree to tree, resting frequently. Plot their direction and water can be found. Water birds can travel long distances without stopping to feed or drink so do not necessarily indicate water nearby. Hawks, eagles and other birds of prey also get liquids from their victims so cannot be taken as a sign of local water.

• Reptiles: Not an indicator of water. They collect dew and get moisture from prey, so can go a long time without.

• Insects: Good indicators, especially bees: they fly at most 6.5km (4 miles) from their nests or hives, but have no regular watering times. Ants are dependent upon water. A column of ants marching up a tree is going to a small reservoir of trapped water. Such reservoirs are found even in arid areas. Most flies keep within 90m (100yd) of water, especially the European Mason Fly with its iridescent green body.

• Human tracks: Will usually lead to a well, bore hole or soak. It may be covered over with scrub or rocks to reduce evaporation. Replace the cover."""
                ]
            },
            {
                "title": "Solar Stills, Condensation & Distillation",
                "subtitle": "Making a solar still, leaf bag condensation, laboratory retorts, and melting ice or snow.",
                "imageName": "purifier.jpg",
                "textSections": [
                    """CONDENSATION: Tree and plant roots draw moisture from the ground, but a tree may take it from a water table 15m (50ft) or more below, too deep to dig down to reach. Don't try; let the tree pump it up for you by tying a plastic bag around a leafy branch. Evaporation from the leaves will produce condensation in the bag.

Choose healthy vegetation and bushy branches. On trees keep the mouth of the bag at the top with a corner hanging low to collect condensed evaporation. Placing a polythene tent over any vegetation will collect moisture by evaporation which will condense on the plastic as it cools. Suspend the tent from the apex or support with a padded stick. Avoid foliage touching the sides of the top or it will divert water droplets which should collect in plastic-lined channels at the bottom.

Even cut vegetation will produce some condensation as it warms up when placed in a large plastic bag. Keep the foliage off the bottom with stones so that water collects below it, and keep the foliage from touching the plastic. Use stones to keep the bag taut. Support the top on a padded stick. Arrange the bag on a slight slope to encourage condensation to run down to the collecting point. When no longer productive, carefully replace with fresh foliage.""",
                    """SOLAR STILL: Dig a hole in the ground approximately 90cm (36in) across and 45cm (18in) deep. Place a collecting can in the centre, then cover the hole with a sheet of plastic formed into a cone. The sun's heat raises the temperature of the air and soil below and vapour is produced. As the air becomes saturated, water condenses on the underside of the plastic, running down into the container. This is especially effective in desert regions and elsewhere when it is hot during the day and cold at night. The plastic cools more quickly than the air, causing heavy condensation. This kind of still should collect at least 570ml (1pt) over a 24-hour period.

The still may also double as a trap. Insects and small snakes are attracted by the plastic. They may slide down into the cone or wriggle underneath it and drop into the hole and then cannot climb out. A solar still can be used to distill pure water from poisonous or contaminated liquids. Roughen the underside of the sheet with a stone to ensure droplets run down it. Use stones or weights to secure edges and keep the cone shape. Fix the can so that trapped creatures cannot tip it over. If feasible, use a syphon to a lower level to draw off water without disturbing the still.

WARNING: URINE AND SEA WATER
Never drink either - Never! But both can produce drinking water if distilled - and sea water will provide you with a residue of salt.""",
                    """DISTILLATION: Distillation kits are part of the equipment of life-rafts, but they can be improvised. To distill liquid you need to make something to do the job of a laboratory retort. Pass a tube into the top of a water-filled covered container, placed over a fire, and the other end into a sealed collecting tin which, preferably, is set inside another container providing a jacket of cold water to cool the vapour as it passes out of the tube. You can improvise the equipment from any tubing - pack frames, for instance. To avoid wasting water vapour, seal around the joins with mud or wet sand.

An easier method is a variation on the desert still. It takes a little longer for the water to condense but may be easier to set up. Take a tube from a covered vessel in which polluted/saltwater, or even urine, is to boil. Set the other end under a solar still. A sheet of metal or bark, perhaps weighted down, will cover the vessel. Even a cone of leaf over the water pot will help direct the steam into the tube.""",
                    """WATER FROM ICE AND SNOW: Melt ice rather than snow - it produces a greater volume faster for less heat: twice as much for half the heat. If forced to heat snow, place a little in the pot and melt that first, gradually adding more to it. If you put a lot of snow into the pot, the lower level will melt and then be soaked up into the absorbent snow above it, leaving a hollow beneath which will make the pot burn. Lower layers of snow are more granular than that on the surface and will yield more water.

WATER FROM SEA ICE: Sea ice is salt (no good for drinking) until it has aged. The more recently frozen, the saltier it will be. New sea ice is rough in contour and milky-white in colour. Old ice is bluish and has rounded edges, caused by weathering. Good water can be obtained from blue ice - the bluer and smoother the better. But beware of even old ice that has been exposed to salt spray."""
                ]
            },
            {
                "title": "Water from Plants & Animals",
                "subtitle": "Tapping hollow joints, water vines, palms, cactus sap, and fluids from animal tissues.",
                "imageName": "food.jpg",
                "textSections": [
                    """WATER FROM PLANTS:

• Water collectors: Cup-shaped plants and cavities between the leaves of bromeliads (many of which are parasitic on the branches of tropical trees) often collect a reservoir of water.

• Bamboo: Bamboo often holds water in its hollow joints. Old and yellow stems are more likely to be water bearing. Shake them - if you can hear water slurping around, cut a notch at the bottom of each joint and tip the water out.

• Traveller's Tree (Ravenala madagascariensis): One of the banana family, it can hold 1-2 litres (2-4 pt) of water between the bases of the chevron of leaf stalks.""",
                    """VINES: Vines with rough bark and shoots about 5cm (2in) thick can be a useful source of water. But you must learn by experience which are the water-bearing vines, because not all have drinkable water and some have a poisonous sap. The poisonous ones yield a sticky, milky sap when cut. You will know not to try that type again - otherwise it is a matter of trial and error and worth trying any species.

Some vines cause a skin irritation on contact if you suck them, so it is better to let the liquid drip into your mouth rather than put your mouth to the stem, and preferable to collect it in a container. To obtain water from a vine, select a particular stem and trace it upwards. Reach as high as possible and cut a deep notch in the stem. Cut off the same stem close to the ground and let the water drip from it into your mouth or into a container. When it ceases to drip, cut a section from the bottom and go on repeating this until the vine is drained. Do NOT cut the bottom of the vine first as this will cause the liquid to run up the vine through capillary action.""",
                    """ROOTS, PALMS & CACTI:

• Roots: In Australia the Water Tree, Desert Oak and Bloodwood have their roots near the surface. Pry these roots out from the ground and cut them up into 30cm (12in) lengths. Remove the bark. Suck out the moisture, or shave to a pulp and squeeze over the mouth. It is not easy to find some of the most useful desert roots unless you have been shown by someone with experience. Australian Aborigines can identify a tiny twig which grows from a football-like bulbous root, which can be a life-saver - but unless you have been shown how to find them it is not worth expending your energy and resources looking.

• Palms: The Buri, Coconut and Nipa palms all contain a sugary fluid which is very drinkable. To start it flowing, bend a flowering stalk downwards and cut off its tip. If a thin slice is cut off the stalk every 12 hours the flow will be renewed, making it possible to collect up to a quart each day. Nipa palms shoot from the base so that you can work from ground level; on grown trees of other species you may have to climb up them to reach a flowering stalk. Coconut milk has considerable water content, but from ripe nuts it is a powerful laxative; drinking too much would make you lose more fluid.

• Cacti: Both the fruit and bodies of cacti store water, but not all cacti produce liquid safe to drink - the Saguaro, the giant multi-fingered cactus of Arizona, is very poisonous. Take care to avoid contact with cactus spines; they can be very difficult to remove, especially the very fine hair-like ones, and can cause festering sores if they stay in the skin.

• Barrel Cactus (Echinocactus grusonii): Can reach a height of 120cm (4ft), is found in the southern United States through to South America and requires considerable effort to cut through its tough, spine-covered outer skin. The best method is to cut off the top and chop out pieces from the inside to suck, or to smash the pulp within the plant and scoop out the watery sap, which varies from tasteless in some plants to bitter in others. An average-sized, 100cm (3½ ft) Barrel cactus will yield about 1 litre (1¾ pt) of milky juice and this is an exception to the rule to avoid milky-sapped plants.""",
                    """WATER FROM ANIMALS:

Animal eyes contain water which can be extracted by sucking them. All fish contain a drinkable fluid. Large fish, in particular, have a reservoir of fresh water along the spine. Tap it by gutting the fish and, keeping the fish flat, remove the backbone, being careful not to spill the liquid, and then drink it. If you need water that badly you should be careful not to suck up the other fish juices in the flesh, for they are rich in protein and will use up water in digestion.

Desert animals can also be a source of moisture. In times of drought in Northwestern Australia, Aborigines dig in dry clay pans for the desert frogs that burrow in the clay to keep cool and survive. They store water in their bodies and it can be squeezed out of them."""
                ]
            },
            {
                "title": "Salt Preservation & Extraction",
                "subtitle": "Biological needs, deficiency symptoms, diluting sea water, and extracting salt from roots.",
                "imageName": "campcraft.jpg",
                "textSections": [
                    """SALT: Salt is essential for water retention. A normal diet includes a daily intake of 10g (1/3 oz). The trouble starts when you start to get rid of it faster than you eat it. The body loses salt in sweat and urine, so the warmer the climate the greater the loss. Physical exertion will also increase the loss. However, replenishing the salt levels in your body is not always recommended, and much will depend on the situation you find yourself in. If you are on reduced food and/or water rations, salt is the first thing that should be cut from your diet, because it increases dehydration.""",
                    """DEFICIENCY & REMEDIES: The first symptoms of salt deficiency are muscle cramps, dizziness, nausea and tiredness. The remedy is to take a pinch of salt in half a litre (approx. 1 pint) of water. Salt supplements in tablet form used to be the prescribed method of increasing sodium levels, but always dissolve these in water, or isotonic drinks - if they are available.""",
                    """SOURCES OF SALT:

What happens if you do not carry salt or your supplies run out? By the coast or at sea there is plenty of saltwater available - a pint of sea water contains about 15g (1/2 oz) of salt, but do NOT just drink it as it is. Dilute it with plenty of fresh water. Evaporating sea water will leave you with salt crystals.

Inland salt supplies are more problematic. In farming areas you will find salt licks for cattle - but you will then be close to civilization and not likely to have reached the stage of salt deprivation. However, all animals need salt and observation of them may reveal a natural source. In one part of Africa, elephants risk the dangerous depths of a dark cave to lick salt from its sides.

Salt can be obtained from some plants. In North America, the best source is the roots of hickory trees, and in Southeast Asia, those of the Nipa Palm can be used in the same way. Boil the roots until all the water is evaporated and black salt crystals are left. If no direct salt sources are available to you, then you will have to rely on getting it second-hand, through animal blood, which should never be wasted as it is a valuable source of minerals."""
                ]
            }
        ]
    },
    {
        "title": "Strategy",
        "description": "Operational tactics for managing accidents, planning group actions, and conducting dynamic risk assessments.",
        "articles": [
            {
                "title": "Introduction to Strategy & Risk",
                "subtitle": "Planning, preparing, avoiding panic, and dynamic risk assessment.",
                "imageName": "strategy.jpg",
                "textSections": [
                    """Good planning and preparation enable the survivor to confront difficulties and dangers that pose a serious threat to survival. They become contingencies for which you are equipped. But you cannot anticipate everything. You must be ready to respond rapidly to the unexpected danger and to deal with potential disaster rationally and realistically. You must overcome the tendency to panic and take the action appropriate to the situation.

Sometimes a collision or other accident occurs with no warning of any kind, but in most instances there is a moment of realization that something is going to happen and it is in that moment that instinctive reaction can save lives. In many situations there is a considerable time in which an awareness of potential disaster can develop and that is when the panic reaction is probably most dangerous.

As mist closes in on a hillside, reducing visibility to almost nothing and making it easy to lose any sense of direction, most people would begin to panic at the thought that they are going to be trapped. They begin to do foolish things and increase their danger. They should, however, already be assessing the possibilities and looking for some suitable shelter in which to wait until conditions become safe to continue. Keeping calm, in the knowledge that you have the ability to handle the situation, will not only enable you to see it through but also to see other solutions.""",
                    """SURVIVAL SCENARIO: On your camp, should you revise your strategy?

You should have a strategy for every scenario, therefore as situations change, so should your strategy. You must be flexible and be prepared to adapt.

Some situations are predictable and knowledge of the techniques for handling them will minimize the risks. Learn them, they may save your life. They may take considerable nerve - like waiting for the right moment to escape from a car that is sinking under water - but they are based on experience. The answer to more general survival problems, however, will often lie in inspired improvisation drawing on those skills appropriate to the situation.

Disaster may involve you in a contained situation which you must handle alone - or you may find yourself one of hundreds of people in a large-scale disaster over which there can be no control at all.""",
                    """DYNAMIC RISK ASSESSMENT: A dynamic risk assessment (DRA) is a continuous process of analyzing your environment to identify hazards before they cause injury or death. In a crisis, the brain is prone to tunnel vision, focusing solely on one goal (like finding food) while ignoring immediate dangers (like crossing a weak snow bridge). Before making any tactical decision, pause and scan for environmental hazards: falling trees (widowmakers), rising water levels, loose rock slopes, avalanche potential, and signs of dangerous wildlife. Never risk your safety to recover non-essential gear.

Conduct a detailed assessment of your group. Check every survivor for injuries, paying close attention to head trauma, hypothermia, and shock. Evaluate each person's physical and mental stamina. A companion who is quietly withdrawn may be suffering from severe shock or hypothermia and requires immediate attention. A sprained ankle or broken bone will dictate your travel speed, shelter design, and resource consumption.

Identify and catalog the natural assets of your terrain. Look for clean, flowing water sources, standing dead wood for fuel, natural rock overhangs that can reduce shelter build times, and clear zones that are suitable for building large rescue signals. Understanding your environment allows you to cooperate with nature rather than fighting against it."""
                ]
            },
            {
                "title": "Car Accident Survival",
                "subtitle": "Brake failure procedures, collision management, brace positions, and jumping out.",
                "imageName": "strategy.jpg",
                "textSections": [
                    """BRAKE FAILURE: If brakes fail while driving, change gear and apply the handbrake. You must do several things at once: take your foot off the accelerator, flick the switch of your warning lights, pump the footbrake rapidly (it may still connect), change down through the gears and apply handbrake pressure. Don't slam the brake on, begin with gentle bursts, gradually braking harder until you stop.

If there is no time for all this, take your foot off the accelerator and change down through the gears - and grab the handbrake - but DON'T apply maximum pressure until you are sure that you won't skid.

Look out for escape lanes and places where you can leave the road, preferably a soft bank or a turning that has an uphill slope. If speed remains unchecked, on a steep hill for example, brush the car along a hedge or wall to reduce speed. Take advantage of a vehicle in front and use it to stop you - run into it as gently as the situation allows. Use warning lights, blow your horn and flash your headlights to give the driver in front as much warning as possible that you are on a collision course.""",
                    """COLLISION & BRACE POSITION: If collision seems inevitable, stay with it and steer the car to do as little damage to others and yourself as possible. Try to avoid a sudden stop by driving into something which will give, like a fence or a hedge rather than a tree.

Seatbelts (compulsory in most countries) will help stop you hitting the windscreen. Most new cars are usually fitted with airbags for both the driver and the front passenger. Given the speed and force with which an airbag inflates, it is vitally important that you do not sit too close to the steering wheel. And if your steering wheel is adjustable, tilt it downwards so that the airbag points towards your chest rather than your head, but make sure you can see the instruments clearly.

If neither of these options are available, adopting the brace position will offer you the best chance of survival in a crash because it stops you from impacting too heavily on the interior of the car. The important thing is to get your upper torso as low as possible. There are two alternative types of brace position depending on the space that you are in. The first position requires you to place your head on your knees, while your hands hold on to your lower legs. The second position is more useful if you are driving the car: place your hands on the steering wheel, then place your forehead onto the back of your hands before the impact.""",
                    """JUMPING OUT: Do NOT try to jump out of a runaway car unless you know it to be headed for a cliff or another substantial drop and that you will not survive the impact. If this is the only available option, then open the door, undo the safety belt, and begin to roll yourself into a ball. Drop from the car in a rolling movement. Do not resist the ground but keep balled up and continue the roll."""
                ]
            },
            {
                "title": "Car Under Water & Railway Tracks",
                "subtitle": "Escaping sinking vehicles, pressure equalization, and level crossing emergencies.",
                "imageName": "strategy.jpg",
                "textSections": [
                    """CAR UNDER WATER: If possible abandon the car before it sinks, for it will not sink immediately and will take time to fill. Water pressure on the outside makes it very difficult to open the door so open the window if you can and wriggle out of it. It takes great presence of mind to manage that when subject to the shock and surprise of the 'splash down', but if there are small children in the car it may be possible to push one through. Do not try to save possessions.

If you have not been fast enough CLOSE the window firmly, get children to stand and lift babies near to the roof. Release seat belts and tell everyone by a door to be ready with a hand on the handle. Release at once any automatic door locks or master locks. Water could prevent them from working. Do not attempt to open doors at this stage.

As water fills the interior, air will be trapped near the roof. The water pressure inside the car will nearly equalize the pressure with that of the water outside the car. As the car comes to rest and is nearly full of water, tell everyone to take a deep breath, open the doors and swim to the surface, breathing out as they do so. Everyone leaving through the same door should link arms. If you have to wait for someone to get out before you, hold your breath for that moment.

PRECAUTION: Always park alongside water, not running towards it. If you have to park a car facing water then leave it in reverse gear and with the handbrake on (if facing away from water, in first gear with the handbrake on).""",
                    """CAR ON RAILWAY TRACKS: If a car breaks down on an unmanned level crossing, put it into gear and use the starter motor to jerk it clear. This will work with a manual gear change but not with an automatic. If a train is approaching abandon the car, carry children or infirm persons to safety and keep away - about 45m (50yds) should be far enough - for if a train is travelling at high speed it could fling car wreckage quite a distance.

If there is no train visible, or you can see one several miles in the distance, you must try to avert the collision. If the car can be moved by pushing, push it clear of all tracks - you cannot be sure which one the train will be on. If there is an emergency telephone warn signalmen further down the track of the situation. If not, walk up the track towards the train. Stand well to one side (high speed trains have quite a slipstream) and wave a car blanket or bright coloured garment to warn the driver. If he is doing his job properly he will know that he is approaching a crossing and should look ahead to see that all is clear."""
                ]
            },
            {
                "title": "Disaster in the Air & After-Crash",
                "subtitle": "Aviation crash landings, ditching, triage, and immediate survival camp strategies.",
                "imageName": "strategy.jpg",
                "textSections": [
                    """DISASTER IN THE AIR: A plane crash or forced landing in difficult terrain is one of the most dramatic of disaster scenarios. Since it could happen anywhere the individual cannot prepare for any specific situation. Airline cabin staff are trained for such emergencies and you should follow their instructions. Aircrew will be trying to land the plane as safely as possible; there is nothing you can do except to keep calm and support the crew in calming the other passengers.

To prepare for a crash landing: tighten the seat belt, link arms with people on either side, hold your chin firmly down on your chest, lean forwards over a cushion, folded blanket or coat, interlink legs with your neighbours if seating permits it, and brace yourself for impact.

When the aircraft finally stops moving - and not before - evacuate the aircraft as instructed in the pre-flight brief. If a ground landing, then quickly get away from the immediate area of the plane, as there is danger of fire or explosion. Even if there is no fire, keep away until the engines have cooled and any spilled fuel evaporated.

If ditching into water, dinghies will be automatically inflated and anchored on the wings. Do not inflate your own lifejacket while you are in the aircraft. To do so would restrict your exit. Wait until you are in the water and then pull the toggle to inflate it and get into a dinghy. If the plane is sinking, release the dinghy from its anchorage as soon as passengers and equipment are stowed. As you leave the plane the more kit you can take with you the better. But do not stop to gather personal belongings and luggage.

SURVIVAL TIP: If bailing out from a plane by parachute in wild country, make your way to the wreck if you can - the wreckage will be much more noticeable to rescuers than a single person or a parachute.""",
                    """AFTER THE CRASH: However self-disciplined you are, the entry into this kind of survival situation will be dramatic, abrupt and confusing. You will be in a state of shock and may be on the verge of panic. If there is fire or the risk of fire or explosion, keep at a distance until that danger seems to have passed, but no further away than seems necessary for safety. Do not allow anyone to smoke if fuel has been spilled. You must not blunder off into unknown terrain, especially at night, and need to maintain contact with other survivors.

Move injured persons to a safe distance with you and try to account for all the people involved. The immediate treatment of the injured is a priority. Treat cases in order of severity of their injuries and with each individual deal first with breathing difficulties, then in sequence with major bleeding, wounds, fractures and shock. Separate the dead from the living if possible - the deaths are part of the frightening strangeness of the event and the survivors will be easier to calm down.

Even with a fire, all may not have been destroyed. Investigate the wreckage and salvage whatever you can of equipment, food, clothing and water. Take NO risks if there is still a chance that fuel tanks could ignite and beware of any noxious fumes from wreckage which has been smouldering.""",
                    """STAYING PUT VS MOVING: If you have to wait for the fire to burn out, take stock of the location in which you find yourself - which should in any case be the next step in your strategy. Is it practical and safe to remain where you are? If your anticipated route is known - and with a flight it will be - some kind of search and rescue operation can be expected and there are considerable advantages in staying where you are.

Searchers will already have some idea of your location, and even if you have been forced off route they will have a record of your last reported position. The wreckage or grounded plane will be more noticeable from the air, especially in heavily wooded country where even a large group of people will be hidden by the trees.

If you find that you are in a very exposed or dangerous location then a move to a more protected position is necessary. However, do not move at night unless the threat to life outweighs the risks of trying to negotiate unknown terrain in the dark.

SURVIVAL TIP: Leave an indication on the crash site of the direction in which you have moved off, so that it is possible for rescuers to know that there are survivors and to know in which direction to go on looking.

The usual reason for making an immediate move will be because you are in an exposed position on a mountain or hillside offering no protection from the elements, or at risk from rock falls or other dangers there. Move down, not up the slope, as conditions are likely to be less exposed on lower ground. Do not all go off looking for a safer location. Send out scouts to investigate the surrounding terrain carefully. They must keep together, working in pairs, and not go off on individual explorations. They can maintain contact vocally and should mark their routes as they proceed so that they can easily retrace their steps."""
                ]
            },
            {
                "title": "PLAN in Action (Protection & Location)",
                "subtitle": "Prioritizing shelter, signaling, ground codes, and when to attempt self-rescue.",
                "imageName": "strategy.jpg",
                "textSections": [
                    """PROTECTION: The first requirement will probably be some immediate shelter from the elements, especially for any injured. A more extended reconnaissance can follow to choose a proper campsite. Make the most of any natural shelter and augment it by using whatever materials are at hand. If injuries are too severe for a person to be moved, some kind of shelter must be provided for them on the spot.

On bare ground, if there is no equipment or wreckage which can be utilized, then the only thing to do is dig down. If possible, find a natural hollow and burrow deeper, using the excavated earth to build up the sides. This will at least get a casualty out of the wind. Get a fire going to provide warmth (it will also help raise morale) and use reflectors to maximize the heating effect, enabling you to conserve fuel.

If the circumstances make movement away unnecessary or impossible, follow similar procedures. Build up rocks, wreckage or equipment to form a wind break if no natural shelter is available. If in a group, huddle together; it will reduce the loss of body heat. Survival time for badly injured persons in these circumstances is limited and you must hope for an early rescue. Fit people must go off in search of water, fuel, shelter materials and food - but always in at least pairs. Lay out as many signals as possible to attract attention.

Remember that shelter may be as necessary from the sun as it is from the wind and cold. Exposure is not only a matter of hypothermia.""",
                    """LOCATION: If you have a radio or mobile phone you can signal for help - but do not go back on board a damaged and potentially explosive aircraft to do so. Wait until you are sure it is quite safe. The rescue party will want to know your location. Those who were travelling overland should have a good idea of their position - even if temporarily lost - and with a map should be able to give a more accurate fix. If you are the victim of disaster at sea or in the air, however, it will help considerably if you know your planned course and have some idea of your position when disaster struck, as well as of wind or current directions.

As often as not you must light fires - three fires are an internationally recognized distress signal. Make them as large as possible. Lay ground signals to attract attention, use pyrotechnics when you know help is within range and even make a noise when help is very near. This is when you are glad that the responsible authorities were told of your intentions and that you kept precisely to your route. It is only a matter of time before rescue comes. Meanwhile make yourself as comfortable as possible.

However, even the most careful plans may go astray. Navigational instruments could fail, storms, high winds or fog could all throw you off course and there you are, safe in your shelter but with no one knowing where. You could have a longer wait than you anticipate and you need to provide for it. You also need to assess where you are on a more local scale, to study the terrain for anything it can tell you, not only to pin-point your position - if that is possible - but to see if there are safer and more comfortable locations to pitch camp, sources for fuel, food and water. In the long term you will also be assessing the possibility of making your own way across the land.""",
                    """SELF-RESCUE VS STAYING PUT:

On land, it is seldom most sensible to set out immediately to walk to safety, rather than wait for rescue. However, if you know that no one will be aware that you are missing, if the terrain is so barren that it provides no food, water or shelter, or if you feel convinced that your reserves of energy and rations are sufficient to see you back to civilization, or to a location where you are sure you will be able to live off the land, you may decide to set off as soon as the light is good enough or conditions are otherwise right.

At sea you will be looking out for any indications that, rather than staying put, there is land close enough for your survival chances to be greater if you try to reach it rather than holding your present position. But you are at the mercy of wind and current, though you can delay your drift with a sea anchor.""",
                    """YOU MUST PLAN: Remember this, it may save your life one day:

• P - Protection: Create immediate shelter, windbreaks, and fire reflectors.
• L - Location: Light three fires, prepare ground signals, and prepare radio/mobile systems.
• A - Acquisition: Systematically search for clean water, tinder, fuel, and wild food.
• N - Navigation: Coordinate your signals, calculate your position, and only move if self-rescue is essential."""
                ]
            },
            {
                "title": "Acquisition of Food & Water",
                "subtitle": "Rationing supplies, wild plant/animal limits, and ecological stewardship.",
                "imageName": "strategy.jpg",
                "textSections": [
                    """ACQUIRING FOOD AND WATER: On an isolated cliff ledge, cut off by the tide or forced by storm or mist to wait until you can move on, there may be little opportunity to exploit natural resources. Do not tuck into emergency rations immediately. You may be there for some time and, hungry though you may be, you should ration them out, allowing for a much longer wait than even a pessimistic assessment suggests. Even in such a situation there may be water and food within reach.

Elsewhere, save your emergency rations for when there is nothing else and tap nature's resources first. Do not just find one source of food. Seek out a variety of plants for leaves, fruit, nuts, roots and other edible parts. Look for signs of animals which can be trapped or hunted.""",
                    """ECOLOGICAL STEWARDSHIP: When it is your very survival that is at stake there is no place for squeamishness about what you will or will not eat or about how you acquire your food, but that does not mean that you should totally abandon concern for wildlife and the environment. When there is an abundance of other choices there is no reason to take already endangered species for your food - animal or vegetable - nor to set traps (which cannot discriminate in what they catch and maim) that will produce more meat than you can eat fresh or preserve. Making the most of nature's resources does not mean plundering them. Over-exploitation will be to your own disadvantage if you have to stay in the area for a long time.

Remember, too, that the most easily obtained nutritious food may be quite different from what you usually eat. If you have already learned to eat an unusual diet as part of your training, you will find it much easier to feed yourself and will be able to encourage others to eat the same things.""",
                    """FIRE & WATER PRIORITY: Fuel for a fire will be needed for boiling water even if the temperature does not demand a fire for warmth - but do not be deluded into thinking that a warm day is going to be followed by a warm night. There can be dramatic temperature changes from day to night in some parts of the world.

SURVIVAL TIP: In the short-term water is much more vital than food for your survival. If fresh running water is not available there are many other sources you can tap, but sterilize or boil to ensure that it is pure. Make finding water sources a priority."""
                ]
            },
            {
                "title": "People & Leadership in Crisis",
                "subtitle": "Group dynamics, roles of children, elderly, and women, and cultural taboos under stress.",
                "imageName": "strategy.jpg",
                "textSections": [
                    """PEOPLE: For an expedition, the planning will include a careful selection of compatible personalities, selected for their fitness, both physically and in experience and training, for the particular project. In a disaster situation anyone may react unexpectedly under stress. With a mishap affecting members of the general public there may be a very varied group of people thrown together: men, women and children, elderly people and babies. There may be pregnant women and people with medical problems or physical disabilities that require particular attention. The accident situations which involve such a varied group are also likely to involve a higher risk of injuries than among a hand-picked group of the trained and fit.""",
                    """DEMOGRAPHICS IN SURVIVAL:

• Babies: Babies may look very fragile - but they are very tough. However, they must be kept warm and fed regularly.

• Children: Children will need reassuring and comforting, especially if they have lost the people with them or they are themselves in pain. Often the adventure of the situation will help to keep them from becoming too worried and it will help to keep them occupied, but they should not be allowed to wander, to play with fire or otherwise expose themselves to further danger.

• Old People: Old people are usually mentally tough and can give reassurance to the young, but they must be kept warm and fed regularly.

• Women: It often seems true that women handle emergencies much better than men and are able to accept responsibility for others more easily.""",
                    """LEADERSHIP & Morale: With a ship or commercial airline, the ship's officers or flight crew can be expected to take charge of the situation, if they are among the survivors, but there will not be the military chain of command or the acceptance of leadership and responsibility which can be expected in a compact organized group. Some democratic procedure to make decisions, plan action and maintain morale must be attempted. The trauma of the experience may leave some people eager to follow any leadership which gives them hope, but it will also throw into relief antagonisms and prejudices which must be overcome.

In an air or sea disaster, people of different cultures and backgrounds may be thrown together and forced into situations which their own social taboos would not permit. Considerable tact may be necessary to overcome these problems. SURVIVAL, however, must take precedence.

The wider your medical knowledge the better, but giving people the will to survive is important and much of this can be achieved by a good 'bedside manner' - if you can give the impression that you know what you are doing you are half-way there. Calmness and confidence in yourself will inspire the confidence and cooperation of others. The more knowledge you have the better you will be able to cope."""
                ]
            }
        ]
    },
    {
        "title": "Climate & Terrain",
        "description": "Techniques for surviving in specialized environments including polar regions, deserts, and tropical jungles.",
        "articles": [
            {
                "title": "Climate Zones & Kenya Scenario",
                "subtitle": "Polar, tundra, coniferous, temperate, grassland, tropical zones, and water discipline lessons.",
                "imageName": "climate.jpg",
                "textSections": [
                    """CLIMATE ZONES: People often view an alien environment as an enemy and feel they must fight it. This is not the way to survive - fight it and you will lose! There are dangers against which precautions must be taken, but nature is neutral. Learn to live with each climate and to use what it offers. Climate is not conditioned only by latitude; location within a continent and altitude are equally important.

• Polar Climates: Polar regions are regarded as those at latitudes higher than 60°33' north and south, but cold weather skills may be needed at very high altitudes everywhere. Near the Equator, in the Andes for example, the snow line is not reached until an altitude of about 5000m (16,500ft), but the nearer the poles the lower the snow line will be - at the southern tip of South America there is permanent snow at only a few hundred metres (a thousand feet). Arctic conditions penetrate deep into the northern territories of Alaska, Canada, Greenland, Iceland, Scandinavia and Russia.

• Tundra: South of the polar cap, the ground remains permanently frozen and vegetation is stunted. Snow melts in summer, but roots cannot penetrate the hard earth. High altitudes produce similar conditions.

• Northern Coniferous Forest: Between the arctic tundra and the main temperate lands is a forest zone, up to 1300km (800 miles) deep. In Russia, where it is known as the Taiga, the forests penetrate up to 1650km (1025 miles) north of the Arctic Circle along some Siberian rivers, but in the Hudson Bay area of Canada the tree line moves an equal distance south of the Circle. Winters are long and severe, the ground frozen for much of the time, summers are short. For only 3-5 months of the year is the ground thawed sufficiently for water to reach the roots of the trees and plants, which especially flourish along the great rivers that flow to the Arctic Ocean. There is a wealth of game: elk, bear, otter, lynx, sable and squirrel, as well as smaller creatures, and many birds. In summer, where the snow melt cannot drain, it creates swamps. Fallen trees and dense growths of sphagnum moss make the going difficult. Mosquitoes can be a nuisance (but they do not carry malaria). Movement is easier in winter, if you have warm clothing. Travel along the rivers, where fishing is good, making a raft from the abundant deadfalls.""",
                    """TEMPERATE, TROPICAL & DESERT ZONES:

• Temperate Climates: The temperate zone of the northern hemisphere, and the similar climates of the southern hemisphere, probably offer the most equitable circumstances for survival without special skills or knowledge. These territories are also those most heavily urbanized and where the survival ordeal is not likely to be very extended. A fit and healthy person, equipped with basic skills, would not be so cut off that they could not reach help within a few day's trek. Heavy winter conditions may call for polar skills.
- Deciduous Forest: As the climate gets warmer and winters less severe, deciduous forest replaces the conifers. Oak, beech, maple and hickory are the main species in America; oak, beech, chestnut and lime, in Eurasia. Soil rich in humus supports many plants and fungi. Survival is not difficult, except at very high altitudes where tundra, or snowfield conditions, appear. Many of these areas have been cleared by man.
- Temperate Grassland: Mainly central continental areas with hot summers, cold winters and moderate rainfall, these have become the world's great food-producing areas - grain is grown and cattle reared. Water can be a problem in summer and shelter in winter.
- Mediterranean Regions: The lands bordering on the Mediterranean are semi-arid areas, with long hot summers and short dry winters. There is sunshine most of the year, and drying winds. At one time this region was forested with oaks. When these were cut down the soil eroded, much of the area became covered with evergreen shrub. The Chapparal of California is very similar. Trees are few and water is a problem. At high altitudes, other conditions prevail.

• Tropical Forests: The land between the tropics includes areas of cultivation and extremes of swamp and desert, but one-third is undeveloped forest: equatorial rainforest, sub-tropical rainforest and montane forest. All feature high rainfall and rugged mountains, which drain into large, swift-flowing rivers, with coastal and other low-lying regions often as swampland.
- Savannah: This is tropical grassland, lying usually between the desert and the tropical forest. Near the forests the grass is tall, up to 3m (10ft) high, and trees more frequent. Temperatures are high the whole year round. More than one-third of Africa is savannah as are large areas of Australia, which are dotted with eucalyptus trees. Similar areas are the llanos of Venezuela and Colombia and the campos in Brazil. Often water is not easily available but, where it is found, there will be lusher vegetation and plenty of wildlife. In Africa large herds of animals can be found.

• Deserts: One-fifth of the earth's land surface is desert - dry barren land where survival is very difficult. Deserts occur where air currents, which rose at the Equator and have already shed their moisture, descend and are rewarmed as they near the Earth, taking what little local moisture is present. There are rarely any clouds to give protection from the sun or to retain heat at night so that great extremes of temperature occur from the highest shade temperatures (58°C/136°F in the Sahara) to below freezing point at night. Only small parts of the world's deserts are sand (about one-tenth of the Sahara); the greater part is flat gravel cut by dried up water courses (wadis). The wind has blown the sand away, piling it up in low-lying areas. Elsewhere there may be wind-carved mountains, dried mudflats and lava flows.""",
                    """SURVIVAL SCENARIO & LESSONS FROM KENYA:

In the mid-1960s I was training a new army unit in Kenya. This training involved tactics, field craft and navigation. They were all experienced soldiers but lacked knowledge in small group operations. The training area was in the Northern Frontier district of Kenya, a very hot and dry area. The recruits were dropped off in groups of 4 and had to navigate across country to a series of rendezvous points (RVs), where they were given water. My job with 3 others was to man these RVs, ensuring that everyone was accounted for and in good health. Each recruit was given half a pint of water strictly issued from a jerry can which held 4.5 gallons (36 pints).

On the third day the heat was taking its toll and everyone was complaining of various ailments like blisters, sores caused by backpacks and fatigue. But one student was particularly bad. He was delirious and verging on the point of collapse. While I was treating him, his partner grabbed a jerry can and tried to swallow the lot. What he couldn't swallow he spilt, and by the time we wrestled the can from him it was almost empty. This was the last of our supplies and there were still more than 30 men to come. The nearest source of water was 3 days away and with no re-supply possible the exercise turned from hard to critical. Although all the recruits came from nearby areas, they had no water discipline, which we found out to our cost. By strictly rationing and sending the strongest for help, everyone survived, but it's a lesson they will never forget.

Lessons learnt:
- Never underestimate the power of self-preservation.
- Protect your water supply.
- Enforce strict rationing.
- Of all the discomforts, thirst is the deadliest.
- When treating a person with dehydration, wet their lips first and look for a gag reflex (swallowing). Administer small sips only.
- When giving treatment, always make sure the patient is lying down in any available shade."""
                ]
            },
            {
                "title": "Polar Regions & Arctic Travel",
                "subtitle": "Seasons, temperature drops, wind chill calculations, and navigation on shifting sea ice.",
                "imageName": "climate.jpg",
                "textSections": [
                    """POLAR CONDITIONS: Antarctica is covered with a sheet of ice. In the Arctic the Pole is capped by deep ice floating on the sea and all the land north of the timber line is frozen. There are only two seasons - a long winter and a short summer - the day varying from complete darkness in midwinter to 24 hours daylight at midsummer.

Arctic summer temperatures can rise to 18°C (65°F), except on glaciers and frozen seas, but fall in winter to as low as -56°C (-69°F) and are never above freezing point. In the northern forests summer temperatures can reach 37°C (100°F), but altitude pushes winter temperatures even lower than in the Arctic. In Eastern Siberia -69°C (-94°F) has been recorded at Verkhoyansk! Temperatures in the Antarctic are even lower than in the Arctic.

Antarctic winds of 177km/h (110mph) have been recorded and, in the Arctic autumn, winter winds reach hurricane force and can whip snow 30m (100ft) into the air, giving the impression of a blizzard - even when it is not snowing. Accompanied by low temperatures, winds have a marked chilling effect - much greater than the thermometer indicates. For instance, a 32km/h (20mph) wind will bring a temperature of -14°C (7°F) down to -34°C (-30°F), and one at 64km/h (40mph) would make it -42°C (-44°F) with even greater drops at lower temperatures. Speeds over 64km/h (40mph) do not appear to make a greater difference.""",
                    """POLAR TRAVEL & NAVIGATION:

Experience shows the best policy is to stay near an aircraft or disabled vehicle. If the spot is hazardous, establish a safe shelter as close by as possible. A decision to walk-out will be based on nearness to civilisation and probability of rescue. Decide early what to do - while you can still think clearly. Cold dulls the mind. Movement in a blizzard is out of the question and, at all times, navigation is difficult on featureless ice and tundra. Ice movement pushes up ridges which make the going treacherous. Summer melt water makes the tundra boggy and even sea ice slushy underfoot. Mosquitoes, black-fly, deerfly and midges can all be a nuisance in the arctic summer. Their larvae live in water - avoid making shelter nearby. Keep sleeves down, collar up, wear a net over the head and burn green wood and leaves on the fire - smoke keeps them at bay. When it turns colder, these nuisances are less active and they disappear at night.

In Alaska, northwestern and northeastern Canada, Greenland, Iceland, Scandinavia, Novaya Zemlya, Spitzbergen and on other islands there are mountains where ice cliffs, glaciers, crevasses and avalanches are hazards. Near the Arctic coastline frequent fog from May to August, sometimes carried far inland, increases navigation problems.

• Navigation: Compasses are unreliable near the Poles; the constellations are better direction-finders and the nights are light enough to travel by. By day use the shadow tip method. Travelling on sea ice do NOT use icebergs or distant landmarks to fix direction. Floes are constantly moving - relative positions may change. Watch for ice breaking up and, if forced to cross from floe to floe, leap from and to a spot at least 60cm (2ft) from the edge. Survivors have been rescued from floes drifting south but sooner or later ice floating into the warmer oceans will melt - though that chance may be worth taking.

• Ice Hazards: AVOID icebergs, they have most of their mass below the water. As this melts, they can turn over without warning, particularly with your added weight. AVOID sailing close to ice-cliffs. Glaciers may 'calve' huge masses of ice, often thousands of tons, which break off into the sea without warning. Bird observations can aid navigation. Migrating wildfowl fly to land in the thaw. Most seabirds fly out to sea during the day and return at night.

• Sky Reflections: Sky reflections help to determine distant terrain. Clouds over open water, timber or snow-free ground appear black below; over sea ice and snowfields, white. New ice produces greyish reflections, mottled ones indicate pack ice or drifted snow."""
                ]
            },
            {
                "title": "Cold Weather Clothing & Gear",
                "subtitle": "Snow shoes, river travel, hypothermia warnings, layering guidelines, and shelter building.",
                "imageName": "climate.jpg",
                "textSections": [
                    """SNOW SHOES & RIVER TRAVEL:

All polar travel is strenuous and should only be attempted by a fit person. On snow with a hard crust, skis are the best means of travel, though difficult to improvise. Skiing in deep loose snow takes great effort and, in soft snow, snow shoes are better. To walk in snow shoes, lift each foot without angling it, unlike a normal stride, keeping the shoe as flat to the ground as possible.
How to make improvised snow shoes: Bend a long green sapling back on itself to form a loop and secure the ends firmly. Add crosspieces and twine - the more the better - but do not make the shoes too heavy. You will not be able to walk far without getting very tired. Allow a firmer central section to attach to your foot.

Follow rivers downstream by raft in summer, on the ice in winter - except in northern Siberia where rivers flow north. On frozen rivers keep to smoother ice at the edges and to outer curves on the bends. Where two rivers join follow the outside edge or take to the outer bank. If the river has many bends, leave the ice and travel by higher ridges.""",
                    """WARNING: ICE COLD WATER IS A KILLER:

Falling into icy water knocks the breath out of you. The body curls up with loss of muscular control and violent shivering. Exposed parts freeze in about 4 minutes, consciousness clouds in 7, death follows in 15-20.
RESIST! Take violent action on hitting the water. Move fast for land. Then roll in snow to absorb water. Get to shelter and into dry kit immediately.""",
                    """CLOTHING & EYE PROTECTION:

Severe cold and harsh winds can freeze unprotected flesh in minutes. Protect the whole body, hands and feet. Wear a hood - it should have a drawstring so that it can partly cover the face. Fur trimming will prevent moisture in the breath freezing on the face and injuring the skin. Outer garments should be windproof, with a close enough weave to prevent snow compacting, but porous enough to allow water vapour to escape - NOT waterproof, which could create condensation inside. Under layers should trap air to provide heat insulation. Skins make ideal outer clothing. Openings allow heat to escape; movement can drive air out through them. If clothing has no draw strings, tie something around sleeves above cuffs, tuck trousers into socks or boots.

If you begin to sweat, loosen some closures (collar, cuffs). If still too warm, remove a layer. Do so when doing jobs like chopping wood or shelter building. Only a plane crash or forced landing is likely to leave someone in polar regions unequipped. Try to improvise suitable clothing before leaving the plane. Wear wool - it does not absorb water and is warm even when damp. Spaces between the knit trap body heat. It is best for inner garments. Cotton acts like a wick, absorbing moisture. When wet, it can lose heat 240 times faster than when dry.

• Feet: Mukluks, boots of waterproof canvas with a rubber sole which comes up to the caulk and with a drawstring to adjust fitting, are ideal. Ideally they should have an insulated liner. Insulate feet with three pairs of socks, graded in size to fit over each other and not wrinkle. If necessary, improvise foot coverings with several layers of fabric. Canvas seat covers can make improvised boots. Trenchfoot can develop when the feet are immersed in water for long periods, as in the boggy tundra during the summer months.

• Snow Glare: Protect the eyes with goggles or a strip of cloth or bark with narrow slits cut for eyes. The intensity of the sun's rays, reflected by snow, can cause snow blindness. Blacken beneath the eyes with charcoal to reduce glare further.""",
                    """CLOTHING & SHELTER PRINCIPLES:

Use the **C.O.L.D.** rules to keep warm:
- C: Keep it CLEAN - Dirt and grease block insulating air spaces!
- O: Avoid OVERHEATING - Ventilate by opening cuffs/collars before you sweat!
- L: Wear it LOOSE - Allow air to circulate!
- D: Keep it DRY - Outside and inside!

SHELTER: You cannot stay in the open to rest. GET OUT OF THE WIND! Look for natural shelter you can improve on, but AVOID the lee side of cliffs where snow could drift and bury your shelter, or sites where rock falls or avalanches are likely. Avoid snow-laden trees - the weight could bring down frozen branches - unless the lower boughs are supported on the snow. There may be a space beneath the branch which will provide a ready-made shelter.

REMEMBER: Don't block EVERY hole to keep out draughts. You MUST have ventilation, especially if burning a fire inside your shelter. Otherwise you may asphyxiate."""
                ]
            },
            {
                "title": "Polar Fuel, Water & Wildlife",
                "subtitle": "Drain sump oil, blubber fuels, casiope plant, melting ice vs snow, polar bears, and seals.",
                "imageName": "climate.jpg",
                "textSections": [
                    """FUEL & WATER SOURCING:

FIRE: Essential for polar survival. Fuel oil from wreckage can provide heat. Drain oil from the sump and reservoir onto the ground as soon as possible - as it cools it will congeal and become impossible to drain. High octane fuel does not freeze so quickly - leave it in the tanks. In the Antarctic and on the Arctic ice, seal and bird fat are the only other fuel sources. On coasts, driftwood can sometimes be collected. In the tundra, low, spreading willow can be found. Birch scrub and juniper also grow beyond the forests. Birch bark makes excellent kindling - the wood is oily. Feather a branch and it will burn even when wet.

• Casiope: Another low-spreading, heather-like plant that Eskimos use for fuel. Evergreen, with tiny leaves and white bell-shaped flowers, and only 10-30cm (4-12in) high, it contains so much resin that it, too, burns when wet.

WATER: Even in the cold you need over a litre (1¾ pt) daily to replace losses. In summer, water is plentiful in tundra lakes and streams. Pond water may look brown and taste brackish but vegetation growing in it keeps it fresh. If in doubt, BOIL. In winter, melt ice and snow. DO NOT eat crushed ice; it can injure your mouth and lips and also cause further dehydration. Thaw snow sufficiently to mould into a ball before attempting to suck it. Remember: if already cold and tired, eating snow will further chill your body.""",
                    """POLAR FOOD & WILDLIFE:

• Antarctic: Lichens and mosses, growing on dark, heat-absorbing rocks on some northern coasts, are the only plants. Seas are rich in plankton and krill which support fish, whales, seals and many seabirds. Most birds migrate in autumn, but flightless penguins stay. They make good eating. Most of the year they take to the water at the first sign of danger but, when incubating eggs, sit tight on their burrows or scrapes.

• Arctic: Ice provides no habitat for plants or ground animals. Even polar bears are likely only where they can find prey - and they are difficult and dangerous to hunt. Seabirds, fish and seals, where there is water, are the potential foods. Foxes - the Arctic fox turns white in winter - sometimes follow polar bears onto sea ice to scavenge their kills. Northern wildlife is migratory and availability depends on the season.

• Tundra and Forest: Plants and animals can be found in winter and summer, and the northern forests offer even more wildlife. Tundra plant species are the same in Russia as in Alaska. All are small compared to warmer climate plants: ground-spreading willow, birch and berry plants with high vitamin content. Lichens and mosses, found widely, form a valuable food source - especially reindeer moss.

• Poisonous Plants: The majority of Arctic plants are edible, but AVOID Water Hemlock - the most poisonous. AVOID the fruit of the Baneberry. AVOID small Arctic buttercups. Other temperate poisonous species found far north include Lupin, Monkshood, Larkspur, Vetch (Locoweed), False Hellebore and Death Camas. Best avoid fungi too - make sure you can distinguish lichens from them! There are no Arctic plants which are known to produce contact poisoning.

• Animals for Food: Bark and greenery stripped from trees is evidence of feeding animals. Caribou (reindeer) are common from Alaska to west Greenland and found across northern Scandinavia and Siberia. Shaggy musk-ox roam in northern Greenland, and in the islands of the Canadian archipelago, elk (moose) are found where there is a mixture of forest and open ground. Wolves are common in northern Canada, Alaska and Siberia (but rare and protected in most European countries). Foxes, mountain hares, squirrels and lemmings are also found. Bears roam the barren lands of the north as well as the forests. They can be dangerous. Give them a wide berth.""",
                    """HUNTING, TRAPPING & SEALS:

Tracks are clear in the snow and easy to follow - but leave a trail of fluttering flags of bright material from wreckage to find your way back to your shelter. Make them high enough not to be covered by a fresh snowfall. Caribou can be very curious and may sometimes be lured by waving a cloth and moving on all fours. Imitating a four-legged animal may also bring wolves closer, thinking you might be prey. Some prey animals can be attracted by the sound made by kissing the back of your hand. Stalking animals is difficult in the exposed Arctic. Use a screen of cloth or snow to hide.

• Seals: A main source of food on polar ice, some seals remain there right through the winter. The Antarctic Weddell seal can dive for 15 minutes before coming up to breathe from pockets of air beneath the ice, or at small holes which it keeps open by nibbling around the edges. Newborn seals cannot swim and are easy to catch. Breathing holes in the ice are the best place to catch seals; recognize them by their cone shape (narrower on the upper surface). Club the animal then enlarge the hole to recover the carcass. Seals provide food, clothing, moccasins and blubber for fires. Eat all except the liver, which has DANGEROUS concentrations of vitamin A. Cook seal meat and polar bear meat to avoid Trichinosis.

• Polar Bears: Confined to the high Arctic, they have a keen sense of smell and are tireless hunters on sea ice. Feeding mainly on seals, they are powerful and dangerous. Always cook their meat: muscles always carry the Trichinosis worm. NEVER eat polar bear liver which has lethal concentrations of vitamin A.

• Preparing Meat: Bleed, gut and skin while the carcass is still warm. Roll hides before they freeze. Cut meat into usable portions and allow to freeze. Do not keep reheating. Remove seal fat and render it down before it turns rancid. Cache food carefully to prevent theft by animals. Rodents, rabbits and hares can carry Tularemia, which can be caught from ticks or handling infected animals. Wear gloves when skinning. Boiled flesh is safe."""
                    """### Fuel & Water Sourcing

#### Fire & Fuel Sourcing
Essential for polar survival. Fuel oil from wreckage can provide heat. **Drain oil from the sump and reservoir onto the ground** as soon as possible - as it cools it will congeal and become impossible to drain. High octane fuel does not freeze so quickly - leave it in the tanks.
* **Blubber**: In the Antarctic and on the Arctic ice, seal and bird fat are the only other fuel sources.
* **Driftwood**: On coasts, driftwood can sometimes be collected.
* **Tundra Plants**: In the tundra, low, spreading willow can be found. Birch scrub and juniper also grow beyond the forests. Birch bark makes excellent kindling - the wood is oily. Feather a branch and it will burn even when wet.
* **Casiope**: Another low-spreading, heather-like plant that Eskimos use for fuel. Evergreen, with tiny leaves and white bell-shaped flowers, and only 10-30cm (4-12in) high, it contains so much resin that it, too, **burns when wet**.

#### Water Sourcing
Even in the cold you need over a litre (1.75 pints) daily to replace losses. In summer water is plentiful in tundra lakes and streams. Pond water may look brown and taste brackish but vegetation growing in it keeps it fresh. If in doubt, **BOIL**.
In winter, melt ice and snow:
* **Do NOT eat crushed ice**: It can injure your mouth and lips and also cause further dehydration.
* **Thaw snow sufficiently** to mould into a ball before attempting to suck it.
* *If already cold and tired, eating snow will further chill your body.*""",
                    """### Polar Food & Wildlife

#### Antarctic Food Sources
Lichens and mosses, growing on dark, heat-absorbing rocks on some northern coasts, are the only plants. Seas are rich in plankton and krill which support fish, whales, seals and many seabirds. Most birds migrate in autumn, but flightless penguins stay. They make good eating. Most of the year they take to the water at the first sign of danger but, when incubating eggs, sit tight on their burrows or scrapes.

#### Arctic Food Sources
Ice provides no habitat for plants or ground animals, even polar bears are likely only where they can find prey - and they are difficult and dangerous to hunt. Seabirds, fish and seals, where there is water, are the potential foods. Foxes sometimes follow polar bears onto sea ice to scavenge their kills. Northern wildlife is migratory and availability depends on season.

#### Tundra and Forest
Plants and animals can be found in winter and summer, and the northern forests offer even more wildlife. Tundra plant species are the same in Russia as in Alaska. All are small: ground spreading willow, birch and berry plants with high vitamin content. Lichens and mosses, found widely, form a valuable food source - especially reindeer moss.
* **Poisonous Plants**: The majority of Arctic plants are edible, but **AVOID Water Hemlock** - the most poisonous. AVOID the fruit of the Baneberry. AVOID small Arctic buttercups. Other temperate poisonous species found far north include Lupin, Monkshood, Larkspur, Vetch (Locoweed), False hellebore and Death camas. Best avoid fungi too - make sure you can distinguish lichens from them!
* **Animals for Food**: Caribou (reindeer) are common from Alaska to west Greenland and found across northern Scandinavia and Siberia. Shaggy musk-ox roam in northern Greenland. Elk (Moose) are found where there is a mixture of forest and open ground. Wolves, foxes, mountain hares, squirrels, rodents, beavers, mink, wolverines and weasels can all be found.
* **Bears**: Bears roam the barren lands of the north as well as the forests. They can be dangerous. **Give them a wide berth.**""",
                    """### Hunting, Trapping & Meat Preparation

#### Hunting & Trapping
Tracks are clear in snow and easy to follow - but leave a trail of fluttering flags of bright material from wreckage to find your way back to your shelter. Make them high enough not to be covered by a fresh snowfall.
* **Caribou**: Can be very curious and may sometimes be lured by waving a cloth and moving on all fours.
* **Small Prey**: Ground squirrels and marmots may run into you if you are between them and their holes. Some documentation shows they can be attracted by the sound made by **kissing the back of your hand** (mimicking a wounded mouse or bird).
* **Seals**: A main source of food on polar ice, some seals remain there right through the winter. Newborn seals cannot swim and are easy to catch. Out of the breeding season, breathing holes in the ice are the best place to catch seals; recognize them by their cone shape. Club the animal then enlarge the hole to recover the carcass. Seals provide food, clothing, moccasins and blubber for fires. Eat all except the liver, which has **DANGEROUS concentrations of Vitamin A**. Cook seal meat to avoid *Trichinosis*.
* **Walruses**: Walruses may look cumbersome but are also very dangerous. **LEAVE THEM ALONE UNLESS YOU ARE ARMED.**
* **Polar Bears**: Always cook meat: muscles always carry the *Trichinosis* worm. **NEVER eat polar bear liver** which can have lethal concentrations of Vitamin A.

#### Preparing Meat
Bleed, gut and skin while the carcass is still warm. Roll hides before they freeze. Cut meat into usable portions and allow to freeze. Do not keep reheating. Once cooked, eat leftovers cold. Leave fat on all animals except seals. Fat is essential in cold areas but, if you eat a lot, make sure you take plenty of fluids. Remove seal fat and render it down before it turns rancid.
* **Tularemia Warning**: Rodents, especially squirrels, and rabbits/hares, can carry **Tularemia**, which can be caught from ticks or handling infected animals. Wear gloves when skinning. Boiled flesh is safe.""",
                    """### Arctic Health & Cold Safety

#### Core Hazards
Frostbite, hypothermia and snow blindness are the main hazards, while efforts to keep warm and exclude draughts can lead to lack of oxygen and carbon monoxide poisoning.
* **Mental Withdrawal**: It is easy to withdraw from reality, layered in clothing and with the head wrapped in a hood. Thinking can become sluggish and obvious things overlooked. **Keep active, keep 'switched on', and conserve energy.**
* **Defecation**: Don't put off defecation - constipation is often brought on that way. Try to time it conveniently before leaving your shelter.

#### Health Safety Guidelines
* **Face**: Wrinkle your face to stop stiff patches forming, pulling muscles in every direction. Exercise hands.
* **Monitoring**: Watch yourself and others for patches of **waxy, reddening or blackened skin**, especially on faces, ears, and hands (signs of frostbite).
* **Circulation**: AVOID tight clothing which will reduce circulation. Exercise fingers and toes to improve circulation.
* **Snow Protection**: Knock snow off before entering shelter, or leave outer clothing at the entrance. Snow will melt in warmth, giving you wet clothing.
* **Metal Warning**: Wear gloves and keep them dry. **NEVER touch metal with bare hands.**
* **Petrol Danger**: AVOID spilling petrol on bare flesh. In sub-zero temperatures it will freeze almost at once and does even more damage than water because of its lower melting point."""
                ]
            },
            {
                "title": "Mountain Navigation & Descents",
                "subtitle": "Improvised shelters, judging steep slopes, climbing safety rules, and descent footwork.",
                "imageName": "climate.jpg",
                "textSections": [
                    """### Mountain Exposure & Shelters

Mountain peaks are exposed to high winds and often covered in snow. They provide neither food nor shelter. Climbing rock and negotiating ice and snowfields calls for special skills. No inexperienced person should think of trying to tackle real mountaineering territory, except in a survival situation.
* **Core Goal**: If no rescue is likely, the first aim in daylight should be to **get down into the valleys** where food and shelter are available. At night and in bad visibility this is too dangerous. Some kind of shelter must be found until visibility improves.
* **Improvising Shelter**: Dig into the snow if there is no shelter among rocks and no wreckage to provide cover. If below the snow line you must cover yourself to prevent exposure. A plastic bag will make an improvised sleeping bag. Do not pull clothes too tightly round you; air within the clothes will provide insulation.
* **Sleeping Position**: On a slope, sleep with your **head uphill**; on rough and stony ground sleep on your stomach for greater comfort.""",
                    """### Judging Terrain & Descending

#### Judging Terrain
As you descend a mountainside it will often be difficult to see what is below you. Can you move around a valley or along a spur to look back at what was below? The opposite side of a valley will give you some idea of what is on your side too. Be cautious if you find you are looking at a distant slope beyond a foreground bluff; the ground is likely to fall steeply between. Scree slopes can be particularly deceptive and appear continuous until you are very close to a cliff.

#### Cliff Descent without Ropes
Negotiating cliffs without a rope is extremely dangerous.
* **Facing the Cliff**: On the steepest cliffs it is necessary to come down facing the cliff, making it very difficult to see footholds below. If there is an adjoining slope, a colleague can observe and give directions.
* **Sideways Position**: To climb down rock faces which are less steep and with deeper ledges, adopt a sideways position using the inside hand for support.
* **Facing Outwards**: For easier crags, descend facing outwards with the body bent and where possible carry weight on the palms of the hands.""",
                    """### Climbing Ascent Rules

Climbing upwards, holds are easier to see, but it is always safer to go round than over obstacles if you are travelling without knowing the route.
1. **Plan the Route**: Always work out your route from the bottom.
2. **Keep Distance**: In climbing, keep the body away from the rock and look up.
3. **Three Points of Contact**: Move only one hand or one foot at a time - always keep **three points of contact**.
4. **Leg Strength**: Keep your weight evenly balanced on the feet rather than hang from the hands. Use small intermediate holds, avoid becoming spread-eagled and let the legs do most of the work. Always place the feet as flat as possible to make maximum contact with the rock.
5. **Chimney Technique**: To climb vertically up fissures, place your back against one surface and wedge your legs across the gap to the other. Slowly move up."""
                ]
            },
            {
                "title": "Ropes, Abseiling & Belaying",
                "subtitle": "Rappelling body loop steps, belaying body wrapping, taking up slack, and avoiding falling rock.",
                "imageName": "climate.jpg",
                "textSections": [
                    """### Ropes & Abseiling (Rappelling)

With a rope firmly anchored at the upper level, it is possible to descend the sheerest cliff. The technique, known as **abseiling or rappelling**, can involve a special sit sling and a karabiner, but the basic method uses just a doubled rope. The rope does not move - you move down it.
* **Preparation**: Friction can damage clothing and skin, so if you can, pad out your shoulders and groin, and wear gloves. Make sure that you are in a safe position before hauling the rope down - its sudden weight could affect your balance.
* **Anchor Point**: The length of the rope controls the amount of descent and there must be a firm anchor point - a rock, or tree which can carry the weight and not cut the rope.

#### Abseiling Steps (Body Loop Method)
1. **Loop & Test**: Loop the rope around a firm anchor and test it with your full body weight. Avoid sharp edges.
2. **Pass Between Legs**: Pass both ends of the rope between your legs from the front.
3. **Wrap Around Body**: Bring the rope around to the left of your body, diagonally across your chest, over your right shoulder, and down across your back.
4. **Two-Handed Grip**: Hold the rope in front with your left hand and at the back with your right hand.
5. **Position**: Plant your feet about 45cm (18in) apart firmly against the slope and lean back. Let the rope around your body carry your weight. Do not try to support yourself with your upper hand.
6. **Descent**: Step slowly downwards. The lower hand controls the rate of descent by paying the rope out one hand at a time.

*CAUTION: Abseiling can be highly dangerous. If not trained in the technique, NEVER attempt it unless accompanied by an expert or in a survival situation.*

#### Using a Cradle
On an unobstructed vertical descent, a cradle made from a **bowline-on-the-bight** can be used to lower people down, or haul them up. Use this technique to rescue anyone who has fallen down a crevasse.""",
                    """### Belaying & Ascents

Belaying is a method of helping others to climb up. First, one person must make the ascent with a rope attached around the waist with a bowline. At each stage of the ascent there must be a platform to accommodate the party and a secure anchor (a tree, spike of rock, or wedged boulder). Anchor the rope with a loop tied in a figure-of-eight or an overhand knot.

The belayer ties on to steady himself, passes the climbing rope over his head and down to his hips, making a twist around the arm closest to the anchor, and takes up the slack. The climber ties on with a bowline around the waist and begins to mount. The belayer takes in the rope to keep it taut.

#### How to Take Up Rope:
1. Pull with both hands so that the rope passes behind your back (pull in with right hand, push away with left).
2. Slide your right hand out for more rope.
3. Bring hands together and hold both parts of the rope in your right hand while the left slides in towards your body to take up slack.
4. Begin again, pulling in with right hand, pulling rope around body with left. **Be ready to arrest the rope if the climber falls.**

The anchor, belayer, and climber should be in a straight line. Older people and children should be roped around the chest. Small children are best carried papoose-style on another climber's back.
*Note: Belaying without an anchor is risky and requires more strength. The rope should then only pass through the belayer's fingers, NOT around the back, lest the belayer be pulled down.*

#### WARNING: Falling Rock Can Kill!
On loose rock always test holds gently and never pull outwards on a loose hold. Be careful that your rope does not dislodge rocks. Even small falling rocks can inflict serious injury. If you knock a piece down, **shout a warning to those below**."""
                ]
            },
            {
                "title": "Icefields, Crevasses & Avalanches",
                "subtitle": "Snow stick brakes, ice mushrooms, crevasse extraction, and avoiding avalanches.",
                "imageName": "strategy.jpg",
                "textSections": [
                    """### Snow & Icefields

On snow, some ice-axe techniques can be improvised with a stout stick - a handled walking stick gives more grip. Driven into the snow when climbing, it gives stability. On steep slopes climb in zig-zags, kicking steps and digging your stick in. On gentle slopes use heels and the stick as a walking cane. On steep slopes descend backwards, driving the stick into the snow for support and as a brake. Sliding down a snow slope is dangerous: digging in the heels helps control speed, but there is always a risk of an unseen precipice ahead! Never slide where there is an avalanche risk.

#### Security Ropes on Ice
Any party moving across a glacier should be tied together, at not less than **9m (30ft) intervals**. The leader should probe the snow with a stick for crevasses. Fix security ropes to a firm anchor at both ends to steady movement across ice patches.

#### Ice & Snow Bollards
If no rock is available, cut an anchor from the ice.
* **Ice Bollard**: Cut a mushroom shape at least 40cm (16in) in diameter and 15cm (6in) deep. Discard at the slightest sign of a crack.
* **Snow Bollard**: Must be much bigger: at least 30cm (1ft) deep and from 1m (3ft) wide in hard snow to 3m (10ft) in soft. Pack gear around it to prevent the rope cutting through.

#### Crevasses
Crevasses are found where a glacier starts at a valley wall, changes direction or spreads. If one of the group falls through, he is belayed by a rope. Pressure on the chest can cause asphyxiation. Pass a rope down with a loop for the victim's foot. If the victim is unconscious, it will take **three people** with man-harness hitches to heave him out. Temperatures are very low; speed is important.""",
                    """### Avalanches & Mud Slides

Avalanches are a serious hazard on slopes of between 20° and 60° (especially **30° to 45°**), usually within 24 hours of a fresh snowfall.
* **Triggers**: Temperature, ground conditions, noise, and human disturbance. Avoid steep ground with fresh snow. Waiting 24 hours for it to settle helps. Rain or a rise in temperature after a snowfall increases risk by lubricating the slide. Heavy snow falling during low temperature can also avalanche because it does not have enough time to stabilize.
* **Slope Types**: Convex slopes under tension are highly unstable. Deep snow-filled gullies and lee slopes are also dangerous. Slopes with rocky outcrops and trees are safer to cross than bare ones.

#### Precautions & Crossings
Test the snow first by digging in your stick to check for layers. Shout or throw rocks to encourage a slide from a safe, protected spot. Rope together and keep **15m (50ft) apart** to spread the load.
* **Convex vs Concave**: Never make camp on the lee side of a convex slope; a concave slope is safer.

#### Mud Slides
Masses of mud sliding on water bury everything. Avoid low-lying areas and wadis; stay on spurs and ridges. If caught, use swimming actions to stay on top and **go feet first**."""
                ]
            },
            {
                "title": "Seashores, Estuaries & Rocky Coasts",
                "subtitle": "Sandy, muddy, and rocky shore resources, tides, and undertow safety.",
                "imageName": "climate.jpg",
                "textSections": [
                    """### Seashore Environments

Most seashores offer abundant sources of food. Coastal waters are home to seaweeds, fish, seals, birds, molluscs, and plankton. Coasts range from sheer cliffs to gently sloping beaches. A beach at the foot of a cliff is easily cut off by high tide.

#### Sandy Beaches
Gentle and sloping, exposing large areas at low tide containing burrowing worms and molluscs. Blown dunes may contain fresh water and vegetation. Dunes are full of insects - **do not choose them for camp**.

#### Muddy Shores & Estuaries
Rivers deposit nutrient-rich sediment forming mud flats that support worms, molluscs, and feeding wildlife.

#### Rocky Shores
Trap pools of water when the tide recedes. Rock pools teem with life. Rocks provide surfaces for univalve shells, sea urchins, seaweed, and crevices for octopuses. Hard fractured rocks provide nesting sites for seabirds.

#### Pebble Beaches
Sustain the least life. The continual movement of pebbles makes a difficult habitat for plants and animals.""",
                    """### Tides & Shore Dangers

#### Tides
Tides vary by location and season. In enclosed seas (e.g. Mediterranean) they change only a few metres. In the Bay of Fundy, they can rise up to **16m (52½ ft)**. Look for the debris line, dry vs wet sand textures, and weed lines on cliffs to determine high tide. Always keep an eye on rising water levels to prevent being cut off. Tides wash up valuable driftwood fuel and trap fish in rock pools.

#### Shore Dangers
*Never underestimate the power and danger of the sea.* Time the tides. Cliffs present access problems; make sure you can get back up. Look out for strong currents off headlands. Sandbanks and submerged rocks are dangerous. Beaches falling steeply into deep water have a **strong undertow**. Use a safety line when entering the water to retrieve kit.""",
                    """### Swimming, Floating & Fresh Water

#### Swimming Safety
If caught in the undertow of a large wave, push off the bottom and swim to the surface. Swim to shore in the trough between waves; face and submerge under oncoming waves.
* **Offshore Currents**: If a current sweeps you offshore, do not fight it - **swim ACROSS it** using side stroke (least tiring) and make for land further down.
* **Swept onto Rocks**: If swept onto rocks, face shorewards, keep shoes on, and adopt a sitting position with **feet in front** to absorb the impact.

#### Floating
A relaxed body floats best. Women float naturally on their backs (extra layer of fat); men float naturally face down - lift head to breathe.

#### Fresh Water Sourcing
Look for small river outlets (large ones are silty/polluted). On sandy shores, dig above high-water mark near vegetation down to moist sand; scoop the fresh water floating on top of the salt water. Rock pools above high-water mark with green algae indicate fresh water.
* **Sea Water Warning**: **NEVER drink sea water without distilling it** - it causes kidney failure. Saltwater can be used to cook, but only if you have adequate fresh water. Use salt residue to preserve meat."""
                ]
            }
        ]
    },
    {
        "title": "Food Procurement",
        "description": "Wild foraging rules, setting primitive animal traps, and hunting/fishing techniques.",
        "articles": [
            {
                "title": "Food & Food Values",
                "subtitle": "Energy requirements, carbohydrates, fats, proteins, and vitamins.",
                "imageName": "food_foraging.png",
                "textSections": [
                    """### Food & Food Values

To survive, you need to understand your body's nutritional needs and how to meet them. In most circumstances, **plants** will be the most readily available food source, but you must know which ones are safe. A healthy body can survive for a time on stored reserves, but a lack of food makes it increasingly difficult to keep warm, recover from injuries, and fight off disease.

#### Energy Needs
The average person in a completely restful state requires **70 calories per hour** just to maintain basic metabolism (involuntary functions like breathing and blood circulation). Simple domestic activities demand another **45 calories per hour**. In a survival situation, physical effort, mental effort, and anxiety can burn up an additional **3,500 calories daily**. Keep calm, relax, and if food is scarce, **DO NOT SQUANDER ENERGY**.

*   **Carbohydrates** (*1g produces 4 calories*): The bulk of the diet and main source of energy. Found as sugars (fruit, honey, syrup) and starches (roots, cereals). Starch granules are insoluble in cold water, but heat causes them to rupture - this is why roots and tubers must be cooked.
*   **Fats** (*1g produces 9 calories*): A concentrated source of energy, providing twice as many calories as carbohydrates. They require a lengthy digestive process which demands an adequate intake of **water**.
*   **Proteins** (*1g produces 4 calories*): Essential for the growth and repair of the body, made of amino acids. Worms contain the highest amount of proteins, containing the eight essential amino acids humans require. Do not squeeze them; isolate them in a container so they dehydrate and preserve their properties.

#### Vitamins & Minerals
*   **Vitamins**: Essential to health and protection from illness. The body naturally carries a **28-day supply** of vitamins. **Vitamin C** is the first that will need to be replenished (herbs are rich in it). **Vitamin A** is the second to go; it aids vision and prevents eye disease. Eat the green shoots and leaves that you see rabbits eating.
*   **Minerals**: Calcium is needed for bones and teeth, while sodium, potassium, and magnesium regulate vital body functions.
*   **Trace Elements**: Tiny amounts of elements like iron, fluorine, and iodine are also required to keep the body running."""
                ]
            },
            {
                "title": "Universal Edibility Test",
                "subtitle": "A step-by-step method to test unknown plants for toxicity.",
                "imageName": "food_foraging.png",
                "textSections": [
                    """### The Universal Edibility Test

If you are unsure of a plant's identity, you must perform the **Universal Edibility Test**. Only one person should test each plant. **NEVER take short cuts - complete the whole test.** If in any doubt, do NOT eat the plant. If stomach trouble occurs, drink plenty of hot water. Inducing vomiting with charcoal or wood ash mixed with water can relieve stomach pain.

1.  **Inspect**: Ensure the plant is not slimy or worm-eaten. Older plants can change chemical content and become toxic.
2.  **Smell**: Crush a small portion. If it smells of *bitter almonds or peaches*, **DISCARD IT IMMEDIATELY** (indicator of prussic acid).
3.  **Skin Irritation**: Rub the juice onto a tender area (e.g., under the arm between armpit and elbow). If any rash, swelling, or discomfort occurs, **DISCARD**.
4.  **Lips, Tongue & Mouth**: If no skin irritation, proceed in stages, waiting **5 seconds** after each:
    *   Touch a small portion to the lips.
    *   Place a small portion in the corner of the mouth.
    *   Place a small portion on the tip of the tongue.
    *   Place a small portion under the tongue.
    *   Chew a small portion.
    *   *If any stinging, burning, or discomfort occurs, DISCARD.*
5.  **Swallow**: Swallow a small amount and **wait 5 hours**. Eat or drink NOTHING else during this period.
6.  **Eating**: If no abdominal pain, nausea, sickness, or stomach griping occurs, the plant is safe."""
                ]
            },
            {
                "title": "Gathering Plants",
                "subtitle": "Harvesting techniques and toxic species to avoid.",
                "imageName": "food_foraging.png",
                "textSections": [
                    """### Gathering Plants & Species to Avoid

#### Gathering Guidelines
*   **Leaves & Stems**: Gather young, pale green growth; older leaves are tough and bitter. Nip off leaves near the stem to prevent damaging and wilting them.
*   **Roots & Tubers**: Dig around the plant to loosen the soil, then pry them out with a sharpened stick to prevent breaking.
*   **Fruit & Nuts**: Pick only ripe, fully colored fruits. Peel tough, bitter skins.
*   **Seeds & Grains**: *Warning!* Avoid grain heads with black spurs. These indicate **ergot poisoning**, a dangerous, hallucinogenic, and sometimes fatal fungal disease. REJECT the whole head!

#### Plants to Avoid
*   **Milky Sap**: AVOID any plant with milky sap, unless positively identified (like dandelions).
*   **Red Foliage**: AVOID red plants, unless positively identified (e.g., the red-streaked stalk of wild rhubarb is edible, but its leaf is poisonous). Hemlock has reddish-purple splotches on its stem.
*   **Five-Segment Fruit**: AVOID fruits divided into five segments.
*   **Barbed Stems**: AVOID grasses or leaves with microscopic hooks that can irritate the mouth and digestive tract.
*   **Poisonous Compounds**:
    *   *Hydrocyanic Acid* (Prussic acid): Smells like bitter almonds (found in Cherry Laurel).
    *   *Oxalic Acid*: Causes a sharp, dry stinging sensation (found in wild rhubarb leaves and wood sorrel).
*   **Bracken Warning**: AVOID mature bracken. It destroys Vitamin B in the body. Eat only tightly coiled young "fiddle heads." All 250 varieties of north temperate ferns are edible when young if you strip their woolly hairs."""
                ]
            },
            {
                "title": "Finding Game & Tracks",
                "subtitle": "Identifying animal trails, tracks, droppings, and feeding signs.",
                "imageName": "food_trapping.png",
                "textSections": [
                    """### Finding Game

Most mammals move at **first and last light**. Larger herbivores graze during the day, while smaller mammals feed mostly at night. To trap or hunt them, you must identify the signs they leave behind.

#### Tracks & Signs
*   **Trails**: Look for runs on wet ground, mud, sand, or snow. Dew and spider webs disturbed on a trail indicate recent activity (within a few hours).
*   **Broken Twigs**: Check height to estimate the animal's size. Trampled leaves that haven't wilted yet indicate a fresh track.
*   **Droppings**:
    *   *Herbivores* (deer, rabbits): Round, straw-like pellets.
    *   *Carnivores* (foxes, wild cats): Long, tapering droppings containing fur and bones.
    *   *Pellets*: Owls and hawks produce pellets containing indigestible fish, bird, or rodent bones. Loose droppings indicate water is nearby, as small birds must stay close to it.
*   **Feeding Signs**: Deer bite off shoots leaving frayed edges, while hares leave a clean, angled bite. Gnawed shells or stripped bark also indicate animal presence. Squirrels strip bark high up, dropping pieces to the ground.
*   **Rootings**: Turned-up soil indicates pigs or boars searching for tubers.
*   **Burrows & Dens**: Many animals live in burrows on high ground. Rabbits' emergency exits are often hidden but can be dug out or hooked with brambles."""
                ]
            },
            {
                "title": "Traps and Snares",
                "subtitle": "Building simple/spring snares, deadfalls, and spear traps.",
                "imageName": "food_trapping.png",
                "textSections": [
                    """### Constructing Snares & Traps

Trapping is far more energy-efficient than active hunting, allowing you to gather plants, collect water, or build shelter while your traps work for you.

#### Simple & Spring Snares
*   **Simple Snare**: A wire loop with a running noose placed at head-height on an active run. The loop should be supported by small twigs. Snare wire is ideal because it holds its shape.
*   **Spring-Pole Snare**: Uses a bent sapling under tension. When triggered, it lifts the animal off the ground, keeping it safe from other predators.

#### Deadfalls & Spear Traps
*   **Figure-4 Deadfall**: A classic trigger mechanism configured in a "4" shape using three notched sticks: a vertical support, a diagonal arm, and a horizontal bait stick. It drops a heavy rock or log on small prey like rodents or squirrels.
*   **Spear Traps**: Heavy spring-activated spears designed for larger game trails. *Use with extreme caution!*

#### WARNING: Rabbit Starvation
Rabbits can provide the easiest of meals, but their meat is extremely lean and lacks essential fat and vitamins. **A diet of pure rabbit meat can lead to death.**
The human body uses its own stored vitamins and minerals to digest the lean protein of rabbit meat, passing them out of the body. Without fats and carbohydrates, you will experience severe weakness, diarrhea, and eventually starvation.
*   *Stewardship*: Always supplement meat diets with wild plants, roots, or fats from other animals (fish, beaver tails, nuts) to maintain a balanced metabolism.
*   *Disease*: Myxomatosis causes swelling on rabbits' heads, making them blind and sluggish. The disease does not harm humans, but cooked flesh must be handled cleanly. Look out for white spots in the liver which indicate infection or Tularemia."""
                ]
            },
            {
                "title": "Mammalian Game Guide",
                "subtitle": "How to handle wildcats, wild dogs, bears, pigs, rabbits, and squirrels.",
                "imageName": "food_trapping.png",
                "textSections": [
                    """### Mammalian Identification & Tactics

*   **Wild Cats**: Secretive and nocturnal. Avoid large cats. Small wildcat meat tastes like rabbit.
*   **Wild Dogs & Canines**: Highly curious; moving on all fours or kissing the back of your hand can draw them closer. Remove anal scent glands before cooking. Wolves/hyenas require thorough cooking to destroy parasites.
*   **Bears**: Solitary and highly dangerous. Wounded bears will attack. **NEVER eat Polar Bear liver**; it contains lethal concentrations of Vitamin A.
*   **Wild Pigs & Boars**: Dangerous when cornered; their tusks can sever the femoral artery. Wallow sites and rooting areas are excellent spots for traps. Cook pork thoroughly to avoid trichinosis.
*   **Rabbits & Hares**: Look for runs. Young rabbits can sometimes be picked up by hand.
*   **Beavers**: Found near dams. Highly nutritious, especially the fat-rich tail.
*   **Squirrels**: Set small wire loop snares along a pole leaned against the tree trunk.
*   **Badgers & Hedgehogs**: Hedgehogs curl up and are easy to catch. Young badger tastes like pork. Both must be cooked thoroughly.
*   **Wolverines**: Chunkier than badgers, highly aggressive. Do not tackle unless armed.
*   **Kangaroos & Wombats**: Kangaroos strike powerfully with hind feet; wombats live in burrows and are trapped like badgers.
*   **Opossums & Raccoons**: Excellent tree climbers, highly inquisitive. Bait spring snares with fruit."""
                ]
            },
            {
                "title": "Reptiles & Amphibians",
                "subtitle": "Crocodiles, lizards, tortoises, edible frogs, toads to avoid, and snakes.",
                "imageName": "food_hunting.png",
                "textSections": [
                    """### Reptile & Amphibian Sourcing

*   **Crocodiles & Alligators**: Avoid large ones. Small specimens under 1.3m (4.5ft) can be caught by baiting a line with a stick. Tail meat is white and extremely tasty. Kill with a sharp blow between the eyes.
*   **Lizards**: All lizards are edible. Catch small ones by the tail or trap them in pits. Avoid the giant Komodo dragon.
*   **Turtles & Tortoises**: Turn them on their backs with a stick to make them defenceless. Cut through the belly shell, discard the head/neck (which can contain poison glands), and boil the meat. Boiled turtle eggs inside females are edible.
*   **Frogs & Toads**: Remove frog skins before cooking to avoid surface toxins. **AVOID toads**; their warty skins secrete highly dangerous toxins. Salamanders and newts are also edible.
*   **Snakes**: A snake is a steak! Use a forked stick to pin the head down, then crush it. **AVOID venomous snakes** unless fully equipped. Never touch the head even after death. The large constrictors (pythons, boas) are not poisonous but have backward-curved teeth.
*   **Birds & Eggs**: All birds are edible. Game birds (grouse, pheasant) are delicious. Sea birds can be oily but are good sources of fat. Eggs are safe and nutritious at any stage of embryo development."""
                ]
            },
            {
                "title": "Fishing & Angling",
                "subtitle": "Angling, fish traps (weir), plant narcotics, and preparing fish.",
                "imageName": "food_hunting.png",
                "textSections": [
                    """### Fishing Techniques

*   **Angling**: Use improvised hooks made of bone, wood, or thorns, and lines of braided plant fiber or inner bark. No angling skills are required for basic survival fishing.
*   **Fish Weir**: A V-shaped stone wall built across a stream that funnels fish into a shallow pool where they can be easily speared or netted.
*   **Fish Narcotics**: Certain plants (like crushed buckeye, lime, or specific narcotics) stun fish when thrown into calm pools, causing them to float to the surface.
*   **Preparing Fish**: Clean fish immediately, remove guts and gills, and cook thoroughly to kill any parasites."""
                ]
            }
        ]
    },
    {
        "title": "Camp Craft",
        "description": "Constructing emergency shelters, starting campfires, and mastering survival knots.",
        "articles": [
            {
                "title": "Shelter & Making Camp",
                "subtitle": "Mindset for camp site selection, weather considerations, and choosing locations.",
                "imageName": "campcraft.jpg",
                "textSections": [
                    """### Shelter & Making Camp

Shelter is necessary to give shade, to repel wind and rain and to keep in warmth. Sleep and adequate rest are essential and the time and effort you put into making your shelter comfortable will make them easier to get. If you are the victim of a plane crash or a vehicle that has let you down, it may provide a shelter or materials from which one can be built - but if there is fire or the threat of fuel tanks exploding, wait until it has burned out before attempting salvage.

If you are the unequipped victim of an accident, are trapped by unexpected mist or caught by nightfall in terrain where it is not safe to proceed, or if exhaustion or injury prevents you going further, you may have to make do with any natural shelter that you can find for the night, or until you can more fully assess the situation. In this case, virtually any protection from wind, rain and cold will be welcome. If movement down a slope seems risky, traversing even a short way along the contour may bring you out of the wind. If no cave or crevice is available to give shelter, make use of any hollow in the ground. Add to its height, if you can, by piling up rocks - but make sure that any structure is stable and use a back-pack, if you have one, to increase the windshield before settling down on the leeward side.

If there is still daylight to see by, you have no injuries to handicap you and are not isolated by unnegotiable cliffs or other barriers, it will be worth seeking possible better places in the vicinity. For a long-term camp you should find a secure site with convenient access to your major needs.""",
                    """### Where to Camp

If you are on high exposed ground go lower down to find a sheltered spot, but on low, wet ground you will need to climb higher to find somewhere securely dry. Look for somewhere sheltered from the wind, on rising ground that has no risk of flooding and is safe from rock falls or avalanches.

Hot air rises, cold air sinks, so valley bottoms will often contain pockets of colder air and, in cold weather, be susceptible to frost and damp mist. In areas that get plenty of rainfall, terraces across a slope will often be damper than the steeper ground above and below them, for water collects there before flowing further downward.

Ideally you should be near water, with a plentiful supply of wood near at hand. Pitching camp too close to water, however, may lead you to be troubled by insects, and the sound of running water can hide other noises which might indicate danger, or the sound of search or rescue parties.

On river banks look for the high water mark: in mountain regions streams can become torrents in minutes, rising as much as 5m (17ft) in an hour! Even on plains keep out of old watercourses, no matter how dry they are. Heavy rainfall in nearby hills can easily send water rushing down them in flash floods, with practically no warning.

Choose ground that is reasonably flat and free of rocks and make sure that you have space to layout signals and that you can be easily spotted by rescue parties.

Check above your head for bees' or hornets' nests and for dead wood in trees that could come crashing down in the next storm or high wind. Keep away from solitary trees, which attract lightning, and in forest areas keep to the edges, where you can see what is going on around you. Don't camp across a game trail - you don't want marauding animals as unwelcome guests or to find your bivouac flattened by a herd of animals on their way to a waterhole - but stay near to any obvious human tracks."""
                ]
            },
            {
                "title": "Types of Shelters",
                "subtitle": "Hasty covers, bough/root shelters, saplings, and sheet setups.",
                "imageName": "campcraft.jpg",
                "textSections": [
                    """### Hasty & Bough Shelters

The type of shelter you build will depend upon local conditions and the materials available - and upon how long you expect to need it. For immediate protection from the elements, rig up a makeshift shelter while you construct something better and more permanent. If you decide to stay put and wait for rescue, a more long-term shelter can be built and improved on as time and energy permit.

*   **Hasty Shelters**: If no materials are available for constructing a shelter, make use of any cover and protection that is available: cliff overhangs, gradients and so forth, which will help shield you from wind or rain. Incorporate natural windbreaks. In completely open plains, sit with your back to the wind and pile any equipment behind you as a windbreak.
*   **Bough Shelters**: Make use of branches that sweep down to the ground or boughs that have partly broken from the tree to give basic protection from the wind - but make sure that they are not so broken that they could come down on your head! Weave in other twigs to make the cover more dense. Conifers are more suited to this technique than broad-leaved trees, as they require less weaving-in to keep out rain.
*   **Root Shelter**: The spreading roots and trapped earth at the base of a fallen tree make a good wind and storm barrier, if they are at the right angle to the wind. Filling in the sides between the extended roots will usually make the shelter much more effective, and provide a good support for building a more elaborate shelter from other materials.""",
                    """### Natural Hollows, Fallen Trunks & Barriers

*   **Natural Hollows**: Even a shallow depression in the ground will provide some protection from wind and can reduce the effort in constructing a shelter. However, take measures to deflect the downhill flow of water around it, especially if it is a hollow on a slope, or you could find yourself lying in a pool. Make a roof to keep the rain off and the warmth in. A few strong branches placed across the hollow can support a light log laid over them, against which shorter boughs and sticks can be stacked to give pitch to the roof and so allow water to run off. Consolidate with turf or with twigs and leaves.
*   **Fallen Trunks**: A log or fallen tree trunk makes a useful windbreak on its own, if it is at the right angle to the wind. With a small trunk, scoop out a hollow in the ground on the leeward side. A log also makes an excellent support for a lean-to roof of boughs.
*   **Stone Barriers**: A shelter is more comfortable if you can sit rather than lie in it, so increase its height by building a low wall of stones around your chosen hollow or shallow excavation. Caulk between the stones (especially the lowest layer) with turf and foliage mixed with mud.
*   **Sapling Shelter**: If suitable sapling growth is available, select two lines of saplings, clear the ground between them of any obstructions and lash their tops together to form a support frame for sheeting. Weigh down the bottom edges of the sheeting with rocks or timber.""",
                    """### Shelter Sheets & Covered Lean-Tos

*   **Shelter Sheet**: With a waterproof poncho, groundsheet or a piece of plastic sheeting or canvas, you can quickly and easily make a number of different shelters. Make a triangular shelter with the apex pointing into the wind. Stake or weigh down edges. If it is long enough, curl the sheeting below you - running downhill so that it keeps out surface water. Use dry grass or bracken as bedding. Do not lie on cold or damp ground.
*   **Tepees**: The quickest type to erect has three or more angled support poles, tied where they cross to make a cone. They can be tied on the ground and lifted into place before covering with hides, birch bark panels or sheeting. Leave an opening at the top for ventilation.
*   **Coverings**: Make wattle and woven coverings for roofs or walls from springy saplings, plant stems, grasses and long leaves. Overlap large leaves like tiles to keep out rain.
*   **Open Lean-To Shelter**: Erect a horizontal cross-piece between trees or on simple supports. On the windward side lean a panel of wattle, or tie or lean saplings at 45 degrees to make a roof. Site your fire on the leeward side. Add side pieces and build a reflector on the other side of the fire to make sure that you get the full benefit of the warmth. You can take this to its logical conclusion by adding a canopy to the front supported by vertical poles."""
                ]
            },
            {
                "title": "Tropical & Bamboo Shelter",
                "subtitle": "Raised jungle beds, Atap thatch weaving, and using bamboo.",
                "imageName": "campcraft.jpg",
                "textSections": [
                    """### Tropical Raised Bed & Atap Thatching

In rain forests and tropical jungle the ground is damp and likely to be crawling with insect life, leeches and other undesirables. Instead of bedding down on the ground you will be better in a raised bed. Consequently you may want to make higher shelters.

Unless you are at an altitude high enough to make the nights cold, you will be less concerned with protection from the wind than with keeping reasonably dry. A thatching of palm, banana and other large leaves makes the best roofs and walls.

*   **ATAP (Wait-a-while vine)**: Atap is especially useful, despite the barbs at each leaf tip which make careful handling necessary. Atap is best used horizontally, splitting each leaf into two from the tip then tearing it into two clean halves down its length. Closely layer halves of atap on your roof frame. You can let it be a little less dense on walls. Woven atap can be particularly effective for the sides of a shelter.
*   **Interweaving Leaflets**: Fold the leaflets on one side across to the other and interweave them. Three-lobed leaves can be locked over a thatching frame without any other fixing being necessary to hold them in place. Palm and other long-stemmed leaves can be secured by carrying the stem around the batten and over the front of the leaf, where it is held in place by the next leaf. Leaves must overlap those below on the outside of the shelter.""",
                    """### Working with Bamboo

Bamboo, a large-stemmed grass, is a very versatile building material and can be used for pole supports, flooring, roofing and walls.

*   **Roofing & Guttering**: Split bamboo vertically to make roofing and guttering to collect rainwater. The split stems, laid alternately to interlock with one another, form efficient and waterproof pantiles.
*   **Flooring & Walls**: Flatten split bamboo for smooth walls, floors or shelving by cutting vertically through the joints every 1.25cm (1/2in) or so around the circumference. It can then be smoothed out.

> [!WARNING]
> Take great care when collecting bamboo. It grows in clumps that are often a tangled mass. Some stems are under tension and when cut fly forcefully and dangerously apart, exploding into sharp slivers.
> Split bamboo can be razor-sharp and cause serious injury. The husks at the base of bamboo stems carry small stinging hairs which cause severe skin irritations."""
                ]
            },
            {
                "title": "Arctic & Snow Shelter",
                "subtitle": "Snow caves, trenches, igloos (spiral/circular), and ventilation safety.",
                "imageName": "campcraft.jpg",
                "textSections": [
                    """### Polar Bivouacs & Snow Trenches

In polar areas simple shelters will be those already waiting for you in natural caves and hollows. If you carry some kind of bivouac, you can erect it and increase its protection by piling up loose snow around and over it. To build in hard snow, you need some kind of implement like spades or ice saws to cut it into blocks.

*   **Conifer Spaces**: A medium-sized tree in northern forests may have a natural space right around the trunk beneath the spreading boughs. Try digging under any tree with spreading branches on the lee side.
*   **Snow Trench**: A quick shelter suitable for one person for short-term use. Mark out an area the size of a sleeping bag and cut out blocks. Dig down at least 60cm (2ft). Along the top of the sides cut a ledge 15cm (6in) wide and deep. Rest the snow bricks on each side of the ledge and lean them in against each other to form a roof. Block the windward end with a block or piled snow, and use a removable block as a door downwind. Fill gaps with loose snow.""",
                    """### Snow Caves & Igloos

*   **Snow Cave**: Dig into a drift of firm snow. Create three levels inside: build a fire on the highest, sleep on the center one, and keep off the lower level which will trap the cold air. Drive a hole through the roof for smoke and another for ventilation. Use a loose-fitting block on the inside as a door so it won't freeze up and jam. Smooth the inside surfaces to discourage melt drips and make a perimeter channel to carry moisture away.
*   **Igloo (Circular Method)**: Mark a circle about 4m (13ft) in diameter and tramp it down. Cut and lay a circle of blocks (45 x 50cm and 10-20cm thick). Center new blocks over the previous vertical joints. Place each layer halfway over the lower tier so it tapers dome-shaped. Make ventilation holes near the top and bottom. Smooth the inside to remove drip-points.
*   **Igloo (Spiral Method)**: Lay the first course of blocks and shape them to the required spiral. Angle the top edge slightly down towards the center. Shape top and bottom faces of subsequent courses to lean inwards. Cut the final block to fit.""",
                    """### Inside the Snow Shelter & Safety Tips

*   **Temperature**: No matter how low the external temperature, inside a well-constructed snow house the temperature will not drop lower than -10°C (14°F). Just burning a candle will raise it by about four degrees.
*   **Dryness**: Do not carry loose snow into the shelter; knock it off boots and clothing before entering.
*   **Tools**: Keep shovels and tools inside the shelter - you may have to dig yourself out.
*   **Igloo Drips**: Drips can be stopped by placing a piece of snow on the source.

> [!IMPORTANT]
> All shelters MUST be adequately ventilated to prevent carbon monoxide poisoning and allow moisture to escape. Two holes are needed - one near the top and one near the entrance. Regularly check holes to ensure they have not become blocked by snow or ice."""
                ]
            },
            {
                "title": "Long-Term Cabins & Caves",
                "subtitle": "Constructing log cabins, jointing corners, rock shelters, and sanitation.",
                "imageName": "campcraft.jpg",
                "textSections": [
                    """### Using Caves

Caves are the most ready-made of shelters. Even a shallow rock shelter offers an excellent temporary shelter, and a larger cave can make an excellent permanent home.
*   **Wind Screen**: If the cave faces into the wind, build a screen out from both sides, one slightly behind the other, overlapping them to provide a baffled entrance.
*   **Fire Placement**: Build the fire at the back of the cave. Smoke will go up to the roof, leaving clear air nearer the floor. A fire near the mouth will pull smoke inwards.

> [!WARNING]
> Check for the possibility of a rock fall inside or outside the cave. Ensure any structure is stable. Animals may occupy the cave; a good fire will usually make them leave. Allow them an escape route.""",
                    """### Building a Log Cabin

A log cabin provides a highly durable permanent home. Scale your cabin to the number it is to house. A 2.5m (8ft) square is a sensible small size.
*   **Corner Joints**: Lay down your first layer of logs in the shape of your hut. Joint the corners by notching them to fit on top of each other. Center new logs to lock the walls. Place logs alternately top-to-bottom to counter natural wood tapering.
*   **Doorway & Ventilation**: Leave space for a doorway on the side away from the prevailing wind. Wedge a sturdy door frame in place. The doorway provides sufficient ventilation; windows are unnecessary.
*   **Roofing**: Build up the front higher than the back to give pitch to the roof. Lay a roof of logs or light timber frame, notch them, and cover with saplings, mud, and turf. Bark from the logs makes an excellent top covering if laid as tiles.
*   **Caulking**: Caulk between logs with mud, wood chips, grass, and moss. Use a sharpened stick to force it into the seams.

### Sanitation & Clean Water
*   **Ablutions**: All washing, cleaning, and waste disposal must be carried out **downstream** of your camp to ensure your drinking water supply upstream remains uncontaminated."""
                ]
            },
            {
                "title": "Fire Lighting & Fuel",
                "subtitle": "Fireplace preparation, tinder/kindling, temple fires, and alternate fuels.",
                "imageName": "campcraft.jpg",
                "textSections": [
                    """### Fireplace Preparation & Design

Fire is essential to survival. It provides warmth, protection, signals, and purifies water.
*   **Clearance**: Scrape away leaves, twigs, moss, and dry grass from a circle at least 2m (6ft) across down to bare earth. Except for signals or to warm a temporary bough shelter, do not light a fire at the base of a tree or stump.
*   **Platform (Wet Ground)**: On wet ground or snow, build the fire on a platform of green logs covered with earth or stones.
*   **Temple Fire**: On swampy land or deep snow, raise a hearth platform on green timber. Four uprights support cross-pieces in their forks, supporting a layer of green logs covered with several inches of earth.
*   **Windy Design**: In strong winds, dig a trench and light the fire inside. Encircle the fire with rocks to retain heat.

> [!WARNING]
> Avoid placing wet or porous rocks near fires (especially river-submerged rocks) as they contain moisture that expands rapidly when heated, causing them to explode and throw dangerous fragments.""",
                    """### Sourcing Tinder, Kindling & Fuel

*   **Tinder**: Material that takes the minimum heat to catch alight (birch bark, dried grass, fine wood shavings, bird down, charred cotton, bat droppings). *Must be kept dry in a waterproof container.*
*   **Kindling**: Dry twigs and softwoods that flare up quickly to raise the flames. Sourced from standing deadwood rather than the damp ground. Shave sticks with shallow cuts to "feather" them.
*   **Fuel**: Heavy woods (hickory, oak, beech) burn hot and slow, forming long-lasting coals. Softwoods (cedar, alder, hemlock, pine) burn too fast and throw sparks. Keep green logs drying next to the fire, but not so close that they ignite.

### Alternate Fuel Sources
*   **Animal Droppings**: Dry thoroughly for a smokeless fire.
*   **Peat**: Fibrous black peat from moors dries quickly when stacked with air gaps.
*   **Oils & Fats**: Burn petroleum, anti-freeze, or engine oils using a wick. Mix petrol with sand in a container as a stove. Animal blubber can be burned by placing a network of bones over a starter flame to support the fat.
*   **Oil & Water Mixture**: One of the hottest fires. Drip 2-3 drops of water to 1 drop of oil onto a hot metal plate heated by a small starter fire below."""
                ]
            },
            {
                "title": "Ignition & Cooking Utilities",
                "subtitle": "Matches, lenses, battery sparks, wild cooking, and meat preservation.",
                "imageName": "campcraft.jpg",
                "textSections": [
                    """### Methods of Ignition

*   **Matches**: The easiest way. Carry "strike anywhere" matches in a waterproof container. Waterproof them by dipping heads in paraffin wax. Whenever you strike a match, **light a candle** first; you can then light many things from the candle and conserve matches.
*   **Lens Focus**: Focus strong direct sunlight through a magnifying glass, camera lens, or telescope lens onto your tinder.
*   **Ammunition Powder**: Pour gunpowder from a cartridge onto tinder, or stuff a cloth plug into a half-emptied casing and fire it into the ground to retrieve a smouldering ember.
*   **Flint & Steel**: Strike a steel blade or wire saw against flint to throw sparks. Scrape magnesium shavings onto tinder first for hot ignition.
*   **Battery Spark**: Attach two wires to a battery's terminals. Touch the bare ends together over tinder (such as a petrol-soaked cloth) to jump a spark.
*   **Fire Bow**: Rotate a hardwood spindle on a softwood base using a bow string under tension to generate friction embers.""",
                    """### Wilderness Cooking & Preservation

Cooking makes food safe, digestible, and boosts morale.
*   **Useful Utensils**: Improvise pots from clay, metal wreckage, or hollow green bamboo. You can boil water in a paper cup or large leaf by placing it directly over coals—the water prevents the container from burning.
*   **Food Preservation**:
    *   **Smoking**: Hang strips of meat or fish inside a teepee structure over a slow, smoky fire (using green hardwoods like oak or maple). Avoid pine/conifers as they deposit bitter resin.
    *   **Drying**: Slice meat thin (6mm) and hang in the wind and hot sun away from flies.
    *   **Salting**: Rub salt into the meat to dehydrate and preserve the flesh.
*   **Cooking Tips**: Boil wild game thoroughly to kill parasites. Cook wild pork (boar) completely to avoid trichinosis. Roast roots in hot ashes to break down insoluble starches."""
                ]
            },
            {
                "title": "Ropes, Lines & Knots",
                "subtitle": "Rope making from fibers, simple/joining knots, loops, and hitches.",
                "imageName": "campcraft.jpg",
                "textSections": [
                    """### Making Ropes & Cordage

If you lack manufactured rope, you can spin sturdy cordage from wild plant fibers, inner tree bark, nettles, or animal hide.
*   **Fiber Sourcing**: Gather nettle stems, inner bark of cedar or elm, or fibrous roots. Soak tough bark in water to separate fibers.
*   **Spinning Ropes**: Split the fibers into thin threads. Twist two strands tightly in a clockwise direction, then cross them over each other counter-clockwise (or vice versa). This reverse-twist lock prevents the rope from unraveling. Feed in new fibers continuously to build length.""",
                    """### Essential Knots & Lashings

Knots must be practiced until you can tie them in the dark with cold, numb hands. Keep all ropes dry and check regularly for fraying.
*   **Simple Knots**:
    *   **Overhand Knot**: The simplest stopper knot.
    *   **Figure-of-Eight**: A reliable stopper knot that is easier to untie after holding a load.
*   **Joining Ropes**:
    *   **Square Knot (Reef Knot)**: Used to join two ropes of equal thickness. *Not for critical safety.*
    *   **Sheet Bend**: Used to join two ropes of unequal thickness, ensuring a secure connection.
*   **Loop-Making**:
    *   **Bowline**: Creates a secure, fixed loop at the end of a rope that will not slip or jam. The "king of knots," ideal for rescue cradles and anchors.
    *   **Bowline-on-the-Bight**: Creates two secure loops in the middle of a rope for hauling casualties.
*   **Hitches**:
    *   **Clove Hitch**: Secures a rope to a post or tree trunk, commonly used to start shelter lashings.
    *   **Taut-Line Hitch**: A friction hitch allowing easy adjustment of line tension, perfect for tarp guy-lines.
*   **Lashings**: Use square lashings to join poles at right angles, and shear lashings to form tripod supports for A-frame structures and tepees."""
                ]
            }
        ]
    },
    {
        "title": "Reading the Signs",
        "description": "Off-grid navigation, predicting weather fronts, and signaling search and rescue.",
        "articles": [
            {
                "title": "Understanding Maps",
                "subtitle": "Reading contours, scale, grids, and local magnetic variation.",
                "imageName": "navigation.jpg",
                "textSections": [
                    """### Maps & Terrain Interpretation

Before embarking on any expedition you will have learned all you can about the terrain, equipped yourself with maps, if available, and worked out routes. Memorize the lie of the land, the direction in which rivers flow, the high ground, the prominent features, the prevailing winds, the weather patterns to expect and any known hazards, check the phase of the moon and times of first and last light - all of which will be invaluable knowledge if you find yourself in difficulties. In a case of accident you may find yourself in a totally unknown territory and have to find out everything about your location from the land itself.

In choosing a camp site, tracing water and finding the other necessities for survival you will need to interpret the surrounding countryside - the other side of a hill may offer quite different conditions - and if you decide not to stay put you will have to interpret both the general geography and the particular landscape as you proceed.

#### Contours & Height
Height cannot be reproduced on flat sheets of paper so altitudes are recorded at regular intervals (usually every 50ft or every 15m) and every point at this height is joined up by a line - the **contour line**.
*   **Steepness**: When the contours are closely grouped, the change in height is more rapid (steep). Greater spaces between the contour lines indicate gentler slopes.
*   **Concave vs Convex**: A *concave slope* (where you can see the top from the bottom) has the higher contours close together. A *convex slope* (where you cannot see the top from the bottom) has the low contours close together.""",
                    """### Map Scales, Keys & Coordinates

*   **Scale**: Ratio scales represent relative sizes: 1:50,000 means that every measure on the map represents a distance 50,000 times greater on the ground.
*   **Standardizations**: Rivers and paths are standardized. British Ordnance Survey (OS) maps show waterways as a single blue line until they represent a width of 8m (27ft) where a double line is used.
*   **Grids**: Grid coordinates allow you to pinpoint locations. Mentally divide a grid square into tenths to form a six-digit map reference (e.g., `155628`).
*   **Compass Variation**: Compass needles point to *magnetic north*, not *true north*. The deviation varies by location and year. Point your compass at the North Star to determine the local variation offset, and adjust your bearings accordingly.
*   **Drawing Your Own Maps**: If stranded, climb a tree or high ridge and draw a custom map. Plot ridges, streams, landmarks, traps, animal dens, and food foraging zones.

> [!TIP]
> **Overestimation Trap**: One of the most common errors is to overestimate how much ground you have covered. Always fit the physical ground you see to the map, rather than forcing the map to fit where you think you are."""
                ]
            },
            {
                "title": "Sun & Shadow Navigation",
                "subtitle": "Finding direction using shadow stick methods and wristwatches.",
                "imageName": "navigation.jpg",
                "textSections": [
                    """### Shadow Stick Methods

The sun rises in the east and sets in the west (approximately). Shadows move clockwise in the Northern Hemisphere and anti-clockwise in the Southern Hemisphere, offering direct orientation.

#### Shadow Stick Method 1
1.  On flat, clear ground, place a 1m (3ft) stick upright in the soil.
2.  Mark the tip of the shadow with a pebble or peg (this point is **West**).
3.  Wait at least 15 minutes, and mark the new shadow tip with a second peg (this point is **East**).
4.  Draw a straight line connecting the two marks. This is your East-West line. North-South runs perpendicular.

#### Shadow Stick Method 2 (High Accuracy)
1.  Mark the first shadow tip in the morning.
2.  Draw a clean, exact circle arc from the stick base, using the shadow length as the radius.
3.  As midday passes, the shadow shrinks and moves. In the afternoon when it expands back and touches the arc line, mark the exact contact point.
4.  Join the morning mark (West) and afternoon mark (East) to establish your line.""",
                    """### Direction by Watch

A traditional watch with hour and minute hands can be used to find direction. Set it to *true local time* (excluding daylight saving shifts). Note: This is inaccurate near the Equator where the sun is directly overhead.

*   **Northern Hemisphere**: Hold the watch horizontal. Point the hour hand directly at the sun. Bisect (split in half) the angle between the hour hand and the 12 o'clock mark. This line points due **South**.
*   **Southern Hemisphere**: Hold the watch horizontal. Point the 12 o'clock mark towards the sun. The midpoint between 12 and the hour hand points due **North**."""
                ]
            },
            {
                "title": "Improvised Compasses",
                "subtitle": "Magnetizing needles, floating compasses, and electrical charges.",
                "imageName": "navigation.jpg",
                "textSections": [
                    """### Magnetizing a Needle

A piece of ferrous metal wire (a sewing needle is ideal) can be magnetized to create an emergency compass.
*   **Stroking Method**: Stroke the needle repeatedly **in one direction only** against a piece of silk, or smoothly from end to end using a magnet. Do not rub back and forth.
*   **Suspension**: Suspend the magnetized needle from a loop of thread, avoiding any kinks or twists in the thread.

#### Floating Needle Compass
A suspended needle can be difficult to read on the move. Instead, place the magnetized needle on a small piece of dry leaf, paper, or bark, and float it in a still pool or container of water. It will align itself along the North-South axis.""",
                    """### Electrical Magnetization

If you have a power source of 2 volts or more (like a dry battery tin):
1.  Wrap insulated wire around the needle. If using bare wire, wrap a few layers of paper or cardboard around the needle first to insulate it.
2.  Attach the ends of the wire to the battery terminals for five minutes. The electrical current will magnetize the steel.

#### Razor Blade Compass
A thin, flat double-edged razor blade is made of two bonded metals. You can magnetize it simply by stropping it carefully against the palm of your hand. Suspend the blade from a thread to find the North-South orientation."""
                ]
            },
            {
                "title": "Nature's Pointers",
                "subtitle": "Reading vegetation growth, tree rings, moss, wind patterns, and the moon.",
                "imageName": "navigation.jpg",
                "textSections": [
                    """### Plant & Tree Pointers

Plants grow towards the sun. In the Northern Hemisphere, their flowers and most abundant growth face **South** (and **North** in the Southern Hemisphere).

*   **Moss growth**: On tree trunks, moss grows greener and more profuse on the side away from the sun (North in the Northern Hemisphere; South in the Southern Hemisphere). The sunny side will look yellowish to brown.
*   **Tree Rings**: Felled stumps show rings spaced wider on the side facing the Equator, where sunlight is abundant and growth is faster. Rings are tighter on the colder side.
*   **Grainy Bark**: Trees with grainy bark display a tighter grain pattern on the cold, north side.
*   **Compass Plants**:
    *   *North Pole Plant* (South Africa): Leans towards the north to maximize sun.
    *   *Compass Plant* (North America): Aligns its leaves directly North-South, showing a distinct profile from East/West.

### Wind & Animal Clues
Prevailing winds shape the landscape. Trees on exposed ridges are bent in one direction. Spiders build webs on the leeward (sheltered) side of structures. Sand and snow dunes feature gentle slopes facing the wind and steep drop-offs on the lee side.""",
                    """### Navigation by the Moon

The moon reflects the sun's light. As it orbits the earth, the lit side indicates direction.
*   **Waxing Moon** (growing towards full): Reflects light on the right (West).
*   **Waning Moon** (shrinking towards new): Reflects light on the left (East).
*   **Moonrise Rule**:
    *   If the moon rises *before* the sun sets, the illuminated side points **West**.
    *   If the moon rises *after* midnight, the illuminated side points **East**."""
                ]
            },
            {
                "title": "Navigating by the Stars",
                "subtitle": "Locating Polaris in the North and the Southern Cross in the South.",
                "imageName": "navigation.jpg",
                "textSections": [
                    """### The Northern Sky & Polaris

Stars rise in the east and set in the west. In the Northern Hemisphere, they circle a single stationary star—**Polaris (the Pole Star)**—which is located directly above true North.

#### Finding the Pole Star
1.  **The Plough (Big Dipper / Ursa Major)**: Locate the seven-star dipper shape. The two stars forming the outer edge of the bowl (Dubhe and Merak) are the **Pointers**. Draw a line from Merak through Dubhe and project it out five times the distance between them. This line lands on Polaris.
2.  **Cassiopeia**: A W-shaped constellation on the opposite side of Polaris from the Plough. The center star of the W points almost directly towards Polaris.
3.  **Orion**: Rises on its side due East and sets due West along the celestial Equator, visible in both hemispheres. Orion's belt (three aligned stars) points East-West.""",
                    """### The Southern Sky & The Southern Cross

The Southern Hemisphere lacks a bright star at the celestial pole. Instead, navigation relies on the **Southern Cross (Crux)** constellation.

#### Finding the South celestial pole
1.  Locate the Southern Cross (five stars, smaller than similar false crosses) situated near the **Coal Sack** (a dark patch in the Milky Way).
2.  Locate the two bright **Pointer Stars** next to the cross.
3.  Project an imaginary line along the long axis of the cross.
4.  Bisect the line between the two pointer stars and project it out perpendicular.
5.  The point where these two lines intersect is the South celestial pole. Drop a vertical line straight down to the horizon from this point to establish **South**."""
                ]
            },
            {
                "title": "Weather Prediction & Clouds",
                "subtitle": "Reading 10 cloud formations, animal forecasts, and atmospheric indicators.",
                "imageName": "navigation.jpg",
                "textSections": [
                    """### Cloud Formations & Weather Signs

Clouds are the most reliable short-term weather indicators. The higher the clouds, the finer the weather.
1.  **Cirrus** (*High, 6000m+*): Wispy "mares' tails" of ice crystals. Fine weather, but changes if they thicken.
2.  **Cirrostratus** (*High*): A thin white veil that creates a halo around the sun/moon. A shrinking ring indicates rain; an expanding ring indicates fine weather.
3.  **Cirrocumulus** (*High*): Small rippled "mackerel sky". Fair weather.
4.  **Altocumulus** (*Medium, 2000-6000m*): Fluffy, greyish masses with shadows. Appears after storms.
5.  **Altostratus** (*Medium*): A grey veil turning the sun to a watery disk. Thickening indicates rain.
6.  **Nimbostratus** (*Low, under 2000m*): Thick, dark rain clouds bringing hours of continuous rain/snow.
7.  **Stratocumulus** (*Low*): Lumpy, rolling grey clouds. May cause drizzle but clears at night.
8.  **Stratus** (*Low*): Uniform sheet of hill fog. Can cause drizzle, but if formed overnight, indicates a fine day.
9.  **Cumulus** (*Low*): Fluffy white cauliflower clouds. Indicates fair weather when separated, but can grow to cause showers.
10. **Cumulonimbus** (*Low to High*): Angry, towering thunderclouds with flat "anvil" tops. Brings lightning, thunder, wind, and hail.""",
                    """### Wildlife & Atmospheric Clues

*   **Animal Indicators**: Animals are sensitive to barometric changes. Birds fly high in fine weather and low before storms. Squirrels stockpile extra food and rabbits feed actively during the day before cold fronts.
*   **Fireside Clues**: If campfire smoke rises straight up, the weather is stable. If it swirls and is beaten down, a storm is coming.
*   **Humidity Indicators**: Salt clumping indicates rising humidity. Wooden handles swell, and curly hair or animal fur becomes tighter and less manageable.
*   **Sound & Smell**: Distant sounds are clearer before rain (moist air amplifies sound). Vegetation opens up, causing forest smells to be highly distinctive before rain.
*   **Sunset/Sunrise rules**:
    *   *Red sky at night*: Atmosphere is dry, indicating fine weather.
    *   *Red sky in the morning*: Approaching storm.
    *   *Grey morning*: Dry day (dew has collected on dust).
    *   *Grey sunset*: Approaching rain."""
                ]
            }
        ]
    },
    {
        "title": "On the Move",
        "description": "Planning routes, navigating groups, traveling at night, upland/jungle traversal, and crossing waterways.",
        "articles": [
            {
                "title": "The Decision to Move",
                "subtitle": "Assessing survival situations, trail marking, and carrying equipment.",
                "imageName": "travel.jpg",
                "textSections": [
                    "Except when local dangers or the need to find water and food make it imperative that you move away from the site of your accident to make camp, you will stay close in the hope of rescue. If you have injured persons and only limited food and water, it would make sense to send a party to contact help while others stay to care for the sick. The fittest and most able should be chosen to make the trek - unless they include a trained medic, who should stay with the sick.",
                    "But what if no rescue comes? Local resources may become exhausted: you go further each day to collect firewood, the game in the area has gone, plants, fungi, fruits and nuts are more difficult to find or require long forays out of camp. Under survival conditions there is also an increased risk of disease from staying too long in one place. Even with the strictest sanitary management the chance of disease gradually builds up.",
                    "Before you finally abandon camp leave signs that will make it clear you have been there and have moved on. Leave a message giving a list of who is in the party and details of your intentions. Mark the trail as you proceed so that if searchers do find the camp they will be able to follow you.",
                    "Build up a stock of preserved food, make water bottles and larger containers too if you envisage crossing waterless territory, litters or other means of transporting any remaining sick, the old or very young. Make suitable foot-coverings and clothing for everyone and packs to carry equipment and supplies. Some form of transport may be possible - a sledge or raft. Take shelter material with you - cloth, canvas, ponchos, even sticks if they are likely to be scarce in the terrain you are crossing.",
                    "### HUDSON BAY PACK\n\nA comfortable and easily improvised way of carrying equipment, this needs strong and preferably waterproof material about 90cm (3ft) square, two small stones and cord or strapping more than long enough to loop across the body.\n\n1. Place stones in diagonally opposite corners of the cloth.\n2. Fold ends of cloth over stones.\n3. Tie cord below the stones, securing them in position. The stones in turn prevent the cord slipping off.\n4. Lay cloth on the ground and roll possessions up tightly.\n5. Wrap pack around the body, either across the back or around the waist.",
                    "### BACK-PACK FRAME & FORK FRAME\n\n*   **Back-pack Frame**: Make a ladder frame to fit against your back, with a right angle projection at the bottom secured by side struts. Add shoulder straps and a belt loop. Use this to support a bag, a bundle of supplies or equipment tied into place.\n*   **Fork Frame**: A quicker, but less-efficient support can be made from a forked bough with cross-pieces to which baggage can be tied.\n*   **Baby Bag**: Carry babies and small children papoose style on your back or front. Tie lower corners of a rectangle of cloth around the waist, pop the child in and tie the upper corners around your neck. Pad at neck to ease pressure or chafing.",
                    "### MAKING A SLEDGE\n\nSledges are particularly useful on snow and ice, when they will move most smoothly, but may also be used on smooth ground. The shape of the front runners is critical, especially on snow. You can make use of doors and cowlings from a crashed aircraft or vehicle in the construction. Tie lines to the front runners with a bowline to the people hauling - ideally two at the front, and two at the rear as brakemen on gradients. Test thoroughly before using on a long trek.\n\n*   **Method 1**: Choose two forked branches and remove one side of each fork. Make smooth for the runners and lash on cross members.\n*   **Method 2**: Choose two longer supple runners. Bend and brace as shown in standard designs. This arrangement keeps the lashings off the ground and may be more comfortable for an injured person. Whichever method you use, add at least one diagonal for strength."
                ]
            },
            {
                "title": "Route Planning",
                "subtitle": "Scouting courses, following waterways, and maintaining direction.",
                "imageName": "travel.jpg",
                "textSections": [
                    "If you are on very high ground, above a large plain, it may be possible to plot out a route with some precision. In most situations visibility will be restricted and you will have to guess what is over the furthest ridge and what occupies the 'dead' ground ahead. Even when you can see the terrain ahead, it is difficult to see the details. What looks like a manageable slope may prove a barrier when you get closer to it. If you have them, make good use of field glasses in studying every potential route.",
                    "To see further you may consider climbing a tree - but keep close to the trunk and test each branch before risking your weight on it. This is NO time to risk a fall.",
                    "### FOLLOWING RIVERS\n\nFollowing a watercourse, however small, offers a route to civilization and a life-support system on the way. Most rivers lead eventually to the sea or great inland lakes. Apart from the rare exception where rivers suddenly descend beneath the earth, they offer clearly defined routes to follow. Sometimes, in their upper reaches, they may cut through gorges and it can be impossible or inadvisable to take a route along their banks, which may be steep, rocky and slippery. In that case take to high ground and cut off the bends, following the general course of the stream.",
                    "On more level ground a river is easier to follow and may well have animal trails beside it which you can use. In tropical conditions the vegetation is likely to be denser by the river - for the light can reach below the trees, and the banks may be hard to negotiate. If the river is wide enough it would be worth considering building a raft. Even if there is no bamboo, which makes an ideal raft-building material, there are likely to be sound fallen trees for timber.\n\n> [!TIP]\n> When, on flat plains, a river makes huge meanders, the inside of the loops may be swampy and prone to flooding - you can recognize such very wet ground by the lushness of the vegetation and rush-like plants. Avoid marshy areas if you can, and cut across the loop.",
                    "### MAINTAINING DIRECTION\n\nHaving decided upon a direction, try to maintain it. Choose a prominent feature in the distance and keep heading towards it. Travelling through forests makes orientation very difficult and a compass becomes a valuable asset.",
                    "If you are in featureless territory, but in a group of three or more, separate to follow each other at wider intervals and look back frequently. If you are following in each other's tracks those behind you will be directly behind each other. If the party always moves on in relay - one moving on ahead, then resting while everyone else moves up from the rear - the straight line will be maintained. On your own you can try to align yourself by looking backwards at your own tracks if they are visible, as they are likely to be on snow or sand. Better still, you can set up sticks or piles of stones in alignment with each other so that you can check that you are not deviating from your route.",
                    "If possible skirt rocky outcrops and areas of dense vegetation and, once on high ground, stick to it until certain that you have found the spur down which you can make the best progress in the desired direction."
                ]
            },
            {
                "title": "Moving in Groups",
                "subtitle": "Assigning responsibilities, formations, and maintaining contact.",
                "imageName": "travel.jpg",
                "textSections": [
                    "Always move in an organized manner, in some kind of formation, and not as an unruly gaggle. This way it will be easier to check that no stragglers have been left behind and to ensure that there is help for anyone in difficulty. Before setting out for the day, have a briefing to discuss the route, any obstacles expected and any special procedures.",
                    "### DIVIDE RESPONSIBILITIES\n\n*   **Scout (Number One)**: Responsible for selecting the best route, avoiding dead falls, loose rocks etc and finding the best way down a slope.\n*   **Navigator (Number Two)**: Responsible for making sure the scout, who will be preoccupied with skirting obstacles, maintains correct overall direction. Others should relieve them frequently, for the lead scout's job in particular is very tiring.\n*   **Group Foraging**: The rest of the party should keep their eyes open for edible plants, berries and fruits and everyone should be responsible for at least one other person to ensure that no one drops by the wayside.",
                    "A head count and check on everyone's condition is particularly important after a river crossing or negotiating a particularly tricky stretch of terrain. Someone should initiate equipment checks at frequent intervals.",
                    "Always travel in at least pairs - and be especially careful in bad weather, and if you have to travel at night, that you do not get split up.",
                    "> [!IMPORTANT]\n> It is usually the person in front who gets split off from the group - people are more likely to remember to look for the stragglers. The scout climbs over an obstacle, the second person sees the scout struggling and then sees an easier route to take - the rest of the party follow and the lead person is separated from the group. This is when the benefit of EVERYONE knowing the proposed route, and nominating prominent features as rallying points, is apparent. If separated or in an emergency everyone knows where to regroup.",
                    "Availability of water, fuel and plants may be an indication of what is available in similar locations further ahead. An eye should always be open for places that offer good shelter - if the weather suddenly turns bad you can backtrack to one of them."
                ]
            },
            {
                "title": "Pace and Progress",
                "subtitle": "Speed estimation, resting schedules, and night travel.",
                "imageName": "travel.jpg",
                "textSections": [
                    "### PACE AND ESTABLISHING SPEED\n\n*   A large group can send an advance party ahead with the responsibility for clearing the route and setting up the night's camp, ready for the slower-moving injured or less able. A clear trail will make the carrying of baggage and any unfit people much easier. Sick and injured should be provided with fully-fit escorts.\n*   Ensure that the lead person in the party does not go too fast for those behind. After an obstacle wait and allow everyone to catch up before moving on.\n*   It is best to try to maintain an even pace - smooth, pendulum-like movement tires the legs less than a jerky pace or flexing the knees. It helps to swing the arms - and they should certainly not be pushed in the pockets, especially when going up or down hills.\n*   Rest frequently. On average take a break of 10 minutes every 30-45 minutes, depending on the terrain and condition of the group.\n*   On steep ground the pace should be shortened, on easy ground lengthened. On descents avoid overstepping for this jars the body and increases fatigue.\n*   In estimating distance you have covered allow 3km (under 2 miles) per hour, but going uphill knock off a third.",
                    "### WALKING AT NIGHT\n\nNegotiating unknown territory at night can be very dangerous, but may be necessary in an emergency, or there are circumstances - in the desert for instance - when it may be more comfortable to travel at night.\n\nKeep to open country if you can. When looking at an object at night it is best to look at one side of it and not directly at it. It is difficult to distinguish anything in a dark central mass but the edges show more clearly and in poor light objects at the edges of your vision are often seen more distinctly.",
                    "> [!IMPORTANT]\n> It takes about 30-40 minutes for the eyes to get accustomed to the dark. Once this is achieved, the eyes must be protected from bright light or the night vision will be impaired for quite a while. If there is an unavoidable reason for having to use a light, cover one eye so that the vision in that eye at least will be retained. A red filter over a torch will help you to retain your night vision.",
                    "Walk SLOWLY in the dark and test each step before putting all your weight forward. If going down a slope use a shuffling step. The ears and nose are good sensors in the dark - the sound of a river or smell of vegetation can aid identification."
                ]
            },
            {
                "title": "Upland and Jungle Travel",
                "subtitle": "Navigating mountainous regions and dense tropical growth.",
                "imageName": "travel.jpg",
                "textSections": [
                    "### UPLAND TRAVEL\n\nIn mountainous and hilly country it is best to keep to high ground - it makes navigation easier. Rivers may be in steep-sided gullies and have rapids, falls, and slippery rocks that are difficult to negotiate on foot. You could end up spending an unhealthy length of time in the water.\n\nUse spurs to climb out of valleys and get on to the ridges. If they are very exposed you may have to drop down into the valleys for shelter at night and to find water but you will be able to cover more ground than by negotiating the spurs.",
                    "> [!NOTE]\n> Do not go down to the valley bottom if you can find shelter and water on the way. Pockets of cold air are quite often trapped in the bottom of valleys. If you carry water and shelter materials, stay on the high ground, choosing the most sheltered spot.",
                    "### STEEP SLOPES\n\n*   Traverse steep slopes in a zig-zag and as you change direction always set off with the uphill foot. This avoids having to cross your legs over each other, which can make you lose balance.\n*   When climbing steep slopes lock your knees together after each step - this rests the muscles.\n*   Descending steep slopes, keep your knees bent. Try to go straight down - and if you are picking up too much speed, sit back. Avoid loose rocks and scree but, if you have to negotiate loose surfaces, it helps to dig in the heels and lean back while descending.\n*   When climbing, test every foothold before putting your weight on it. Don't step on stones or logs on steep slopes, they may dislodge.",
                    "### JUNGLE TRAVEL\n\nIn dense jungle you may have to cut your way through if there is no way of going round. Chop downwards and as low as possible at the stems on both sides so that they fall away from the path you are making, not across it. Avoid leaving spikes standing; bamboo points can be lethal if someone stumbles. High growth and creeper can often be cut and travelled over.",
                    "> [!WARNING]\n> Don't try to tear through \"wait-a-while\" (atap and rattan) vines - they have thorns like fish hooks at the end of the leaf that will tear your clothes and skin. Back off and untangle. Rattan is one of the best sources of jungle water vines.",
                    "Keep feet covered to protect them from sapling spikes, snakes and chigoes (chiggers). Stop frequently to remove parasites. Chigoes ignored for more than an hour or so will cause infection."
                ]
            },
            {
                "title": "Waterways and Rafts",
                "subtitle": "Building river transport, bamboo assemblies, and steering.",
                "imageName": "travel.jpg",
                "textSections": [
                    "If a river is wide enough to be navigable, it will be easier to float on it than to walk beside it. More practical for the survivor than trying to hollow a canoe will be to construct a raft, which will not capsize so readily. All boats and rafts must be soundly tested in safe water near the camp before setting out on a journey.\n\nChoose leaning trees for they are the easiest to drop. With dead falls the top of the trunk is usually sound enough to use. Never take chances with a flimsy raft on any water. On mountain rivers there are often rapids which only a really tough structure will survive.",
                    "### BAMBOO RAFT\n\nA single layer will not support you unless it is very long, so go for a two-layer model. Cut thickish bamboo in 3m (10ft) lengths. Make holes through the nodes near the ends and half-way along. Pass stakes through these holes to connect the poles. Lash each of the poles to each of the stakes with twine, rattan or other vines. Make a second deck to fit on top of the first and lash the two together.",
                    "### GRIPPER BAR RAFT\n\nThis is the quickest raft to build. You need logs for the deck and four thickish stakes with some pliability which are long enough to overlap the width of the deck.\n\n1. Place two of the stakes on the ground and lay the logs over them.\n2. Place the other stakes on top.\n3. Tie each pair of stakes firmly together on one side.\n4. With a helper standing on top to force the other ends together, tie these so that the logs are gripped tightly between them. Notching the ends of these gripper bars will stop the ropes from slipping.",
                    "### STEERING AND PROPULSION\n\nTo steer the raft make a paddle rudder and mount it on an A-frame near one end of the raft. Secure the A-frame with guy-lines to the corners of the raft and tie the rudder onto it so that it does not slip. The rudder can also be used as a sweep for propulsion.\n\nIn shallow water the best means of controlling a raft is like a punt, but preferably with two long poles - with one person poling at one front corner of the raft, and another at the diagonally opposite back corner.",
                    "### RAFT SAFETY\n\n*   Tie all equipment securely to the raft or to the safety line, making sure nothing trails over the edges where it could snag.\n*   Everyone aboard should have a bowline attached around the waist and secured to a safety line or to the raft.\n*   In narrow swift-flowing rivers with dangerous rapids and waterfalls it is better not to tie on, as you may get dragged under if the raft capsizes.\n*   If the survival group is a large one, several rafts will be needed. The fittest should be on the first raft, carrying no equipment or provisions, acting as scouts to give early warnings.\n*   Only raft by day, NEVER in the dark. At night secure the raft firmly and make temporary shelter on higher ground away from the river."
                ]
            },
            {
                "title": "Crossing Rivers",
                "subtitle": "Studying currents, wading safely, and swimming.",
                "imageName": "travel.jpg",
                "textSections": [
                    "### STUDY THE WATER\n\nThe surface movement of a stream or river can tell you a great deal about what is beneath:\n*   **Chevron shape (V-shape)**: The main flow of the current around any rock or projection. The V widens downstream.\n*   **Standing waves**: Waves that appear to stay in one position on the surface are usually evidence of a boulder on the bottom deflecting water upwards.\n*   **Eddies and Backward Pulls**: Deflections near the surface create an eddy downstream where surface water runs back against the main flow. If a large boulder coincides with a steep drop in the level of the bottom, these eddies can produce a powerful backward pull downstream of the obstruction and pull swimmers in - they are VERY dangerous.",
                    "### WADING ALONE\n\nNever underestimate any stretch of water. Cut a stick to aid balance and cross facing towards the current and you will be more able to avoid being swept off your feet. Roll trousers up, so that they offer less surface to the current, or if they are going to get wet anyway take them off. Keep your boots on, they will give a better grip than bare feet. Undo the belt fastening of a back-pack so that you can slip it off easily if you get swept over.\n\nTurn at a slight angle, your back towards the bank you want to reach; the current will move you in that direction. Do not take strides but shuffle sideways, using the stick to test for depth and trying each foothold before using it.",
                    "> [!WARNING]\n> **ICE-COLD WATER IS A KILLER**: Do not attempt swimming or wading across a stream when the water is at very low temperatures, it could prove fatal. Make a raft of some kind. Only wade if you can do it without getting more than your feet wet and dry them vigorously as soon as you reach the other bank.",
                    "### GROUP CROSSINGS\n\n*   **Line Formation**: Line up behind the strongest, who crosses facing the current. The others each hold the one in front at the waist and move in step, offering less obstruction to the current.\n*   **Side-by-Side Formation**: Link arms side-by-side and hold on to a pole or branch to keep them in alignment. They cross facing the bank and moving forwards. Only the side of the first person opposes the current.\n*   **Using Ropes**: If a rope is available, use a loop three times as long as the width of the stream. The person crossing is secured to the loop around the chest. The strongest crosses first while the other two pay out the rope. Once across, they untie and the next crosses, controlled by the others.",
                    "### SWIMMING AND FLOTATION AIDS\n\nIf you can't swim, DON'T try - rely on others to get you across with the help of some sort of float. Do not swim with your clothes on. Once wet they will give you no protection from cold. Always make sure you have found a place on the other side where you will be able to get out of the water.\n\n*   **Waterproof Bag Float**: Put your clothes and belongings inside a waterproof bag, leaving plenty of air space. Tie the neck, bend it over, and tie again. Hang on to it and kick.\n*   **Waterproof Sheet Bundle**: Pile twigs and straw into the centre of a sheet to create air pockets, pile your clothes and equipment on top, and tie up the bundle securely. Do not attempt to sit on the bundles.\n*   **Group Floats**: For a group, split into fours. Each four should lash their bags together and use them as support for an injured member or a non-swimmer."
                ]
            },
            {
                "title": "Survival Case Study",
                "subtitle": "The Trinity Mountains Plane Crash",
                "imageName": "travel.jpg",
                "textSections": [
                    "This is a case study from a documented account in the 1950s: a family of three - a father, mother, and child - set off by small plane from the east coast of the United States to get to California.",
                    "After various stops for fuel and rest the family arrived safely at their destination, although the father, who was the pilot, reported a minor fault when the plane landed for the final time. When the family were ready to head back east he went up for a test flight to make sure that the repairs he had requested were successful. However, what they failed to do was to register a flight plan, and this proved to be a fatal error.",
                    "> [!IMPORTANT]\n> You should always tell someone where you are going and how long you expect to be, otherwise no one will realise you are missing and think to look for you.",
                    "Nonetheless, when the plane crashed in the Trinity Mountains in northern California, nobody knew they were missing. Despite their initial error in failing to alert the authorities about their route, this family was trained in survival techniques and, having survived the impact, remained alive for the next ten days near the wreckage.",
                    "They then made the decision to leave the wreckage in search of civilization. And this is where they finally fell down; they didn't know how to effectively navigate and they left the security of the wreckage. Survival skills are very important but you also need to know the best possible way to get to safety.",
                    "The family were eventually discovered only a number of days after they had died, only 50 km (30 miles) from the nearest road. In this case the family had left a diary that was found by rescuers, revealing their whereabouts.",
                    "> [!NOTE]\n> The lessons to be learnt from this case study are that you should always let people know where you are, stay where you are for as long as possible, but if you really feel that you must leave the area, try to leave behind a message with your future movements."
                ]
            }
        ]
    },
    {
        "title": "Health",
        "description": "Wilderness first aid, CPR procedures, and treatment of animal and insect bites.",
        "articles": [
            {
                "title": "First Aid Priorities",
                "subtitle": "Camp hygiene, safety assessments, and triage sequence.",
                "imageName": "health.jpg",
                "textSections": [
                    "Maintaining health is of primary importance to the survivor. Do not take any unnecessary risks which could lead to injury. Aim at a varied and balanced diet and make sure that you get adequate rest. Away from people, you are not exposed to contagious infections. Although some diseases are insect- or waterborne, sensible precautions - especially boiling water and properly cooking food - will protect you from many infections.",
                    "### triage sequence\n\nIn an accident involving many injured people you must know which patients to treat first. When a patient has multiple injuries, breathing, heartbeat and bleeding should be given priority. Assess the injuries and handle in the following sequence:\n\n1. Restore and maintain breathing/heartbeat\n2. Stop bleeding\n3. Protect wounds and burns\n4. Immobilize fractures\n5. Treat shock",
                    "> [!IMPORTANT]\n> Before approaching any accident victim, check for danger to yourself and protect yourself from it. Look out for electric cables, gas pipes, falling debris, dangerous structures or wreckage. Give initial check-up without moving the patient, if possible, but - if there is continuing danger - move the patient and yourself to a safer location.",
                    "First reduce any further danger to the casualty or yourself by moving them to safety - away from a burning vehicle or building. In the case of a road accident, stop the traffic. With electrocution, switch off the current. If you can't, stand on dry non-conductive material and push or lever the patient from the power source with a dry non-conductive pole or stick BEFORE touching them. If gas or poisonous fumes are threatening, turn them off at source and take casualties to fresh air.",
                    "### unconscious casualties\n\nIf the patient is breathing, and does not appear to have any spinal injury, check that there are no obstructions in the mouth, deal with any serious bleeding and place him or her in the recovery position. Lying on the back, turn the casualty on one side. This produces a stable position so that any liquids or vomit will not enter or block the lungs, and the tongue will not fall back to block the airway.",
                    "### RECOVERY POSITION\n\nMove the arm and leg on one side of the body outwards to stop the patient lying flat; elbow and knee should both be bent. Turn the head in the same direction. Lay the other arm down along the other side of the patient. Allow the other leg to bend slightly. Pull the jaw forward to check that the tongue is at the front of the mouth and not blocking the airway. Loosen tight clothing.",
                    "> [!WARNING]\n> Do NOT place a casualty with a suspected spinal injury in the recovery position. Use an artificial airway to maintain their respiration and as a means of administering mouth-to-mouth resuscitation."
                ]
            },
            {
                "title": "Airway Obstruction",
                "subtitle": "Choking clearing procedures and special cases.",
                "imageName": "health.jpg",
                "textSections": [
                    "Normal breathing is quiet and easy. Noisy breathing, froth around the nose or lips and blueness around the lips and ears are all signs of difficult or obstructed breathing. Check breathing regularly by listening carefully near the nose and mouth. Clear the airway of any foreign matter: weed, vomit, false teeth or food. Sweep the mouth with a finger and ensure the tongue has not fallen back.",
                    "If someone appears to be choking, but can breathe and cough, their own coughing is more effective than your aid. A blow on the back may sometimes help. If the victim cannot speak, use the Heimlich manoeuvre with adults.",
                    "### HEIMLICH MANOEUVRE\n\n1. Stand or kneel behind casualty, arms around them.\n2. Clench one hand over the other, thumb side of fist pressing between waist and bottom of ribs.\n3. Apply pressure and jerk quickly upwards four times.\n\n**If this does not work**:\nGive four sharp blows to the back between the shoulder blades to loosen object and four more 'hugs'. Stop when victim starts breathing or coughs loudly. REPEAT if this does not succeed at first. DO NOT GIVE UP!\n\n*   *Unconscious patient*: Lay on back, kneel astride, place your hands, one on top of the other, with the heels resting above the navel, and make quick thrusts up to the centre of the ribcage. If the blockage does not shift, roll patient on side and strike four times between the shoulder blades. Repeat as necessary.",
                    "### SURVIVAL SELF-HELP\n\nIf alone, use the Heimlich manoeuvre by pulling or pushing against a blunt projection - an earth bank, a fallen tree, or a chair back in a domestic situation.",
                    "### SPECIAL CASES\n\n*   **Babies**: Support the baby, face down, straddling your forearm, with the head definitely lower than the chest. Use the heel of the free hand to give four quick blows between the shoulder blades. Place free hand on back of baby's head and turn over. Use two fingertips to press four times, quickly and fairly firmly, on centre chest. Repeat. Be ready to give mouth-to-mouth (and nose).\n*   **Children**: Small children: hold them upside down and strike four rapid blows between the shoulder blades using the heel of the hand. Older children: place across the knee, or bend forward from a sitting position, supporting chest with one hand while administering blows. Alternatively, perform Heimlich using two fingers of each hand instead of fists.\n*   **Pregnancy and Obesity**: Abdominal Heimlich is impossible. Position fists instead against the middle of the breastbone and follow similar thrust procedure."
                ]
            },
            {
                "title": "Emergency Cricothyroid Incision",
                "subtitle": "Drastic action for absolute airway blockages.",
                "imageName": "health.jpg",
                "textSections": [
                    "On the rare occasion when repeated attempts with the Heimlich manoeuvre fail to dislodge an obstruction, drastic action is required: a cut into the patient's throat below the obstruction. Also used in cases where an injury to the jaw prevents the patient from breathing, this is a technique only for a life-or-death situation. It is risky for the untrained, but worth trying to save a life in cases where the casualty will certainly die without it.",
                    "### Cricothyroid Technique\n\nThis technique is superior to a tracheotomy (where the cut is made below the Adam's apple) because there is no significant bleeding.",
                    "### PREPARATION\n\nYou need a sharp blade, a scalpel or a penknife (not a wide knife), and a hollow tube (a ballpoint pen case, a clean fuel or hydraulic line from a vehicle, tubing from a back-pack, a small syringe, or even a hollow plant stem). They should be sterilized if boiling water or a flame is available, but do not waste time getting them.",
                    "> [!WARNING]\n> Contamination with oil or petrol from a dirty vehicle hose could produce chemopneumonia. Ensure the tube is as clean as possible.",
                    "### STEP-BY-STEP PROCEDURE\n\n1. Lay casualty on back, shoulders elevated, head and neck presenting a straight line.\n2. Run a finger down the Adam's apple - the bone-like projection on the front of the neck - and find another small projection just below it. Between the Adam's apple and this smaller projection you will find a central valley (cricothyroid membrane).\n3. Make an incision here at the exact midpoint. Keep the incision small but deep - straight down for about 1-2cm (1/2 to 3/4 in). Note the distance on the blade beforehand. You will feel the blade move more easily as it cuts through to the windpipe. Do NOT push down further.\n4. Twist the blade sideways to open up the cut.\n5. Insert the tube in the incision and push it down to keep the cut open and allow air into the lungs. Once in place, secure firmly with adhesive tape or bandage to keep it upright and prevent it falling out."
                ]
            },
            {
                "title": "Preventing Asphyxiation",
                "subtitle": "Dealing with chest compression, smoke, and carbon monoxide.",
                "imageName": "health.jpg",
                "textSections": [
                    "### CHEST COMPRESSION\n\nAny compression of the chest can cause asphyxiation. A climber who slips and is held suspended by a rope around his chest will find it extremely difficult to breathe. Pass down a rope with a loop (bowline or manharness hitch) to stand in and relieve the pressure.",
                    "An avalanche of snow, or a fall of earth can exert pressure on the chest and make breathing difficult. Adopt a crouched position if possible, with bent arms and elbows tucked well in, and this will protect the chest. If a person is trapped under wreckage with pressure on the chest, and the weight cannot be lifted off, use a lever to lift it and prop securely.",
                    "### SMOKE AND GAS\n\nTo prevent smoke entering the lungs, place fine mesh material over the nose and mouth to filter it. Smoke can be seen and there is a chance of avoiding it. Gases cannot usually be seen and safety is gained only in fresh air upwind of them, or with a respirator. Casualties must have fresh air.",
                    "### CARBON MONOXIDE POISONING\n\nOxygen can be used up in a shelter which lacks ventilation or becomes blocked and sealed by rubble or snow. This is a danger in igloos especially if draughts are sealed. With a stove or fire, not only is the oxygen used, even more seriously, carbon monoxide is produced.",
                    "This gas is DEADLY in confined spaces, but the occupants rarely recognize its presence. The symptoms of carbon monoxide poisoning resemble those of an overdose of alcohol: memory and judgment are impaired, with an increase in confidence and a disregard of danger.",
                    "> [!IMPORTANT]\n> Always ensure that you have adequate ventilation, especially when using stoves. Adjust any burning with a yellow flame. Light a candle in your shelter. If the flame gets longer and higher - or in extreme cases shoots to the roof - there is a severe lack of oxygen and it is high time to ventilate. Casualties must have fresh air."
                ]
            },
            {
                "title": "Drowning and Electrocution",
                "subtitle": "Managing immersion, shock, and lightning casualties.",
                "imageName": "health.jpg",
                "textSections": [
                    "### DROWNING\n\nDrowning can occur through fluid blockages but generally the patient will be in water or have their face in liquid. Face, especially lips and ears, will be livid and congested, possibly with fine froth at the mouth and nostrils - it is the froth that is blocking the air passage.\n\nDo not attempt to remove liquid from the lungs - you can't. Begin artificial respiration as early as possible. If still in water, support the floating body and begin mouth-to-mouth resuscitation after quickly removing weed, false teeth or any other mouth obstructions. On land, the Holger Nielsen method can also be used.",
                    "### ELECTROCUTION\n\nThe cause will usually be obvious. Electrocution may stop the heart and muscle spasms may throw the victim some distance. Electrical burns will be much deeper than their appearance suggests.\n\nNever touch the victim until the current is off or contact is broken. If an appliance is involved, it may be possible to break contact by pulling on insulated cable. Beware of any liquids which will conduct current - victims may urinate. Give artificial respiration and treat for cardiac arrest if necessary before treating burns. TAKE NO RISKS.",
                    "### LIGHTNING\n\nLightning is another form of electrocution. The victim is usually stunned and falls unconscious. Clothing may catch fire, and the patient may have electrical burns, which will be more severe where watches, jewellery, buckles or other metal objects are worn. Give artificial respiration if necessary and treat burns. Prolonged resuscitation may be needed. Recovery is often delayed."
                ]
            },
            {
                "title": "Artificial Respiration",
                "subtitle": "Kiss of life, Silvester, and Holger Nielsen methods.",
                "imageName": "health.jpg",
                "textSections": [
                    "### MOUTH-TO-MOUTH ('KISS OF LIFE')\n\nThe fastest and most effective method. Begin as soon as the airway has been cleared. Normal recovery is rapid, except in cases of electric shock, drugs and carbon monoxide poisoning. In these cases nerves and muscles are paralyzed, or carbon monoxide has displaced oxygen in the bloodstream. Be prepared to carry on a long time.\n\n1. With patient lying on back, hold jaw well open, bending head back (prevents tongue falling and blocking airway).\n2. Hold nostrils closed with other hand.\n3. Check mouth and throat clear of obstruction.\n4. Place mouth over patient's mouth and exhale.\n5. Watch for chest to rise as you blow gently. (If chest does not rise, turn him on his side and thump between shoulder blades to remove obstruction.)\n6. Remove mouth, take a deep breath while checking chest falls automatically. You should feel or hear air returning.\n7. REPEAT, as quickly as possible for the first six inflations, then at 12 per minute until breathing is established.\n\n*   **For a child**: Do not blow. Exhale normally, or in gentle puffs for a baby. Give first four inflations as quickly as possible. Blowing forcefully may damage delicate lungs.\n*   **Mouth-to-nose**: Use if you cannot seal your lips around victim's mouth, holding his mouth closed. For babies, cover both nose and mouth.",
                    "> [!IMPORTANT]\n> KEEP GOING! With any form of resuscitation the first five minutes are probably the most critical but, if breathing does not start, keep artificial respiration up for at least an hour. In a group take turns.",
                    "### SILVESTER METHOD\n\nRecommended when poisoning or facial injury prevent mouth-to-mouth resuscitation, especially when the patient may need cardiac compression (which can be done by the same first-aider).\n\n1. With casualty lying on back, raise shoulders with a pad of folded blanket or clothing. Kneel astride casualty's head.\n2. Place hands flat over lower ribs and rock forward to press steadily downwards.\n3. Lift casualty's arms upwards and outwards as far as possible.\n4. REPEAT rhythmically about 12 times per minute for adults. If no improvement, turn patient on side and strike between shoulders to remove obstruction.",
                    "### HOLGER NIELSEN METHOD (FACE DOWN)\n\nThis is the technique recommended for resuscitating a drowning victim if mouth-to-mouth is not practicable, or if the patient cannot be turned on their back. Casualty lies face down; liquids can flow freely from the mouth and will not cause choking.\n\n1. Place head turned to one side, arms bent, forehead resting on hands. Bring tongue forward, clear mouth.\n2. Kneel on one knee at head, placing hands over shoulder blades, thumbs touching and fingers spread.\n3. Perform the following procedure to a count of eight:\n    *   *Count 1-2-3*: Rock forward with arms straight, producing gentle, even, increasing pressure (about 2 seconds).\n    *   *Count 4*: Rock back, sliding hands to grasp patient's upper arms (1/2-1 second).\n    *   *Count 5-6-7*: Pull and raise patient's arms gently by rocking further backwards (2 seconds). Avoid raising trunk or disturbing head.\n    *   *Count 8*: Lower patient's arms to ground and slide hands back to initial position (1/2-1 second).\n4. REPEAT 12 times per minute."
                ]
            },
            {
                "title": "Cardiac Compression",
                "subtitle": "Taking pulse, CPR techniques, and airway equipment.",
                "imageName": "health.jpg",
                "textSections": [
                    "### TAKING PULSE\n\n*   **Wrist (Radial)**: Rest fingers lightly at the front of the wrist, over the radial artery, about 1cm (1/2 in) from thumb side at lower end of forearm.\n*   **Neck (Carotid)**: Turn face to one side. Slide fingers from Adam's apple into groove alongside.\n*   **Rates**: In a relaxed adult 60-80 per minute (average 72); in young children 90-140 per minute. Count the beats in 30 seconds and multiply by two.",
                    "### CARDIAC COMPRESSION\n\nIf you cannot feel a pulse and the pupils of the eyes are much larger than normal, start cardiac compression while artificial respiration is continued. First place the casualty on a firm surface, chest up. Using the edge of the hand, strike firmly on the lower part of the breastbone. The jarring may start the heart. If still no pulse, proceed with compression.\n\n1. Kneel beside the casualty. Place heel of one hand on lower half of breastbone (sternum), making sure it is not on the end of, or below, the breastbone.\n2. Place heel of other hand over it. Keep rest of hand OFF chest.\n3. Keeping arms straight, rock forward and press down smoothly.\n4. In adults, press down about 4cm (1 1/2 in) at a rate of 60 times per minute. Press smoothly and firmly; erratic or rough pressing could cause injury.\n\n*   **Infants and Children**: For babies and small children, light pressure with two fingers is enough at a rate of 100 times per minute. For older children up to ten years, use the heel of one hand only and push 80-90 times per minute.",
                    "### CPR COORDINATION\n\n*   **If alone**: Give 15 heart compressions followed by two rapid lung-inflations.\n*   **If two first-aiders**: Give five heart-compressions followed by one deep lung-inflation. Repeat.",
                    "### ARTIFICIAL AIRWAY & EXTRACTOR\n\n*   **Artificial Airway**: Insert the artificial airway to a third of its length, end pointing to the roof of the mouth, then turn it through 180 degrees to point down the throat.\n*   **Mucus Extractor**: Placed down artificial airway; its one-way valve allows mucus to be sucked out without risk of swallowing. Without one, you can use any tube or straw, trying NOT to swallow the mucus yourself."
                ]
            },
            {
                "title": "Bleeding Control",
                "subtitle": "Staunching blood flow, pressure points, and tourniquets.",
                "imageName": "health.jpg",
                "textSections": [
                    "An average person has up to 6.25 litres (11pt) of circulating blood. The loss of 0.5 litre (1pt) causes mild faintness, 1 litre (1 3/4 pt) faintness with an increase in pulse and breathing, 1.5 litres (2 1/2 pt) collapse. Loss of more than 2.24 litres (4pt) may cause death. Fluids must be replaced by giving water.",
                    "Bleeding from veins and capillaries can be stemmed by simple pressure over the bleeding point. Wounds on limbs should be elevated above the heart. Maintain continuous, firm pressure for 5-10 minutes. If blood seeps through, place another pad on top. Secure with a bandage.",
                    "### ARTERIAL BLEEDING & PRESSURE POINTS\n\nBleeding from an artery comes in powerful, rapid spurts, in time with the pulse. It can be temporarily controlled by compressing an artery where it crosses a bone at these pressure points:\n*   **Temple/Scalp**: Forward of/above ear\n*   **Face below eyes**: Side of jaw\n*   **Shoulder/Upper arm**: Above clavicle\n*   **Elbow**: Underside of upper arm\n*   **Lower arm**: Crook of elbow\n*   **Hand**: Front of wrist\n*   **Thigh**: Mid-way in groin/top of thigh\n*   **Lower leg**: Upper sides of knee\n*   **Foot**: Front of ankle",
                    "### TYING ARTERIES\n\nIn the case of major wounds to which a pressure dressing cannot be applied, or a limb partially severed, you must trace the bleeding artery and tie it off. Apply a temporary tourniquet first. Sterilize fishing line, thread or fine string by boiling or soaking in alcohol. Clean the wound with sterile (boiled) water and gently explore it with a clean finger to locate the severed artery. Tie it securely. Cautiously relax the tourniquet as soon as possible to check if bleeding has stopped. Do NOT leave the tourniquet in position.",
                    "### TOURNIQUETS\n\nThere are only two places where a tourniquet may be placed: on the upper arm, just below the armpit, and around the upper thigh.\n\n1. Use a piece of cloth at least 5cm (2in) wide. If using wire or cord, apply over a fold of clothing.\n2. Wrap around limb three times and tie a half knot.\n3. Place a stick over the knot and tie a double knot over it.\n4. Twist the stick, tightening the band until bleeding stops. Securing the stick.\n\n> [!WARNING]\n> A tourniquet cuts off the blood flow and if left on too long can cause gangrene and loss of a limb. Release it slowly to check bleeding. NEVER cover a tourniquet. Write 'TK' and the time applied on the victim's forehead.",
                    "### OTHER BLEEDING\n\n*   **Venous Bleeding**: Darker venous blood flows more slowly. Use a large pad and apply pressure over a wide area. Secure after 10 minutes.\n*   **Internal Bleeding**: Pale, cold, clammy skin, restless/faint, pulse weak but fast. Coughed-up blood indicates lung bleeding; brown coffee grounds vomit indicates stomach. Lie patient flat with legs elevated. Keep moderately warm.\n*   **Nosebleed**: Sit patient up with head slightly forward. Pinch the soft part of the nostrils for five minutes. Breathe through mouth; do not sniff."
                ]
            },
            {
                "title": "Wounds and Suturing",
                "subtitle": "Cleaning, stitches, specific wounds, and amputations.",
                "imageName": "health.jpg",
                "textSections": [
                    "Open wounds carry the risk of infection by bacteria, most importantly Tetanus. Wounds caused by glass, metal or burns must have foreign bodies extracted. Clean the wound vicinity and irrigate to wash out dirt. Clean from the centre outwards. Change dressings if they become wet, omit an offensive smell, or if pain increases.",
                    "Local infection can be treated by soaking in hot salty water or applying poultices made of mashed rice, potatoes, roots, tree bark, or clay. Apply as hot as tolerated.",
                    "> [!TIP]\n> Soap is an excellent antiseptic. If none is available, use urine to wash wounds. Urine is a sterile fluid that will not introduce infection, and its uric acid has a slight beneficial cleaning effect.",
                    "### SUTURING WOUNDS\n\nMinor wounds can be closed by suturing if no medics are available. Use a sterilized needle and thread or gut. Make each stitch individually, beginning at the mid-point of the wound. Draw edges together and tie off. Alternatively, use butterfly sutures or cut adhesive plasters in a butterfly shape.\n\n*   *Open Treatment*: If unable to clean a wound thoroughly, it must be left open to heal from the inside. If it becomes infected, remove stitches to let pus out. Deep wounds may require packing with a sterilized bandage, leaving a tail hanging out to drain.",
                    "### SPECIFIC WOUNDS\n\n*   **Sucking Chest Wound**: The chest sucks air through the wound into the space around the lung. Seal with a waterproof wrapper (or plastic film) taped on the top and sides, leaving the bottom edge free to allow air to escape as the casualty exhales.\n*   **Abdominal Wounds**: Do NOT give solids or liquids. If the gut is extruded, cover it and keep it damp. Do not attempt to push it back into place. Dress and bandage firmly.\n*   **Head Injuries**: Ensure airway is maintained. Control bleeding. The conscious casualty can sit up, but the unconscious patient must be placed in the recovery position (if no neck/spine injury).",
                    "### EMERGENCY AMPUTATION\n\nIf a limb is trapped in a burning wreck, or gangrene sets in and survival depends on it, amputation may be necessary. Apply a tourniquet and be ready to tie off arteries. Cut as close to the wound site as possible (through bone or at the nearest joint). Make an incision, allow skin and muscles to retract, then saw through the bone. Leave the stump open to allow for drainage, applying a light bandage."
                ]
            },
            {
                "title": "Burns and Fractures",
                "subtitle": "Cooling burns, fluid replacement, traction, and splints.",
                "imageName": "health.jpg",
                "textSections": [
                    "### BURNS ASSESSMENT\n\nBurns cause severe pain, fluid loss, and make victims highly susceptible to shock and infection. Assess body area affected: Head = 9%, Arms = 9% each, Front torso = 18%, Back torso = 18%, Genitals = 1%, Legs = 9% front/back each. Burns over 50% are usually fatal without medical facilities.",
                    "### EXTINGUISH & COOL\n\n1. Get the victim on the ground and roll over, covering with a blanket or poncho. Do not let them run.\n2. Remove smouldering clothing and jewellery immediately.\n3. Drench burned tissues with water to cool. Submerge under slowly running cold water for at least 10 minutes.\n\n> [!WARNING]\n> Do NOT use antiseptic, butter, grease, lard, calamine lotion, Vaseline or anything similar on burns. Cooling should continue until pain does not increase when withdrawn from water. Leave blisters alone.",
                    "### BURN FLUIDS\n\nGive small cold drinks frequently. Add a half teaspoonful of salt (and a pinch of bicarbonate of soda) to a pint of water. If you have no salt, give small amounts of boiled animal blood.",
                    "### FRACTURES AND SPLINTING\n\nThere are open fractures (bone pushes through skin) and closed fractures. Examine early before swelling. If a limb is distorted, straighten it before splinting by applying traction (a slow, strong, steady pull). Compare alignment with the other limb.",
                    "Immobilize the whole length of the limb. Use slings to support bent-arm fractures. If no splint is available, strap the injured limb to the uninjured limb or body. Insert padding (moss is ideal) in any natural hollows to keep limbs in position. Secure firmly above and below the fracture. Check circulation periodically.",
                    "### LOWER LEG BINDINGS\n\nFor any fracture of the thigh or lower leg, a figure-of-eight bandage should be applied, binding the feet and ankles of both legs together. This controls rotation and counters shortening. Splint from ankle to armpit for hip/upper leg fractures."
                ]
            }
        ]
    },
    {
        "title": "Disaster Survival",
        "description": "Urban survival strategies, natural disasters (earthquakes and floods), and fire safety.",
        "articles": [
            {
                "title": "Drought and Water Storage",
                "subtitle": "Water preservation, cistern pits, and sanitation hygiene.",
                "imageName": "disaster.jpg",
                "textSections": [
                    "Drought, caused by long periods of dry weather or insufficient rainfall, creates desert in areas where it is a permanent condition. Elsewhere, drought may be a regular seasonal feature for part of the year. In temperate regions, if rainfall drops far below the normal, periodic drought may be produced with vegetation unable to obtain water. In cases where the dry spell may not be so obvious, a condition known as 'invisible drought' occurs, causing deprivation right through the food chains.",
                    "### FIRE RISK & HYGIENE\n\n*   **Carcass Burial**: The corpses of dead animals must be buried in deep graves or burned to remove sources of infection. Because drought leaves everything tinder dry, the risk of fire spreading is considerable. If you must have a fire, dig down to bare earth, keep the fire small and attended at all times.\n*   **Sewer Seals**: In houses, lack of water for sanitation can bring the risk of infection. If the water level in a water closet no longer seals the S-bend, disease may spread from the sewers. Do not use the WC but leave sufficient water in the bowl to form a barrier. Make an outdoor latrine instead. Clean hands after defecation and before preparing food, even when water is short.",
                    "### WATER STORAGE PITS\n\nStore as much water as possible and use it wisely. Keep it covered and shaded to avoid evaporation. Dig a pit for a storage cistern in a shady spot, avoiding tree roots. Line it with a polythene sheet or with cement (allow the cement to thoroughly dry before filling). In a clay area, dig a pit and line it with clay. Building the concrete or clay up into a partial dome helps keep the contents cool and leaves a smaller opening to cover.",
                    "> [!IMPORTANT]\n> NEVER waste water. Water used for cooking can later be used for washing. Boil all drinking water. High ground shows greater variation between day and night temperatures, offering a better chance of dew collection in the early morning.",
                    "> [!WARNING]\n> *   Be especially careful of contamination of water supplies. Disease from dead animals may be rampant. Boil all water.\n*   Flies may be a serious problem - ensure all foodstuffs are covered. Protect from dust as topsoil is blown away.\n*   When nature is disturbed, normally docile animals can act abnormally. Crazed by thirst, they may attack."
                ]
            },
            {
                "title": "Forest and Wildfires",
                "subtitle": "Wind tracking, escapes, and vehicle/earth shelters.",
                "imageName": "disaster.jpg",
                "textSections": [
                    "Fire requires heat, fuel and oxygen. The first sign of an approaching forest fire will be the smell of smoke, followed by the sound of the fire. You may notice unusual animal behaviour before realizing the cause. If caught in an area where fire is raging, do NOT immediately flee unless the fire is very close.",
                    "### ESCAPE ROUTE\n\n*   Do NOT discard clothing; it shields you from the radiated heat.\n*   Smoke indicates the wind direction; the fire travels fastest in that direction. If the wind is blowing away from you toward the fire, move INTO the wind.\n*   Head for natural fire breaks like rivers or roadways. A river is the best break; you are reasonably safe in the water.\n*   Fire travels faster uphill, so do NOT make for high ground.\n*   If you can neither skirt nor outdistance the blaze, take refuge in a large clearing, deep ravine, watercourse, or gully.",
                    "### RUNNING THROUGH FLAMES\n\nIf the fire front is not too deep, run through the flames to already burned-out land. Cover exposed skin. If water is available, pour it over clothing, hair, and flesh. Dampen a piece of cloth to cover your nose and mouth. Thick vegetation burns fiercely, so choose your breakthrough spot with care. Take a deep breath and RUN.",
                    "### FIRE SMOTHERING\n\nIf fire-beating equipment is available (twigs or spade-shaped rubber beaters), do NOT beat rapidly; that fans the flames and spreads sparks. Smother the fire by bringing the beater down over the flames to extinguish them. If no equipment is available, use a coat, blanket, or leafy branch.",
                    "### VEHICLE SHELTER\n\nIf caught in a forest fire in a vehicle, stay inside, windows shut, and turn off ventilation. The car provides protection from radiant heat. Drive away if possible; if immobilized, stay put. People have survived by staying in a vehicle until the glass began to melt, whereas running outside would have killed them.",
                    "### GOING TO EARTH\n\nIf there is no break and the fire is too deep to run through, seek the protection of the earth. Scrape a hollow, throw earth onto a coat or cloth, and pull it over you with its earth covering. Cup your hands over your mouth and nose to cool and filter hot air and sparks. Try to hold your breath as the fire passes. *Warning*: Risk of suffocation is high.",
                    "### FIGHTING FIRE WITH FIRE\n\nIf the main fire is still some distance away, burn a patch of ground before it reaches you. With nothing left to ignite, the main fire cannot advance, creating a place of refuge. Light your own fire along a line at least 10m (preferably 100m) wide. It will burn in the same direction, creating a break you can move into. *Warning*: Winds may swirl; do not attempt this unless desperate."
                ]
            },
            {
                "title": "Burning Buildings and Evacuation",
                "subtitle": "Containing fires, lift hazards, and dropping from heights.",
                "imageName": "disaster.jpg",
                "textSections": [
                    "Smoke is usually the first indication of a building fire. Smother small fires with a blanket or curtain to deprive them of oxygen, or use sand, water, or extinguishers.",
                    "### ELECTRICAL FIRES\n\nIf the fire is caused by an electrical fault, turn off power at the mains before using water. Turn off gas too.\n\n> [!WARNING]\n> If television sets or computer monitors (VDUs) catch fire, do NOT use water on them. Residual electrical charges can deliver a fatal shock, and cold water can cause the tube to explode. Smother them and approach from behind.",
                    "### EVACUATION RULES\n\nIf the fire is too big to fight, evacuate. Close all doors and windows to contain the fire. Fire travels upwards faster than downwards. Staircases, lift-wells, and ventilation shafts are dangerous. NEVER use a lift during a fire; use a smoke-free staircase.",
                    "Before opening any door, feel the doorknob with the back of your hand. If warm, do NOT open. Open doors only a crack while bracing your foot against them to prevent the pressure of hot gases from forcing them wide open. Crouch low to avoid smoke, and close doors behind you.",
                    "### WAITING FOR RESCUE\n\nIf isolated, go to a room as far from the fire as possible (not on a higher level). Choose a room with soft ground outside (lawns, flowerbeds) rather than concrete. Close the door and pack any gaps with mats, curtains, or wet cloths. Attract attention through the window.",
                    "To break windows, use furniture. If using a hand, wrap it first; an elbow protected by a thick jacket is also effective. Do not bring your limb back quickly through broken glass.",
                    "### PREPARING TO DROP\n\nIf no rescue is coming, drop from the window. Tie sheets, blankets, or mats together using reef knots and test them. Secure one end to heavy furniture, heating pipes, or the window frame. Drop cushions, pillows, or mattresses below to soften your landing. Lower yourself out and hang from the sill to reduce the fall distance. Do NOT jump unless caught in a blanket.",
                    "### THE FALL TECHNIQUE\n\nProtect your head with a motorcycle helmet, or a jersey/towel wrapped like a turban. Push yourself away from the building with the side of one foot. As you let go, turn away from the wall, bend your knees, and leave your arms up to protect the sides of your head. Land on the balls of your feet, bend your knees fully, and roll over onto one side or somersault forward to distribute the impact."
                ]
            },
            {
                "title": "Vehicle Fires",
                "subtitle": "Car engine fires, passenger cabin fumes, and aircraft safety.",
                "imageName": "disaster.jpg",
                "textSections": [
                    "The greatest danger with cars is the fuel tank igniting and exploding. The aim is to control the fire before it reaches the tank. Fuel lines (if not armoured) usually catch fire first, acting as a fuse to the tank.",
                    "### IN A GARAGE\n\nIf a car catches fire in a garage, smoke and toxic fumes build up quickly. If you cannot put it out, remove the car from the building. Do NOT get inside. Push or pull it. If the car has a button starter, select low gear or reverse and use the starter motor to bounce the car out. With conventional ignition, turn the key in short bursts. The car will jerk forward violently.",
                    "> [!IMPORTANT]\n> Keep your fire extinguisher in the passenger compartment where you can reach it immediately, NOT in the boot/trunk. An impact could distort the boot lid and trap the extinguisher.",
                    "### EXITING & FUMES\n\nIf doors jam in a crash, kick the windscreen out. If the fire is inside, use the extinguisher or smother it with a rug. Synthetic upholstery materials burn rapidly and release toxic gases; exit immediately once flames are out. If fire is on the outside (spilt fuel), keep windows shut, drive out of the danger zone, and abandon the car.",
                    "### AIRCRAFT FIRES\n\nAeroplanes have automatic engine extinguishers and hand-held cabin units. Summon cabin crew immediately if you suspect fire. Smother small cabin fires with blankets or clothing. The main dangers occur during takeoff/landing when fuel tanks may rupture."
                ]
            },
            {
                "title": "Chemical and Biological Warfare",
                "subtitle": "Toxins, pathogens, skin penetration, and decontamination.",
                "imageName": "disaster.jpg",
                "textSections": [
                    "Biological agents fall into two groups: pathogens (living germs like anthrax) and toxins (poisons). Germs must be inhaled, enter through broken skin, or be digested. They have incubation periods of hours to months. Toxins are naturally occurring or manufactured poisons. Unlike germs, toxins can penetrate unbroken skin, and their symptoms (paralysis, convulsions, blisters, shock) appear immediately.",
                    "### PROTECTION & TUCKING\n\nIf you suspect biological agents:\n1. Wrap a damp cloth around your mouth and nose to filter inhalation.\n2. Cover all exposed skin, buttoning/zipping up clothing.\n3. Tuck trousers into socks and wear gloves.\n4. Leave the area immediately.",
                    "### DECONTAMINATION\n\nOnce out of the danger zone, wash thoroughly with soap and hot water. Clean your teeth, hair, and fingernails. Wash all clothing and equipment in hot, soapy water.",
                    "### ANTHRAX WARNING\n\nAnthrax is carried by animals and transmitted from dead carcasses. Signs on a carcass include bloating, incomplete rigor mortis, and dark blood oozing from the nostrils and anus. Avoid contact, wash thoroughly if exposed, and seek antibiotics. Early human signs are pustules with dark centres.",
                    "### CHEMICAL AGENTS\n\nChemical agents exist as liquids, gases, or aerosols. They affect breathing, nerves, or blood. Look for coughing, itching, tears, and a wasted landscape with limp vegetation. Learn these indicator smells:\n*   **Almonds**: Indicates a blood agent.\n*   **Newly Cut Grass**: Indicates a choking agent.\n\nCover the body with waterproof garments, goggles, and masks. Decontaminate immediately after escaping."
                ]
            },
            {
                "title": "Gases and Industrial Spills",
                "subtitle": "Confined spaces, Hazchem codes, and spillage zones.",
                "imageName": "disaster.jpg",
                "textSections": [
                    "Explosive gases build up in caves and mines. In domestic settings, oxygen deficiency and carbon monoxide occur in sealed shelters. Burning plastics and synthetic materials produce highly toxic fumes during house and vehicle fires.",
                    "### INDUSTRIAL DISASTERS\n\nIf a major chemical release occurs (such as Bhopal), stay indoors and keep all doors and windows closed. Look for warning labels where chemicals are stored (such as the yellow triangle or HAZCHEM sign).",
                    "Avoid contact with chemicals and inhalation of fumes. Flush skin spillages with copious amounts of water. *Warning*: Adding water to some chemicals can cause violent reactions. AVOID touching anyone contaminated with chemicals, and do NOT give mouth-to-mouth resuscitation until you know what chemicals are involved.",
                    "### ROAD & RAIL ACCIDENTS\n\nKeep well clear of accidents involving bulk tankers. Spillages may be visible, but gas escapes are often invisible. If not trained and equipped, do NOT attempt to fight chemical fires. Call the emergency services and keep back.",
                    "Hazardous chemical tankers carry panel warning codes (such as the British Hazchem code, EC ADR signs, or UN EAC codes) which instruct emergency teams on water use, respirators, and evacuation. A final letter **E** in the British code is an instruction to **EVACUATE** the area. If you see these signs, keep your distance."
                ]
            },
            {
                "title": "Floods and Tsunami Evacuation",
                "subtitle": "Flash floods, staying put, and tsunami shoreline warnings.",
                "imageName": "disaster.jpg",
                "textSections": [
                    "Flooding is caused by overflowing rivers, dam collapses, heavy storms, or sub-ocean earthquakes. Rainy spells after dry seasons can rapidly produce torrents in dry riverbeds, creating a rushing wall of water.",
                    "### FLASH FLOODS\n\nKeep clear of water channels and low-lying ground. Camp on a spur. Flash floods are common in valley bottoms; avoid them during storms. If trapped by water, collect rainwater to drink; floodwater is contaminated. Boil all non-rain water.",
                    "### FLOODED BUILDINGS\n\nIf in a solid building, stay there rather than evacuating on foot. Turn off gas and electricity. Gather emergency food, warm clothes, matches, candles, camp stoves, and seal drinking water in screw-topped plastic bottles to avoid contamination.",
                    "Move to an upper floor, or onto the roof if in a single-storey building. Tie everyone to a chimneyshaft or solid structure using sheets or ropes. Stay until the water stops rising, preparing a raft as a backup.",
                    "### ROAD ESCAPES\n\n*   Do NOT attempt to cross a pool or stream unless you are CERTAIN the water is below the centre of the car's wheels or below your knees.\n*   If crossing, use river-crossing wading techniques.\n*   Take extreme care on submerged bridges; the road beneath may have been swept away.",
                    "### FLOOD AFTERMATH\n\nReceding waters leave silt, debris, and animal carcasses. Burn all animal corpses to prevent disease; do NOT eat them. Boil all drinking water.",
                    "### TSUNAMI WARNING\n\nA tsunami is a series of ocean waves up to 30m (98ft) high caused by submarine earthquakes. Keep away from shores and take to high ground when you feel tremors. Do NOT go to look for a tsunami; if you are close enough to see the wave, you are too close to escape."
                ]
            },
            {
                "title": "Hurricanes and Tornadoes",
                "subtitle": "Cyclones, barometric drops, and pressure equalization.",
                "imageName": "disaster.jpg",
                "textSections": [
                    "A hurricane is a wind exceeding force 12 on the Beaufort Scale (above 120kph / 74mph). They are known as hurricanes in the Atlantic, cyclones in the Indian Ocean, typhoons in the Pacific, and willy-willies in Australia. They develop over warm summer oceans, creating a low-pressure core. Winds rotate anti-clockwise in the North, clockwise in the South. The centre (eye) is temporarily calm.",
                    "### HURRICANE WARNINGS\n\nWarnings are issued 24 hours in advance. Indicators of an approaching storm without radio include a rising swell, highly coloured sunsets, converging cirrus cloud banners, and a rapid barometric pressure drop.",
                    "### SHELTER RULES\n\n*   Keep away from the coast (tidal waves) and river banks.\n*   Board up windows and secure outdoor objects.\n*   At sea, take down all canvas, batten hatches, and stream the sea anchor.\n*   In a solid building, stay in the cellar or under the stairs. Store drinking water. Shut off power.\n*   Outdoors, shelter in a cave, ditch, or the lee side of a rocky outcrop. Lie flat. Avoid small trees.\n*   *The Eye*: Stay put when the wind drops. The eye brings a short calm, followed by winds from the opposite direction. Move to the other side of your windbreak.",
                    "### TORNADOES (TWISTERS)\n\nTornadoes are violent whirling winds descending from cumulonimbus clouds. Wind speeds reach 620kph (385mph). The funnel at ground level is 25-50m (80-160ft) wide, sucking up everything in its path. Tornadoes travel at 50-65kph (30-40mph) and sound like a spinning top, audible up to 40km away.",
                    "### TORNADO PRECAUTIONS\n\n*   Shelter in a storm cellar or concrete building. Stay close to outside walls, under sturdy furniture.\n*   **Open and Closed Doors**: Open windows on the side of the house opposite the tornado's approach, and close doors/windows on the facing side. This equalizes pressure and prevents the house from 'exploding'.\n*   Do NOT stay in a caravan or car.\n*   If caught outdoors, move at right angles to the tornado's path. Lie flat in a ditch and cover your head."
                ]
            },
            {
                "title": "Lightning and Earthquakes",
                "subtitle": "Electrostatic insulation, tectonic ruptures, and structural shelter.",
                "imageName": "disaster.jpg",
                "textSections": [
                    "### LIGHTNING DANGERS\n\nKeep away from hill brows, tall trees, metal fences, and lone boulders. Make for low, level ground.",
                    "### INSULATION TECHNIQUE\n\nIf you cannot get away from tall objects, sit on dry insulating material (a dry coil of climbing rope or rubber-soled shoes). Do NOT sit on anything wet. Bend your head down, hug your knees to your chest, and lift your feet off the ground. Do not touch the ground with your hands. If no insulation is available, lie flat.",
                    "If you feel a skin tingling or hair standing on end, drop to your knees immediately with hands touching the ground. This directs the charge through your arms to the earth, bypassing vital organs. Then quickly lie flat. Do not hold metal tools.",
                    "### CAVE SHELTER\n\nShelter at least 1m (3ft) inside a deep cave with 1m clearance on either side. Do NOT shelter in cave mouths or overhangs; lightning can spark across the gap. Avoid wet rock fissures.",
                    "### EARTHQUAKES\n\nEarthquakes are caused by tectonic ruptures releasing tension in the crust. Shock waves are preceded by foreshocks (tremors) and seismic quiet. Tectonic plates shift along faults (such as the San Andreas Fault). Animals act crazed or run before tremors start.",
                    "### DOMESTIC PRECAUTIONS\n\nRemove heavy objects from high shelves. Shelves should have lips or low barriers. Store water, food, torches, and extinguishers. Keep away from windows and brick chimneys.",
                    "### INDOORS & UNDER FURNITURE\n\nIf indoors, stay there. Douse fires. Stay away from glass and windows. Shelter in inside corners, supported doorways, or cellars. Get beneath a table or desk which provides an air space. In high-rise offices, stay put; never use a lift.",
                    "### OUTDOORS & IN CARS\n\nIf outdoors, move to an open area away from buildings, power cables, and trees. Masonry falling from buildings poses the greatest street risk. If in a car, stop safely away from bridges or overpasses, stay inside, and crouch below seat level."
                ]
            }
        ]
    },
    {
        "title": "Survival at Sea",
        "description": "Abandoning ship procedures, dinghy management, sea survival hydrology, ocean foraging, and shark defense.",
        "articles": [
            {
                "title": "Abandoning Ship",
                "subtitle": "Drills, clothing choices, and emergency entry.",
                "imageName": "sea.jpg",
                "textSections": [
                    "Conditions of survival at sea are perhaps worse than those of any other environment and make the sternest demands. Planes and boats carry survival equipment, but even getting into a dinghy in a heavy sea can be difficult. A survival situation at sea in warmer climates is preferable to cold-water survival, where hypothermia sets in rapidly. If you do find yourself going into cold water, take as much survival kit as you can, and get out of the water as soon as possible.",
                    "### LIFEBOAT DRILL\n\nLifeboat drill is carried out on every ship soon after it sails and should become a well-rehearsed procedure. Passengers are instructed in how to fit lifejackets, how to proceed to their lifeboat stations, and what to take with them. If the signal is given to abandon ship, put on warm, preferably woollen, clothing (including a hat and gloves) and wrap a towel around your neck. Clothes will not drag you under and they help ward off exposure.",
                    "> [!IMPORTANT]\n> Don't inflate your lifejacket until you leave the ship or plane. On small boats, lifejackets should be worn at all times. They are brightly coloured and usually equipped with a whistle, light, marker dye, and shark repellent for warmer waters.",
                    "Do NOT push or shout; an orderly embarkation into lifeboats and onto rafts or dinghies is faster and prevents panic. If you have to jump overboard, first throw something that floats and jump close to it.",
                    "Without a lifejacket or lifebelt, air trapped in clothing will help buoyancy - a good reason for keeping your clothes on despite advice to strip them off. The human body is of lower density than saltwater; relaxing in the water prevents drowning."
                ]
            },
            {
                "title": "Man Overboard and Swimming",
                "subtitle": "Attracting attention, navigating oil slicks, and breathing techniques.",
                "imageName": "sea.jpg",
                "textSections": [
                    "If you have been swept overboard, your first aim, apart from keeping afloat, will be to attract attention. Sound travels well over water - shouting and splashing can be effective. Wave with one arm above the water (not both, or you will go under) to make yourself noticed. Use your whistle and light if equipped.",
                    "### SWIMMING SAFEGUARDS\n\n*   Swim slowly and steadily. If abandoning a sinking boat or aircraft, get upwind and stay clear of it. Keep away from any oil or fuel slick.\n*   **Fire**: If you have to enter the water through flames, jump in feet-first and upwind. Swim into the wind using a breaststroke. Try to make breathing holes by splashing the flames away from your head. If the fire is small, swim underwater until clear.\n*   **Explosion**: If there is danger of an underwater explosion, swim on your back to reduce the risk of internal injury.",
                    "### RELAXED FLOTATION TECHNIQUE\n\nIf the sea is too rough to float on your back, or you need to conserve energy without a lifejacket:\n\n1. Float upright in the water and take a deep breath.\n2. Lower your face into the water (keeping your mouth closed) and bring your arms forward to rest at water level.\n3. Relax in this position until you need to take in more air.\n4. Raise your head above the surface, treading water, and exhale. Take another breath and return to the relaxed position.",
                    "### IMPROVISED FLOTATION\n\nYou can improvise a short-term flotation bag from a pair of trousers. Knot the bottoms of the legs, sweep them over the head to fill with air, then hold the waist below the water to trap the air inside, making the legs into water wings to lean on."
                ]
            },
            {
                "title": "Inflatable Dinghies",
                "subtitle": "Inflation, boarding, righting, and leak repair.",
                "imageName": "sea.jpg",
                "textSections": [
                    "Aircraft and many boats carry dinghy-type lifeboats. Many are self-inflating and activated by saltwater immersion; others have a pump provided. They are built in sections so that if one compartment is punctured, the others keep the dinghy afloat.",
                    "### BOARDING & HAULING\n\nGet aboard as soon as possible. Move to the end (not the side) of the dinghy, place one leg over the edge, and roll in. Do NOT jump into a dinghy from above, as you may damage it.\n\nTo haul someone else aboard, hold their shoulders and lift one leg over the end, then roll them in. Discourage them from putting their arms around your neck. Once aboard, tie yourself and others to the dinghy.",
                    "### RIGHTING A DINGHY\n\nMost dinghies have righting straps on the bottom, and larger ones have a righting line attached to one side. Grab it from the opposite side, brace your feet against the dinghy and pull. The dinghy should rise up and over, pulling you out of the water momentarily. In heavy seas or high winds, this is extremely difficult.",
                    "### DINGHY MAINTENANCE\n\n*   Ensure the dinghy is fully inflated (firm but not rock-hard). Re-inflate with your breath or a pump if needed. The valves are one-way.\n*   Check for leaks. Escaping air causes bubbles underwater and a hissing sound above. Deal with leaks using the conical plugs in the dinghy kit; screw them into the holes to seal. Use rubber patches and adhesive for other punctures. Make daily checks."
                ]
            },
            {
                "title": "Survival Afloat",
                "subtitle": "Triage order, sea anchors, logs, and watches.",
                "imageName": "sea.jpg",
                "textSections": [
                    "Rafts and boats are built to carry a limited number of survivors. Safety of the majority must be the priority. Place the infirm, youngsters, and injured in the craft first, followed by as many able-bodied as accommodated. The rest must hang on in the water, rotating on a regular change-over rota. Stow all gear and tie it securely. Ensure sharp objects are covered.",
                    "### SEA ANCHORS\n\nIf a distress call has gone out, maintain your location by streaming a sea anchor. This keeps the boat pointing into the weather and slows down drift. Improvise a sea anchor from a canvas bag or a weighted object (like clothing tied to a paddle).",
                    "### LOGKEEPING\n\nEven if alone, keep a daily log to occupy the mind and stay oriented. Record names of survivors, date, time, position of accident, weather conditions, equipment salvaged, and daily sightings.",
                    "### CLIMATE PROTECTION\n\n*   **Cold Climates**: Get out of the water. Keep the craft dry by bailing. Squeeze out wet clothes and put them back on if dry ones aren't available. Wrap in canvas/parachutes and huddle. Do mild stretching to prevent muscle stiffness.\n*   **Hot Climates**: Keep the body covered. Protect head and neck. Improvise eye shields. Dampen clothes with sea water to cool, but ensure you dry out by evening. Release some air from the dinghy during the heat (air expands) and reinflate when it cools.",
                    "### WATCHES\n\nAssign watches so there is a lookout at all times, including at night. Keep watch shifts short to avoid exhaustion. Look out for shipping, aircraft, signs of land, seaweed, shoals of fish, birds, and inspect the raft for chafing."
                ]
            },
            {
                "title": "Ocean Travel and Land Signs",
                "subtitle": "Currents, sails, and interpreting natural indicators.",
                "imageName": "sea.jpg",
                "textSections": [
                    "If a distress signal has been sent, or you are in shipping lanes, stay in the vicinity for 72 hours. Otherwise, get underway to utilize initial energy. In the open ocean, currents seldom exceed 9-13km (6-8 miles) per day. Take in the sea anchor and sail with the wind. Rudder control can be achieved using a paddle.",
                    "### USING THE WIND\n\nImprovise a sail if you do not have one. Do NOT secure the lower edges; hold the lower lines by hand so you can release them immediately if a sudden gust hits, preventing a capsize. In rough water, stream the sea anchor from the bow to keep the nose into the wind and stay low.",
                    "### LAND INDICATORS\n\nWhen no land is in sight, watch for these signs:\n*   **Clouds**: Cumulus clouds in an otherwise clear sky often form over land. In the tropics, a greenish tint on the underside of clouds (lagoon glare) reflects shallow reef waters.\n*   **Birds**: Most seabirds do not fly more than 100 miles from land. They fly outwards before noon and return in late afternoon. Continuous bird cries indicate nearby land.\n*   **Driftwood**: Coconuts, driftwood, and drifting vegetation indicate land, though currents can carry them far.\n*   **Sea Swells**: Swell height decreases if protected by land. If the wind is constant but waves decrease, land lies to windward.\n*   **Sea Colour**: Muddy water containing silt indicates the mouth of a large river."
                ]
            },
            {
                "title": "Water and Hydration",
                "subtitle": "Rationing schedules, dew collection, and strict prohibitions.",
                "imageName": "sea.jpg",
                "textSections": [
                    "Although a minimum of 1 litre (1 3/4 pt) a day is necessary to keep fit, you can survive on 55-220cc (2-8oz). Ration water immediately. Keep the ration strict until rescue. Reduce sweating by staying in the shade and dampening skin with sea water (if safe). Take anti-seasickness pills immediately to prevent fluid loss from vomiting.",
                    "> [!IMPORTANT]\n> If you are low on water, do NOT eat, especially protein foods (fish and seaweed) which require water to digest. Carbohydrates require less water.",
                    "### WATER RATIONING PROTOCOL\n\n*   **Day 1**: NO WATER. The body has a natural reservoir.\n*   **Days 2-4**: 400cc (14fl oz) daily if available.\n*   **Day 5 onwards**: 55-225cc (2-8fl oz) daily, depending on climate.\n*   *Drinking Method*: Moisten the lips, tongue, and throat before swallowing.",
                    "### GATHERING WATER\n\n*   **Rain**: Rig catchment sheets from canvas or plastic. When it rains, drink your fill slowly (gulping will cause vomiting). Stow excess. Puddles in the boat may be salty.\n*   **Dew**: Rig canvas at night with edges folded to catch condensation.\n*   **Sea Ice**: Use only old sea ice (blue-grey with rounded contours). New sea ice is salty. Old ice loses its salt after a year and can be melted or sucked.\n*   **Fish Fluids**: Drink the aqueous fluid along the spine and in the eyes of large fish. Do NOT drink other body fluids (high in protein/fat).",
                    "> [!WARNING]\n> *   DO NOT drink sea water (increases dehydration rapidly).\n*   DO NOT drink urine.\n*   DO NOT drink alcohol.\n*   DO NOT smoke.\n*   DO NOT eat unless water is available."
                ]
            },
            {
                "title": "Ocean Food Foraging",
                "subtitle": "Fishing methods, netting, and catching sea birds.",
                "imageName": "sea.jpg",
                "textSections": [
                    "Conserve emergency food supplies, taking small nibbles only, and live off the sea. In the open sea, out of sight of land, fish are generally safe to eat. Nearer shores, reefs, and lagoons, normally edible fish (like Red Snapper and Barracuda) can be poisonous.",
                    "### FISHING RULES\n\n*   Do NOT handle fishing line with bare hands and never tie it to an inflatable dinghy; salt makes the line razor-sharp. Wear gloves.\n*   Fish are attracted to the shade of a raft. Pass a net under the keel to catch them.\n*   Use a torch or moon reflections (on tinfoil or metal) to attract fish at night.\n*   Improvise hooks from pocket-knives, wire, or buckles. Keep spinners moving. Use fish offal for bait.\n*   Fish spoils quickly. In the tropics, eat immediately. In cooler zones, clean, gut, and dry excess fish in the sun.",
                    "### CATCHING BIRDS\n\nBirds are attracted to rafts. Keep still until they settle to grab them. Alternatively, catch them using lines trailed with a diamond-shaped tin gorge wrapped in fish. When the bird swallows it, the gorge lodges across its gullet.",
                    "### SEAWEED & PLANKTON\n\n*   Floating Sargassum seaweed can be gathered using a makeshift grapple hook. Raw seaweed is tough and salty; do not eat it when water is short. However, shake the weed over the boat to collect small edible crabs, shrimps, and fish.\n*   Plankton can be strained from the water using fine mesh cloth and provides an excellent food source."
                ]
            },
            {
                "title": "Dangerous Sea Creatures",
                "subtitle": "Poisonous fish, sharks, and landing on shores.",
                "imageName": "sea.jpg",
                "textSections": [
                    "### TOXIC FISH & JELLYFISH\n\nMany reef fish have toxic flesh (liver, intestines, eggs). Toxins are water-soluble and heat-resistant; cooking does NOT neutralize them. They cause numbness, temperature-reversal sensations (cold feels hot), vomiting, paralysis, and death. Rays have poisonous tail barbs, and Stonefishes/Toadfishes have venomous spines. Avoid jellyfish and the Portuguese Man-of-War; their trailing streamers carry painful toxins.",
                    "### AGGRESSIVE FISH\n\nAvoid Barracudas (will charge shiny objects), Sea Bass, Moray Eels, and venomous sea snakes.",
                    "### SHARK DEFENSE\n\nSix sharks account for most casualties: Great White, Mako, Tiger, Hammerhead, Bull, and Grey Nurse. Sharks locate prey by smell and water vibrations. They are attracted by blood, waste, and weak, fluttering movements. Regular, strong swimming strokes repel them.\n\n*   **In the water**: Avoid passing waste; if you must urinate, do so in short spurts. If threatened in a group, bunch together, face outwards, and kick/punch the snout using a stiff arm. Shout underwater.\n*   **On a raft**: Do not trail limbs. Do not fish or dump offal when sharks are present. Jab the snout with a paddle. If you catch a small shark, club it hard on the head before bringing it aboard. Do not attempt this with large sharks; cut the line.",
                    "### MAKING A LANDFALL\n\nWhen approaching land, select a beaching point away from rocks. Take down the sail and watch for currents. A sloping beach with small surf is ideal. Paddle hard on the back of a breaker to ride it in. In heavy surf, turn to face seaward and paddle into oncoming waves.\n\n*   If floating into an estuary, reach a bank quickly; the ebb tide can sweep you back out. If swept out, ballast the dinghy with water and stream the sea anchor.\n*   **Swimming ashore**: If swimming onto rocks in heavy surf, keep clothes, shoes, and lifejacket on. Raise your legs in front of you to take the impact on the soles of your feet, bending your knees to absorb the shock."
                ]
            }
        ]
    },
    {
        "title": "Rescue",
        "description": "Signaling systems, distress codes, rescue patterns, helicopter coordination, and the Lows Gully case study.",
        "articles": [
            {
                "title": "Signaling Basics",
                "subtitle": "Emergency distress calls, mobile phone use, and vehicle wreck signals.",
                "imageName": "rescue.jpg",
                "textSections": [
                    "The first requirement for rescue is to let others know of your situation and, if possible, your location. Once you are in contact you can pass on other information. If you have a working mobile or satellite phone, use it sparingly to conserve batteries.",
                    "If you don't have phone systems, use internationally recognized distress signals. The letters SOS (Save Our Souls) is the best known. It can be written, transmitted by radio, spelt out by semaphore, or sent in Morse code by any method. The signal 'Mayday' (from French m'aidez - help me) is used in radiotelecommunications by ships and planes.",
                    "### WRECKAGE UTILITY\n\nIf you are with a stranded vehicle or downed aircraft, it provides many signaling aids:\n*   **Fuel and Oils**: Burn fuel, oil, and hydraulic fluid. Tyres and electrical insulation generate dense black smoke.\n*   **Reflectors**: Glass, chrome, engine cowlings, and hubcaps make great reflectors.\n*   **Bright Materials**: Arrange colourful lifejackets, dinghies, and parachutes around your location to catch attention.\n*   **Lights and Horns**: Keep battery power in reserve to flash headlamps or sound the horn when searchers are observed."
                ]
            },
            {
                "title": "Fire and Smoke Signals",
                "subtitle": "Setting signal fires, site selection, and smoke colors.",
                "imageName": "rescue.jpg",
                "textSections": [
                    "Fire and smoke are excellent ways of attracting attention. Establishing signal fires is one of the primary tasks once immediate treatment and shelter needs are met. Gather fuel for campfires and signal fires as soon as possible.",
                    "### SITING SIGNALS\n\n*   Choose high points for light signals. Erect an unusual silhouette on a ridge.\n*   If laying out ground marks, use level ground or slopes that are visible during aerial searches.\n*   *Ridge Tip*: Planes fly over hilly territory from lower to higher ridges. Slopes behind ridges may be hidden. Siting signals near the tops of ridges ensures visibility from either direction.\n*   Do not build fires under trees; the canopy blocks the signal. Place them in clearings. If by a lake or river, build rafts to place fires on and anchor them.",
                    "### FIRE TYPES\n\n*   **Three Fires**: Three fires placed in a triangle or a straight line is an internationally recognized distress signal. Keep them prepared and covered to stay dry.\n*   **Torch Trees**: For small isolated trees, build a fire between the boughs using dry twigs. If the tree is dead, start a fire at its base. It will burn for a long time. *Warning*: Do not risk starting a forest fire.\n*   **Luminous Cone Fires**: Make a tripod with a platform to support the fire, keeping tinder off damp ground. Cover the cone with evergreen boughs to keep it dry. If parachute fabric is available, cover the tripod to keep it dry and noticeable by day, stripping it off before ignition.",
                    "### SMOKE INDICATORS\n\nUse smoke during daylight to locate your position, adjusting materials based on the environment:\n*   **Light Smoke**: Stands out against dark earth or forest. Produce it with green grass, leaves, moss, ferns, and damp mats.\n*   **Dark Smoke**: Shows best against snow or desert sand. Use rubber, tyres, or oil.\n*   *Wind & Display*: Ensure smoke is downwind of the landing site and panel codes so it does not obscure them from above."
                ]
            },
            {
                "title": "Ground-to-Air Panel Codes",
                "subtitle": "International emergency markings and visual codes.",
                "imageName": "rescue.jpg",
                "textSections": [
                    "These symbols are internationally recognized emergency signals. Remember the main ones with the mnemonic **FILL** (Food, Injury, Illness, Location). The single bar 'I' is the most important.",
                    "### VISUAL PANEL CODE KEY\n\n*   `I` : Serious injury - immediate casualty evacuation needed (NEED DOCTOR)\n*   `II` : Need medical supplies\n*   `F` : Need food and water\n*   `N` : Negative (No)\n*   `Y` or `A` : Affirmative (Yes / All well)\n*   `L` : All is well\n*   `X` : Unable to move on\n*   `K` : Indicate direction to proceed\n*   `->` : Am moving in this direction\n*   `JL` : Do not understand\n*   `[]` : Need compass and map\n*   `Triangle` : Think safe to land here\n*   `LL` : Aircraft badly damaged",
                    "### DISPLAY PARAMETERS\n\nMake panel codes as large as possible. The recommended size is **10m long and 3m wide (34ft x 10ft)** for each symbol, with 3m (10ft) between symbols.",
                    "Lay them in the open, avoiding steep gullies, ravines, or reverse slopes. Improvise with wreckage, or dig shallow trenches, banking the earth to increase shadow depth. Use rocks or boughs. On snow, tramping out the symbols works well.",
                    "### MORSE CODE CORE WORDS\n\nCarry a copy of the Morse code on your person. Learn these essential codes:\n*   **SOS**: `... --- ...`\n*   **HELP**: `.... . .-.. .--.`\n*   **INJURY**: `.. -. .--- ..- .-. -.--`\n*   **TRAPPED**: `- .-. .- .--. .--. . -..`\n*   **LOST**: `.-.. --- ... -`\n*   **WATER**: `.== .- - . .-.``"
                ]
            },
            {
                "title": "Heliograph and Light Signals",
                "subtitle": "Directing mirror flashes and transmitter procedures.",
                "imageName": "rescue.jpg",
                "textSections": [
                    "### HELIOGRAPH SIGNALING\n\nUse the sun and a reflector to flash light signals. Tin lids, glass, foil, or mirrors can be used. Long flashes represent dashes, quick ones represent dots. Sweep the horizon. If a plane approaches closely, flash intermittently to avoid dazzling the pilot. Once seen, STOP signaling.",
                    "### SIGHTING METHODS\n\n*   **Double-sided Reflector**: Sight the target through the central hole. Angle the mirror so the dot of light on your face disappears back through the hole, aligning it with the target.\n*   **Single-sided Reflector**: Cast the sun reflection onto a nearby surface (the ground or a hand) and line it up with the target.",
                    "### RADIO TRANSMITTERS\n\nShip and plane emergency transceivers are often preset to fixed distress channels (121.5 and 243 MHz) with a range of about 32km (20 miles). Conserve batteries by transmitting in structured patterns rather than continuous broadcasts.",
                    "### BODY SIGNALS\n\n*   **Pick us up**: Arms raised vertically overhead.\n*   **Need mechanical help**: One arm raised, pointing to the ground, other arm horizontal.\n*   **Land here**: Arms pointing down at the ground.\n*   **Do NOT land here**: Both arms crossed overhead.\n*   **Yes**: Wave a white cloth horizontally.\n*   **No**: Wave a white cloth vertically."
                ]
            },
            {
                "title": "Search Patterns",
                "subtitle": "How search patrols operate on land and sea.",
                "imageName": "rescue.jpg",
                "textSections": [
                    "A search starts from the last known location and sweeps along the proposed route. Understanding search patterns helps you place signals effectively.",
                    "### STANDARD SEARCH PATTERNS\n\n*   **Base Line (Box Search)**: Conducted when high winds or bad weather occur. Searchers check the lee sides of ridges and slopes for shelter.\n*   **Watercourse Search**: Follows the main stream and checks all tributaries. Used if the last known position was on or near a river.\n*   **Fan Search**: Used when the last known position is certain, but the travel direction is unknown. Sweeps out in a fan shape.\n*   **Creeping Line**: Parallel sweeps toward and away from the sun. The sun angle highlights reflections from wreckage.",
                    "### TRACKS AND CONTOURS\n\n*   **Track Crawl**: Parallels both sides of the expected flight path. Aircraft fly one hour, then reverse.\n*   **Square Search**: Works outward in a square from the last known position.\n*   **Contour Search**: Follows the contours of mountains and valleys, sweeping several times to cover steep drops."
                ]
            },
            {
                "title": "Helicopter Rescue",
                "subtitle": "Landing zone preparations, winching, and safety guidelines.",
                "imageName": "rescue.jpg",
                "textSections": [
                    "Helicopters carry out the actual rescue. Prepare a landing site at ground level to minimize risks.",
                    "### LANDING ZONE PREPARATION\n\n*   **Dimensions**: A level, cleared area at least **26m (85ft)** in diameter is required. Clear a further 5m (17ft) buffer to a height of 60cm (2ft).\n*   **Approach & Exit**: Obstruction-free paths are needed into the prevailing wind (no obstacles within a 15-degree angle of the pad).\n*   **Slope**: The landing gradient must not exceed 7 degrees (a slope of 1 in 10).\n*   **Ground**: Must be firm and free of loose material (leaves, twigs). Stamp down soft snow to prevent downwash blinding. Water dry ground to prevent dust.",
                    "### MARKINGS & HIGH ALTITUDE\n\n*   Mark the touchdown point with a large **H** using rocks, clothing, or panels. Indicate wind direction using smoke (downwind of the pad) or a large 'T' (horizontal bar upwind).\n*   The payload of a helicopter is reduced at high altitudes. If possible, select a landing site below **1830m (6000ft)**.",
                    "### APPROACH RULES\n\nRotors remain turning during touchdown. Follow these rules:\n*   **NEVER approach from the rear**. This is a blind spot and the tail rotor is dangerous.\n*   On sloping ground, approach from the downslope (uphill direction) to stay below the rotor blades. Never approach from upslope.\n*   Stow all radio aerials. Hold carrying poles horizontally, never vertically.",
                    "### WINCH LIFTING\n\nIf a landing is impossible, winching is used:\n*   **Double Lift**: A crewman is lowered with a second strop. He wraps his legs around your midsection and supports your head.\n*   **Single Lift**: Put the strop under your armpits, tighten the grommet, and give a 'thumbs up' sign. Once lifting begins, keep your arms down at your sides. If you raise your arms, you risk slipping out."
                ]
            },
            {
                "title": "Survival Case Study",
                "subtitle": "The Lows Gully Expedition",
                "imageName": "rescue.jpg",
                "textSections": [
                    "This case study highlights the dangers of inadequate planning, group splits, and traveling without signaling gear.",
                    "In 1994, an expedition of two British officers and three Hong Kong Chinese soldiers descended into Lows Gully on Mount Kinabalu in Malaysia. The plan was to travel light; they carried 10 days' rations and a video camera, but **no radio and no flares**.",
                    "By the third day, the team split because some members were not in shape for the descent. The fittest forged ahead while the second group rested, planning to follow later. When the second group began, slow progress with novice climbers left them with only 3 days' rations.",
                    "Torrential mountain rains flooded the gully. The advance team became separated during the struggle through dense undergrowth. Two members continued, running out of food and becoming violently ill after eating toxic forest plants.",
                    "The Malaysian Army and a Royal Air Force rescue team launched a massive search. After 10 days, a Malaysian helicopter spotted the stranded second team. They were rescued **31 days** after setting out.",
                    "> [!IMPORTANT]\n> **Lessons learned**: Plan adequately, keep the group together, do not underestimate the environment, and always carry signaling gear (flares, radios) and emergency survival supplies."
                ]
            }
        ]
    }
]

# Ensure output directory exists
if not os.path.exists(JSON_OUTPUT_DIR):
    os.makedirs(JSON_OUTPUT_DIR, exist_ok=True)

with open(JSON_OUTPUT_PATH, 'w', encoding='utf-8') as f:
    json.dump(structured_chapters, f, indent=4, ensure_ascii=False)

print(f"Successfully generated clean survival content JSON at {JSON_OUTPUT_PATH}")
