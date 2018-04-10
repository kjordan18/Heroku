import csv
import os

# creating path to open csv file
csvpath = os.path.join('budget_data_1.csv')

#defining variables and creating empty lists
columnsum = 0
date = []
revenue = []
diff = []
loop = 1

# print statements into terminal
print('Financial Analysis')
print('_________________________')
#creating a path for the new text file
with open(csvpath, newline='') as f:
    with open('output1.txt', 'w') as text_file:  
        text_file.write("Financial Analysis\n" +"_________________________\n" )
        
        #skip headers row

        next(f)
        counter=csv.reader(f,delimiter=",")

        # calculating total months
        totalmonths = str(len(list(counter)))

        #print total months into terminal
        print( "Total Months: " + totalmonths)

        #write total months into text file
        text_file.write("Total Months : " + totalmonths + "\n")
        f.seek(0)

        #initial values for total revenue calculations (skip headers)
        next(f)
        total = 0
        #loop through data
        for row in counter:
            #calculate total revenue
            total+=int(row[1])
        money=float(total)
        amountindollars = '${:,.2f}'.format(money)
        #print total revenue into terminal
        print("Total revenue: " + amountindollars)
        #write total revenue into text file
        text_file.write("Total Revenue : " + amountindollars + "\n")
        f.seek(0)
        
        #get date
        next(f)
        for row in counter:
            date.append(row[0])
        f.seek(0)
        
        #get revenue
        next(f)
        L=csv.reader(f,delimiter=",")
        # loop through data to get revenue change
        for row in L:
            #add revenue values to empty list
            revenue.append(row[1])
            # create variable to store previous revenue
            zerorow = int(revenue[0])
        #add previous revenue to empty list
        diff.append(int(zerorow))
        # while loop for finding average change of revenue         
        while (int(totalmonths)-loop)>0:
            diff.append(int(revenue[loop])-int(revenue[loop-1]))
            loop=loop+1
        #finding greatest increase and decrease in revenue
        minvalue = min(diff)
        maxvalue = max(diff)
        #finding corresponding dates
        maxdate = diff.index(maxvalue)
        mindate = diff.index(minvalue)
        #calculating average change
        averagechange=sum(diff)/int(totalmonths)
        #format values
        formataverage = str('${:,.2f}'.format(averagechange))
        printmaxval = str('${:,.2f}'.format(maxvalue))
        printminval = str('${:,.2f}'.format(minvalue))
        
        # print statements to terminal
        print("Average Change : " + formataverage)
        print("Greatest Increase in Revenue : " + str(date[maxdate]) + " " + printmaxval)
        print("Greatest Decrease in Revenue : " + str(date[mindate]) + " " + printminval)

        #write change values into text file
        text_file.write("Average Change : " + formataverage +"\n")
        text_file.write("Greatest Increase in Revenue : " + str(date[maxdate]) + " "+ printmaxval +"\n")
        text_file.write("Greatest Decrease in Revenue : " + str(date[mindate]) + " " + printminval + "\n")

#defining variables and creating empty lists for second data set
columnsum = 0
date1 = []
revenue1 = []
diff1 = []
loop1 = 1        

csvpath2 = os.path.join('budget_data_2.csv')
print('Financial Analysis')
print('_________________________')
with open(csvpath2, newline='') as f:
    with open('output2.txt', 'w') as text_file:  
        text_file.write("Financial Analysis\n" +"_________________________\n" )
        
        next(f)
        counter=csv.reader(f,delimiter=",")
        totalmonths = str(len(list(counter)))
        print( "Total Months: " + totalmonths)
        text_file.write("Total Months : " + totalmonths + "\n")
        f.seek(0)

        next(f)
        total = 0
        for row in counter:
            total+=int(row[1])
        money=float(total)
        amountindollars = '${:,.2f}'.format(money)
        print("Total revenue: " +amountindollars)
        text_file.write("Total Revenue : " + amountindollars + "\n")
        f.seek(0)
        
        #get date
        next(f)
        for row in counter:
            date1.append(row[0])
        f.seek(0)
        
        #get revenue
        next(f)
        L=csv.reader(f,delimiter=",")
        for row in L:
            revenue1.append(row[1])
            zerorow = int(revenue1[0])
        diff1.append(int(zerorow))         
        while (int(totalmonths)-loop1)>0:
            diff1.append(int(revenue1[loop1])-int(revenue1[loop1-1]))
            loop1=loop1+1
        minvalue = min(diff1)
        maxvalue = max(diff1)
        maxdate = diff1.index(maxvalue)
        mindate = diff1.index(minvalue)
        averagechange=sum(diff1)/int(totalmonths)
        formataverage = str('${:,.2f}'.format(averagechange))
        printmaxval = str('${:,.2f}'.format(maxvalue))
        printminval = str('${:,.2f}'.format(minvalue))
        
        print("Average Change : " + formataverage)
        print("Greatest Increase in Revenue : " + str(date1[maxdate]) + " " + printmaxval)
        print("Greatest Decrease in Revenue : " + str(date1[mindate]) + " " + printminval)

        text_file.write("Average Change : " + formataverage +"\n")
        text_file.write("Greatest Increase in Revenue : " + str(date1[maxdate]) + " "+ printmaxval +"\n")
        text_file.write("Greatest Decrease in Revenue : " + str(date1[mindate]) + " " + printminval + "\n")