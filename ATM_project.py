import functools
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="atm"
)

mycursor=mydb.cursor()
#mycursor.execute("create database atm")
#=================================================================
def menus():
    
    print("1-->insert user details")
    print("2-->view balance")
    print("3-->withdrawl amount")
    print("4-->deposit amount")
    print("5-->delete user details")
    print("6-->exit program")
    print("----------------------------")
    
    
#----------------------------------------------------------------
def insert_data(acc_type,first_name,last_name,account_no,pin,account_balance):
    insert_user=f"insert into {acc_type} (first_name,last_name,account_no,pin,account_balance) values (%s,%s,%s,%s,%s)"
    val=(first_name,last_name,account_no,pin,account_balance)
    
    mycursor.execute(insert_user,val)
    mydb.commit()
    print("---------------------------------")
    print("data inserted sucessfully")
    print("------------------------------")
    return choice()
#-------------------------------------------------------------------

def view_balance(ac_type,name,acc_pin):
    mycursor.execute(f"select account_balance from {ac_type} where first_name='{name}' and pin='{acc_pin}'")
    result=mycursor.fetchall()
    print("--------------------------------")
    
    for i in result:
        print(f"Your account balance is {i}")
    print("-----------------------------------")
    return choice()

#------------------------------------------------------------------

def withdrawl(accc_type,acc1_pin):
    withdraw=input("Enter your withdrawl amount :")
    mycursor.execute(f"select account_balance-{withdraw} from {accc_type} where pin='{acc1_pin}' ")
    result1=mycursor.fetchall()
    print("---------------------------------------")
    for j in result1:
        my_int1=int(j[0])
        if my_int1 < 500:
            print("you must have minimum RS.500 in your account")
            print(f"you cannot withdrawl RS.{my_int1}")
        else:
            print(f"your current total balance is {j}")
            my_int=int(j[0])
            mycursor.execute(f"update {accc_type} set account_balance='{my_int}' where pin='{acc1_pin}'")
            mydb.commit()
            print("data updated sucessfully")
            print("--------------------------------------")
    return choice()
    
#------------------------------------------------------------------
def deposit_amount(a_type,ac1_pin):
    deposit_amt=int(input("Enter your deposit amount :"))
    mycursor.execute(f"select account_balance+{deposit_amt} from {a_type} where pin='{ac1_pin}' ")
    result=mycursor.fetchall()
    for n in result:
        print(f"your current total balance is {n}")
    my_int=int(n[0])
    mycursor.execute(f"update {a_type} set account_balance='{my_int}' where pin='{ac1_pin}'")
    mydb.commit()
    print("amount deposited sucessfully")
    print("--------------------------------------")
    
    return choice()
        
#-------------------------------------------------------------------
def delete_user(ac_name,pin_no):
    mycursor.execute(f"delete from {ac_name} where pin='{pin_no}'")
    mydb.commit()
    print(" user deleted sucessfully")

       
#-------------------------------------------------------------------   
def choice():
    menus()
    user=int(input("Enter your choice :"))
#--------------------------------------------------------------------
    if user==1:
        print("-----------------------------------")
        print("1-->saving account")
        print("2-->current account")
        print("Enter 1 or 2")
        acc_type=int(input("Enter your account type :"))
        print("----------------------------------")
        if acc_type==1:
            acc_type="saving_acc"
            first_name=input("Enter your first_name :").lower().strip()
            if first_name!='/0':
                last_name=input("Enter your last name :").lower().strip()
                if last_name!='/0':
                    account_no=input("Enter you account number :")
                    if account_no!='/0':
                        pin=int(input("Enter you pin :"))
                        if pin >=1000:
                            account_balance=int(input("Enter your account balance :"))
                            if account_balance > 0:
                                insert_data(acc_type,first_name,last_name,account_no,pin,account_balance)
                                print("-------------------------------------------------")
                            else:
                                print("you have selected incorrect choice")
                        else:
                            print("you have selected incorrect choice")
                    else:
                        print("you have selected incorrect choice")
                else:
                    print("you have selected incorrect choice")
            else:
                print("you have selected incorrect choice")
