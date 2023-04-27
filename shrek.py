import pyautogui
import random
import time

shrek_quotes = [
    "Ogres are like onions...they have layers.",
    "In the morning, I'm making waffles!",
    "Donkey, you're going the right way for a smack bottom.",
    "I like that boulder. That is a nice boulder.",
    "What are you doing in my swamp?",
    "It's not ogre...not yet.",
    "I live in a swamp. I put up signs. I'm a terrifying ogre! What do I have to do to get a little privacy?",
    "That'll do, Donkey. That'll do.",
    "I'm not the monster here. You are. You and the rest of that fairy tale trash, poisoning my perfect world.",
    "This is the part where you run away.",
    "Oh, you little...!",
    "Well, the reason you don't see many fairy tale endings is because no one ever gets to the end of the story.",
    "Don't mess with me. I'm the stair master.",
    "Blue flower, red thorns. Blue flower, red thorns. Man, this would be so much easier if I wasn't color-blind!",
    "What a lovely singing voice you must have. Shame I didn't hear it!",
    "I'm an ogre! You know, 'grab your torch and pitchforks'!",
    "Do you know the muffin man?",
    "Better out than in, I always say.",
    "I don't want to be a hero. I just want to go home.",
    "My swamp!",
    "I can't believe I'm losing to a bunch of amateurs. This is my swamp!",
    "That is nasty. That is disturbing. That is not right!",
    "This is gonna be fun. We can stay up late, swapping manly stories, and in the morning, I'm making waffles.",
    "I'm gonna go see Farquaad. Let me get this straight: you're gonna go fight a dragon and rescue a princess just so Farquaad will give you back your swamp, which you only don't have because he filled it full of freaks in the first place. Is that about right?",
    "Not the buttons! Not my gumdrop buttons!",
    "Hey, look at me, I'm a flying talking donkey!",
    "I can't feel my toes! I don't have any toes!",
    "I think I need a hug.",
    "Oh, come on, donkey. Look at him in his wee little boots. You know, how many cats can wear boots? Honestly.",
    "You're going the wrong way! It's the other way!",
    "What's the matter with you? What you got against the whole world anyway?",
    "Do you want me to go first? I'm pretty sure I know how to swim.",
    "Listen, little donkey, take a look at me. What am I?",
    "We can stay up late, swapping manly stories, and in the morning, I'm making waffles.",
    "I'm a donkey on the edge!",
    "Whoa. Look at that. Who'd want to live in a place like that?",
    "I can't believe we're flying with a dragon. On a dragon. We're flying on a dragon!",
    "And then one time I ate some rotten berries. Man, there were some strong gases seepin' outta my butt that day!",
    "I'll find those stairs. I'll whip their butt too. Those stairs won't know which way they're going.",
    "Princess Fiona: [sings] I need a hero! I'm holding out for a hero 'til the end of the night...",
    "Shrek: Donkey, two things, okay? Shut... up. Now go over there and see if you can find any stairs.",
    "I can't stop eating... I won't stop eating!",
    "You know, I always thought I'd rescued a damsel in distress. [Fiona burps] She's not that I expected.",
    "Donkey: [singing] On the road again. Sing it with me, Shrek. I can't wait to get on the road again.",
    "You, uh... you don't entertain much, do you?",
    "Blue flower, red thorns... blue flower, red thorns... this would be so much easier if I wasn't color-blind!",
    "I'm not the one with the problem, okay? It's the world that seems to have a problem with me!",
    "And in the morning, I'm making waffles!",
    "Shrek: Well, it's no wonder you don't have any friends. Donkey: Wow. Only a true friend would be that truly honest.",
    "Shrek: I hope you heard that! She called me a 'noble steed.' She think I'm a steed.",
    "You and the rest of that fairy-tale trash poisoning my perfect world.",
    "Donkey: You, uh... you don't live in a swamp. Shrek: I put up signs. I'm a terrifying ogre! What do I have to do to get a little privacy?",
    "The Princess will be up the stairs in the highest room in the tallest tower.",
    "Now really, it's rude enough being alive when no one wants you, but showing up uninvited to a wedding?",
    "There's a stack of freshly made pancakes in the middle of the woods, donkey. The question is, who cooked them?",
    "You and me both, pal. I... oooh! That is NICE. I like that.",
    "I like my privacy. I'm a loner, Dottie. A rebel.",
    "But that's just a donkey with a-... Hey, wait a minute. I know that donkey!",
    "He hooffed und he poooffed... und he... signed an eviction notice.",
    "Some of you may die, but it's a sacrifice I am willing to make.",
    "Oh! You want to talk about it? Well, why didn't you say so? [tosses dishes aside and sits down] Do you want to talk about it?",
    "What did you do with the princess?",
    "Yeah, it's getting him to shut up that's the trick.",
    "On the contrary, I have found a whole new respect for ogre's. Note to self, don't die.",
    "If I'm gonna die, I'm gonna die historic on the Fury Road.",
    "You don't know what it's like to be considered a freak. [pause] Well, maybe you do. But that's why we gotta stick together.",
    "Now, why don't you go celebrate your freedom with your own friends? Hmm? [pauses, then sadly] But, uh, I don't have any friends. And I'm not goin' out there by myself, Hey, wait a minute! I got a great idea! I'll stick with you. You're mean, green, fightin' machine. Together we'll scare the spit out of anybody that crosses us.",
    "What's the matter, you got something in your eye?"]

# vrime da se pribacis na taj prozor
time.sleep(10)


# umisto 100 stavi koliko puta zelis da spama
for i in range(100):
    pyautogui.typewrite(random.choice(shrek_quotes))
    time.sleep(0.01)
    pyautogui.press('enter')
    time.sleep(0.01)