import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="online_ticket"
    
)
mycursor=mydb.cursor()

#mycursor.execute("create database online_ticket")
#===========================================================================

def menus():
     print("1-->view train data")
     print("2-->Book ticket")
     print("3-->view booked ticket")
     print("4-->delete the booked data")
     print("5-->update address ")
     print("6-->exit program")
     
#-----------------------------------------------------------------

def view_traindata():
    print("1.show all available train")
    print("2.show particular train")
    print("enter 1 or 2")
    print("---------------------------")
    user_type=int(input("Enter your choice :"))
    print("-------------------------------")
    if user_type==2:
        train_from=input("Train From :").lower().strip()
        if train_from!='/0':
            train_to=input("Train To :").lower().strip()
            if train_to!='/0':
                mycursor.execute(f"select * from train_ticket where train_from='{train_from}' and train_to='{train_to}'")
                result=mycursor.fetchall()
                print("  Train name   ,   Train_no ,  From  ,  To    ,   train_fair" )
                for i in result:
                    print(i)
            else:
                print("sorry............... \n retry...........")
        else:
            print("sorry............... \n retry...........")
    elif user_type==1:
        mycursor.execute("select * from train_ticket order by train_name asc")
        result1=mycursor.fetchall()
        print("  Train name     ,  Train_no ,  From  ,  To    , train_fair" )
        for j in result1:
            print(j)
    return choice()
        
#------------------------------------------------------------------------------    
def train_ticket_book(name,mobile_no,gender,train_from,train_to,train_fair):
    insertdata="insert into book_ticket (name,mobile_no,gender,train_from,train_to,train_fair) values (%s,%s,%s,%s,%s,%s)"
    val=(name,mobile_no,gender,train_from,train_to,train_fair)
    mycursor.execute(insertdata,val)
    mydb.commit()
    mycursor.execute(f"select * from train_ticket where train_from='{train_from}' and train_to='{train_to}'")
    result=mycursor.fetchall()
    for i in result:
        print(i)
    mycursor.execute(f"select train_name from train_ticket where train_from='{train_from}' and train_to='{train_to}'")
    result1=mycursor.fetchall()
    for j in result1:
        print(f"Your train {j} is booked now")
    print("-------------------------------")
    print("train ticket sucessfully booked")
    print("------------------------------")
    return choice()
#------------------------------------------------------------------------------
def view_booked():
    user_confirm=input("Did you booked the ticket already (yes/no) :").lower().strip()
    if user_confirm=="yes":
        print("1-->show all data")
        print("2-->show particular data")
        print("Enter 1 or 2")
        user=int(input("Enter choice :"))
        if user==1:
            mycursor.execute("select * from book_ticket order by name asc")
            print("-----------------------------------------------")
            print("   name  , mobile_no , gender , from   ,     to  ,  fair ,address")
            reslt=mycursor.fetchall()
            for x in reslt:
                print(x)
            print("--------------------------------")
        elif user==2:
            name=input("Enter your name :").lower().strip()
            train_from=input("Train from :").lower().strip()
            train_to =input("Train to :").lower().lower()
            mycursor.execute(f"select * from book_ticket where name='{name}'")
            print("   name  , mobile_no , gender ,  from   ,   to  , ticket_fair " )
            result=mycursor.fetchall()
            print("-----------------------------------------------")
            print("   name  , mobile_no , gender , from   ,     to  ,  fair ,address")
            for i in result:
                print(i)
                mycursor.execute(f"select train_name from train_ticket where train_from='{train_from}' and train_to='{train_to}'")
                result1=mycursor.fetchall()
                for j in result1:
                    print(f" you train name is {j}")
                    print("-------------------------------------")  
        else:
            print("sorry ................ \n retry ...........................")  
    else:
        print("sorry ..........\n you have to book the ticket first... \n ......................................")
    return choice()

#---------------------------------------------------------------------------
def delete_data(delete_name):
    mycursor.execute(f"delete from book_ticket where name='{delete_name}'")
    mydb.commit()
    print(f"your ticket:{delete_name} has been cancelled ")
    print("-------------------------------------------")
    return choice()
#----------------------------------------------------------------------------
def update_data(update_address,update_name):
   # mycursor.execute("alter table book_ticket add address varchar(255)")
    mycursor.execute(f"update book_ticket set address='{update_address}' where name='{update_name}'")
    mydb.commit()
    print("-------------------------------------------")
    print(f"Your data:{update_name} has been updated")
    print("-------------------------------------------")
    return choice()    
#----------------------------------------------------------------------------
def choice():
    menus()
    print("----------------------------")
    user=int(input("Enter your choice :"))
#-----------------------------------------------------------------------------
    if user==1:
        view_traindata()
#------------------------------------------------------------------------------
    elif user==2:
        name=input("Enter your name :").lower().strip()
        if name!='/0':
            mobile_no=input("Enter your Mobile_number :")
            if mobile_no!='/0':
                gender=input("Enter you gender :").lower().strip()
                if gender=="male" or gender=="female" or gender =="others":
                    train_from=input("Train from :").lower().strip()
                    if train_from!='/0':
                        train_to=input("Train to :").lower().strip()
                        if train_to!='/0':
                            train_fair=int(input("Train Fair Rs."))
                            if train_fair!='/0':
                                train_ticket_book(name,mobile_no,gender,train_from,train_to,train_fair)
                            else:
                                print("sorry................... \n retry ..................")
                        else:
                            print("sorry................... \n retry ..................")
                    else:
                        print("sorry................... \n retry ..................")
                else:
                    print("sorry................... \n retry ..................")
            else:
                print("sorry................... \n retry ..................")
        else:
            print("sorry................... \n retry ..................")
                
#-------------------------------------------------------------------------------------
    elif user==3:
        print("-----------------------------------------")
        view_booked()
        
#------------------------------------------------------------------------------------
        
    elif user==4:
        print("-----------------------------")
        delete_name=input("Enter Name to delete :").lower().strip()
        if delete_name!='/0':
            delete_data(delete_name)
        
#------------------------------------------------------------------------------------
        
    elif user==5:
        print("--------------------------------")
        update_adderss=input("Enter address to update :")
        if update_adderss !='/0':
            update_name=input("Enter your name :").lower().strip()
            if update_name!='/0':
                update_data(update_adderss,update_name)
        
#-----------------------------------------------------------------------------------
        
    elif user==6:
        print("---------------------")
        print("thank you")
        return 0
#------------------------------------------------------------------------------------
print("-----------------------------")
print("-------------------")
import datetime
from datetime import date
#-------------------------------
x=datetime.datetime.now()
this_date=x.strftime("%d")
print(f"Date :-> {this_date}")
#------------------------------------
today=x.strftime("%A")
print(f"DAY :->  {today}")
#-----------------------------------
this_month=x.strftime("%B")
print(f"Month :-> {this_month}")
#------------------------------------
this_year=x.strftime("%Y")
print(f"Year :-> {this_year}")
#---------------------------------------
this_hour=x.strftime("%H")
this_minute=x.strftime("%M")
this_second=x.strftime("%S")
print(f"Time :-> {this_hour}:{this_minute}:{this_second}")
print("-----------------------------------")
#===================================================
print(choice())
print("-----------------------------")