class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class doublylinkedlist:
    def __init__(self):
        self.first=None
    def insert(self,data):
        temp=node(data)
        if(self.first==None):
            self.first=temp
            self.first.next=temp
        else:
            cur=self.first
            while(cur.next!=self.first):
                cur=cur.next
            cur.next=temp
            temp.next=self.first
    def delete(self):
        if(self.first==None):
            print("list is empty")
            return
        else:
            cur=self.first
            self.first=self.first.next
            print("the deleted item:",cur.data)
            
    def display(self):
        if(self.first==None):
            print("list is empty")
            return
        cur=self.first
        while(cur!=None):
            print(cur.data,end=" ")
            cur=cur.next
    def search(self,item):
        if(self.first==None):
            print("list is empty")
            return
        cur=self.first
        while(cur!=None):
            if(cur.data==item):
                print("item found")
                return
            else:
                cur=cur.next
        print("item not found")
dll=doublylinkedlist()
while(True):
    ch=int(input("\nenter the choice 1-insert 2-delete 3-display 4-search"))
    if(ch==1):
        item=int(input("enter the data"))
        dll.insert(item)
        dll.display()
    elif(ch==2):
        dll.delete()
        dll.display()
    elif(ch==3):
        dll.display()
    elif(ch==4):
        item=int(input("enter the item"))
        dll.search(item)
        dll.display()
    else:
        break
