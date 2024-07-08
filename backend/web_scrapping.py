from bs4 import BeautifulSoup
import requests

def extract_text_from_url(url) -> str:
	try:
		response = requests.get(url)
		soup = BeautifulSoup(response.content, 'html.parser')
		text = soup.get_text()
		return text
	except Exception as ex:
		print(f"Error fetching or parsing contentfrom url {url}, error: {ex}")
		return ''