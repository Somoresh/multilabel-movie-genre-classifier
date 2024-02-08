from selenium import webdriver
from selenium.webdriver.common.by import By
from tqdm import tqdm
import pandas as pd
import time


if __name__ == "__main__":
    driver = webdriver.Chrome()
    
    
    df = pd.read_csv("movies.csv")
    movie_urls = df['link'].to_list()

    for movie_url in movie_urls:
        driver.get(movie_url)
        
        title = driver.find_elements(By.CLASS_NAME, "sc-69e49b85-0 jqlHBQ")
        print(title)

        description = driver.find_elements(By.CLASS_NAME, "sc-466bb6c-1 dWufeH")
        print(description)

        director = driver.find_elements(By.CLASS_NAME, "ipc-metadata-list-item__label ipc-metadata-list-item__label--btn")
        print(director)

        writers = driver.find_elements(By.CLASS_NAME, "ipc-metadata-list-item__label ipc-metadata-list-item__label--btn")
        print(writers)
        
        break