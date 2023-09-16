

# Cafe's Order System 

# Utilizing Everything I've learned from the NetworkChuck Python Course

print("Welcome to Doki-Doki Cafe!" )

Name = input("\nWhat should I call you, dear customer?\n" + "\nYour name: ")

V = input("\nAre you a Vegetarian or not? \n\nYes(Y) / No(N): ")

MenuDic= {False : "MENU \n\n Drinks:\n  A. Coffee\n  B. Tea\n  C. Strawberry Milkshake\n \n\n Food:\n  D. Fish and Chips\n  E. Burger and Fries\n  F. Steak with Gravy",
         
          True : "VEGETARIAN MENU \n\n Drinks:\n  A. Dairy-Free Coffee\n  B. Tea\n  C. Kiwi Smoothie\n\n Food:\n  D. Coconut Tofu Stir-Fry\n  E. Adobo Mushroom Tacos\n  F. Baked Oatmeal"}

#Responses

#Yes or No responses
responseN = ["No", "No.", "no", "no.", "Nope", "Nope.", "N" , "n"]

responseY = ["Yes", "yes", "yes.", "Yes.", "Yup", "Yup.", "Y", "y"]

#Menu responses


letter = {1: "a" or "A" or "Letter a." or "Letter A." or "Letter A" or "Letter a" or "Choice A." or "Choice a." or "Choice A" or "Choice a",
          2: "b" or "B" or "Letter b." or "Letter B." or "Letter B" or "Letter b" or "Choice B." or "Choice b." or "Choice B" or "Choice b",
          3: "c" or "C" or "Letter c." or "Letter C." or "Letter C" or "Letter c" or "Choice C." or "Choice C." or "Choice C" or "Choice c",
          4: "d" or "D" or "Letter d." or "Letter D." or "Letter D" or "Letter d" or "Choice D." or "Choice d." or "Choice D" or "Choice d",
          5: "e" or "E" or "Letter e." or "Letter E." or "Letter E" or "Letter e" or "Choice E." or "Choice e." or "Choice E" or "Choice e",
          6: "f" or "F" or "Letter f." or "Letter F." or "Letter F" or "Letter f" or "Choice F." or "Choice f." or "Choice F" or "Choice f"}


items = {}


