spy_detail={}
spy_status_history={}
status=["Available","Sleeping","Busy","Living The Moment"]
def add_a_status(spy_name):
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
        return()
def add_friend(spy_name):
    f_name=raw_input("Enter your friend's name: ")
    if len(f_name)==0:
        print "Name cannot be empty. Try again.\n"
    f_age=int(raw_input("Enter your friend's age: "))
    if f_age<12 or f_age>50:
        print "Sorry cannot add friend. Cannot authenticate the age.\n"
    f_rating=float(raw_input("Enter your friend's rating: "))
    if f_rating<spy_detail[spy_name]["rating"]:
        print "Sorry cannot add friend. Rating not more than yours.\n"
    spy_detail[spy_name]["friends"].append(f_name)
    print "\nFriend has been added successfully.\n"
def send_message(spy_name):
    leng=len(spy_detail[spy_name]["friends"])
    if leng==0:
        print "You have no friends added. \n"
    else:
        print "You have following people in your friend list: \n"
        for i in range(0,leng):
            print str(i+1)+". "+str(spy_detail[spy_name]["friends"][i])
        position=int(raw_input("Enter the number corresponding to your choice of friend to whom you want to send the message: "))
        position=position-1
        if (position<0 or position>=leng):
            print "You hav entered a wrong input\nTry again.\n"
        else:
            print "The position of the friend in the list is: %i" %(position)
while True:
    while True:
        user_choice=int(raw_input("Do you want to continue using a:\n1. Default user.\n2. Create new user.\nEnter 1 or 2: "))
        if user_choice==1:
            import spy_details
            spy_name=spy_details.default_spy_detail.keys()[0]
            if spy_name in spy_detail.keys():
                print "Default user name already exists in the spy dictionary"
            else:
                spy_detail.update(spy_details.default_spy_detail)
                spy_status_history.update({spy_name:[]})
        elif user_choice==2:           
            spy_name=raw_input("Login:\nEnter your spy name: ")
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
                    if rating<0:
                        print "Rating cannot be negative."
                        break
                    elif rating>10:
                        print "Rating cannot be grater than 10."
                        break
                    else:
                        print "Rating has been accepted.\n"
                    spy_detail.update({spy_name:{"salutation":salutation,"age":age,"rating":rating,"friends":[],"status":""}})
                    spy_status_history.update({spy_name:[]})
                else:
                    print "Sorry, we can't authenticate your age.....try again"
        else:
            print "Wrong input. Try again\n"
            continue
        if spy_name in spy_detail.keys():
            print "\nWelcome %s %s!" %(spy_detail[spy_name]["salutation"],spy_name)
            print "Your age: %i" %(spy_detail[spy_name]["age"])+"\nYour Rating is: %.2f\n" %(spy_detail[spy_name]["rating"])
            while True:
                menu=int(raw_input("Menu:\n1. Add a status update\n2. Add a friend\n3. Send a secret message\n4. Read a secret message\n5. Read chats from a user\n6. Exit\nEnter from 1,2,3,4,5 or 6: "))
                loop=0
                if menu==1:
                    add_a_status(spy_name)                    
                elif menu==2:
                    add_friend(spy_name)                    
                elif menu==3:
                    send_message(spy_name)
                elif menu==6:
                    print "The program will now Exit."
                    exit()
                else:
                    print "Wrong input. Try again"
                continue
exit()
