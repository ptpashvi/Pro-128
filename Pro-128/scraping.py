from bs4 import BeautifulSoup

start_url = "https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"

browser = webdriver.Chrome("/Users/kalpeshpatel/Desktop/Python/C127/chromedriver_mac64/chromedriver")
browser.get(start_url)

time.sleep(10)

planet_data = []

def scrap():
    for i in range(0, 10):
        soup = BeautifulSoup(browser.page_source, "html.parsel")
        
        for ul_tag in soup.find_all("ul", attrs={"class", "exoplanet"}):
            li_tags = ul_tag.find_all("li")
            
            temp_list = []
            
            for index, li_tag in enumerate(li_tags):
                if index == 0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                    
                else: 
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")
            
            planet_data.append(temp_list)
            
    print(planet_data[1])