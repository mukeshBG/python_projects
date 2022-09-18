import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="covid_19"
)
mycursor=mydb.cursor()
#--------------------------------------------------------
#mycursor.execute("create database covid_19")
#mycursor.execute("create table covid19_result(country varchar(50),state varchar(40),state_positive int,state_negative int)")
#mycursor.execute("create table country(region varchar(40),population int,covid_cases int,covid_deathcase int,recover_case int)")
#mycursor.execute("create table covid_data(name varchar(100),age int,gender varchar(25),city varchar(40),covid_result varchar(10))")
def menu():
    print("--------------------------")
    print("------MENUS---------------")
    print("--------------------------")
    print("1.insert data")
    print("2.view  data")
    print("3.update data")
    print("4.delete data")
    print("5.top 10 country view")
    print("6.covid country,state wise (+)&(-) insert ")
    print("7.view (+) and (-) cases")
    print("8.exit program")
    print("----------------------")
    

#===================================================== 
def insert_data(name,age,gender,city):
    insrt_data="insert into covid_data (name,age,gender,city) values (%s,%s,%s,%s) "  
    val=(name,age,gender,city)
    mycursor.execute(insrt_data,val)
    mydb.commit()
    print("---------------------")
    print("data inserted sucessfully")
    print("---------------------")
    return choice()
#-----------------------------------------------------
def view_data():
    mycursor.execute("select * from covid_data order by name asc")
    result=mycursor.fetchall()
    print("   name , age ,  gender ,  city ")
    for i in result:
        print(i)
    print("---->data sucessfully viewed..........")
    return choice()
#===================================================
def update_data(covid_rslt,update_name):
    #mycursor.execute("alter table covid_data add covid_result varchar(20)")
    mycursor.execute(f"update covid_data  set covid_result='{covid_rslt}' where name='{update_name}'")
    mydb.commit()
    print(f"{update_name} data updated sucessfully")
    return choice()
#===================================================
def delete_data(delete_info):
    mycursor.execute(f"delete from covid_data where name='{delete_info}'")
    mydb.commit()
    print(".................................................")
    print(f"Your data:{delete_info} has deleted sucessfully ")
    return choice()
   
#=========================================================
  
def view_countrydata():
    mycursor.execute("select * from country order by population desc" )
    result=mycursor.fetchall()
    print(" Country  ,population ,covid_cases,death_cases,recovered")
    for i in result:
        print(i)
    return choice()
#=========================================================
def covid_result(country,state,state_positive,state_negative):
    sql="insert into covid19_result (country,state,state_positive,state_negative) values (%s,%s,%s,%s)"
    val=(country,state,state_positive,state_negative)
    mycursor.execute(sql,val)
    mydb.commit()
    print("covid-19 state wise statistics inserted sucessfully")
    return choice()
        
#====================================================    

def view_result():
    print("---------------------------------")
    user_db=input("did you inserted the data (yes/no):").lower().strip()
    if user_db=="yes":
        print("--------------------")
        print("1-->show all data ")
        print("2-->show particular data")
        print("Enter 1 or 2 .......")
        print("-------------------")
        user_type=int(input("enter your choice :"))
        print("-----------------")
        if user_type==1:
            mycursor.execute("select * from covid19_result order by state asc")
            result=mycursor.fetchall()
            print("  country , state , positive ,negative")
            for i in result:
                print(i)
        elif user_type==2:
            country_name=input("enter your country name :").lower().strip()
            state_name=input("Enter you state name :").lower().strip()
            mycursor.execute(f"select * from covid19_result where country='{country_name}' and state='{state_name}'")
            print("  country , state , positive, negative")
            result1=mycursor.fetchall()
            for j in result1:
                print(j)
        else:
            print("Enter the correct choice")
    else:
        print("Enter the data before viewing")    
            
    return choice()
    
 
def choice():
    menu()
    user=int(input("enter your choice :"))  
#-------------------------------------------------------------  
    if user==1:
        name=input("Enter your name :").lower().strip()
        age=int(input("enter your age :"))
        gender=input("Enter your gender :")
        city=input("Enter your city :").lower().strip()
        if gender=="male" or gender=="female" or gender=="others":
            if age>15:
                insert_data(name,age,gender,city)
        else:
            print("you have enter the data incorrectly \n please check your data and re-enter")
#----------------------------------------------------------
    elif user==2:
        view_data()
#---------------------------------------------------------
    elif user==3:
        update_input=input("(Did you log-in this page before (yes/no) :")
        if(update_input=="yes"):
            update_name=input("Enter your name to update your covid-result :")
        else:
            print(" sorry................ \n your permission denied")
        print("covid symptoms")
        print("1.fever")
        print("2.tiredness")
        print("3.dry cough")
        covid_user=input("If you have any of the symptoms severely which is listed above :")
        if covid_user=='1' or covid_user=='2' or covid_user=='3':
            covid_rslt="positive"
        else:
            covid_rslt="negative"
        update_data(covid_rslt,update_name)
#--------------------------------------------------------
    elif user==4:
        delete_info=input("enter the name that you want to delete :").lower().strip()
        delete_data(delete_info)
#--------------------------------------------------------
    elif user==5:
        view_countrydata()
#--------------------------------------------------------
    elif user==6:
        country=input("Enter the country :").lower().strip()
        if country !='\0':
            state=input("Enter your state :").lower().strip()
            if state!='\0':
                state_positive=int(input(f"enter your {state} positive cases :"))
                state_negative=int(input(f"Enter your {state} negative cases :"))
                covid_result(country,state,state_positive,state_negative)
            else:
                print("you have to enter state name properly")
        else:
            print("you have to enter country name properly")
        
#---------------------------------------------------------
    elif user==7:
        view_result()

#-----------------------------------------------------------
    elif user==8:
        print("thank you --------------")
        
#------------------------------------------------------------
    else:
        print("enter the correct choice :")
#============================================       

#===================================================
print("-----------------------------------------------")
print("::::::::::::::::::::::::::::::::::::::::::::::::")
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
print(choice())
print("-------------------")
