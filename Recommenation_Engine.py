import numpy as np
import scipy.stats as sc

w= 944;
matrix = np.zeros((944,1983)) #Numpy matrix of zeros for placing the rating of every user  
pr = np.zeros((944,1983))
rating,user,item = 0,0,0
user1,item2 = 0,0
mean = [0 for s in range(w)] 
    #for opening the file and reading data from it
f=open('train_all_txt.txt',"r")
lines= f.readlines()
pr1= 0
for x in lines:
    user = int(x.split(' ')[0])  #Spliting the every line into 3 different catagories user,item and rating 
    item = int(x.split(' ')[1])
    rating = int(x.split(' ')[2])
    matrix[user-1][item-1] = rating 
f.close()    

user1 = len(range(943))
item2 = len(range(1682))    

    #For calculating mean of the given user rating per item
for e in range(user1):
    sum,rate = 0,0
    for f in range(item2):
        if(matrix[e][f] > 0):
            sum += matrix[e][f]
            rate += 1
            
    if(rate>0):
        mean[e] = sum/rate
     #For Calculating pearson similarity    
for y in range(user1):
    for z in range(user1):
        a = matrix[y]
        b = matrix[z]
        pr[y][z] = sc.pearsonr(a,b)[0]
    if(pr>0).all:
        pr[:,::-1].sort()
#file = open('output.txt','w') 
    #Calculation of predicted values 
for c in range(user1):
    for d in range(item2):
        if(matrix[c][d] == 0):
            sum1,avg,predict = 0,0,0
            for i in range(user1):
                if((matrix[i][d] != 0) & (c!= i)):
                    sum1+= (matrix[i][d]-mean[i])*pr[c][i]     
                    avg += pr[c][i]
                    #print(den)
            if((avg!=0)):
                predict = (mean[c]+(sum1/avg))
                matrix[c][d] = int(np.round(predict))
        
        #cold start problem allocating 1's for ratings less then 0 and 5 for more 5 evaluations
            
            if(matrix[c][d]<=0):
                matrix[c][d] = 1
            if(matrix[c][d] > 5):
                matrix[c][d] = 5
        s = c+1
        t = d+1
        print(s,t,'%d'%matrix[c][d])    
        """file.write('%d' % s)
        file.write(' %d' % t)
        file.write(' %d\n' % matrix[c][d])
        file.close()"""
