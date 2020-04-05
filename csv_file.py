import csv
import random
import math 

with open('grocerystores.csv','r') as csvinput:
    with open('stores.csv', 'w') as csvoutput:
        writer = csv.writer(csvoutput, lineterminator='\n')
        reader = csv.reader(csvinput)

        userList = []
        benList = [] 

        for row in reader:
            userList.append(row)   

        #alter columns and time
        for row in range(len(userList)):
            #create time columns
            if row == 1:
                for i in range(9,22):
                    if i <= 11:
                        time1 = str(i) + " " + 'am'
                        userList[row].append(time1)
                    else:
                        time2 = str(i) + " " + 'pm'
                        userList[row].append(time2)
                    userList[row].append('safe/in between/unsafe')
            #randomly generate number of people
            elif row >= 2:
                #print(userList[row][9])
                for idx in range(8,34):
                    num_people = random.randint(2, 500)
                    userList[row].append(num_people)
                    #calculate safe/unsafe
                    if userList[1][idx] == "safe/in between/unsafe":
                        area = int(userList[row][idx-1]) * 6 * math.pi**2
                        #get rid of comma
                        store_area =  userList[row][7].replace(',', '')
                        space_left = float(store_area) - area
                        #unsafe 
                        if space_left <= 6*math.pi**2:
                            userList[row][idx] = 'unsafe'
                        #in between
                        elif space_left > 6*math.pi**2 and space_left <= 30*math.pi**2:
                            userList[row][idx] = 'in between'
                        #safe
                        else:
                            userList[row][idx] = 'safe'
        
        #add rows to new csv file 
        for rowidx in range(len(userList)):
            if rowidx != 0:
                writer.writerow(userList[rowidx])
           