# Main Function
def myFunction():

    TotalOrders = int(input("Here's the menu." + " What would you like today?\n\n\n" + menu
                           + "\n\n\nNumber of items to order: "))

    if TotalOrders == 1:

        order1 = input("\n\nInput your 1st Order: ")

        NumOrder1 = input("\nHow many " + items[order1] + "(s) do you want?\n" + "\nNumber of " + items[order1] + ": ")

        orderT = int(NumOrder1)

        total = price * orderT

        print("\nAlright, " + NumOrder1 + " of " + items[order1] + "(s)."
             + "\n\nGood choice!" + "\n\nYour total will be $" + str(total) + "\n\nWe'll deliver your order as fast as possible.\n")

        exit()


    elif TotalOrders == 2: 

        order1 = input("\n\nInput your 1st Order: ")

        NumOrder1 = input("\nHow many " + items[order1] + "(s) do you want?\n" + "\nNumber of " + items[order1] + ": ")

        order2 = input("\nInput your 2nd Order: ")

        NumOrder2 = input("\nHow many " + items[order2] + "(s) do you want?\n" + "\nNumber of " + items[order2] + ": ")

        orderT = int(NumOrder1) + int(NumOrder2)

        total = price * orderT

        print("\nAlright, " + NumOrder1 + " of " + items[order1] + "(s) and "
             + NumOrder2 + " of " + items[order2] + "(s)."
           + "\n\nGood choices!" + "\n\nYour total will be $" + str(total) + "\n\nWe'll deliver your order as fast as possible.\n")

        exit()


    elif TotalOrders == 3:

        order1 = input("\n\nInput your 1st Order: ")

        NumOrder1 = input("\nHow many " + items[order1] + "(s) do you want?\n" + "\nNumber of " + items[order1] + ": ")

        order2 = input("\nInput your 2nd Order: ")

        NumOrder2 = input("\nHow many " + items[order2] + "(s) do you want?\n" + "\nNumber of " + items[order2] + ": ")

        order3 = input("\n\nInput your 3rd Order: ")

        NumOrder3 = input("\nHow many " + items[order3] + "(s) do you want?\n" + "\nNumber of " + items[order3] + ": ")

        orderT = int(NumOrder1) + int(NumOrder2) + int(NumOrder3)

        total = price * orderT

        print("\nAlright, " + NumOrder1 + " " + items[order1] + "(s), "
             + NumOrder2 + " " + items[order2] + "(s), and"
            + NumOrder3 + " " + items[order3] + "(s)."
           + "\n\nGood choices!" + "\n\nYour total will be $" + str(total) + "\n\nWe'll deliver your order as fast as possible.\n")

        exit()

    elif TotalOrders == 4:

        
        order1 = input("\n\nInput your 1st Order: ")

        NumOrder1 = input("\nHow many " + items[order1] + "(s) do you want?\n" + "\nNumber of " + items[order1] + ": ")

        order2 = input("\nInput your 2nd Order: ")

        NumOrder2 = input("\nHow many " + items[order2] + "(s) do you want?\n" + "\nNumber of " + items[order2] + ": ")

        order3 = input("\n\nInput your 3rd Order: ")

        NumOrder3 = input("\nHow many " + items[order3] + "(s) do you want?\n" + "\nNumber of " + items[order3] + ": ")

        order4 = input("\n\nInput your 3rd Order: ")

        NumOrder4 = input("\nHow many " + items[order4] + "(s) do you want?\n" + "\nNumber of " + items[order4] + ": ")

        orderT = int(NumOrder1) + int(NumOrder2) + int(NumOrder3) + int(NumOrder4)

        total = price * orderT

        print("\nAlright, " + NumOrder1 + " " + items[order1] + "(s), "
             + NumOrder2 + " " + items[order2] + "(s),"
            + NumOrder3 + " " + items[order3] + "(s), and" 
            + NumOrder4 + " " + items[order4] +"(s)."
           + "\n\nGood choices!" + "\n\nYour total will be $" + str(total) + "\n\nWe'll deliver your order as fast as possible.\n")

        exit()

    elif TotalOrders == 5:

        order1 = input("\n\nInput your 1st Order: ")

        NumOrder1 = input("\nHow many " + items[order1] + "(s) do you want?\n" + "\nNumber of " + items[order1] + ": ")

        order2 = input("\nInput your 2nd Order: ")

        NumOrder2 = input("\nHow many " + items[order2] + "(s) do you want?\n" + "\nNumber of " + items[order2] + ": ")

        order3 = input("\n\nInput your 3rd Order: ")

        NumOrder3 = input("\nHow many " + items[order3] + "(s) do you want?\n" + "\nNumber of " + items[order3] + ": ")

        order4 = input("\n\nInput your 4th Order: ")

        NumOrder4 = input("\nHow many " + items[order4] + "(s) do you want?\n" + "\nNumber of " + items[order4] + ": ")

        order5 = input("\n\nInput your 5th Order: ")

        NumOrder5 = input("\nHow many " + items[order5] + "(s) do you want?\n" + "\nNumber of " + items[order5] + ": ")

        orderT = int(NumOrder1) + int(NumOrder2) + int(NumOrder3) + int(NumOrder4) + int(NumOrder5)

        total = price * orderT

        print("\nAlright, " + NumOrder1 + " " + items[order1] + "(s), "
             + NumOrder2 + " " + items[order2] + "(s),"
            + NumOrder3 + " " + items[order3] + "(s),"
            + NumOrder4 + " " + items[order4] +"(s), and"
            + NumOrder5 + " " + items[order5] +"(s)."
           + "\n\nGood choices!" + "\n\nYour total will be $" + str(total) + "\n\nWe'll deliver your order as fast as possible.\n")

        exit()

    elif TotalOrders == 6:

        order1 = input("\n\nInput your 1st Order: ")

        NumOrder1 = input("\nHow many " + items[order1] + "(s) do you want?\n" + "\nNumber of " + items[order1] + ": ")

        order2 = input("\nInput your 2nd Order: ")

        NumOrder2 = input("\nHow many " + items[order2] + "(s) do you want?\n" + "\nNumber of " + items[order2] + ": ")

        order3 = input("\n\nInput your 3rd Order: ")

        NumOrder3 = input("\nHow many " + items[order3] + "(s) do you want?\n" + "\nNumber of " + items[order3] + ": ")

        order4 = input("\n\nInput your 4th Order: ")

        NumOrder4 = input("\nHow many " + items[order4] + "(s) do you want?\n" + "\nNumber of " + items[order4] + ": ")

        order5 = input("\n\nInput your 5th Order: ")

        NumOrder5 = input("\nHow many " + items[order5] + "(s) do you want?\n" + "\nNumber of " + items[order5] + ": ")

        order6 = input("\n\nInput your 6th Order: ")

        NumOrder6 = input("\nHow many " + items[order6] + "(s) do you want?\n" + "\nNumber of " + items[order6] + ": ")

        orderT = int(NumOrder1) + int(NumOrder2) + int(NumOrder3) + int(NumOrder4) + int(NumOrder5) + int(NumOrder6)

        total = price * orderT

        print("\nAlright, " + NumOrder1 + " " + items[order1] + "(s), "
             + NumOrder2 + " " + items[order2] + "(s),"
            + NumOrder3 + " " + items[order3] + "(s),"
            + NumOrder4 + " " + items[order4] +"(s),"
            + NumOrder5 + " " + items[order5] +"(s), and"
            + NumOrder6 + " " + items[order6] + "(s)."
           + "\n\nGood choices!" + "\n\nYour total will be $" + str(total) + "\n\nWe'll deliver your order as fast as possible.\n")

        exit()

    elif TotalOrders >= 7:

        print("\nSorry. We only have six items in the menu.")

        myFunction()

        exit()


# Start

print("\nWelcome, " + Name + "!\n")


if V in responseY:

    menu = MenuDic[True]

    price = 6

    items = { letter[1]: "Dairy-Free Coffee", letter[2]: "Tea", letter[3] : "Kiwi Smoothie", letter[4] : "Coconut Tofu Stir-Fry", letter[5]: "Adobo Mushroom Tacos", letter[6] : "Baked Oatmeal"}

    myFunction()

elif V in responseN:

    menu = MenuDic[False]

    price = 5

    items = { letter[1]: "Coffee", letter[2]: "Tea", letter[3] : "Strawberry Milkshake", letter[4] : "Fish and Chips", letter[5]: "Burger and Fries", letter[6] : "Steak and Gravy"}

    myFunction()

#End