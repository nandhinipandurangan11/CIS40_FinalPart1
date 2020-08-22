# CIS40: Summer 2020: Final Part 1: Nandhini Pandurangan
# This file imports the Order Class from Nandhini_Pandurangan_CIS40_FinalPart1.py
# It creates Order objects and runs the related methods

from Nandhini_Pandurangan_CIS40_FinalPart1 import Order

# if this file is being run directly,
if __name__ == '__main__':
    flag = True

    while flag:

        # using the customer name to initialize the Order object
        customer_name = input("\nWhat is your name? ")

        # calling related methods
        o = Order(customer_name)
        o.displayMenu()
        o.getInput()
        subtotal, total, tax = o.calculate_bill()
        if o.displayBill(subtotal, total, tax):
            o.saveToFile(subtotal, total, tax)

        # Continuing for the next customer
        invalid_input = True

        # input validation
        while invalid_input:
            next_customer = input("\nWould the next customer like to place their order? Y/N: ")
            next_customer = next_customer.upper()

            if next_customer == 'Y':
                flag = True
                invalid_input = False

            elif next_customer == 'N':
                flag = False
                invalid_input = False
                print("\n ----De Anza Grill is closed---- \n ")

            else:
                print("\n-----ERROR! Please enter 'Y' or 'N' ----- \n")


