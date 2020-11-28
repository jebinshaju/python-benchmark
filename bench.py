import datetime

print("........}}}}}}}}}}}}}}}}........System benchmark........{{{{{{{{{{{{{{{......")
print("*Higher number more stress!!!*")
n=int(input("Enter a number to test your system : "))
now = datetime.datetime.now()
for i in range(0,n+1):
    print(i,end=" <> ")
    cn=datetime.datetime.now()
    tt=cn-now
print("The time required to complete test: ",tt)
