phoneNumber = input("Tel nomer kiriting(eximple: 993461121): ")

result = "+998 (" + phoneNumber[0:2] + ")-" + phoneNumber[2:5] + "-" + phoneNumber[5:7] + "-" + phoneNumber[7:9]

print("Result:", result)