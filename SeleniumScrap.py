from selenium import webdriver
from selenium.webdriver.chrome.options import Options
DRIVER_PATH =r'C:\Users\User\Desktop\chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)

options = Options()
options.headless = True
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)

#options.add_argument("--window-size=1920,1200")
with open('filescrap.txt','r') as file:
    for line in file:
        lList=[]
        b='\n'
        driver.get(line)
        allmenu= driver.find_elements_by_class_name('leftmenu')
        #a=[]
        for menu in allmenu:
            for a in menu.find_elements_by_tag_name("a"):
                lList.append(a.get_attribute('href'))
        # links = driver.find_elements_by_tag_name('a')
        # for link in links:
        #     lList.append(link.get_attribute('href'))
        b=b.join(lList)
        filename=line
        filename=filename.split("/")[-1].strip('\n')
        filename= 'C:\\Users\\User\Desktop\\topicList\\'+filename+'.txt'
        with open(filename,'w')as file:
            file.write(b)
        print(filename)
driver.close()

