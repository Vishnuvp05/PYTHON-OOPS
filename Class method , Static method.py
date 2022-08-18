#when an object is passed as an first argument then it is instance method 

#when class name is passed as a first argument then it is called as a class method 

#niether class name nor object passed as a first argument then it is called as static method

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
             
        def pay_bag(self , amount):
             self.bag =self.bag + amount
            
        @classmethod
        def change_bag(cls , amount):
            cls.bag=amount
         
        @classmethod
        def cust_data(cls , data):  
           name ,biscuit ,bread , chocolate ,soap = data.split(",")
           return cls(name , biscuit , bread , chocolate , soap )
       
        @staticmethod
        def stocks(stk):
            available_stk = ['foods', 'drinks']
            if stk in available_stk:
                return True
            return False
        
cust1 = Supermarket('vishnu',2 , 2 ,4 , 7)
cust2 = Supermarket('prasath',4 , 3 , 4 , 5)

data = 'vimal , 7 , 8 , 9 ,7 '
cust3 =Supermarket.cust_data(data)
Supermarket.change_bag(20)

cust1.pay_bag(100)
cust2.pay_bag(120)
print(cust1.bag)
print(cust2.bag)
print(cust3.bag)
print(Supermarket.no_of_cust)
print(cust1.stocks('foods'))