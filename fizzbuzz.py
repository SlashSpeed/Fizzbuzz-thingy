print("Welcome to fizzbuzz! Please follow the instructions below!")


number = int(raw_input("Please enter one number between 1 and 100, right here: "))
    
print("You selected number: " + str(number) + ". This program will now count from " + str(number) + " to 100")
for number in range(number, 100):       
    if number % 3 == 0 and number % 5 == 0:
        print("fizzbuzz")
        continue
        
    if number % 3 == 0:
        print("fizz")
        continue
        
    if number % 5 == 0:
        print("buzz")
        continue
        
        
    print(number)
            
print("That's it! All done! Thank you for taking your time in testing my code.")
