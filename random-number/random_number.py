import random 

#สุ่มเลข

secret  =  random.randint(1,10)

while True:
    guess = int(input("ท้ายเลข1-10: "))

    if guess == secret:
        print("ยินดีด้วยคุณท้ายถูก: ")
        break # ถ้ามันถูกจะออกจาก loop ทันที
    else:
        print("ผิดลองใหม่")

    
