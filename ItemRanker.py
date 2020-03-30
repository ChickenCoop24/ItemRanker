listtype = input("What type of Item are you listing? (Use the singular version ex: Instead of of Movies use Movie): ")
s ="s"
list1 =[]
print("Enter a series of 10 %ss in any order:" % listtype)
i = 1
done = False
while done == False:
    if i == 1:
        userinput = input("1st %s: Enter done to finish inputing: " % listtype)
        if userinput == "done" or userinput == "Done":
            done = True
        else:
            list1.append(userinput)
    elif i==2:
       userinput = input("2nd %s: Enter done to finish inputing: " % listtype)
       if userinput == "done" or userinput == "Done":
           done = True
       else:
           list1.append(userinput)
    elif i==3:
        userinput = input("3rd %s: Enter done to finish inputing: " % listtype)
        if userinput == "done" or userinput == "Done":
            done = True
        else:
            list1.append(userinput)
    else:
        userinput = input("%sst %s: Enter done to finish inputing: " % (i, listtype))
        if userinput == "done" or userinput == "Done":
            done = True
        else:
            list1.append(userinput)
    i+=1   
def sortlist():
    sortedlist = False
    while sortedlist == False:
        for x in range (0, len(list1)):
            item = list1[x]
            position = input("Position %s: What position should %s be in? Use an integer number " % (x+1, list1[x]))
            position = int(position)
            a = list1[position-1]
            list1[position-1] = item
            list1[x] = a
        for j in range(0, len(list1)):
            print("%s. %s" % (j+1, list1[j]))
        satisfied= input( 'Are you happy with your current list? (y/n) ')
        if satisfied == 'y' or satisfied == "Y":
            sortedlist = True
        else:
            continue
sortlist()
print("Here is your list:")
for a in range (0, len(list1)):
    print("%s. %s" % (a+1, list1[a]))
finished = False
while finished == False:
    finalsatisfied = input("Are you sure you are satisfied with your list? (y/n) ")
    if finalsatisfied == "y" or finalsatisfied == "Y":
        finished = True
    else:
        sortlist()
        continue
exportlist = input("Would you like to export your list to a text doc? (y/n) ")
if exportlist == "y" or exportlist == "Y":
    exportFile = open("RankedItems.txt", "a")
    listname = input("What would you like the title of the list to be? ")
    exportFile.write(listname + "\n")
    for w in range(0, len(list1)):
        exportFile.write("%s. %s \n" % (w+1, list1[w]))
    exportFile.write("\n")
    exportFile.close()
    print("List exported succesfully. List name is 'RankedItems.txt' ")
    print("Thank you for using my program")
    end = input("Press enter key to exit")
else:
    print("Thank you for using my program")
    end = input("Press enter key to exit")
    

            
        

