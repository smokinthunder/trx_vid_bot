from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
import undetected_chromedriver as uc


def process_terabox_link(input_string):
    s_index = input_string.find("/s/")
    if s_index == -1:
        return "Input string should contain '/s/'"
    sliced_part = input_string[s_index + 3:]
    result = "https://teradownloader.com/download?link=https%3A%2F%2Fteraboxlink.com%2Fs%2F" + sliced_part
    return result

def main():
    print("Enter a Terabox link:")
    terabox_link = input()
    driver = uc.Chrome()

    try:
        processed_link = process_terabox_link(terabox_link)
        print(f"Processed link: {processed_link}")
        
        driver.get(processed_link)
        
        elem = WebDriverWait(driver, 100).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'text-white') and contains(@class, 'bg-blue-700')]"))
        )
        elem.click()

        time.sleep(500)
        
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
