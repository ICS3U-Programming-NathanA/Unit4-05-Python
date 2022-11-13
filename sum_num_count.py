#!/usr/bin/env python3

# Created By: Nathan A
# Date: Nov. 13, 2022
# This program asks the user for the amount of numbers they want to add up it then adds up the numbers they enter


def main():

    # declare sum_str and sum_int to 0
    sum_str = ""
    sum_int = 0

    # Gets the total amount of numbers to be added
    total_num_str = input("Enter the amount of numbers to enter: ")

    # Try catch to catch any errors
    try:
        total_num_int = int(total_num_str)

    except:
        print("You must enter a positive integer.")
        input("Please restart.")

    if total_num_int > 0:
        # A while Loop if the total number is greater than 0
        while total_num_int > 0:
            # Gets the user_num
            user_num_str = input("Enter a number to add to the sum: ")
            print("\n")

            # Try catch the user_num to catch any errors
            try:
                user_num_int = int(user_num_str)
            except:
                print("You must enter a valid number.\n")
                continue
            else:

                # If theres only 1 number left
                if total_num_int == 1:

                    # Tells the user that the program added the user_num to the sum
                    print("Added {} to the sum\n".format(user_num_int))

                    # Adds the user_num to the string
                    sum_str += user_num_str

                    # Display the equation
                    print("{}\n".format(sum_str))

                    # Adds the integer to the sum
                    sum_int += user_num_int

                    # Decrements the total_num_int
                    total_num_int -= 1

                    continue

                elif user_num_int == 0:
                    # Tells the user the number added to the sum
                    print("Added 0 to the sum\n")
                    continue

                elif user_num_int < 0:
                    # Tells the user the number added to the sum
                    print("You must enter a positive number.")
                    continue

                else:

                    # Tells the user the number added to the sum
                    print("Added {} to the sum\n".format(user_num_int))

                    # Adds the user_num to the string
                    sum_str += user_num_str + "+"

                    # Display equation
                    print("{}\n".format(sum_str))

                    # Adds the integer form of the number to the sum
                    sum_int += user_num_int

                    # Decrements the total_num_int
                    total_num_int -= 1

                    continue
    else:
        print("You must input more than 0 numbers to enter\n")
        input("Please restart")
    print("{}".format(sum_str), "= {}".format(sum_int))
    print("Sum = {}".format(sum_int))


if __name__ == "__main__":
    main()
