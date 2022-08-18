

#PYTHON-OOPS 

#class - blueprint of template ,it occupies a memory space only when an object is created 

#class consists collection of methods and attributes , when a variable is used in class it is called as an attribute

#when a function is created in class it is called as method 

#creating a program code for a supermarket to calculate total cost of a thinga that a customer bought 


class Supermarket:   

    bag=10     
    no_of_cust = 0
    def __init__(self, name ,biscuit , bread , chocolate , soap):   #init is a special method used to reduce no of codes 
         self.name = name    #self is used to point current object and to hold objec
         self.biscuit = 8 * biscuit
         self.bread = 9 * bread
         self.chocolate = 10 * chocolate
         self.soap = 11 * soap
         Supermarket.no_of_cust=Supermarket.no_of_cust+1    

    def items(self):   # class method
        list = f'''customer Name : {self.name}\n Biscuit: {self.biscuit}rs\n Bread : {self.bread}rs
 Chocolate : {self.chocolate}rs\n soap : {self.soap}rs\n'''
        return list

    def pay_bag(self , amount):
        self.bag =self.bag + amount
        
cust1 = Supermarket('vishnu',2 , 2 ,4 , 7)
cust2 = Supermarket('prasath',4 , 3 , 4 , 5)


cust1.pay_bag(100)
cust2.pay_bag(120)
print(cust1.bag)
print(cust2.bag)
print(Supermarket.no_of_cust)

#Instance variables are owned by instances of class . This ,means tha for each subject instance variable is unique 
#Class variable - if the value of the variable is not varied from object to object 
