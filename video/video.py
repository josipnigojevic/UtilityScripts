from moviepy.editor import *
from moviepy.video.VideoClip import TextClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.audio.io.AudioFileClip import AudioFileClip
import pyttsx3
import random
from pydub import AudioSegment
from io import BytesIO

# Initialize the engine
engine = pyttsx3.init()

# Set the properties
engine.setProperty('rate', 150)  # Speed percent (can go over 100)
engine.setProperty('pitch', 3000)
engine.setProperty('volume', 1)  # Volume 0-1
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) # here we use the second voice in the list



# video text
text = [
'Daniel wlah once battled an army of booboo monsters using only his silly poopoo jokes as weapons.',
'When Daniel wlah drinks too much cummy juice, he turns into a silly peepee superhero.',
'Daniel wlah\'s favorite food is a cummy poopoo sandwich with a side of yummy booboo fries.',
'Last night, Daniel wlah dreamed that he was flying through a magical cummy universe filled with silly booboo creatures.',
'Daniel wlah\'s trusty sidekick is a silly poopoo monkey named Cummy who loves to eat yummy cummy cakes.',
'The magical peepee fountain that Daniel wlah discovered in the middle of the booboo forest cured his silly poopoo disease.',
'Daniel wlah once saved a group of helpless booboo fairies from the evil grasp of a cummy witch.',
'When Daniel wlah enters the silly poopoo palace, he is greeted by a team of cummy guards who only speak in silly peepee rhymes.',
'Daniel wlah\'s secret weapon in battle is a powerful peepee cannon that shoots cummy bubbles at his enemies.',
'The silly cummy party that Daniel wlah threw in the middle of the booboo desert was so epic that it became a legend among the silly poopoo tribes.',
'Daniel wlah once rode a magical booboo unicorn through the clouds, leaving a trail of yummy sprinkles behind him.',
'The silly poopoo robot that Daniel wlah created using a jar of cummy sprinkles became his trusty sidekick on many adventures.',
'Daniel wlah once visited a planet made entirely of peepee and spent the day sliding down its booboo mountains.',
'When Daniel wlah drank the magical cummy potion, he could hear the silly voices of booboo fairies whispering in his ear.',
'Daniel wlah\'s greatest fear is running out of yummy cummy cakes, which he considers to be his source of silly poopoo power.',
'daniel wlah\'s secret hideout is located in the middle of the booboo jungle, protected by a team of cummy guards.',
'Last Halloween, daniel wlah dressed up as a silly poopoo monster and scared all his friends with his cummy laser gun.',
'When daniel wlah traveled to the magical land of peepee, he met a group of silly booboo wizards who taught him the ways of cummy magic.',
'daniel wlah\'s favorite pastime is building silly poopoo castles out of cummy sand on the beach.',
'The silly peepee dance that daniel wlah invented became an instant hit among the booboo tribes, who would perform it during their cummy rituals.',
'daniel wlah once battled an army of cummy robots using only his trusty booboo sword and his silly poopoo jokes.',
'The silly cummy potion that daniel wlah drank made him so powerful that he could control the silly poopoo weather with his mind.',
'daniel wlah\'s pet peepee dragon, named Cummy, loves to eat yummy cummy cakes and blow silly booboo fireballs.',
'The magical booboo tree that daniel wlah discovered in the middle of the cummy desert granted him the power of silly poopoo wisdom.',
'daniel wlah\'s silly poopoo spaceship, powered by cummy fuel, can travel at the speed of peepee light.',
'When daniel wlah visited the silly cummy planet, he discovered a hidden treasure trove filled with priceless booboo artifacts.',
'The silly peepee language that daniel wlah invented is now spoken by millions of silly poopoo creatures all over the world.',
'daniel wlah\'s silly cummy laser gun, which shoots out streams of silly poopoo bubbles, has saved him from many dangerous situations.',
'When daniel wlah entered the cummy castle, he was greeted by the evil queen of booboo, who challenged him to a silly peepee duel.',
'daniel wlah\'s ultimate goal is to unite the silly poopoo tribes and create a world where cummy magic and silly adventures are the norm.',
'daniel wlah\'s silly poopoo hat, decorated with cummy jewels and a peepee feather, is his trademark accessory.',
'The cummy river that flows through daniel wlah\'s silly booboo village is said to have magical properties that can grant silly wishes.',
'daniel wlah\'s cummy compass, which always points towards the nearest silly poopoo adventure, has never failed him.',
'The silly peepee race that daniel wlah participated in had obstacles like the booboo wall and the cummy pit.',
'daniel wlah\'s silly poopoo team, made up of cummy warriors and peepee mages, is the strongest in all the land.',
'The silly cummy festival that daniel wlah attended had competitions like the booboo toss and the peepee relay.',
'daniel wlah\'s silly poopoo treasure map, marked with cummy symbols and peepee riddles, led him to a chest full of riches.',
'The cummy potion that daniel wlah brewed in his silly booboo cauldron gave him the power of peepee flight.',
'daniel wlah\'s silly poopoo rock band, named the Cummy Bunnies, is known for their catchy peepee lyrics and wild stage antics.',
'The silly cummy monster that daniel wlah defeated in the booboo forest was actually just a misunderstood peepee creature.',
'daniel wlah\'s silly poopoo best friend, a cummy robot named Bleep, always has his back during silly adventures.',
'The cummy castle that daniel wlah explored was filled with peepee traps and booboo puzzles.',
'daniel wlah\'s silly poopoo dance moves, which involve lots of cummy shuffling and peepee jumping, always impress his friends.',
'The silly cummy potion that daniel wlah drank gave him the ability to see into the future and predict booboo disasters.',
'daniel wlah\'s silly poopoo scooter, made out of cummy wood and powered by peepee energy, is the envy of all his friends.',
'The cummy crystal that daniel wlah found in the silly poopoo cave was rumored to have the power to grant eternal peepee life.',
'daniel wlah\'s silly booboo village is known for its famous cummy restaurant, which serves the best peepee soup in the land.',
'The silly cummy circus that daniel wlah visited had performers like the acrobatic booboo clowns and the peepee tightrope walkers.',
'daniel wlah\'s silly poopoo superhero alter ego, named Cummy Man, is known for his incredible peepee strength and cummy agility.',
'The cummy potion that daniel wlah brewed in his silly booboo lab allowed him to communicate with peepee animals and booboo plants.',
'daniel wlah\'s silly poopoo magic show, which involves lots of cummy tricks and peepee illusions, always wows the audience.',
'The silly cummy spaceship that daniel wlah built in his backyard, powered by peepee crystals and cummy fuel, can travel to the moon and back.',
'daniel wlah\'s silly poopoo backpack, filled with cummy snacks and peepee gadgets, is always by his side during silly adventures.',
'The cummy portal that daniel wlah discovered in the booboo mountains led him to a silly poopoo dimension filled with strange creatures',
'The silly cummy carnival that daniel wlah attended had rides like the booboo coaster and the peepee ferris wheel.',
'daniel wlah\'s silly poopoo dance moves, inspired by cummy magic and peepee rhythm, always impress his friends.',
'The cummy potion that daniel wlah drank made him grow a silly peepee tail, much to his surprise.',
'The silly cummy fashion show that daniel wlah participated in had outfits made of booboo feathers and peepee sequins.',
'daniel wlah\'s silly poopoo pet, a cummy dragon named Sparky, breathes peepee fire and loves to cuddle.',
'The cummy library that daniel wlah visited contained rare books on silly poopoo history and peepee science.',
'daniel wlah\'s silly cummy phone, which doubles as a peepee flashlight and a booboo translator, is his most prized possession.',
'The silly peepee obstacle course that daniel wlah conquered had challenges like the cummy rope climb and the booboo balance beam.',
'The cummy chef that daniel wlah met at the booboo market taught him how to make a delicious peepee stew.',
'daniel wlah\'s silly poopoo vehicle, a cummy hovercraft powered by peepee magic, can travel through any terrain.',
'The silly cummy game that daniel wlah played with his friends involved throwing booboo balls and catching peepee frisbees.',
'The cummy mountain that daniel wlah climbed had a peepee waterfall at its peak, which he used to cool off.',
'daniel wlah\'s silly poopoo dream is to build a cummy castle made entirely out of booboo bricks and peepee mortar.',
'The silly cummy maze that daniel wlah navigated had twists and turns that led to secret booboo rooms and peepee passages.',
'The cummy telescope that daniel wlah used to gaze at the stars showed him a peepee constellation shaped like a booboo dragon.',
'daniel wlah\'s silly poopoo quest to find the fabled cummy sword of booboo legend has led him on many peepee adventures.',
'The silly cummy party that daniel wlah hosted had decorations made of booboo balloons and peepee confetti.',
'The cummy island that daniel wlah discovered was home to a tribe of silly poopoo mermaids who spoke in peepee songs.',
'daniel wlah\'s silly poopoo invention, a cummy robot that can cook peepee pancakes and clean booboo dishes, has made his life easier.',
'The silly cummy tournament that daniel wlah competed in had events like the booboo joust and the peepee archery contest.',
'When daniel wlah met the silly poopoo king, he was gifted a cummy crown adorned with peepee jewels.',
'The booboo maze that daniel wlah navigated had traps like the cummy spikes and the silly poopoo pendulum.',
'daniel wlah\'s silly cummy ship, powered by peepee crystals and equipped with booboo cannons, sailed the seven silly seas.',
'The cummy castle that daniel wlah conquered had a silly poopoo dungeon filled with booboo monsters and peepee traps.',
'daniel wlah\'s silly poopoo cookbook, filled with cummy recipes and peepee anecdotes, is a must-read for all adventurous chefs.',
'The cummy oracle that daniel wlah consulted predicted a silly future filled with booboo riches and peepee surprises.',
'daniel wlah\'s silly poopoo backpack, filled with cummy tools and peepee snacks, is always by his side during silly adventures.',
'The silly cummy dance that daniel wlah learned at the booboo ball was a hit with the peepee crowd.',
'daniel wlah\'s silly poopoo bedtime stories, featuring cummy dragons and peepee princesses, are a hit with silly children everywhere.',
'The booboo potion that daniel wlah brewed in his cummy cauldron granted him the power of silly invisibility.',
'daniel wlah\'s silly poopoo fashion sense, with cummy boots and peepee scarves, is the envy of silly creatures everywhere.',
'The silly cummy mountain that daniel wlah climbed had obstacles like the booboo boulder and the peepee crevasse.',
'daniel wlah\'s silly poopoo sword, forged from cummy steel and infused with peepee magic, is his trusty weapon in battle.',
'The cummy carnival that daniel wlah attended had rides like the booboo coaster and the silly poopoo ferris wheel.',
'daniel wlah\'s silly peepee jokes, told with cummy timing and a booboo punchline, always get a laugh.',
'The silly cummy portal that daniel wlah discovered led him to a booboo dimension filled with peepee wonders.',
'daniel wlah\'s silly poopoo disguise, with cummy glasses and a peepee wig, helped him sneak into the booboo party undetected.',
'The cummy creature that daniel wlah befriended in the silly swamp turned out to be a valuable peepee ally.',
'daniel wlah\'s silly poopoo guitar, made from cummy wood and adorned with peepee strings, is his instrument of choice for silly serenades.',
'The silly cummy riddle that daniel wlah solved had clues like the booboo footprint and the peepee feather.']

