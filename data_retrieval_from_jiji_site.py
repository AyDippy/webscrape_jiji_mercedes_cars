import time
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setting up my ChromeDriver
PATH = "C:/Program Files (x86)/chromedriver.exe"
service = Service(PATH)
driver = webdriver.Chrome(service=service)

# Open CSV file to save the extracted data
csv_file = open('car_details_from_links.csv', mode='w', newline='', encoding='utf-8')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Car Name', 'Location', 'Company Name', 'Make', 'Model', 'Color', 'Price', 'Manufacture Year', 'Link'])

# Read the saved links from the file
with open('saved_links.txt', 'r') as file:
    links = file.readlines()

# Loop through each link, access the page, and extract the data
for link in links:
    link = link.strip()  # Remove any leading/trailing whitespace or newline characters

    # Open the link in the browser
    driver.get(link)

    try:
        # Wait until the page loads fully and required elements are present
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='b-advert-title-inner qa-advert-title b-advert-title-inner--h1']"))
        )

        # Scraping car details
        car_name = driver.find_element(By.XPATH, "//div[@class='b-advert-title-inner qa-advert-title b-advert-title-inner--h1']").text
        loca_raw = driver.find_element(By.XPATH, "//div[@class='b-advert-info-statistics b-advert-info-statistics--region']").text.split(', ')
        location = ", ".join(loca_raw[:-1])
        name_of_company = driver.find_element(By.CLASS_NAME, 'b-seller-block__name').text
        make = driver.find_element(By.XPATH, "//div[@itemprop='brand' and contains(@class, 'b-advert-attribute__value')]").text
        model = driver.find_element(By.XPATH, "//div[@itemprop='model' and contains(@class, 'b-advert-attribute__value')]").text
        color = driver.find_element(By.XPATH, "//div[@itemprop='color' and contains(@class, 'b-advert-attribute__value')]").text
        price = driver.find_element(By.XPATH, "//div[@itemprop='price' and contains(@class, 'qa-advert-price-view-title')]").text
        year_of_manufacture = driver.find_element(By.XPATH, "//div[@itemprop='productionDate' and contains(@class, 'b-advert-attribute__value')]").text

        # Write the data into the CSV file
        csv_writer.writerow([car_name, location, name_of_company, make, model, color, price, year_of_manufacture, link])

    except Exception as e:
        print(f"Error processing link {link}: {e}")

# Close CSV file and browser when done
csv_file.close()
driver.quit()