""" 
Output 1: 

What is your name? Siri Cortana 

 -----------------------------------
         DE ANZA GRILL MENU        

ITEM:               PRICE:   Order #:
De Anza Burger      5.25         1
Bacon Cheese        5.75         2
Mushroom Swiss      5.95         3
Western Burger      5.95         4
Don Cali Burger     5.95         5

 -----------------------------------

Hi! I will be taking your order today!

Are you student or staff? Enter 'p' for student and 'r' for staff: w

-----ERROR! Please enter 'p' or 'r' ----- 

Are you student or staff? Enter 'p' for student and 'r' for staff: P

What would you like to order today?
Please enter the order number or 'e' to exit: 9

-----ERROR: please enter a valid order number!-----

Please enter the order number or 'e' to exit: 2

How many Bacon Cheeses would you like? 1

Would you like to order anything else today? Enter 'y' for yes and 'n' for no: i

-----ERROR: please enter 'y' or 'n' -----


Would you like to order anything else today? Enter 'y' for yes and 'n' for no: Y

 -----------------------------------
         DE ANZA GRILL MENU        

ITEM:               PRICE:   Order #:
De Anza Burger      5.25         1
Bacon Cheese        5.75         2
Mushroom Swiss      5.95         3
Western Burger      5.95         4
Don Cali Burger     5.95         5

 -----------------------------------
Please enter the order number or 'e' to exit: e

Thank you for shopping with us!

 -----------------------------------
         DE ANZA GRILL BILL        

Customer:  Siri Cortana  

ITEM:              Quantity:  COST:  
Bacon Cheese           1      5.75

 -----------------------------------
			 Subtotal: 5.75
			 Total:    5.75

Would the next customer like to place their order? Y/N: o

-----ERROR! Please enter 'Y' or 'N' ----- 


Would the next customer like to place their order? Y/N: Y

What is your name? Charlotte Web

 -----------------------------------
         DE ANZA GRILL MENU        

ITEM:               PRICE:   Order #:
De Anza Burger      5.25         1
Bacon Cheese        5.75         2
Mushroom Swiss      5.95         3
Western Burger      5.95         4
Don Cali Burger     5.95         5

 -----------------------------------

Hi! I will be taking your order today!

Are you student or staff? Enter 'p' for student and 'r' for staff: r

What would you like to order today?
Please enter the order number or 'e' to exit: e

Thank you for shopping with us!
See you next time!

Would the next customer like to place their order? Y/N: n

 ----De Anza Grill is closed---- 
 
------------------------------------------------------------------------------------------

Output2: 

What is your name? Nandhini Pandurangan

 -----------------------------------
         DE ANZA GRILL MENU        

ITEM:               PRICE:   Order #:
De Anza Burger      5.25         1
Bacon Cheese        5.75         2
Mushroom Swiss      5.95         3
Western Burger      5.95         4
Don Cali Burger     5.95         5

 -----------------------------------

Hi! I will be taking your order today!

Are you student or staff? Enter 'p' for student and 'r' for staff: P

What would you like to order today?
Please enter the order number or 'e' to exit: 6

-----ERROR: please enter a valid order number!-----

Please enter the order number or 'e' to exit: 3

How many Mushroom Swisss would you like? 5

Would you like to order anything else today? Enter 'y' for yes and 'n' for no: Y

 -----------------------------------
         DE ANZA GRILL MENU        

ITEM:               PRICE:   Order #:
De Anza Burger      5.25         1
Bacon Cheese        5.75         2
Mushroom Swiss      5.95         3
Western Burger      5.95         4
Don Cali Burger     5.95         5

 -----------------------------------
Please enter the order number or 'e' to exit: 1

How many De Anza Burgers would you like? 6

Would you like to order anything else today? Enter 'y' for yes and 'n' for no: y

 -----------------------------------
         DE ANZA GRILL MENU        

ITEM:               PRICE:   Order #:
De Anza Burger      5.25         1
Bacon Cheese        5.75         2
Mushroom Swiss      5.95         3
Western Burger      5.95         4
Don Cali Burger     5.95         5

 -----------------------------------
Please enter the order number or 'e' to exit: 1

How many De Anza Burgers would you like? 2

Would you like to order anything else today? Enter 'y' for yes and 'n' for no: u

-----ERROR: please enter 'y' or 'n' -----


Would you like to order anything else today? Enter 'y' for yes and 'n' for no: n

Thank you for shopping with us!

 -----------------------------------
         DE ANZA GRILL BILL        

Customer:  Nandhini Pandurangan 

ITEM:              Quantity:  COST:  
De Anza Burger         8      42.00
Mushroom Swiss         5      29.75

 -----------------------------------
			 Subtotal: 71.75
			 Total:    71.75

Would the next customer like to place their order? Y/N: i

-----ERROR! Please enter 'Y' or 'N' ----- 


Would the next customer like to place their order? Y/N: y

What is your name? Walt Disney

 -----------------------------------
         DE ANZA GRILL MENU        

ITEM:               PRICE:   Order #:
De Anza Burger      5.25         1
Bacon Cheese        5.75         2
Mushroom Swiss      5.95         3
Western Burger      5.95         4
Don Cali Burger     5.95         5

 -----------------------------------

Hi! I will be taking your order today!

Are you student or staff? Enter 'p' for student and 'r' for staff: r

What would you like to order today?
Please enter the order number or 'e' to exit: 2

How many Bacon Cheeses would you like? 2

Would you like to order anything else today? Enter 'y' for yes and 'n' for no: Y

 -----------------------------------
         DE ANZA GRILL MENU        

ITEM:               PRICE:   Order #:
De Anza Burger      5.25         1
Bacon Cheese        5.75         2
Mushroom Swiss      5.95         3
Western Burger      5.95         4
Don Cali Burger     5.95         5

 -----------------------------------
Please enter the order number or 'e' to exit: 4

How many Western Burgers would you like? 3

Would you like to order anything else today? Enter 'y' for yes and 'n' for no: N

Thank you for shopping with us!

 -----------------------------------
         DE ANZA GRILL BILL        

Customer:  Walt Disney 

ITEM:              Quantity:  COST:  
Bacon Cheese           2      11.50
Western Burger         3      17.85

 -----------------------------------
			 Subtotal: 29.35
			 Tax:      2.64
			 Total:    31.99

Would the next customer like to place their order? Y/N: i

-----ERROR! Please enter 'Y' or 'N' ----- 


Would the next customer like to place their order? Y/N: N

 ----De Anza Grill is closed---- 
"""