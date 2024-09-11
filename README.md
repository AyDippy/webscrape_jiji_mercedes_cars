# Mercedes-Benz Cars Scraper

## Overview
This project is a Python-based web scraping tool that gathers details about Mercedes-Benz cars from [Jiji.ng](https://jiji.ng). The tool navigates through the website, scrapes the car listings, and stores the extracted data in a CSV file. The data includes essential car details such as name, location, price, make, model, color, year of manufacture, and links to the respective car pages.

The project is divided into two parts:
- **`main.py`**: Scrapes and saves the links to the individual Mercedes-Benz car listings from Jiji.
- **`data_retrieval_from_jiji_site.py`**: Uses the saved links from `main.py` to extract detailed car information and saves it to a CSV file.

## Features
- **Scrapes Data Automatically**: Collects up-to-date information on Mercedes-Benz car listings.
- **Handles Infinite Scrolling**: Automatically scrolls down to load more listings, ensuring comprehensive data extraction.
- **Saves Data in CSV Format**: Outputs the scraped data in a structured CSV format for easy analysis or integration into other systems.
- **Avoids Duplicate Data**: Ensures that duplicate links and data entries are avoided through efficient link management.

## Dataset
The dataset consists of over **500 rows of car details** extracted from **3000 links**, focusing on Mercedes-Benz car models listed on Jiji.ng.

## Data Fields
The data collected for each car includes:
- **Car Name**: The specific model and trim of the Mercedes-Benz car.
- **Location**: Where the car is located (city and region).
- **Company Name**: The seller or dealer offering the car.
- **Make**: The manufacturer (Mercedes-Benz).
- **Model**: The model of the car (e.g., GLE-Class, CLA 250).
- **Color**: The color of the car.
- **Price**: The listed price of the car.
- **Manufacture Year**: The year the car was produced.
- **Link**: The URL to the car listing.

## Project Structure
- **`main.py`**: The script responsible for retrieving and saving the links to car listings from Jiji.
- **`data_retrieval_from_jiji_site.py`**: The script that reads the saved links and extracts detailed information about each car.
- **`saved_links.txt`**: A file containing the URLs of individual car listings.
- **`car_details_from_links.csv`**: The final output file that contains the extracted car details.
- **`requirements.txt`**: Lists all the dependencies needed to run the project.

## Prerequisites
Before running the project, ensure you have the following installed:
- Python 3.x
- Selenium
- BeautifulSoup4
- Requests
- Lxml
- ChromeDriver

To install all the required dependencies, run:
```bash
pip install -r requirements.txt
```

## How to Run the Project

### Step 1: Clone the Repository
```bash
git clone https://github.com/your-username/mercedes-scraper.git
```

### Step 2: Install Dependencies
Run the following command to install the required packages:
```bash
pip install -r requirements.txt
```

### Step 3: Download and Set Up ChromeDriver
Download ChromeDriver matching your Chrome version from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads), and place it in your project directory.

### Step 4: Run the Link Scraper (`main.py`)
This script will scrape all the Mercedes-Benz car links from Jiji and store them in `saved_links.txt`.

```bash
python main.py
```

### Step 5: Run the Data Retrieval Script (`data_retrieval_from_jiji_site.py`)
This script will read the links from `saved_links.txt` and scrape the detailed car information for each link, saving the results in a CSV file.

```bash
python data_retrieval_from_jiji_site.py
```

### Step 6: View the Results
After running both scripts, you will find:
- **`saved_links.txt`**: Contains the links to the scraped car listings.
- **`car_details_from_links.csv`**: Contains the detailed data of all the Mercedes-Benz car listings.

## Example of the Output (CSV)
| Car Name                             | Location       | Company Name    | Make          | Model    | Color | Price         | Manufacture Year | Link |
|--------------------------------------|----------------|-----------------|---------------|----------|-------|---------------|------------------|------|
| Mercedes-Benz GLE-Class GLE 350 2016 | Lagos, Surulere | Rafis autos    | Mercedes-Benz | GLE-Class | Blue  | ₦ 38,500,000  | 2016             | [Link](https://example.com) |

## Challenges Encountered
- **Handling Infinite Scrolling**: The site had infinite scrolling, which required custom logic to scroll until no new content was loaded.
- **Duplicate Entries**: To avoid repeated entries, the scraper used a set to store unique URLs and ensure each car was processed only once.
- **Performance Optimization**: The project initially scraped thousands of links but was optimized to handle pagination and avoid reloading unnecessary data.

## Future Improvements
- **Enhancing Data Coverage**: Extend the scraper to cover more car models or categories beyond Mercedes-Benz.
- **Parallel Scraping**: Implement parallel processing to reduce the time taken to scrape large datasets.
- **Data Enrichment**: Include additional data fields like mileage, engine type, or seller ratings.

## Contributing
Contributions are welcome! Please fork the repository, make your changes, and submit a pull request. For significant changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
