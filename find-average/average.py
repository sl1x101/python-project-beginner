
number_lists = []
total_average = 0

while True:
    # check number 
    try :
        value = int(input("Enter number(0 to exit )"))
    except ValueError:
        print("Enter number!")
        continue

    # exit program
    if value == 0 :
        print("Exit.....")
        break
    
    number_lists.append(value)

if number_lists:
    total_average = sum(number_lists) / len(number_lists)
    print(f"Number: {number_lists}")
    print(f"Total: {len(number_lists)}")
    print(f"average: {total_average.f2}")
else:
    print("No Data in list....")
    