#====================================================================================
        elif acc_type==2:
            acc_type="current_acc"
            first_name=input("Enter your first_name :").lower().strip()
            if first_name!='/0':
                last_name=input("Enter your last name :").lower().strip()
                if last_name!='/0':
                    account_no=input("Enter you account number :")
                    if account_no!='/0':
                        pin=int(input("Enter you pin :"))
                        if pin >=1000:
                            account_balance=int(input("Enter your account balance :"))
                            if account_balance > 0:
                                insert_data(acc_type,first_name,last_name,account_no,pin,account_balance)
                                print("-------------------------------------------------")
                            else:
                                print("you have selected incorrect choice")
                        else:
                            print("you have selected incorrect choice")
                    else:
                        print("you have selected incorrect choice")
                else:
                    print("you have selected incorrect choice")
            else:
                print("you have selected incorrect choice")
        else:
            print("you have selected incorrect choice")
            
#---------------------------------------------------------------------
    elif user==2:
        acc_pin=int(input("Enter pin :"))
        print("------------------------")
        if acc_pin>=1000:
            print("1-->saving account")
            print("2-->current account")
            print("Enter 1 or 2")
            ac_type=int(input("Enter your choice :"))
            print("------------------------------")
            if ac_type==1:
                ac_type="saving_acc"
                name=input("Enter your name :").lower().strip()
                if name!='/0':
                    view_balance(ac_type,name,acc_pin)
                else:
                    print("sorry............. \n retry.............")
#----------------------------------------------------------------------
            elif ac_type==2:
                ac_type="current_acc"
                name=input("Enter your name :").lower().strip()
                if name!='/0':
                    view_balance(ac_type,name,acc_pin)
                else:
                    print("sorry............\nretry.................")
        else:
            print("you entered the wrong pin")       
    
#--------------------------------------------------------------------  
    elif user==3:
        acc1_pin=int(input("Enter pin :"))
        print("------------------------")
        if acc1_pin>=1000:
            print("1-->saving account")
            print("2-->current account")
            print("Enter 1 or 2")
            accc_type=int(input("Enter your choice :"))
            if accc_type==1:
                accc_type="saving_acc"
                mycursor.execute(f"select account_balance from {accc_type} where pin='{acc1_pin}'")
                result=mycursor.fetchall()
                for i in result:
                    print(f"your current_balance is {i}")
                withdrawl(accc_type,acc1_pin)
            elif accc_type==2:
                accc_type="current_acc"
                mycursor.execute(f"select account_balance from {accc_type} where pin='{acc1_pin}'")
                result=mycursor.fetchall()
                for x in result:
                    print(f"your current_balance is {x}")
                withdrawl(accc_type,acc1_pin)
            else:
                print("sorry..........\nretry..............")
        else:
            print("enter the correct pin ")
            
    elif user==4:
        ac1_pin=int(input("Enter your pin :"))
        if ac1_pin > 1000:
            print("1-->saving_acc")
            print("2-->current_acc")
            print("Enter 1 or 2")
            a_type=int(input("Enter choice :"))
            if a_type==1:
                a_type="saving_acc"
                mycursor.execute(f"select account_balance from {a_type} where pin='{ac1_pin}'")
                result=mycursor.fetchall()
                for a in result:
                    print(f"your current_balance is {a}")
                deposit_amount(a_type,ac1_pin)
            elif a_type==2:
                a_type="current_acc"
                mycursor.execute(f"select account_balance from {a_type} where pin='{ac1_pin}'")
                result=mycursor.fetchall()
                for b in result:
                    print(f"your current_balance is {b}")
                deposit_amount(a_type,ac1_pin)
            else:
                print("sorry..........\nretry..............")
        else:
            print("enter the correct pin ")
#-----------------------------------------------------------------------------------------------
    elif user==5:
        pin_no=int(input("Enter pin number :"))
        if pin_no >= 1000:
            print("1-->saving_acc")
            print("2-->current_acc")
            ac_name=int(input("Enter your choice :"))
            if ac_name==1:
                ac_name="saving_acc"
                delete_user(ac_name,pin_no)
            else:
                print("sorry...........\nretry.................")
        elif ac_name==2:
            pin_no=int(input("Enter pin number :"))
            if pin_no >= 1000:
                ac_name="current_acc"
                delete_user(ac_name,pin_no)
        else:
            print("sorry...........\nretry.................")
#----------------------------------------------------------------------------------------------

    elif user==6:
        print("Thank you ")
        print("--------------------------------")
                 
#-----------------------------------------------------------------------------------------------           
    else:
        print("you have selected incorrect choice")
#-----------------------------------------------------------------------------------------------
print("---------------------------")
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
print("=====================================")
print("1-->insert ")
user_insert=int(input("Insert your Atm card :"))
if user_insert==1:
    print("Card Inserted")
    print(choice())
else:
    print("you want to insert card \n you might choice option correctly")
print("---------------------------")