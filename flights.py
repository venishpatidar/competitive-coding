import collections
import itertools
import numpy as np
cities=4
arr = np.zeros((5,5))
arr[1][2] = 10
arr[2][1] = 10
arr[3][1] = 24
arr[1][3] = 24
arr[2][3] = 2
arr[3][2] = 2
arr[2][4] = 15
arr[4][2] = 15
arr[4][3] = 7
arr[3][4] = 7
final = []

#search = np.amin(arr[start])
#nextpos = np.where(arr[start] == search)
#start = int(nextpos[0])
 

class fl:
    def __init__(self,home,dest,fix):
        fix[:,home] = 0
        self.ho = home 
        self.array = fix
        self.des = dest
        self.toreturn = []
        #self.routes = np.where(fix!=0) 
       # self.a = collections.Counter(self.routes[0])
        #self.count = 0
        

    def flights(self,home,dest,prev=0):
        routes = np.where(self.array!=0) 
        self.a = collections.Counter(routes[0])
        self.start = routes[0]
        self.end = routes[1]
        ref = np.where(self.start==home)
        #print  self.end ,self.ref[0],"\n"
        #print (len(ref[0]), self.a[home])
        x = 0
        while x<(self.a[home]):
            #print home,"aa",x,"p",prev,ref[0]
            try:
                
                if(self.end[ref[0][x]]==dest):
                    self.toreturn.append(str(str(home)+str(self.end[ref[0][x]])))
                    #print home,"->",self.end[ref[0][x]]
                    
                else:
                    
                    if(self.end[ref[0][x]]==prev):
                        raise Exception("a")
                    #print home,"->",self.end[ref[0][x]]
                    self.toreturn.append(str(str(home)+str(self.end[ref[0][x]])))
                    self.flights(self.end[ref[0][x]],dest,home)
                x+=1 
            except Exception as e:
                #print e
                x+=1
    def getall(self):
        return self.toreturn
    
    def flightroutes(self):
        routes = np.unique(self.toreturn)
        s = []
        e = []
        ref = []
        index = 0
        for x in routes:
            s.append(int(x[0]))
            e.append(int(x[1]))
            
            if(int(x[0])==self.ho):
                ref.append(index)
            index+=1
        all_possible_way = [] 
        allcombs = []
        for x in range(len(routes)):
            allcombs.append(list(itertools.permutations(routes,x))) 
        i = 0
        seperator = ''
        for x in allcombs:
            for y in x:
                all_possible_way.append(seperator.join(y))
        way = []
        self.to_calc = []
        all_possible_way.remove("")
        for x in all_possible_way:
            if(int(x[0])==self.ho and int(x[len(x)-1])==self.des):
                way.append(x)
        for x in way:
            temp = []
            temp2 = []
            check = 0

            for y in x:
                temp.append(y)
            i = 1
            while i < (len(temp)-1):
                if (temp[i]==temp[i+1]):
                    check+=1
                i+=2

            if (len(temp)==2):
                self.to_calc.append(temp)
            elif(check == (len(temp)-2)/2):
                self.to_calc.append(temp)
            
            


        #print s.join(allcombs[2][4])
        #print routes
        #print way
    def cheapestprice(self):
        prices = []
        for x in self.to_calc:
            i = 0
            to_add = []
            while i < len(x):
                to_add.append(self.array[int(x[i])][int(x[i+1])])
                i+=2
            prices.append(np.sum(to_add))
        print prices
        return int(np.amin(prices))

num_of_cities = []

for x in range(1,cities+1):
    num_of_cities.append(x)

all_pairs = np.array(list(itertools.combinations(num_of_cities,2)))
all_cheap_price = []
ii = 1
 
for x in all_pairs:
    print x[0],x[1]
    print arr
    a = fl(int(x[0]),int(x[1]),arr)
    a.flights(int(x[0]),int(x[1]))
    a.flightroutes()
    all_cheap_price.append(a.cheapestprice())
    ii+=1

