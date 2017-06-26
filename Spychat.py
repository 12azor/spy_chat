spy_detail={"an":{"salutation":"Mr","age":20,"rating":8,"friends":[],"status":""}}
spy_status_history={"an":[]}
status=["Available","Sleeping","Busy","Living The Moment"]
while True:
    while True:
        spy_name=raw_input("Login:\nEnter your spy name: ")
        if spy_name in spy_detail.keys():
            print "Welcome %s %s!" %(spy_detail[spy_name]["salutation"],spy_name)
            menu=int(raw_input("Menu:\n1. Add Status \n2. Add A Friend \n3. Send An Encoded Message \n4. Read Message \n5. Read Pevious History\nEnter from 1,2,3,4,5: "))
            loop=0
            if menu==1:
                if spy_detail[spy_name]["status"]== "":
                    print "\nYou do not have any previous status.\n"
                    loop=1
                if loop==0:
                    print "\nYou already have a status.\n"
                choice=int(raw_input("Status options. Would you like to:\n1. Choose from pre-defined list of status\n2. Choose from your status history\n3. Create new status\nPress 1 or 2 or 3: "))
                if choice==1:
                    length=len(status)
                    for i in range(0,length):
                        print "%s. "%(i+1)+status[i]
                    status_1=int(raw_input("Enter the number corresponding to status you want to choose: "))
                    spy_detail[spy_name]["status"]=status[status_1-1]
                    print "\nStatus uploaded successfully\n"
                    spy_status_history[spy_name].append(status[status_1-1])
                elif choice==2:
                    length=len(spy_status_history[spy_name])
                    if length==0:
                        print "\nYou have no previous status.\n"
                        continue
                    else:
                        for i in range(0,length):
                            print "%s. "%(i+1)+spy_status_history[spyname][i]
                        status_1=raw_input("Enter the number corresponding to status you want to choose: ")   
                        spy_detail[spy_name]["status"]=spy_status_history[spyname]["status"][status_1-1]
                        print "\nStatus uploaded successfully\n"
                elif choice==3:
                    status_1=raw_input("Enter your new status: ")
                    spy_detail[spy_name]["status"]=status_1
                    print "\nStatus uploaded successfully\n"
                    spy_status_history[spy_name].append(status_1)
                else:
                    print "\nWrong input, Try again"
                    continue
            elif menu==2:
                f_name=raw_input("Enter your friend's name: ")
                if len(f_name)==0:
                    print "Name cannot be empty. Try again.\n"
                    break
                f_age=int(raw_input("Enter your friend's age: "))
                if f_age<12 or f_age>50:
                    print "Sorry cannot add friend. Cannot authenticate the age.\n"
                    break
                f_rating=float(raw_input("Enter your friend's rating: "))
                if f_rating<spy_detail[spy_name]["rating"]:
                    print "Sorry cannot add friend. Rating not more than yours.\n"
                    break
                spy_detail[spy_name]["friends"].append(f_name)
                print "Friend has been added successfully.\n"
            elif menu==3:
                leng=len(spy_detail[spy_name]["friends"])
                if leng==0:
                    print "You have no friends added. \n"
                    continue
                else:
                    print "You have following people in your friend list: \n"
                    for i in range(0,leng):
                        print str(i+1)+". "+str(spy_detail[spy_name]["friends"][i])
                    position=int(raw_input("Enter the number corresponding to your choice of friend: "))
                    position=position-1
                    if (position<0 or position>=leng):
                        print "You hav entered a wrong input\nTry again.\n"
                        break
                    else:
                        print "The position of the friend in the list is: %i" %(position)
                    
                
        else:
            if len(spy_name)<1:
                print "\nYour name is invalid. Try again.\n"
                continue
            else:
                sal=int(raw_input("What is your salutaion?\n1. Mr\n2. Ms\nEnter 1 or 2: "))
                if sal==1:
                    salutation="Mr"
                elif sal==2:
                    salutation="Ms"
                else:
                    print "Wrong Input.\n"
                    continue
                age=int(raw_input("What is your age %s %s?\n" %(salutation, spy_name)))
                if age>=12 and age<=50:
                    rating=float(raw_input("What is your rating?\n"))
                    spy_detail.update({spy_name:{"salutation":salutation,"age":age,"rating":rating,"friends":[],"status":""}})
                    spy_status_history.update({spy_name:[]})           
                    continue
                else:
                    print "Sorry, we can't authenticate your age.....try again"        
    answer = raw_input('Do you want to run the program again? (y/n): ')
    if answer == "y":
        continue
    else:
        print "The program will exit now. Goodbye!!!"
        break
exit()
