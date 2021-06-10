

"""
Till Now implemented with 10 Drivers 10 customers
q1 : AVG DriverID => give the average rating points for the driver ID given

q2 : AVG CustomerID => give the average rating points for the customer ID given

q3 : TRIP CustomerID Rating DriverID Rating => Add the trip and rating points with customerID and driverID
"""


class Driver:
    def __init__(self):
        pass
    
    def defineDriver(self,D_id,name):
        self.D_name = name
        self.D_id = D_id
        self.avg_D_rating =0
        self.noOfRides =0

d = [0 for i in range(111)]
for i in range(11):
    d[i] = Driver()
    d[i].defineDriver(i,str("Driver"+chr(ord("A") +i)))
    d[i].avg_D_rating = (10+i)
    d[i].noOfRides=1

        
class Customer:
    def __init__(self):
        pass
    
    def defineCustomer(self,C_id,name):
        self.cus_name = name
        self.cus_id = C_id
        self.avg_C_rating =0
        self.noOfRides =0
        self.drivers=[]

c = [0 for i in range(111)]
for i in range(11):
    c[i] = Customer()
    c[i].defineCustomer(i,"Customer"+chr(ord("A") +i))
    c[i].avg_C_rating = (100+i)
    c[i].noOfRides= 1

print("Ratings before the Ride")
print(d[5].D_id , d[5].D_name, end="   :  ") 
print(d[5].avg_D_rating) 

print(c[5].cus_id , c[5].cus_name, end="   :  ") 
print(c[5].avg_C_rating)    
    
class TRIP_CustomerIDRating_DriverIDRating(Driver, Customer):
    def __init__(self):
        pass
    
    def enterRatings(self,id_D,ratingD,id_C,ratingC):
        print("id_D,ratingD,id_C,ratingC",id_D,ratingD,id_C,ratingC)
        print("d[id_D].avg_D_rating :",d[id_D].avg_D_rating)
        d[id_D].avg_D_rating = ( (d[id_D].avg_D_rating  * d[id_D].noOfRides) + ratingD) / (d[id_D].noOfRides+1)
        d[id_D].noOfRides += 1
        print("d[id_D].avg_D_rating :",d[id_D].avg_D_rating)
        
        #c[id_C].drivers.append() 
        c[id_C].avg_C_rating = ((c[id_C].avg_C_rating  * c[id_C].noOfRides) + ratingC) / (c[id_C].noOfRides+1 )
        c[id_C].noOfRides += 1        


obj_TRIP_CustomerIDRating_DriverIDRating = TRIP_CustomerIDRating_DriverIDRating()
obj_TRIP_CustomerIDRating_DriverIDRating.enterRatings(5,11,50,111)



print("Ratings after the Ride")
print(d[5].D_id ,d[5].D_name, end="   :  ") 
print(d[5].avg_D_rating) 

print(c[5].cus_id, c[5].cus_name, end="   :  ") 
print(c[5].avg_C_rating)



class Features(Driver, Customer):
    def __init__(self):
        pass
    
    def findTopCustomer(self,listOfAllCustomerObjects):
        listOfAllCustomerObjects.sort(key = lambda y:y.avg_C_rating)
        listOfAllCustomerObjects.reverse()
        for i in range(len(listOfAllCustomerObjects)):
            print(listOfAllCustomerObjects[i].cus_id, listOfAllCustomerObjects[i].cus_name,
                          listOfAllCustomerObjects[i].avg_C_rating)
            
    def findTopDriver(self,listOfAllDriverObjects):
        listOfAllDriverObjects.sort(key = lambda y:y.avg_D_rating)
        listOfAllDriverObjects.reverse()
        for i in range(len(listOfAllDriverObjects)):
            print(listOfAllDriverObjects[i].D_id, listOfAllDriverObjects[i].D_name,
                          listOfAllDriverObjects[i].avg_D_rating)
    """            
    def eligibleCustomerID(self,c,d,cus_id):
        #return D_id
        for i in range(len(d)):
            if d[i].avg_D_rating > c[cus_id].avg_C_rating :
                pass
    """    
        
f = Features()
f.findTopCustomer(c)

f.findTopDriver(d)

f.eligibleCustomerID(c,d,5)

      
list1=[[3,5],[5,8],[1,9],[2,8]]
list1.sort(key = lambda  y:y[0])        
print(list1)            
            
            
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    