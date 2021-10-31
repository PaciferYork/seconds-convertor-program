print("Welcome to Time Converter program.\n")

print("Please enter time in seconds\n")
inp1= int(input())
print("\n")
print("You entered", inp1, "seconds")

print("What you want to find?\nTo convert seconds to minutes enter 1,\nTo convert  seconds to hours enter 2,\nTo convert seconds to days enter 3,\nTo convert seconds to weeks enter 4.\n")
inp2 = int(input())
print ("You entered", inp2)

if inp2 == 1:
	print (inp1/60, "mins.")

elif inp2 == 2:
	print (inp1/3600, "hrs")
	
elif inp2 == 3:
	print (inp1/86400, "days")
	
else:
	print ("Under Process")


