import random 

secret  =  random.randint(1,10)
count_round = 0
while True:
    guess = int(input("ท้ายเลข1-10: "))
    print(f"count: {count_round}")
    
    #break loop 
    if guess == 0 :
        print("หยุดท้ายเลข")
        break

    if count_round == 3:
        print("game over!")
        print("number is :",secret)
        break
    #condition check hight to low if 
    if guess  > secret:
        print ("Hight")
    elif guess < secret :
        print("Low")

    if guess == secret:
        print("ยินดีด้วยคุณท้ายถูก: ")
        break # ถ้ามันถูกจะออกจาก loop ทันที
    else:
        print("ผิดลองใหม่")
    count_round += 1


    
