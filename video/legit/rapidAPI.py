import requests

url = "https://large-text-to-speech.p.rapidapi.com/tts"

payload = {"text": "Perfection is achieved not when there is nothing more to add, but rather when there is nothing more to take away."}
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "944c17b0f2mshd172ff7649ad5a2p1d8599jsnad462818439f",
	"X-RapidAPI-Host": "large-text-to-speech.p.rapidapi.com"
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)
# Write the speech output to a file
with open("output.wav", "wb") as f:
    f.write(response.content)