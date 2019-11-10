 
lst=[]
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
      
	  
	  
		


def p_leave(root):
    if(root):
        p_leave(root.left)
        if root.left is None and root.right is None:
            print(root.data)
            lst.append(root.data)
        p_leave(root.right)
	
		 
		
           
		    

		 

 
def boundLeft(root):
    if(root):
        if (root.left):
            print(root.data)
            lst.append(root.data)
            boundLeft(root.left)
        elif(root.right):
            print (root.data)
            lst.append(root.data)
            boundLeft(root.right)
	
	 
		 
			
			 
			 
			 
		
		 
			 
			 
		
		


 
def right(root):
    if(root):
        if (root.right):
            right(root.right)
            print(root.data)
            lst.append(root.data)
        elif(root.left):
            right(root.left)
            print(root.data)
            lst.append(root.data)
	
	 
		 

			 
			 
		
		 
			 
			 




def bound(root):
    if (root):
        print(root.data)
        lst.append(root.data)
        boundLeft(root.left)
        p_leave(root.left)
        p_leave(root.right)
        right(root.right)
        print(root.data)
        lst.append(root.data)
        
    
         
         		
         
        
        
        



root = Node(40) 
root.left = Node(20)
root.right = Node(60)
root.right.right = Node(70)
root.right.left = Node(50)
root.right.left.right = Node(55)
root.left.left = Node(10) 
root.left.right = Node(30)
root.left.left.right = Node(5)
root.left.left.right.right = Node(45)
 
bound(root) 
print("\n")
print('Total amount',sum(lst))

