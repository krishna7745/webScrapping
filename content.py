import os
topicList=r'C:\Users\User\Desktop\topicList'
print(os.chdir(topicList))
print(os.getcwd())
Files=os.listdir()
parentdir=r'C:\Users\User\Desktop\content'
#print(os.chdir(parentdir))
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
DRIVER_PATH =r'C:\Users\User\Desktop\chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
options = Options()
options.headless = True
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
for file in Files:
    with open(file,'r') as topic:
        file= file.strip('\n')
        file=file.split('.')[0]
        path= parentdir+'\\'+file
        print(path)
        os.mkdir(path)
        os.chdir(path)
        c=0
        for line in topic:
            c+=1
            filename=line
            filename=filename.split("/")[-1].strip('\n')
            filename= path+'\\'+str(c)+"."+filename+'.txt'
            print(filename)
            driver.get(line)
            try:
                data=driver.find_element_by_id('city').text
            except:
                pass
            with open(filename,'w',encoding='utf-8') as f:
                f.write(data)
    os.chdir(topicList)
