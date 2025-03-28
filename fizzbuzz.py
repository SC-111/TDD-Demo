def num_checker(input_value):
    if input_value % 3 == 0 and input_value % 5 == 0:
        return "FizzBuzz"
    elif input_value % 3 == 0:
        return "Fizz"
    elif input_value % 5 == 0:
        return "Buzz"
    else:
        return str (input_value)
    
for i in range (50):
    print (num_checker (i))
