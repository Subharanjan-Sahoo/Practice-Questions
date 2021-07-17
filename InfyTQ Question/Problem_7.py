def Candies(sold):
    if sold >= 5 :
        print("Invalid Input")
    elif sold == 0 :
        print("Invalid Input")
        print("Number of Candies Available: ", 10)
    else :
        print("Number of Candies sold: ", sold)
        print("Number of Candies Available : " , 10 - sold)



num = int(input("Enter the number of candies are sold: "))
Candies(num)