spy_detail={}
spy_status_history={}
status=["Available","Sleeping","Busy","Living The Moment"]
special_words=["SOS","save_me","help_me","help","save"]

def add_a_status(spy_name):
    loop=0
    if spy_detail[spy_name]["status"]== "":
        print "\nYou do not have any previous status.\n"
        loop=1
    if loop==0:
        print "\nYou already have a status. Your status is : "+str(spy_detail[spy_name]["status"])
    choice=int(raw_input("\nStatus options. Would you like to:\n1. Choose from pre-defined list of status\n2. Choose from your status history\n3. Create new status\nPress 1 or 2 or 3: "))
    if choice==1:
        length=len(status)
        for i in range(0,length):
            print "%s. "%(i+1)+status[i]
        status_1=int(raw_input("Enter the number corresponding to status you want to choose: "))
        spy_detail[spy_name]["status"]=status[status_1-1]
        if spy_detail[spy_name]["status"] not in spy_status_history[spy_name]:
            spy_status_history[spy_name].append(spy_detail[spy_name]["status"])
        print "\nStatus uploaded successfully"
        print "Your status is : "+str(spy_detail[spy_name]["status"])
    elif choice==2:
        length=len(spy_status_history[spy_name])
        if length==0:
            print "\nYou have no previous status.\n"
        else:
            for i in range(0,length):
                print "%s. "%(i+1)+spy_status_history[spy_name][i]
            status_1=int(raw_input("Enter the number corresponding to status you want to choose: "))
            spy_detail[spy_name]["status"]=spy_status_history[spy_name][status_1-1]
            print "\nStatus uploaded successfully"
            print "Your status is : "+str(spy_detail[spy_name]["status"])
    elif choice==3:
        status_1=raw_input("Enter your new status: ")
        spy_detail[spy_name]["status"]=status_1
        print "\nStatus uploaded successfully"
        print "Your status is : "+str(spy_detail[spy_name]["status"])
        spy_status_history[spy_name].append(status_1)
        if spy_detail[spy_name]["status"] not in spy_status_history[spy_name]:
            spy_status_history[spy_name].append(spy_detail[spy_name]["status"])
    else:
        print "\nWrong input, Try again"
    return()
    
def add_friend(spy_name):
    f_name=raw_input("Enter your friend's name: ")
    if len(f_name)==0:
        print "Name cannot be empty. Try again.\n"
        return(0)
    f_age=int(raw_input("Enter your friend's age: "))
    if f_age<12 or f_age>50:
        print "Sorry cannot add friend. Cannot authenticate the age.\n"
        return(0)
    f_rating=float(raw_input("Enter your friend's rating: "))
    if f_rating<spy_detail[spy_name]["rating"]:
        print "Sorry cannot add friend. Rating not more than yours.\n"
        return(0)
    spy_detail[spy_name]["friends"].update({f_name:{"f_age":f_age,"f_rating":f_rating,"chat":{}}})
    print "\nFriend has been added successfully.\n Details of the recently added friend:\n%s \n"%(f_name)+str(spy_detail[spy_name]["friends"][f_name])
    return(len(spy_detail[spy_name]["friends"].keys()))
    
def select_a_friend(spy_name):
    leng=len(spy_detail[spy_name]["friends"])
    if leng==0:
        print "You have no friends added. \n"
        return("null")
    else:
        print "You have following people in your friend list: \n"
        for i in range(0,leng):
            print str(i+1)+". "+str(spy_detail[spy_name]["friends"].keys()[i])
        position=int(raw_input("Enter the number corresponding to your choice of friend to whom you want to communication with: "))
        position=position-1
        if (position<0 or position>=leng):
            print "You have entered a wrong input\nTry again.\n"
        else:
            return(position)
def send_a_message(spy_name):
    position=select_a_friend(spy_name)
    f_name=spy_detail[spy_name]["friends"].keys()[position]
    from steganography.steganography import Steganography
    i_path = "C:\Users\ASUS\Desktop\Acadview\\"
    i_img_name=raw_input("What is the image name(Type along with the extension)?: ")
    path=i_path+i_img_name
    print "your path with specified image name is: "+path
    o_img_name=raw_input("What name should be the output file?(Type along with extension): ")
    o_path = "C:\Users\ASUS\Desktop\Acadview\\"
    output_path=o_path+o_img_name
    text =raw_input("Enter the TEXT you want to encode: ")
    from datetime import datetime
    date=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    spy_detail[spy_name]["friends"][f_name]["chat"].update({"communication":"sent","text":text, "time":date,"boolean":True})
    print "please wait..................................."
    s=text.strip().split(" ")		
    Steganography.encode(path, output_path, text)
    print "\nMessage has been encoded and sent to %s.\n" %(str(spy_detail[spy_name]["friends"].keys()[position]))
    for i in range(len(s)):
        for j in range(len(special_words)):
            if special_words[j]==s[i]:
                print "Your message was an emergency message.\n"
                return()
def read_a_message(spy_name):
    position= select_a_friend(spy_name)
    from steganography.steganography import Steganography
    f_name=spy_detail[spy_name]["friends"].keys()[position]
    print "Friend %s selected\n" %(f_name)
    o_img_name=raw_input("What is the name of the output file you want to decode?(Type along with extension): ")
    o_path = "C:\Users\ASUS\Desktop\Acadview\\"
    output_path=o_path+o_img_name
    from datetime import datetime
    date=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print "please wait...................................."
    secret_text = Steganography.decode(output_path)
    print "\nYour secret text is: "+secret_text
    spy_detail[spy_name]["friends"][f_name]["chat"].update({"communication":"received","text":secret_text, "time":date,"boolean":False})
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
                    friends_count=add_friend(spy_name)
                    print "You have %i friends as of now.\n" %(friends_count)
                elif menu==3:
                    send_a_message(spy_name)
                elif menu==4:
                     read_a_message(spy_name)
                elif menu==6:
                    print "The program will now Exit."
                    exit()
                else:
                    print "Wrong input. Try again"
                continue
exit()
