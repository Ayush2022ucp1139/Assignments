def temp_converter(choice,value):
    if(choice == 1):
        degree_fahrenheit = (9/5)*value + 32
        return degree_fahrenheit
    
    elif(choice == 2):
        degree_celsius = ((value-32)*5)/9
        return degree_celsius
    else:
        print("Enter a valid value of  choice!")

temp = int(input("Enter the value of the temperature: "))
choice = int(input("Enter 1 (to convert the value to F) or 2 (to convert the value to C): "))
converted_temp = temp_converter(choice,temp)

print(converted_temp)

# if(choice == 1):
#     print(temp + ' C ' + ' is ' + converted_temp + ' F ')
# else:
#     print(temp + ' F ' + ' is ' + converted_temp + ' C ')    




