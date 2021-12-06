from configparser import Error
import psycopg2
from config import config

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
		
        # create a cursor
        cur = conn.cursor()
        
	# execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)
        menu()
       
	# close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


def read(tables):
    params = config()
    conn = psycopg2.connect(**params)
    cur = conn.cursor()
    
    read_table = input("Enter the table name which to read:")

    read_command = {
        'department': "SELECT * from department;",
        'passenger' : "SELECT * from passenger;",
        'restaurant' : "SELECT * from restaurant;",
        'routes' : "SELECT * from routes;",
        'station' : "SELECT * from station;",
        'timetable' : "SELECT * from timetable;",
        'train' : "SELECT * from train;",
        'trainstatus' : "SELECT * from trainstatus;",
        'user' : 'SELECT * from "user";'
    }
    if read_table in tables:
        cur.execute(read_command[read_table])
        conn.commit()
        # read_output= cur.fetchall()
        # print(read_output)
        print("\n")
        for table in cur.fetchall():
            print(table)
        print("\n")
    else:
        print("Invalid table name \n")
        return

def insert(tables):
    params = config()
    conn = psycopg2.connect(**params)
    cur = conn.cursor()
    
    insert_table = input("Enter the table name in which to insert a new record:")
    insert_table=insert_table.lower()
    insert_command = {
        'department': "INSERT into Department values(%s, %s, %s, %s);",
        'passenger' : "INSERT into Passenger values(%s, %s, %s, %s, %s, %s, %s, %s);",
        'restaurant' : "INSERT into Restaurant values(%s, %s,%s, %s);",
        'routes' : "INSERT into Routes values(%s, %s, %s, %s, %s, %s);",
        'station' : "INSERT into Station values(%s, %s);",
        'timetable' : "INSERT into timetable values(%s, %s, %s, %s, %s);",
        'train' : "INSERT into Train values(%s, %s, %s, %s, %s, %s);",
        'trainstatus' : "INSERT into TrainStatus values();",
        'user' : "INSERT into \"user\" values(%s, %s);"
    }
    if insert_table=='department':
        try:
            station_id=input('Enter Station ID:')
            dept_id=input('Enter Department ID:')
            department_name=input('Enter Department Name:')
            department_head=input('Enter Department Head Name:')
            cur.execute(insert_command[insert_table], (station_id,dept_id,department_name,department_head))
            conn.commit()
            print("Record successfully inserted.")
        except Exception as e:
            print(f"Error: '{e}'")
            print("Record Not Inserted")

    elif insert_table=='passenger':
        try:
            pnr = input('Enter PNR : ')
            bookinguser = input('Enter Booking Username : ')
            bookingdate = input('Enter Booking Date : ')
            passengername = input('Enter Passenger Name : ')
            age = input('Enter Age : ')
            gender = input('Enter gender : ')
            seatnumber = input('Enter seatnumber : ')
            reservationstatus = input('Enter Reservation Status : ')
            cur.execute(insert_command[insert_table], (pnr,bookinguser,bookingdate,passengername,age,gender,seatnumber,reservationstatus))
            conn.commit()
            print("Record successfully inserted.")
        except Exception as e:
            print(f"Error: '{e}'")
            print("Record Not Inserted")

    elif insert_table=='restaurant':
        try:
            station_id=input('Enter Station ID :')
            restaurant_id=input('Enter Restaurant ID :')
            restaurantname=input('Enter Restaurant Name :')
            items=input('Enter Items(as a List) : ')
            cur.execute(insert_command[insert_table], (station_id,restaurant_id,restaurantname,items))
            conn.commit()
            print("Record successfully inserted.")
        except Exception as e:
            print(f"Error: '{e}'")
            print("Record Not Inserted")

    elif insert_table=='station':
        try:
            station_id=input('Enter Station ID :')
            stationname=input('Enter Station Name :')
            cur.execute(insert_command[insert_table], (station_id,stationname))
            conn.commit()
            print("Record successfully inserted.")
        except Exception as e:
            print(f"Error: '{e}'")
            print("Record Not Inserted")

    elif insert_table=='timetable':
        try:
            station_id=input('Enter Station ID : ')
            timetable_id=input('Enter Timetable ID : ')
            trainnumber=input('Enter Train Number : ')
            departuredate=input('Enter Departure Date : ')
            departuretime=input('Enter Departure Time : ')
            cur.execute(insert_command[insert_table], (station_id,timetable_id,trainnumber,departuredate,departuretime))
            conn.commit()
            print("Record successfully inserted.")
        except Exception as e:
            print(f"Error: '{e}'")
            print("Record Not Inserted")

    elif insert_table=='train':
        try:
            startstationid=input('Enter Starting Station ID : ')
            endstationid=input('Enter Last Station ID : ')
            train_id=input('Enter Train ID : ')
            trainname=input('Enter Train Name : ')
            traintype=input('Enter Train Type : ')
            availclass=input('Enter Available Classes : ')
            cur.execute(insert_command[insert_table], (startstationid,endstationid,train_id,trainname,traintype,availclass))
            conn.commit()
            print("Record successfully inserted.")
        except Exception as e:
            print(f"Error: '{e}'")
            print("Record Not Inserted")
    elif insert_table=='trainstatus':
        try:
            station_id=input('Enter Station ID :')
            availableseat=input('Enter Number of Available Seats :')
            bookedseat=input('Enter Number of Booked Seats')
            waitingseat=input('Enter Number of Waiting Seats')
            cur.execute(insert_command[insert_table], (station_id,availableseat,bookedseat,waitingseat))
            conn.commit()
            print("Record successfully inserted.")
        except Exception as e:
            print(f"Error: '{e}'")
            print("Record Not Inserted")
    elif insert_table=='user':
        try:
            username=input('Enter Username :')
            password=input('Enter Password :')
            cur.execute(insert_command[insert_table], (username,password))
            conn.commit()
            print("Record successfully inserted.")
        except Exception as e:
            print(f"Error: '{e}'")
            print("Record Not Inserted")
    else:
        print("Invalid table name")

