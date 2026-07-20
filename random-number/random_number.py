import random 

secret  =  random.randint(1,10)
hp = 3
score = 0

while True:
    guess = int(input("ท้ายเลข1-10: "))
    
    #break loop 
    if guess == 0 :
        print("หยุดท้ายเลข")
        break

    if hp == 0:
        print("game over!")
        print("number is :",secret)
        break

    if guess == secret:
        score += 10
        print("ยินดีด้วยคุณท้ายถูก: ")
        break # ถ้ามันถูกจะออกจาก loop ทันที
    elif guess < secret:
        print("มากกว่านี้เกินไป")
    else:
        print("น้อยกว่านี้")
    hp -= 1
    print(f"เหลืิอพลังชีวิต: {hp}")

    
