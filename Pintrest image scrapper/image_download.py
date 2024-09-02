from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import requests
import os

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("--start-maximized")

# Set path for ChromeDriver
driver_path = "C:\\Program Files\\chromedriver-win64\\chromedriver.exe"  # Update this with your ChromeDriver path
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Function to scrape images from Pinterest
def scrape_images(query, num_images):
    search_url = f"https://in.pinterest.com/search/pins/?rs=ac&len=2&q={query}&eq={query}&etslf=34230"
    driver.get(search_url)
    time.sleep(5)  # Wait for the page to load fully

    # Create output directory named after the query
    output_folder = query  # Use the query as the folder name
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    count = 0
    downloaded_urls = set()  # To keep track of downloaded image URLs

    # Scroll down to load more images
    while count < num_images:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)  # Adjust the sleep time if necessary

        # Find all image elements
        image_elements = driver.find_elements(By.CSS_SELECTOR, "img[alt]")

        for img in image_elements:
            if count >= num_images:
                break
            try:
                # Get the image URL (check both 'src' and 'srcset' attributes)
                img_url = img.get_attribute("src") or img.get_attribute("srcset")
                if img_url and img_url.startswith("http") and img_url not in downloaded_urls:
                    img_data = requests.get(img_url).content
                    with open(os.path.join(output_folder, f"image_{count + 1}.jpg"), "wb") as handler:
                        handler.write(img_data)
                    downloaded_urls.add(img_url)
                    count += 1
                    print(f"Downloaded image {count}: {img_url}")
            except Exception as e:
                print(f"Could not download image {count}: {e}")

    print(f"Downloaded {count} images.")
    driver.quit()

# Usage
scrape_images("Andrew Garfield", 100) 