#text = [
#    'According to the United Nations, nearly 690 million people are hungry, and this number is expected to rise due to the COVID-19 pandemic.',
#    '9 out of 10 people in the world breathe polluted air, which causes an estimated 7 million premature deaths annually.',
#    'The gap between the rich and poor is widening, with the top 1%\ of the world\'s population owning more wealth than the other 99%.',
#    'The world\'s oceans are becoming more acidic due to increased levels of carbon dioxide, which can harm marine life and ecosystems.',
#    'The global refugee crisis is at its highest level since World War II, with nearly 26 million people forced to flee their homes due to conflict or persecution.',
#    'Climate change is causing more frequent and severe natural disasters, including hurricanes, floods, and wildfires.',
#    'The Amazon rainforest, which produces 20%\ of the world\'s oxygen, is being destroyed at an alarming rate due to deforestation.',
#    'More than 2 billion people lack access to clean drinking water, and the world\'s water resources are being depleted at an unsustainable rate.',
#    'Antibiotic resistance is a growing threat to public health, and it is estimated to cause 10 million deaths annually by 2050.',
#    'Millions of children around the world are forced into child labor, which deprives them of their childhood and education.',
#    'The world\'s population is projected to reach 9.7 billion by 2050, which could lead to food and water shortages and further strain on the environment.',
#    'The use of single-use plastics is contributing to a global waste crisis, with an estimated 8 million tons of plastic entering the oceans each year.',
#    'Mental illness affects millions of people worldwide, and many do not have access to adequate treatment or support.',
#    'Income inequality is linked to higher rates of crime, social unrest, and political instability.',
#    'Human trafficking is a growing problem, with an estimated 25 million people forced into labor or sexual exploitation worldwide.',
#    'The global economy is heavily dependent on fossil fuels, which contribute to climate change and other environmental problems.',
#    'The digital divide between developed and developing countries is widening, with millions of people lacking access to the internet and digital technologies.',
#    'The world\'s bee population is declining, which could have significant consequences for food production and ecosystem health.',
#    'The United States, Russia, and China possess the majority of the world\'s nuclear weapons, and the risk of nuclear war remains a concern.',
#    'Income inequality is linked to lower life expectancy and poorer health outcomes, particularly in low-income communities.',
#    'The world\'s population is aging, which could strain healthcare systems and social security programs.',
#    'The global economy is vulnerable to financial crises, which can lead to unemployment, poverty, and social unrest.',
#    'The opioid epidemic in the United States is causing an estimated 130 deaths per day and has devastated many communities.',
#    'The use of child soldiers is still prevalent in many parts of the world, with an estimated 250,000 children involved in armed conflicts.',
#    'Many species of plants and animals are becoming extinct at an alarming rate due to habitat loss, climate change, and other factors.',
#    'Income inequality is linked to lower levels of education and literacy, which can limit opportunities and perpetuate poverty.',
#    'The use of landmines in war zones has caused countless deaths and injuries, and many countries still produce and use them.',
#    'Over 1 billion people worldwide live with disabilities, and many face discrimination and lack of access to essential services.',
#    'The global fashion industry is the second-largest polluter in the world, generating vast amounts of waste and carbon emissions.',
#    'Gender-based violence affects millions of people worldwide, and many do not have access to adequate support or justice.',
#    'The global education system is failing many children, with an estimated 260 million children out of school and many more not receiving quality education.',
#    'The use of fossil fuels is a major contributor to climate change, which could lead to disastrous consequences for the planet and its inhabitants.',
#    'The world\'s forests are being destroyed at an alarming rate, with an estimated 18 million acres lost each year due to deforestation.',
#    'The global food system is unsustainable and contributes to environmental degradation, biodiversity loss, and food insecurity.',
#    'Mental health disorders affect millions of people worldwide, and many face stigma and discrimination when seeking treatment.',
#    'Income inequality is linked to poor health outcomes, including higher rates of chronic disease and shorter life expectancy.',
#    'The global population is growing, which puts additional strain on resources and exacerbates many of the world\'s problems.',
#    'The use of pesticides and other chemicals in agriculture has harmful effects on human health and the environment.',
#    'The world\'s oceans are becoming more acidic, which can harm marine life and threaten global food security.',
#    'The use of non-renewable resources is depleting the planet\'s natural resources and contributing to environmental degradation.',
#    'Millions of people are displaced from their homes due to conflict, persecution, and natural disasters, and many do not have access to adequate support.',
#    'The global healthcare system is facing significant challenges, including rising costs and inequalities in access to care.',
#    'Climate change is causing mass migration, which can lead to social unrest and political instability.',
#    'The use of single-use plastics is causing significant harm to the environment, including pollution of oceans and other water bodies.',
#    'The global economy is heavily dependent on fossil fuels, which makes it vulnerable to price shocks and supply disruptions.',
#    'The world\'s freshwater resources are becoming increasingly scarce, which could lead to conflicts over water resources.',
#    'Income inequality is linked to higher rates of crime and social unrest, which can have significant consequences for communities and societies.',
#    'The use of child labor and forced labor is still prevalent in many parts of the world, including in industries such as fashion, electronics, and agriculture.',
#    'The global energy system is unsustainable and contributes to climate change and other environmental problems.',
#    'The world\'s population is aging, which could lead to significant challenges for healthcare systems and social security programs.',
#    'The use of landmines in conflict zones continues to cause significant harm to civilians, including many children.',
#    'The global economy is vulnerable to financial crises, which can lead to unemployment, poverty, and social unrest.',
#    'Income inequality is linked to lower levels of social mobility and opportunities, which perpetuates poverty and inequality.',
#    'The use of nuclear weapons poses a significant threat to global security and the survival of humanity.',
#    'The global tourism industry has significant environmental and social impacts, including the destruction of natural habitats and exploitation of local communities.',
#
#]
# Define the video parameters
WIDTH, HEIGHT = 1500, 1000
DURATION = 8
DURATION_2 = 80





