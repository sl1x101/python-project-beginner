import random as rm


#สุ่มเลข

secret  =  rm.randint(1,10)
guess = int(input("ท้ายตัวเลข 1-10: "))
print("เลขที่คุณท้าย: ",guess)