import time

class Node:
    def __init__(self, embryo, next):   # Class for linked list
        self.embryo = embryo
        self.next = next

    def getEmbryo(self):        # Methods to return and set 
        return self.embryo

    def getNext(self):
        return self.next

    def setEmbryo(self,newEmbryo):
        self.embryo=newEmbryo

    def setNext(self,newEmbryo):
        self.next=newEmbryo  


class HashLinear:
    def __init__(self,M):
        self.M = M      
        self.T = [Node(None,None) for i in range(0,M)]  # Making the Hash table 

    def insert(self, data):
        sum=0
        #for i in range(0,len(data)):
            #sum+=ord(data[i])     # First version of hashing
        #slot=(sum%self.M)      # Counting the slot where we put the data
        slot=HashLinear.hashing(self.M,data)
        current=self.T[slot]

        if current.getEmbryo()==None:   # If the data is the first one in this position
            current.setEmbryo(data)
            return

        while current.getNext()!=None:  # Finding a open position in the linked list
            current=current.getNext()
        current.setNext(Node(data,None))


    def delete(self, data):
        sum=0
        #for i in range(0,len(data)):    # Counting the slot where we try to find the data to be deleted
        #    sum+=ord(data[i])  # First version of hashing
        #slot=(sum%self.M)
        slot=HashLinear.hashing(self.M,data)
        current=self.T[slot]

        if current.getEmbryo()==data:
            self.T[slot]=current.getNext()  # If there is only one item in the linked list
            return


        while current.getNext()!=None:
            if current.getNext().getEmbryo()==data:    # If the next item is the wanted data
                current2=current.getNext()             # Find the route that where we change the deleted route
                if current2.getNext()!=None:           # If we have None after the data we set the next one to be None
                    if current2.getNext().getNext()!=None:
                        current.setNext(Node(current2.getNext().getEmbryo(),current2.getNext().getNext().getEmbryo()))
                        # If there is another item after the data's next one we want the route to go that way also
                        break
                    else:
                        current.setNext(Node(current2.getNext().getEmbryo(),current2.getNext().getNext()))
                        # If there isn't another item after the data's next one we want the route to end there
                        break
                else:
                    current.setNext(Node(current2.getNext(),None))
                    break
            current=current.getNext()

        
    def print(self):
        for i in range(0,self.M):
            current=self.T[i]       # Current changes so we can go through all the hash table
            if current!=None:
                help=0
                while current.getNext()!=None:  # The while-loop goes through all the linked list
                    if current.getEmbryo()!=None:
                        output=current.getEmbryo()  # Print items
                        print(output, end=" ")
                    current=current.getNext()
                    help+=1
                if current.getEmbryo()!=None:       # Here we print the last item in the linked list if it isn't None
                    print(current.getEmbryo(), end="|")
                elif help!=0:
                    print(end="|")
        print()

    def search(self,data):
        sum=0
        #for i in range(0,len(data)):    # Counting the slot where we try to find the data
            #sum+=ord(data[i])          # First version of hashing
        slot=HashLinear.hashing(self.M,data)
        #slot=(sum%self.M)
        current=self.T[slot]

        while current.getNext()!=None:
            if current.getEmbryo()==data:   # Return True if we find it, else we return False
                return bool(True)
            current=current.getNext()

        if current.getEmbryo()==data:   # We check the last item in the linked list 
            return bool(True)
            
        return bool(False)


    def hashing(n,data): # Making an improvement to hashing by using polynomial hashing
        sum=0
        for i in range(0,len(data)):
            sum+=ord(data[i])*(11111**(len(data)-i-1))  # Multiply by 11111^(len(data)-i-1) to avoid collisions
        slot=sum%n
        
        return slot


if __name__ == "__main__":
    start_time=time.time()
    table = HashLinear(10000)
    end_time=time.time()

    start_time1=time.time()
    file=open("Practical-Assignment\words_alpha.txt","r",encoding="utf-8")
    
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
    file2=open("Practical-Assignment\kaikkisanat.txt","r",encoding="utf-8")
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
    print("Finding the common words:", round(end_time2-start_time2,3),"seconds")