from bs4 import BeautifulSoup
import requests

def extract_text_from_url(url):
	try:
		response = requests.get(url)
		soup = BeautifulSoup(response.content, 'html.parser')
		text = soup.get_text()

		return text

	except Exception as es:

		print(f"Error fetching or parsing content: {e}")

		return None