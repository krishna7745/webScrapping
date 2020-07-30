import os
import requests
from bs4 import BeautifulSoup
import multiprocessing
topicList=r'C:\Users\User\Desktop\topicList'
print(os.chdir(topicList))
print(os.getcwd())
Files=os.listdir()
parentdir=r'C:\Users\User\Desktop\contentHtml'
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
            page=requests.get(r'https://www.javatpoint.com/cpp-data-types')
            try:
                soup=BeautifulSoup(page.content,'html.parser')
                div=soup.find_all('div',id='city')
            except:
                pass
            with open(filename,'w',encoding='utf-8') as f:
                f.write(str(div[0]))
    #os.chdir(topicList)
    #lock.release()
threads=[]
if __name__ == '__main__':
    while Files:
        #thread=threading.Thread(target=threadfile,args=(file,lock))
        thread= multiprocessing.Process(target=threadfile,args=(Files.pop(),))
        threads.append(thread)
        thread.start()
        # thread2.start()
        # thread3.start()
        # thread4.start()
        # thread1.join()
        # thread2.join()
        # thread3.join()
        # thread4.join()


