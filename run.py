#Made for the sole purpose of GCI 2019
print()
while True:
	inp1=int(input("Enter the power from 0 to 1024 : "))
	print()
	base=2
	final=1
	for i in range(0,inp1):
		final*=base
	print("2 to the power {} is : {}".format(inp1,final))
	print()
	tmp=input("Do you want to continue[y/N]:")
	print()
	if tmp=="y":
		continue
	else:
		print("Closing...")
		break
