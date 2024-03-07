import os
import time
import subprocess
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService

# Get the current script's directory
script_directory = os.path.dirname(os.path.realpath(__file__))

# URL of the website to scrape
url = "https://wigle.net/uploads"

# Set up the Chrome driver (you'll need to download chromedriver: https://sites.google.com/chromium.org/driver/)
chrome_path = os.path.join(script_directory, "chromedriver.exe")  # Assume chromedriver.exe is in the same folder as the script

# Time for the user to log in (in seconds)
login_time = 60

# Output directory for downloaded files (same as the script's directory)
output_directory = script_directory

try:
    chrome_service = ChromeService(chrome_path)
    driver = webdriver.Chrome(service=chrome_service)

    # Open the webpage
    driver.get(url)

    # Display message to the user
    print(f"***** Please log in within the next {login_time} seconds.***** The ChromeDriver window is open.")

    # Sleep for the specified duration
    time.sleep(login_time)

    # Extract links using Selenium
    links = driver.find_elements(By.XPATH, '//a[@title="Download Summary KML"]')

    # Check if links are found
    if links:
        # Download the files using curl format
        for link in links:
            download_link = link.get_attribute("href")

            # Extract filename from the URL
            filename = os.path.join(output_directory, download_link.split("/")[-1])

            # Add ".kml" file extension
            filename_with_extension = f"{filename}.kml"

            # Build the curl command
            curl_command = [
                "curl",
                download_link,
                "-H", "accept: application/vnd.google-earth.kml+xml",
                "-H", "authorization: Basic YourAPIHere",
                "--output", filename_with_extension  # Specify the local filename explicitly with ".kml" extension
            ]

            # Run the curl command using subprocess
            subprocess.run(curl_command)

            print(f"File '{filename_with_extension}' downloaded successfully.")

    else:
        print("No links with the specified title attribute found.")

except Exception as e:
    print(f"An error occurred: {str(e)}")

finally:
    # Close the browser
    if 'driver' in locals() and driver is not None:
        driver.quit()
