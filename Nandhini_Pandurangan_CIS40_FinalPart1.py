# CIS40: Summer 2020: Final Part 1: Nandhini Pandurangan
# This program simulates a customer ordering from De Anza Grill

import time
import datetime


class Order:
    """
    Order class contains methods that allow the user to order from De Anza Grill
    # The functions in this class are __init__(), displayMenu(), getInput(),
    # calculate_bill(), displayBill, and saveToFile()
    """
    def __init__(self, customer_name):
        """
        Constructor receives one argument and initializes instance variables
        """
        self.customer_name = customer_name
        self._NUM_BURGERS = 5
        self._burger_prices = {"De Anza Burger": 5.25, "Bacon Cheese": 5.75, "Mushroom Swiss": 5.95,
                               "Western Burger": 5.95, "Don Cali Burger": 5.95}
        self._burger_quantities = {"De Anza Burger": 0, "Bacon Cheese": 0, "Mushroom Swiss": 0, "Western Burger": 0,
                                   "Don Cali Burger": 0}
        self._STAFF_TAX = 0.09
        self._staff_status = True  # default true

    def displayMenu(self):
        """
        Displays the menu
        """
        # formatting the output
        menu_msg = "DE ANZA GRILL MENU"

        print("\n", "-" * 35)
        print(menu_msg.center(35))
        print()

        print("ITEM:             ", " PRICE:  ", "Order #:")

        # using a for loop to iterate through burger_names and burger_prices
        i = 1
        for key, value in self._burger_prices.items():
            space = " " * (18 - len(key))
            space2 = " " * 7
            print(key, space, value, space2, i)
            i += 1

        print("\n", "-" * 35)

    def getInput(self):
        """ Gets the user input for staff_status and burger_quantities"""

        flag0 = True  # controls input validation for staff_status

        print("\nHi! I will be taking your order today!\n")

        while flag0:  # checking if customer is student or staff
            customer_status = input("Are you student or staff? Enter 'p' for student and 'r' for staff: ").strip()
            customer_status = customer_status.lower()  # making the input lowercase so it is easier to check
            if customer_status == 'r':
                self._staff_status = True
                flag0 = False
            elif customer_status == 'p':
                self._staff_status = False
                flag0 = False
            else:
                print("\n-----ERROR! Please enter 'p' or 'r' ----- \n")

        # ------------------------------- gathering user input for order and quantity -----------------------------
        flag1 = True  # controls order_num, quantity, and exit_status input validation
        order_num = 0
        quantity = 0

        print("\nWhat would you like to order today?")
        while flag1:
            flag2 = True  # controls order_num
            flag3 = True  # controls quantity
            flag4 = True  # controls exit

            while flag2:  # validating order_num input
                try:
                    order_num = input("Please enter the order number or 'e' to exit: ").strip()
                    if order_num == 'E' or order_num == 'e':  # if user wishes to exit
                        flag1 = False
                        flag2 = False
                        flag3 = False
                        flag4 = False
                        continue

                    order_num = int(order_num)

                    if order_num <= 0:  # if order_num is negative
                        print("\n-----ERROR: please enter a valid order number!-----\n")
                        continue
                    elif order_num > self._NUM_BURGERS:  # else if order_num is greater than the number of burgers
                        print("\n-----ERROR: please enter a valid order number!-----\n")
                        continue
                    else:  # else order_num is a valid order
                        flag2 = False

                except:  # if order_num is not an integer
                    print("\n-----ERROR: please enter a valid order number!-----\n")

            while flag3:  # validating quantity of order
                try:
                    quantity = int(input(
                        "\nHow many {0}s would you like? ".format(list(self._burger_prices)[order_num - 1])).strip())

                    if quantity < 0:  # if order_num is negative
                        print("\n-----ERROR: please enter a valid quantity!-----\n")
                        continue
                    else:  # else quantity is a valid integer

                        # indexing the dictionary to access the correct key and using the key to update the quantity
                        self._burger_quantities[list(self._burger_quantities)[order_num - 1]] += quantity
                        flag3 = False

                except:  # if quantity is not an integer
                    print("\n-----ERROR: please enter a valid quantity!-----\n")

            while flag4:  # validating exit_status
                exit_status = input(
                    "\nWould you like to order anything else today? Enter 'y' for yes and 'n' for no: ").strip()
                exit_status = exit_status.lower()  # making the input lowercase so it is easier to check
                if exit_status == 'n':  # if user wishes to exit
                    flag4 = False
                    flag1 = False
                elif exit_status == 'y':  # if user wishes to continue shopping
                    flag4 = False
                    self.displayMenu()
                else:  # if user enters input other than "y" or "n"
                    print("\n-----ERROR: please enter 'y' or 'n' -----\n")

        print("\nThank you for shopping with us!")

    def calculate_bill(self):
        """ Calculates the bill using burger_prices and burger_quantities """

        subtotal = 0  # total before tax
        total = 0
        tax = 0

        # iterating through burger_prices and burger_quantities lists to get subtotal
        for i in range(len(self._burger_prices)):
            subtotal += list(self._burger_prices.values())[i] * list(self._burger_quantities.values())[i]

        # calculate tax only if the customer is staff
        if self._staff_status:
            tax = subtotal * self._STAFF_TAX
            total = subtotal + tax
        else:
            total = subtotal

        # formatting the numbers
        subtotal = round(subtotal, 2)
        total = round(total, 2)
        tax = round(tax, 2)

        return subtotal, total, tax

    def displayBill(self, subtotal, total, tax):
        """ Displays the bill """

        # does not display bill if the customer did not buy anything
        if subtotal == 0:
            print("See you next time!")
            return False  # False is returned if the bill was not printed

        # printing out the bill
        bill_msg = "DE ANZA GRILL BILL"

        print("\n", "-" * 35)
        print(bill_msg.center(35))
        print()
        print("Customer: ", self.customer_name, "\n")
        print("ITEM:             ", "Quantity:", " COST:  ")

        # print out the items only if the quantity bought is greater than zero
        for i in range(len(self._burger_prices)):
            if list(self._burger_quantities.values())[i] > 0:
                space = " " * (21 - len(list(self._burger_prices)[i]))
                space2 = " " * 4
                print(list(self._burger_prices)[i], space, list(self._burger_quantities.values())[i], space2,
                      "%.2f" % (list(self._burger_prices.values())[i] * list(self._burger_quantities.values())[i]))

        print("\n", "-" * 35)
        print("\t\t\t Subtotal: %.2f" % subtotal)

        # print out the tax only if the user is staff
        if self._staff_status:
            print("\t\t\t Tax:      %.2f" % tax)

        # print total
        print("\t\t\t Total:    %.2f" % total)

        return True  # True is returned if the bill was printed

    def saveToFile(self, subtotal, total, tax):
        """ Saves the bill to a file"""

        # creating the name of the file to be written to
        timeStamp = time.time()
        orderTimeStamp = datetime.datetime.fromtimestamp(timeStamp).strftime('%Y-%m-%d %H-%M-%S')
        orderTimeStamp += ".txt"

        # "with open" makes sure that file is closed at the end
        with open(orderTimeStamp, "w") as receipt:

            # writing the bill to file
            bill_msg = "DE ANZA GRILL BILL\n"
            dash = "\n" + "-" * 35 + "\n"

            receipt.write(dash)
            receipt.write(bill_msg.center(35))
            receipt.write("\n")

            customer_info = "Customer: " + self.customer_name + "\n\n"
            receipt.write(customer_info)


            bill_item_header = "ITEM:             " + "Quantity:" + " COST:  \n"
            receipt.write(bill_item_header)

            # write the items only if the quantity bought is greater than zero
            for i in range(len(self._burger_prices)):
                if list(self._burger_quantities.values())[i] > 0:
                    space = " " * (21 - len(list(self._burger_prices)[i]))
                    space2 = " " * 6
                    item = list(self._burger_prices)[i] + space + str(
                        list(self._burger_quantities.values())[i]) + space2 + str(
                        round(list(self._burger_prices.values())[i] * list(self._burger_quantities.values())[i], 2)) + "\n"
                    receipt.write(item)
            receipt.write(dash)

            subtotal_msg = "\t\t\t Subtotal: " + str(subtotal) + "\n"
            receipt.write(subtotal_msg)

            # write the tax only if the user is staff
            if self._staff_status:
                tax_msg = "\t\t\t Tax:      " + str(tax) + "\n"
                receipt.write(tax_msg)

            # write total
            total_msg = "\t\t\t Total:    " + str(total) + "\n"
            receipt.write(total_msg)

