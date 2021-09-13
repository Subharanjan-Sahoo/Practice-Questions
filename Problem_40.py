'''

We want to estimate the cost of painting a property. Interior wall painting cost is Rs.18 per sq.ft. and exterior wall painting cost is Rs.12

per sq.ft.

Take input as

1. Number of Interior walls

2. Number of Exterior walls

3. Surface Area of each Interior Wall in units of square feet

4. Surface Area of each Exterior Wall in units of square feet

If a user enters zero as the number of walls then skip Surface area values as User may don't want to paint that wall. Calculate and display the total cost of painting the property

Example 1:

6

3

12.3

15.2

12.3

15.2

12.3

15.2

10.10

10.10

10.00

Total estimated Cost: 1847.4 INR

'''
def estimate(inner_wells,ext_wells):
    inner_well_sum = 0
    inner_well_cost = 1
    exe_well_sum = 0
    if inner_wells > 0:
        for i in range(inner_wells):
            area = float(input())
            inner_well_sum = inner_well_sum + area
    inner_well_cost = 18 * inner_well_sum    
    if ext_wells > 0:
        for j in range(ext_wells):
            area = float(input())
            exe_well_sum = exe_well_sum + area 
    exe_well_cost = 12 * exe_well_sum
    

    print("Total estimated cost : ", exe_well_cost + inner_well_cost,"INR")
        


inner_wells = int(input())
ext_wells = int(input())
estimate(inner_wells, ext_wells)