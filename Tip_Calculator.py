print("***Welcome to Tip Calculator!***")
bill=float(input("Enter Total Bill: "))
tip=int(input("How much tip would you like to give? 10, 12 or 15: "))
bill_spliting=int(input("How many people to split the bill?: "))
result=bill*tip/100
final_result=round((bill+result)/bill_spliting,2)
print(f"Each person should pay: ${final_result}")