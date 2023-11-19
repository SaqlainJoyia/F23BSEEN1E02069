string=input("Enter the characters:")
char_len=len(string)
lst=list(string)
print("Printing only even index char")
for i in range (char_len) :
    if i%2==0:
        print(lst[i])
