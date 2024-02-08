from selenium import webdriver
from selenium.webdriver.common.by import By
from tqdm import tqdm
import pandas as pd
import time


if __name__ == "__main__":
    driver = webdriver.Chrome()
    base_url = "https://www.imdb.com/chart/top/"
    movie_urls = []

    for idx in tqdm(range(100)):
        page_no = idx + 1
        page_url = f"{base_url}"
        driver.get(page_url)
        list = driver.find_elements(By.CLASS_NAME, 'ipc-metadata-list-summary-item')
        
        for item in list:
            url_tag = item.find_element(By.CLASS_NAME, 'ipc-title-link-wrapper')
            title = url_tag.text
            movie_url = url_tag.get_attribute('href')
            movie_urls.append(
                {
                    "title": title,
                    "url": movie_url
                }
            )

        time.sleep(1)

df = pd.DataFrame(data=movie_urls, columns=movie_urls[0].keys())
df.to_csv("movie_urls.txt", index=False)
        