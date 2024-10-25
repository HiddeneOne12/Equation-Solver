from datetime import datetime, time

# Get the current date and time
now = datetime.now()
def performAddOperations():
    a = int(input("Enter 1 number :"))
    b = int(input("Enter 2 number :"))
    addition = a + b
    if(addition > 10):
        print("Answer is Greater than 10 :" , addition)
    elif(addition < 10):
        print("Answer is Less than 10 :" , addition)    
    else:
        print("Answer is Equal to 10 :" , addition)    
        
performAddOperations()            
    
# Define Morning the time range
morning_start_time = time(0, 0) 
morning_end_time = time(12, 0) 

# Define Noon the time range
noon_start_time = time(12, 0) 
noon_end_time = time(17, 0) 

# Define Evening the time range
evening_start_time = time(17, 0) 
evening_end_time = time(20, 0) 

# Define Night the time range
night_start_time = time(20, 0) 
night_end_time = time(0, 0) 

# printing greetings on basis of time of day using if else

if(morning_start_time <= now.time() and now.time() < morning_end_time):
    print("Good Morning Nigga!")
elif(noon_start_time <= now.time() and now.time() < noon_end_time):
    print("Good Afternoon Nigga!")
elif(evening_start_time <= now.time() and now.time() < evening_end_time):
    print("Good Evening Nigga!")
else:
    print("Good Night Nigga!")      

number1 =  input("Enter 1st number nigga:")
number2 = input("Enter 2st number nigga:")

# This is Addition Algorithm
addition = int(number1)  + int(number2) 
print("Addition of numbers are" , addition) 

# This is Subtraction Algorithm
subtraction = int(number1)  - int(number2) 
print("Subtraction of numbers are" , subtraction) 

# This is Multiplication Algorithm
multiplication = int(number1)  * int(number2) 
print("Multiplication of numbers are" , multiplication) 

# This is Division Algorithm
division = int(number1) / int(number2) 
print("Addition of numbers are" , division) 

# This is Division Algorithm With whole number as answer
whole =int(number1)  // int(number2) 
print("Whole of numbers are" , whole) 

# This is Mod Algorithm
mod = int(number1)  % int(number2) 
print("Mode of numbers are" , mod) 

print("Date Time" , now) 


    