# Create a black clip with the given duration
background = ColorClip((WIDTH, HEIGHT), color=(0, 0, 0), duration=DURATION_2)

quotes = random.sample(text, 10)

output_wav_audio =" ".join(quotes) 

# save the TTS output to a WAV file
engine.save_to_file(output_wav_audio, 'output.mp3')

# run the TTS engine
engine.runAndWait()

# Add text to the clip
txt = TextClip(quotes[0], fontsize=25, color='white')
txt = txt.set_pos('center').set_duration(DURATION)

# Add text to the clip
txt_2 = TextClip(quotes[1], fontsize=25, color='white')
txt_2 = txt_2.set_pos('center').set_duration(DURATION)
txt_2 = txt_2.set_start(8)

# Add text to the clip
txt_3 = TextClip(quotes[2], fontsize=25, color='white')
txt_3 = txt_3.set_pos('center').set_duration(DURATION)
txt_3 = txt_3.set_start(16)

# Add text to the clip
txt_4 = TextClip(quotes[3], fontsize=25, color='white')
txt_4 = txt_4.set_pos('center').set_duration(DURATION)
txt_4 = txt_4.set_start(24)

# Add text to the clip
txt_5 = TextClip(quotes[4], fontsize=25, color='white')
txt_5 = txt_5.set_pos('center').set_duration(DURATION)
txt_5 = txt_5.set_start(32)

