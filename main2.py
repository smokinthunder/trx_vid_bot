from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import random

def process_terabox_link(input_string):
    s_index = input_string.find("/s/")
    if s_index == -1:
        return "Input string should contain '/s/'"
    sliced_part = input_string[s_index + 3:]
    result = "https://teradownloader.com/download?link=https%3A%2F%2Fteraboxlink.com%2Fs%2F" + sliced_part
    return result

def main():
    terabox_link = "https://teraboxlink.com/s/1XO8UE22d5Q3gygKVVDK-dA"
    
    # Initialize Firefox driver with specified binary path and options
    options = webdriver.FirefoxOptions()
    options.binary_location = '/usr/bin/firefox'  # Update this path to your Firefox binary location
    options.headless = False  # Change to True if you want to run in headless mode

    # Set custom user-agent
    options.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

    driver = webdriver.Firefox(options=options)

    try:
        processed_link = process_terabox_link(terabox_link)
        print(f"Processed link: {processed_link}")
        
        driver.get(processed_link)

        # Wait for Cloudflare protection to be bypassed
        WebDriverWait(driver, 120).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'text-white') and contains(@class, 'bg-blue-700')]"))
        )

        # Click the button to initiate download
        elem = driver.find_element(By.XPATH, "//button[contains(@class, 'text-white') and contains(@class, 'bg-blue-700')]")
        elem.click()

        # Adding random sleep to simulate human behavior
        time.sleep(random.randint(5, 10))  # Random sleep between 5 to 10 seconds

        print("Download completed successfully.")
    except TimeoutException:
        print("Error: The element was not found in the allotted time.")
    except NoSuchElementException:
        print("Error: The specified element could not be located.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
