import requests
import os
from bs4 import BeautifulSoup

page_number = 1
url = "https://anyflip.com/xugzr/odkz"
base_image_url = url.replace("://", "://online.") + f"/files/mobile/{page_number}.jpg"

# Function to extract titles from HTML
def get_page_titles(html_content):
	soup = BeautifulSoup(html_content, 'html.parser')
	titles = soup.find_all("span", title=True)
	titles = titles[2].text
	titles.replace(" ", "_")
	print(titles)
	return titles

# Function to download images
def download_image(image_url, folder, page_number):
	response = requests.get(image_url)
	if response.status_code == 200:
		with open(os.path.join(folder, f"{page_number}.jpg"), 'wb') as f:
			f.write(response.content)

# Main script
response = requests.get(url)
if response.status_code == 200:
	page_titles = get_page_titles(response.content)
	os.makedirs("downloaded_images", exist_ok=True)

	while(True):
		base_image_url = url.replace("://", "://online.") + f"/files/mobile/{page_number}.jpg"
		print(f"Downloading page {page_number}")
		this_image = requests.get(base_image_url)
		print(this_image.status_code)
		if this_image.status_code !=200:
			break
		download_image(base_image_url, "downloaded_images", page_number)
		page_number+=1
	print("Download complete.")
else:
	 print(f"Failed to fetch the content. Status code: {response.status_code}")


