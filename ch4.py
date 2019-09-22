largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" :
        break
    elif num != "done":
        try:
            n=float(num)
        except:
            print('Invalid input')
            continue
        if smallest is None:
            smallest=n
            largest=n
        elif n <smallest:
            smallest=n
        elif n > largest:
            largest=n

print("Maximum is ", int(largest))
print('Minimum is ',int(smallest))
