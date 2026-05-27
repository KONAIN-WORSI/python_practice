def arm_strong():
    raw_input = input("Enter your number: ")
    
    num_length = len(raw_input)
    
    num = int(raw_input)
    
    total_sum = 0 
    for digit in raw_input:
        digits = int(digit)
        total_sum += digits ** num_length
        
    
    if total_sum == num:
        print(f"This is {num} arm strong number")
    else:
        print(f"This is {num} not arm strong number")\
        
        
        
arm_strong()
    