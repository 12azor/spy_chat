spy_detail={}                                                       # Empty dictionary for spy details like name, rating, age, friends etc.
spy_status_history={}                                               # Empty dictionary for spy's status history.
status=["Available","Sleeping","Busy","Living The Moment"]          # Pre defined set of statuses
special_words=["SOS","save_me","help_me","HELP","SAVE","RESCUE"]    # Set of special words to check in encoded text the spy will send
count=0                                                     #used for the storage of chat in chat dictionary under spy_detail dictionary(implemented in program)

def add_a_status(spy_name):         #method to add a status
    loop=0                          #used to determine whether the spy has a current status or not
    if spy_detail[spy_name]["status"]== "":
        print "\nYou do not have any previous status.\n"
        loop=1
    if loop==0:
        print "\nYou already have a status. Your status is : "+str(spy_detail[spy_name]["status"])
    choice=int(raw_input("\nStatus options. Would you like to:\n1. Choose from pre-defined list of status\n2. Choose from your status history\n3. Create new status\nPress 1 or 2 or 3: "))
    if choice==1:                   #for pre-defined list of status
        length=len(status)
        for i in range(0,length):
            print "%s. "%(i+1)+status[i]
        status_1=int(raw_input("Enter the number corresponding to status you want to choose: "))
        spy_detail[spy_name]["status"]=status[status_1-1]                       #puts new status for the spy
        if spy_detail[spy_name]["status"] not in spy_status_history[spy_name]:  #checks for repititive statuses
            spy_status_history[spy_name].append(spy_detail[spy_name]["status"]) #appends the status to spy status history
        print "\nStatus uploaded successfully"
        print "Your status is : "+str(spy_detail[spy_name]["status"])
    elif choice==2:                                 #for status history
        length=len(spy_status_history[spy_name])    #checks if he has any previous status or not
        if length==0:
            print "\nYou have no previous status.\n"
        else:
            for i in range(0,length):
                print "%s. "%(i+1)+spy_status_history[spy_name][i]
            status_1=int(raw_input("Enter the number corresponding to status you want to choose: "))
            spy_detail[spy_name]["status"]=spy_status_history[spy_name][status_1-1] #puts new status for the spy
            print "\nStatus uploaded successfully"
            print "Your status is : "+str(spy_detail[spy_name]["status"])
    elif choice==3:                             #for new status
        status_1=raw_input("Enter your new status: ")
        spy_detail[spy_name]["status"]=status_1 #puts new status for the spy
        print "\nStatus uploaded successfully"
        print "Your status is : "+str(spy_detail[spy_name]["status"])
        spy_status_history[spy_name].append(status_1)
        if spy_detail[spy_name]["status"] not in spy_status_history[spy_name]:
            spy_status_history[spy_name].append(spy_detail[spy_name]["status"]) # appends the status to spy status history
    else:
        print "\nWrong input, Try again"
    return()
    
def add_friend(spy_name):           #method to add a friend
    f_name=raw_input("Enter your friend's name: ")
    if len(f_name)==0:              #checks if name is empty
        print "Name cannot be empty. Try again.\n"
        return(-1)
    f_age=int(raw_input("Enter your friend's age: "))
    if f_age<12 or f_age>50:        #checks if age is under the required constraints
        print "Sorry cannot add friend. Cannot authenticate the age.\n"
        return(-1)
    f_rating=float(raw_input("Enter your friend's rating: "))
    if f_rating<spy_detail[spy_name]["rating"]:         #checks rating
        print "Sorry cannot add friend. Rating not more than yours.\n"
        return(-1)
    spy_detail[spy_name]["friends"].update({f_name:{"f_age":f_age,"f_rating":f_rating,"chat":{},"avg words":0}}) #updates and adds friend to spy_details dictionary
    print "\nFriend has been added successfully.\n Details of the recently added friend:\n%s \n"%(f_name)+str(spy_detail[spy_name]["friends"][f_name])
    return(len(spy_detail[spy_name]["friends"].keys())) #returns number of friends the spy has
    
def select_a_friend(spy_name):                          #method to select a friend and return position
    leng=len(spy_detail[spy_name]["friends"])
    if leng==0:
        print "You have no friends added. \n"
        return("null")
    else:
        print "You have following people in your friend list: \n"
        for i in range(0,leng):
            print str(spy_detail[spy_name]["friends"].keys()[i])+"    ONLINE"
        position=raw_input("Enter the NAME OF THE FRIEND with whom you wish to continue with: ")
        if (position not in spy_detail[spy_name]["friends"].keys()):
            print "You have entered a wrong input\nTry again.\n"
            return("null")
        else:
            return(position)
