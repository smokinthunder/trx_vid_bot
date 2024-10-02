import requests

url = "https://terabox-downloader-direct-download-link-generator.p.rapidapi.com/fetch"

payload = { "url": "https://teraboxlink.com/s/1XO8UE22d5Q3gygKVVDK-dA" }
headers = {
	"x-rapidapi-key": "452e0ac1f5mshfc0ab50beeb55e0p15b98djsn687513ed817b",
	"x-rapidapi-host": "terabox-downloader-direct-download-link-generator.p.rapidapi.com",
	"Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json()[0]['dlink'])