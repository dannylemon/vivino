from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import csv
import time

driver = webdriver.Firefox()
move = ActionChains(driver)

driver.get("https://www.vivino.com/explore")
# ?country_codes[]=be // seria a continuação do link para um countrycode específico.

driver.execute_script("document.querySelector('.rc-slider-handle-1').style.left = '0%'")
driver.execute_script(
    "document.querySelector('.rc-slider-handle-2').style.left = '100%'"
)
driver.find_element_by_css_selector(".rc-slider-handle-1").click()
driver.find_element_by_css_selector(".rc-slider-handle-2").click()


def scroll_down():

    # Get scroll height.
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:

        # Scroll down to the bottom.
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load the page.
        time.sleep(3)

        # Calculate new scroll height and compare with last scroll height.
        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:

            break
        last_height = new_height


genrewine_button = driver.find_element_by_xpath(
    "/html/body/div[2]/div[4]/div/div/div[2]/div[1]/div/div[1]/div[2]/label[6]"
    # label: 1-red 2-white 3-sparkling 4-rose 5-dessert 6-port
)
genrewine_button.click()

anyrating_radio = driver.find_element_by_xpath('//*[@id="1"]')
anyrating_radio.click()

scroll_down()

query_text = str(
    driver.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/h2").text
)
wine_quantity = int((query_text.split()[1]))

print(wine_quantity)


class wine:
    def __init__(self, genre, winery, name, country, region, rating, numberofratings):
        self.genre = genre
        self.winery = winery
        self.name = name
        self.country = country
        self.region = region
        self.rating = rating
        self.numberofratings = numberofratings


wines = []

for i in range(1, wine_quantity + 1):
    winery = str(
        driver.find_element_by_xpath(
            "/html/body/div[2]/div[4]/div/div/div[2]/div[2]/div[1]/div["
            + str(i)
            + "]/div[2]/div[1]/a/span[1]"
        ).text
    )
    name = str(
        driver.find_element_by_xpath(
            "/html/body/div[2]/div[4]/div/div/div[2]/div[2]/div[1]/div["
            + str(i)
            + "]/div[2]/div[1]/a/span[2]"
        ).text
    )
    country = str(
        driver.find_element_by_xpath(
            "/html/body/div[2]/div[4]/div/div/div[2]/div[2]/div[1]/div["
            + str(i)
            + "]/div[2]/div[1]/div/a[2]"
        ).text
    )
    region = str(
        driver.find_element_by_xpath(
            "/html/body/div[2]/div[4]/div/div/div[2]/div[2]/div[1]/div["
            + str(i)
            + "]/div[2]/div[1]/div/a[3]"
        ).text
    )
    rating = str(
        driver.find_element_by_xpath(
            "/html/body/div[2]/div[4]/div/div/div[2]/div[2]/div[1]/div["
            + str(i)
            + "]/div[2]/div[2]/div/div/div[1]"
        ).text
    )
    numberofratings = str(
        driver.find_element_by_xpath(
            "/html/body/div[2]/div[4]/div/div/div[2]/div[2]/div[1]/div["
            + str(i)
            + "]/div[2]/div[2]/div/div/div[2]/div[2]"
        ).text
    )
    wines.append(wine("Port", winery, name, country, region, rating, numberofratings))
with open("port_wine.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(
        ["Genre", "Winery", "Name", "Country", "Region", "Rating", "Number of Ratings"]
    )
    for wine in wines:
        writer.writerow(
            [
                wine.genre,
                wine.winery,
                wine.name,
                wine.country,
                wine.region,
                wine.rating,
                wine.numberofratings,
            ]
        )
print("Finished writing")
# print(wines[75].numberofratings)
# outputFile = open('output.csv', 'w', newline='')
# outputWriter = csv.writer(outputFile)
# outputWriter.writerow(wines)
# outputFile.close()

# print("parou de novo")

# save_data("your_file.ods", wines)
# print("parou de novo")

# redwine_xpath /html/body/div[2]/div[4]/div/div/div[2]/div[1]/div/div[1]/div[2]/label[1]
# whitewine_xpath /html/body/div[2]/div[4]/div/div/div[2]/div[1]/div/div[1]/div[2]/label[2]
# sparklingwine_xpath /html/body/div[2]/div[4]/div/div/div[2]/div[1]/div/div[1]/div[2]/label[3]
# rosewine_xpath /html/body/div[2]/div[4]/div/div/div[2]/div[1]/div/div[1]/div[2]/label[4]
# dessertwine_xpath /html/body/div[2]/div[4]/div/div/div[2]/div[1]/div/div[1]/div[2]/label[5]
# portwine_xpath /html/body/div[2]/div[4]/div/div/div[2]/div[1]/div/div[1]/div[2]/label[6]

# primeirovinhodalista______xpath /html/body/div[2]/div[4]/div/div/div[2]/div[2]/div[1]/div[1]
# vinicoladeumvinhox________xpath /html/body/div[2]/div[4]/div/div/div[2]/div[2]/div[1]/div[i]/div[2]/div[1]/a/span[1]
# nomedeumvinhox____________xpath /html/body/div[2]/div[4]/div/div/div[2]/div[2]/div[1]/div[i]/div[2]/div[1]/a/span[2]
# paisdeumvinhox____________xpath /html/body/div[2]/div[4]/div/div/div[2]/div[2]/div[1]/div[i]/div[2]/div[1]/div/a[2]
# regiaodeumvinhox__________xpath /html/body/div[2]/div[4]/div/div/div[2]/div[2]/div[1]/div[i]/div[2]/div[1]/div/a[3]
# notadeumvinhox____________xpath /html/body/div[2]/div[4]/div/div/div[2]/div[2]/div[1]/div[i]/div[2]/div[2]/div/div/div[1]
# numeroderatingsdeumvinhox_xpath /html/body/div[2]/div[4]/div/div/div[2]/div[2]/div[1]/div[i]/div[2]/div[2]/div/div/div[2]/div[2]
