class stack:
    def __init__(self):
        self.items=[]
    def isempty(self):
        return self.items==[]
    def push(self,item):
        self.items.append(item)
        print(item)
    def pop(self):
        return self.items.pop()
    def display(self):
        return self.items
s=stack()
while(True):
    ch=int(input("enter your choice"))
    if ch==1:
        item=int(input("enter the item"))
        s.push(item)
    elif ch==2:
        print("the deleted item:",s.pop())
    elif ch==3:
        s.isempty()
    elif ch==4:
        s.display()
    else:
        break
    
        
    
