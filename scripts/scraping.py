from selenium import webdriver
import time

# Scraps price


class Scraping:
    def __init__(self, url, cooldown):
        self.driver = webdriver.Chrome(
            executable_path="C:/Users/dratw/Documents/PythonProjects/betowanieProjekt/chromedriver.exe"
        )
        self.url = url
        self.cooldown = cooldown

    def __getFloor(self):
        self.driver.get(self.url)
        floor = self.driver.find_element("xpath",
                                         "/html/body/div[1]/div/main/div/div/div[5]/div/div[1]/div/div[3]/div/div[6]/a/div/span[1]/div"
                                         ).get_attribute("innerText")
        return float(floor)

    def process(self):
        floor_price1 = self.__getFloor()
        print("Floor at the time of betting: {}".format(floor_price1))
        time.sleep(self.cooldown * 60)
        floor_price2 = self.__getFloor()
        print("Floor currently: {}".format(floor_price2))
        self.driver.close()
        return [floor_price1, floor_price2]