def update(tables):
    params = config()
    conn = psycopg2.connect(**params)
    cur = conn.cursor()
    
    update_table = input("Enter the table name in which to update : ")
    update_table=update_table.lower()
    update_command = {
        'department': "UPDATE Department SET Department_Name = %s, Department_Head = %s WHERE Dept_ID = %s;",
        'passenger' : "UPDATE Passenger SET PassengerName =%s, Age = %s, Gender = %s WHERE PNR = %s;",
        'restaurant' : "UPDATE Restaurant SET RestaurantName = %s WHERE Restaurant_ID = %s;",
        'routes' : "UPDATE Routes ;",
        'station' : "UPDATE Station ;",
        'timetable' : "UPDATE timetable ;",
        'train' : "UPDATE Train SET TrainName = %s, TrainType = %s WHERE Train_ID = %s;",
        'trainstatus' : "UPDATE TrainStatus AvailableSeat = %s,	BookedSeat = %s, WaitingSeat = %s WHERE StatusID = %s;",
        'user' : "UPDATE \"user\" SET passwd = %s WHERE username = %s;"
    }
    if update_table=='department':
        try:
            dept_id=input('Enter Department ID of record to be updated :')
            department_name=input('Enter New Department Name:')
            department_head=input('Enter New Department Head Name:')
            cur.execute(update_command[update_table], (department_name,department_head,dept_id))
            conn.commit()
            print("Record successfully updated.")
        except Exception as e:
            print(f"Error: '{e}'")
            print("Record Not Updated.")

    elif update_table=='passenger':
        try:
            pnr=input('Enter PNR of record to be updated :')
            passengername = input('Enter New Passenger Name : ')
            age = input('Enter New Age : ')
            gender = input('Enter New gender : ')
            cur.execute(update_command[update_table], (passengername,age,gender,pnr))
            conn.commit()
            print("Record successfully Updated.")
        except Exception as e:
            print(f"Error: '{e}'")
            print("Record Not Updated.")

    elif update_table=='restaurant':
        try:
            rest_id=input('Enter Restaurant ID of record to be updated :')
            restaurantname = input('Enter New Restaurant Name : ')
            cur.execute(update_command[update_table], (restaurantname,rest_id))
            conn.commit()
            print("Record successfully updated.")
        except Exception as e:
            print(f"Error: '{e}'")
            print("Record Not Updated.")

    # elif insert_table=='routes':
    #     cur.execute(insert_command[insert_table], ('CHN','CHNBNC100','12:15:00','12:20:00','15','45'))
    #     conn.commit()

    # elif update_table=='station':
    #     cur.execute(update_command[update_table], ('CHE', 'CHENNAI'))
    #     conn.commit()

    # elif update_table=='timetable':
    #     cur.execute(update_command[update_table], ('CHE', 'CHETT', '12', '2020-04-23','10:20:00'))
    #     conn.commit()

    elif update_table=='train':
        try:
            train_id=input('Enter Train ID of record to be updated :')
            trainname = input('Enter New Train Name : ')
            traintype = input('Enter New Train Type : ')
            cur.execute(update_command[update_table], (trainname,traintype,train_id))
            conn.commit()
            print("Record successfully updated.")
        except Exception as e:
            print(f"Error: '{e}'")
            print("Record Not Updated.")
    
    elif update_table=='trainstatus':
        try:
            statusid=input('Enter Status ID of record to be updated :')
            AvailableSeat = input('Enter New Available Seats : ')
            BookedSeat =  input('Enter New Booked Seats : ')
            WaitingSeat = input('Enter New Waiting Seats : ')
            cur.execute(update_command[update_table], (AvailableSeat,BookedSeat,WaitingSeat,statusid))
            conn.commit()
            print("Record successfully updated.")
        except Exception as e:
            print(f"Error: '{e}'")
            print("Record Not Updated.")

    elif update_table=='user':
        try:
            username=input('Enter Username of record to be updated :')
            password = input('Enter New Password : ')
            cur.execute(update_command[update_table], (password,username))
            conn.commit()
            print("Record successfully updated.")
        except Exception as e:
            print(f"Error: '{e}'")
            print("Record Not Updated.")

    else:
        print("Invalid table name")
        print("Record Not Updated.")

