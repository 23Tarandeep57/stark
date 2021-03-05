import math
def check(num):
    
    for i in range(2,int(math.sqrt(int(num)))+2):
        
        if int(num)%i==0:
            print('The number is not a prime')
            print()
            break 
        
        elif int(num)%i!=0 and i>=int(math.sqrt(int(num)))+1:
            
            print("The number is prime")
            print()
        
while True:
        
    num = input("Enter the number you want to check: ")
    if int(num) >=4:
        check(num)
        
    elif int(num)==2 or int(num)==3:
        print('its a prime number')
        print()
    elif int(num) == 1:
        print("Neither composite nor prime")
        print()
    