def send_a_message(spy_name):           #method to send an encryted message
    global count
    position=select_a_friend(spy_name)  #calls select_a_friend function and stores the value it returns in position variable
    if position=="null":
        return(0)
    else:
        f_name=position
        from steganography.steganography import Steganography   #imports Steganography
        i_path = "C:\Users\ASUS\Desktop\Acadview\\"
        i_img_name=raw_input("What is the image NAME(Type along with the extension)?: ")
        path=i_path+i_img_name
        print "your path with specified image name is: "+path
        o_img_name=raw_input("What NAME should be the output file?(Type along with extension): ")
        o_path = "C:\Users\ASUS\Desktop\Acadview\\"
        output_path=o_path+o_img_name
        text =raw_input("Enter the TEXT you want to encode: ")
        from datetime import datetime                           #imports datetime
        date=datetime.now().strftime('%Y-%m-%d %H:%M:%S')       #stores current date and time
        count=count+1
        spy_detail[spy_name]["friends"][f_name]["chat"].update({count:{"secret text":text, "time":date,"Message sent":True}}) #stores in chat dictionary under spy_detail dictionary
        ######## MESSAGE SENT(Boolean) = True if the message was sent.#########
        print "please wait..................................."		
        Steganography.encode(path, output_path, text)
        s=text.split(" ")
        text=text.strip().split(" ")
        leng=len(spy_detail[spy_name]["friends"][f_name]["chat"].keys())
        avg=float(spy_detail[spy_name]["friends"][f_name]["avg words"])
        avg=float(avg+len(text))
        avg=float(avg/leng)
        spy_detail[spy_name]["friends"][f_name]["avg words"]=avg
        print "\nMessage has been encoded and sent to: "+ str(f_name)
        print "Avg words spoken by the spy to this friend= "+str(spy_detail[spy_name]["friends"][f_name]["avg words"])
        for i in range(len(s)):                                 #HANDLE TO checks for special words in secret text.
            for j in range(len(special_words)):
                if special_words[j]==s[i]:
                    print "Your message was an emergency message.\n"
        if len(text)>100:
            del spy_detail[spy_name]
            print "%s has been deleted from dictionary for speaking more than 100 words. Kindly create account again. :)"%(spy_name) #HANDLE FOR DELETING SPY FOR SPEAKING MORE THAN 100 WORDS
            return(1)
        else:
            return(0)
def read_a_message(spy_name):               #method to read the encrypted message.
    global count
    position= select_a_friend(spy_name)     #calls select_a_friend function and stores the value it returns in position variable
    if position=="null":
        return()
    else:
        from steganography.steganography import Steganography   #imports Steganography
        f_name=position
        print "Friend %s selected\n" %(f_name)
        o_img_name=raw_input("What is the name of the output file you want to decode?(Type along with extension): ")
        o_path = "C:\Users\ASUS\Desktop\Acadview\\"
        output_path=o_path+o_img_name
        from datetime import datetime
        date=datetime.now().strftime('%Y-%m-%d %H:%M:%S')       #stores current date and time
        print "please wait...................................."
        secret_text = Steganography.decode(output_path)
        if len(secret_text)==0:                                 #HANDLE FOR NO SECRET TEXT IN IMAGE
            print "Image has no secret message"
        else:
            print "\nYour secret text is: "+secret_text
            count=count+1
            spy_detail[spy_name]["friends"][f_name]["chat"].update({count:{"secret text":secret_text, "time":date,"Mesaage Read":True}}) #stores in chat dictionary under spy_detail dictionary
            ######## MESSAGE SENT(Boolean) = True if the message was sent.#########

def chat_read(spy_name):
    position= select_a_friend(spy_name)     #calls select_a_friend function and stores the value it returns in position variable
    if position=="null":
        return()
    f_name=position                         #gets the name of the friend from the position
    print "Chat history is as follows:\n %s: " %(f_name)
    print spy_detail[spy_name]["friends"][f_name]["chat"]
        
    

while True:
    user_choice=int(raw_input("Do you want to continue using a:\n1. Default spy.\n2. Create new spy.\nEnter 1 or 2: "))
    if user_choice==1:                      #for default spy
        import spy_details                  #imports default spy's information
        spy_name=spy_details.default_spy_detail.keys()[0] 
        if spy_name in spy_detail.keys():   #checks if the name of the default spy already exits in the spy_detail dictionary
            print "Default user name already exists in the spy dictionary"
        else:
            spy_detail.update(spy_details.default_spy_detail)   #adds to the spy_detail dictonary
            spy_status_history.update({spy_name:[]})
    elif user_choice==2:                                        #for new spy
        spy_name=raw_input("Login:\nEnter your spy name: ")
        if len(spy_name)<1:                                     #checks for valid name
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
            if age>=12 and age<=50:                                     #checks for valid age
                rating=float(raw_input("What is your rating?(Enter 0-10)\n"))       #checks for rating
                if rating<0:
                    print "Rating cannot be negative."
                    break
                elif rating>10:
                    print "Rating cannot be grater than 10."
                    break
                else:
                    print "Rating has been accepted.\n"
                spy_detail.update({spy_name:{"salutation":salutation,"age":age,"rating":rating,"friends":{},"status":""}}) #adds new spy to spy_detail dictionary
                spy_status_history.update({spy_name:[]})                #creates spy status history for the new spy
            else:
                print "Sorry, we can't authenticate your age.....try again"
                continue
    else:
        print "Wrong input. Try again\n"
        continue
    if spy_name in spy_detail.keys():                                   #checks whether the spy has been added to the spy_details or not
        print "\nWelcome %s %s!" %(spy_detail[spy_name]["salutation"],spy_name) #welcome note!
        print "Your age: %i" %(spy_detail[spy_name]["age"])+"\nYour Rating is: %.2f\n" %(spy_detail[spy_name]["rating"])
        while True:
            menu=int(raw_input("Menu:\n1. Add a status update\n2. Add a friend\n3. Send a secret message\n4. Read a secret message\n5. Read chats from a user\n6. Exit\nEnter from 1,2,3,4,5 or 6: ")) #menu options
            if menu==1:
                add_a_status(spy_name)                    
            elif menu==2:
                friends_count=add_friend(spy_name)
                if friends_count!= -1:
                    print "You have %i friends as of now.\n" %(friends_count)
            elif menu==3:
                spy_del=send_a_message(spy_name)
                if spy_del==1:                                          #Checks if was returned with error, if not, goes into loop
                    break
            elif menu==4:
                 read_a_message(spy_name)
            elif menu==5:
                chat_read(spy_name)
            elif menu==6:
                print "The program will now Exit....BYE %s %s" %(spy_detail[spy_name]["salutation"], spy_name)
                exit()                                                  #exits the program
            else:
                print "Wrong input. Try again"
            continue
exit()
