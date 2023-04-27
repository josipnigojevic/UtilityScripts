import webbrowser
import time
import random

# List of URLs to open
urls = [
    'https://www.google.com',
    'https://www.youtube.com',
    'https://www.facebook.com',
    'https://www.reddit.com',
    'https://www.amazon.com',
    'https://www.wikipedia.org',
    'https://www.twitter.com',
    'https://www.instagram.com',
]

# Time between website openings (in seconds)
delay = 300  # 5 minutes

while True:
    # Choose a random URL from the list
    url = random.choice(urls)

    # Open the URL in the default browser
    webbrowser.open(url)

    # Wait for the specified delay before opening another website
    time.sleep(delay)
