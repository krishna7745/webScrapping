from selenium import webdriver
from selenium.webdriver.chrome.options import Options
DRIVER_PATH =r'C:\Users\User\Desktop\chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
driver.get('https://www.javatpoint.com/arduino')
allmenu= driver.find_elements_by_class_name('leftmenu')
a=[]
for menu in allmenu:
    for a in menu.find_elements_by_tag_name("a"):
        print(a.get_attribute('href'))
driver.close()
