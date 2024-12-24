matn = input("1-matinni kiriting: ")

matn2 = input("2-matinni kiriting: ")

result = matn2 is matn # bu holatda false qiymat chiqaveradi sababi ular turli xil obyeklar hattoki qiymatlari teng bo`lsa ham`
print("result1: ", result)
matn2 = matn

result = matn2 is matn # bu holatda true qiymat chiqaveradi 

print("result2: ", result)