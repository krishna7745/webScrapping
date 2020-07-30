import os
import threading
import multiprocessing
topicList=r'C:\Users\User\Desktop\topicList'
print(os.chdir(topicList))
print(os.getcwd())
Files=os.listdir()
parentdir=r'C:\Users\User\Desktop\contentHtml'
#print(os.chdir(parentdir))
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
DRIVER_PATH =r'C:\Users\User\Desktop\chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
options = Options()
options.headless = True
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
#multiprocessing.set_start_method('spawn')
def  threadfile(file):
    #lock.acquire()
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
                data=driver.find_element_by_id('city').get_attribute('innerHTML')
            except:
                pass
            with open(filename,'w',encoding='utf-8') as f:
                f.write(data)
    #os.chdir(topicList)
    #lock.release()
threads=[]
if __name__ == '__main__':
    while Files:
        #thread=threading.Thread(target=threadfile,args=(file,lock))
        thread1= multiprocessing.Process(target=threadfile,args=(Files.pop(),))
        thread2= multiprocessing.Process(target=threadfile,args=(Files.pop(),))
        thread3= multiprocessing.Process(target=threadfile,args=(Files.pop(),))
        thread4= multiprocessing.Process(target=threadfile,args=(Files.pop(),))
        thread1.start()
        thread2.start()
        thread3.start()
        thread4.start()
        thread1.join()
        thread2.join()
        thread3.join()
        thread4.join()


