largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    
    try:
        n = int(num)
        if largest is None or largest < n:
            largest = n
        elif smallest is None or smallest > n:
            smallest = n
            
    except ValueError:
        print("Invalid input")
        continue
    
    
    

print("Maximum", largest)
print("Minimum", smallest)