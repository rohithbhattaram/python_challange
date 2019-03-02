import os
import csv
count_mon=0
sum_pro_los=0
n = 0.0
p=0.0
found = False


              
csvpath = os.path.join('..','PyBank','budget_data.csv')

with open(csvpath,newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")
    #Skip Headers 
    next(csvreader, None)
   
    
    
    for row in csvreader:
        count_mon=count_mon+1
        sum_pro_los=sum_pro_los+ float(row[1])
        if float(row[1]) > float(n ) :
           n = row[1]
           myList_pro  = row
        if float(row[1]) < float(p ) :
           p = row[1]
           myList_loss = row

    
    print("Here is the Financial Analysis Over the Period of our Company : ")
    print("-----------------------------------------------------------------")
    print("Number of months included in sheet:" + str(count_mon))
    print("Sum of profit loss over the period:" + str(sum_pro_los))
    print("Average of Profit loss over period:"+ str(round(sum_pro_los/count_mon,2)))
    print("Greatest Increse in profits appered in  :"+ myList_pro[0] + " , profit of :"+ str(myList_pro[1]))
    print("Greatest Decrese in profits appered in  :"+ myList_loss[0] + " , loss of :"+ str(myList_loss[1]))
    print("-----------------------------------------------------------------")