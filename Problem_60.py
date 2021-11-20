'''
Problem Statement – Vohra went to a movie with his friends in a Wave theatre and during  
break time he bought pizzas, puffs and cool drinks. Consider   the following prices : 

Rs.100/pizza
Rs.20/puffs
Rs.10/cooldrink
Generate a bill for What Vohra has bought.

Sample Input 1:

Enter the no of pizzas bought:10
Enter the no of puffs bought:12
Enter the no of cool drinks bought:5
Sample Output 1:

Bill Details

No of pizzas:10
No of puffs:12
No of cooldrinks:5
Total price=1290
ENJOY THE SHOW!!!

'''
def BillDetails(input1,input2,input3):
    
    print("No of Pizzas: ", input1)
    print("No of Puffs: ", input2)
    print("No of Cooldrinks: ", input3)
    print("Total price : ", (100*input1)+(20*input2)+(10*input3))
    print("ENJOY THE SHOW!!!")



input1 = int(input("Enter the no of pizzas bought: "))
input2 = int(input("Enter the no of puffs bought: "))
input3 = int(input("Enter the no of cool drinks bought:"))
BillDetails(input1,input2,input3)

