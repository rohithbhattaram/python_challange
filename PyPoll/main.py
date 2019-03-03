import os
import csv



can_one_votes = 0 
can_two_votes = 0 
can_thr_votes = 0 
can_fur_votes = 0 
can_otr_votes = 0 

nam_1 = " "
nam_2 = " "
nam_3 = " "
nam_4 = " "
Winner = " "


votes = 0
candidates = []

              
csvpath = os.path.join('..','PyPoll','election_data.csv')

with open(csvpath,newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")
    #Skip Headers 
    # next(csvreader, None)


    for row in csvreader : 
        votes = votes+1
        if row[2] not in candidates :
            candidates.append(row[2])
        if len(candidates) > 0 :
            # print(len(candidates))
            if row[2] == candidates[0] :
                can_one_votes = can_one_votes + 1
                nam_1 = candidates[0]
        if len(candidates) > 1 :
            # print(len(candidates))
            if row[2] == candidates[1] :
                can_two_votes = can_two_votes + 1
                nam_2 = candidates[1] 
        if len(candidates) > 2 :
            # print(len(candidates))
            if row[2] == candidates[2] :
                can_thr_votes = can_thr_votes + 1
                nam_3 = candidates[2] 
        if len(candidates) > 3 :
            # print("Candidate 4 name :"+ candidates[3])
            # print(len(candidates))
            if row[2] == candidates[3] :
                can_fur_votes = can_fur_votes + 1
                nam_4 = candidates[3] 
        if len(candidates) > 4 :
            # print(len(candidates))
            if row[2] == candidates[4] :
                can_otr_votes = can_otr_votes + 1
        if len(candidates) > 5 :
            if row[2] ==  candidates[5] :
                can_otr_votes = can_otr_votes + 1
        if len(candidates) > 6 :
            if row[2] ==  candidates[6] :
                can_otr_votes = can_otr_votes + 1

    print("Election Results :")
    print("---------------------------------------------------")
    print("Total polled Votes :" + str(votes) ) 
    print("----------------------------------------------------")
    print("Votes Polled for "+candidates[0] + "  are :"+ str(can_one_votes))
    print("Votes Polled for "+candidates[1] + "  are :"+ str(can_two_votes))  
    print("Votes Polled for "+candidates[2] + "  are :"+ str(can_thr_votes))  
    print("Votes Polled for "+candidates[3] + "  are :"+ str(can_fur_votes))  
    print("Votes Polled for others are :"+ str(can_otr_votes))
    print("----------------------------------------------------")
    print("Percent of Votes Polled :")

    print (candidates[0] + " = " + str(round((can_one_votes/votes)*100, 2)))
    print (candidates[1] + " = " + str(round((can_two_votes/votes)*100, 2)))
    print (candidates[2] + " = " + str(round((can_thr_votes/votes)*100, 2)))
    print (candidates[3] + " = " + str(round((can_fur_votes/votes)*100, 2)))
    print ("Others = " + str(round((can_otr_votes/votes)*100, 2)))
    print("----------------------------------------------------")
    

    output_path = os.path.join("..", "PyPoll", "Election_Results.csv")

     # Open the file using "write" mode. Specify the variable to hold the contents
    with open(output_path, 'w', newline='') as csvfile:
     # Initialize csv.writer
        csvwriter = csv.writer(csvfile)

    myVotes_list=[can_one_votes, can_two_votes, can_thr_votes, can_fur_votes, can_otr_votes]
    p = max(myVotes_list)
    if p == can_one_votes :
        print ("WINNER OF ELECTION IS :"+candidates[0])
        Winner = str(candidates[0])
    elif p == can_two_votes :
         print ("WINNER OF ELECTION IS :"+candidates[1])
         Winner = str(candidates[1])
    elif p == can_thr_votes :
         print ("WINNER OF ELECTION IS :"+candidates[2])
         Winner = str(candidates[2])
    elif p == can_fur_votes :
         print ("WINNER OF ELECTION IS :"+candidates[3])
         Winner = str(candidates[3])
    else : 
         print ("WINNER OF ELECTION IS :"+candidates[4])
         Winner = str("Others")
     
output_path = os.path.join("..", "PyPoll", "Election_Results.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

            # Initialize csv.writer
        csvwriter = csv.writer(csvfile)

         
        csvwriter.writerow(['Total Votes', str(votes)])
        csvwriter.writerow([ candidates[0] + " Scored Votes :", str(can_one_votes), candidates[0] + "  Percent of Votes :" ,str(round((can_one_votes/votes)*100, 2))  ])
        csvwriter.writerow([ candidates[1] + " Scored Votes :", str(can_two_votes),  candidates[1] + "  Percent of Votes :" ,str(round((can_two_votes/votes)*100, 2))  ])
        csvwriter.writerow([ candidates[2] + " Scored Votes :", str(can_thr_votes),  candidates[2] + "  Percent of Votes :" ,str(round((can_thr_votes/votes)*100, 2))  ])
        csvwriter.writerow([ candidates[3] + " Scored Votes :", str(can_fur_votes),  candidates[3] + "  Percent of Votes :" ,str(round((can_fur_votes/votes)*100, 2))  ])
        csvwriter.writerow([  " Others Scored Votes :", str(can_otr_votes),   " Others  Percent of Votes :" ,str(round((can_otr_votes/votes)*100, 2))  ])
        csvwriter.writerow(["Winner Of Election :", Winner ])

    
