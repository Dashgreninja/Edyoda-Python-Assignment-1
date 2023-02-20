numbers=[]
while True:
    elements=(input("Enter no. or Enter 'q' to quit : "))
    if elements=='q':
        break
    else:
        numbers.append(int(elements))
    
even=0
odd=0
for i in numbers:
    if i % 2 == 0:
        even+=1
    else:
        odd+=1
print('Number of even numbers : ',even)
print('Number of odd numbers : ',odd)
