"""
This is just for testing
how much faster it is to use hashing
instead of just a list 
"""

import time

class List:
    def __init__(self):
        self.list=[]

    def insert(self,data):
        self.list.append(data)

    def search(self,data):
        for i in range(0,len(self.list)):
            if self.list[i]==data:
                return bool(True)
        return bool(False)

if __name__ == "__main__":
    start_time=time.time()
    table = List()
    end_time=time.time()

    start_time1=time.time()
    file=open("Harkkatyö\words_alpha.txt","r",encoding="utf-8")
    
    l=file.readline()
    l=l.strip("\n")

    while l!="":
        l=file.readline()
        l=l.strip("\n")
        if l!="":
            table.insert(str(l))
    file.close()
    end_time1=time.time()

    start_time2=time.time()
    file2=open("Harkkatyö\kaikkisanat.txt","r",encoding="utf-8")
    sum=0
    
    l2=file2.readline()
    l2=l2.strip("\n")

    while l2!="":
        l2=file2.readline()
        l2=l2.strip("\n")
        if table.search(str(l2))==True:
            sum+=1
    file2.close()
    end_time2=time.time()
    print("Common words:", sum)
    print("Initializing the hash table:", round(end_time-start_time,3),"seconds")
    print("Adding the words:", round(end_time1-start_time1,3),"seconds")
    print("Finding the common words:", round((end_time2-start_time2)/60,3),"minutes")