def delete(tables):
    params = config()
    conn = psycopg2.connect(**params)
    cur = conn.cursor()
    
    delete_table = input("Enter the table name from which to delete a record:")
    delete_table=delete_table.lower()
    delete_command = {
        'department': "DELETE FROM Department WHERE Dept_ID = %s;",
        'passenger' : "DELETE FROM Passenger WHERE PNR = %s;",
        'restaurant' : "DELETE FROM Restaurant WHERE Restaurant_ID = %s;",
        'routes' : "DELETE FROM Routes WHERE Train_ID = %s;",
        'station' : "DELETE FROM Station WHERE Station_ID = %s;",
        'timetable' : "DELETE FROM timetable WHERE TimeTable_ID =%s;",
        'train' : "DELETE FROM Train WHERE Train_ID = %s;",
        'trainstatus' : "DELETE FROM TrainStatus WHERE StatusID = %s;",
        'user' : "DELETE FROM \"user\" WHERE username = %s;"
    }
    if delete_table=='department':
        try:
            dept_id=input('Enter Department ID of record to be deleted : ')
            cur.execute(delete_command[delete_table], (dept_id,))
            conn.commit()
            print("Record successfully deleted.")
        except Exception as e:
            print(f"Error: '{e}'")
            print("Record not deleted.")

    elif delete_table=='passenger':
        try:
            pnr=input('Enter PNR of record to be deleted : ')
            cur.execute(delete_command[delete_table], (pnr,))
            conn.commit()
            print("Record successfully deleted.")
        except Exception as e:
            print(f"Error: '{e}'")
            print("Record not deleted.")


    elif delete_table=='restaurant':
        try:
            rest_id=input('Enter Restaurant ID of record to be deleted : ')
            cur.execute(delete_command[delete_table], (rest_id,))
            conn.commit()
            print("Record successfully deleted.")
        except Exception as e:
            print(f"Error: '{e}'")
            print("Record not deleted.")

    elif delete_table=='routes':
        try:
            train_id=input('Enter Train ID of record to be deleted : ')
            cur.execute(delete_command[delete_table], (train_id,))
            conn.commit()
            print("Record successfully deleted.")
        except Exception as e:
            print(f"Error: '{e}'")
            print("Record not deleted.")

    elif delete_table=='station':
        try:
            station_id=input('Enter Station ID of record to be deleted : ')
            cur.execute(delete_command[delete_table], (station_id,))
            conn.commit()
            print("Record successfully deleted.")
        except Exception as e:
            print(f"Error: '{e}'")
            print("Record not deleted.")

    elif delete_table=='timetable':
        try:
            timetable_id=input('Enter Timetable ID of record to be deleted : ')
            cur.execute(delete_command[delete_table], (timetable_id,))
            conn.commit()
            print("Record successfully deleted.")
        except Exception as e:
            print(f"Error: '{e}'")
            print("Record not deleted.")

    elif delete_table=='train':
        try:
            train_id=input('Enter Train ID of record to be deleted : ')
            cur.execute(delete_command[delete_table], (train_id,))
            conn.commit()
            print("Record successfully deleted.")
        except Exception as e:
            print(f"Error: '{e}'")
            print("Record not deleted.")

    elif delete_table=='trainstatus':
        try:
            statusid=input('Enter Status ID of record to be deleted : ')
            cur.execute(delete_command[delete_table], (statusid,))
            conn.commit()
            print("Record successfully deleted.")
        except Exception as e:
            print(f"Error: '{e}'")
            print("Record not deleted.")

    elif delete_table=='user':
        try:
            username=input('Enter username of record to be deleted : ')
            cur.execute(delete_command[delete_table], (username,))
            conn.commit()
            print("Record successfully deleted.")
        except Exception as e:
            print(f"Error: '{e}'")
            print("Record not deleted.")

    else:
        print("Invalid table name \n")
        print("Record not deleted.")

def menu():
    params = config()
    conn = psycopg2.connect(**params)
    cur = conn.cursor()
    
    print("Welcome to the Railway Management System:")
    tables = ['department', 'passenger', 'restaurant', 'routes', 'station', 'timetable', 'train', 'trainstatus', 'user']
    
    #cur.execute('\d')
    print('\n')

    while(True):
        ans = int(input('''1. Insert
2. Read
3. Update
4. Delete
0. Exit
Enter your choice: '''))

        if ans==1:
           insert(tables)
        elif ans==2:
            read(tables)
        elif ans==3:
            update(tables)
        elif ans==4:
            delete(tables)
        elif ans==0:
            return
        else:
            print("Invalid choice")