# Add text to the clip
txt_6 = TextClip(quotes[5], fontsize=25, color='white')
txt_6 = txt_6.set_pos('center').set_duration(DURATION)
txt_6 = txt_6.set_start(40)

# Add text to the clip
txt_7 = TextClip(quotes[6], fontsize=25, color='white')
txt_7 = txt_7.set_pos('center').set_duration(DURATION)
txt_7 = txt_7.set_start(48)

# Add text to the clip
txt_8 = TextClip(quotes[7], fontsize=25, color='white')
txt_8 = txt_8.set_pos('center').set_duration(DURATION)
txt_8 = txt_8.set_start(56)

# Add text to the clip
txt_9 = TextClip(quotes[8], fontsize=25, color='white')
txt_9 = txt_9.set_pos('center').set_duration(DURATION)
txt_9 = txt_9.set_start(64)

# Add text to the clip
txt_10 = TextClip(quotes[9], fontsize=25, color='white')
txt_10 = txt_10.set_pos('center').set_duration(DURATION)
txt_10 = txt_10.set_start(72)


# Combine the text clip with the background music
final_clip = CompositeVideoClip([background, txt, txt_2, txt_3, txt_4, txt_5, txt_6, txt_7, txt_8, txt_9, txt_10])








# Write the output file
final_clip.write_videofile("output.mp4", fps=24)

audio_clip = AudioFileClip("output.mp3")
video_clip = VideoFileClip("output.mp4")
audio_clip_2 = AudioFileClip("62965__buddhamaster__right-behind-the-wall-c-3.mp3")
audio_clip_2 = audio_clip_2.volumex(0.3)
audio_clip = audio_clip.volumex(0.8)
combined_audio = CompositeAudioClip([audio_clip, audio_clip_2])

final_clip_two = CompositeVideoClip([video_clip.set_audio(combined_audio)])



final_clip_two.write_videofile("gofno.mp4")