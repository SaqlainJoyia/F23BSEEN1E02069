# Display number divisible by 5 from a list 
 
list= [10, 20, 33, 46, 55]

print("Given list: ",list)
print("Divisible 5 : ")

for number in list:
    if number % 5 ==0:
        print(number)
