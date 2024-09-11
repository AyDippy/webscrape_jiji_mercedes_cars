import time
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# Setting up my ChromeDriver
PATH = "C:/Program Files (x86)/chromedriver.exe"
service = Service(PATH)
driver = webdriver.Chrome(service=service)

# Setting up to store unique links and avoid duplicates
processed_links = set()

# Open the website
driver.get("https://jiji.ng/")

# Search for "MERCEDES"
search = driver.find_element(By.CLASS_NAME, 'multiselect__input')
search.send_keys('MERCEDES')
search.send_keys(Keys.RETURN)

# Interact with the elements after search
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        '//*[contains(@style, \'background-image: url("https://assets.jijistatic.net/art/attributes/categories/vehicles/cars.png");\')]'))
    )

    actions = ActionChains(driver)
    actions.click(element).perform()

    driver.implicitly_wait(30)

    # Change the view to display the car listings
    icon_change = driver.find_element(By.XPATH,
                                      "//*[@class='b-adverts-listing-change-view__icon icon sprite-icons' and @color='#6C8EA0']")
    actions.click(icon_change).perform()

    # Set initial height for infinite scrolling
    previous_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to load more content
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)  # Wait for new content to load

        # Find car listings
        car_data = driver.find_elements(By.XPATH,
                                        "//div[contains(@class, 'b-list-advert__item-wrapper') and contains(@class, 'b-list-advert__item-wrapper--base')]//a")

        # Process the href links and save them to the file if they are new
        for car in car_data:
            href_link = car.get_attribute('href')

            if href_link not in processed_links:
                processed_links.add(href_link)  # Add to the set of processed links
                print(href_link)  # Print or log the href

                # Save the href link to a file
                with open('saved_links.txt', 'a') as file:
                    file.write(href_link + '\n')

        # Checking if the page has loaded new content by comparing the page height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == previous_height:
            break  # Exit loop if no new content is loaded
        previous_height = new_height

    time.sleep(10)

except Exception as e:
    print(f"Error occurred: {e}")

finally:
    driver.quit()
