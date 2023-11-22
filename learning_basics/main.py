# Starting with basic syntax
# print("Hello")
# print("20 days and " + str(50) + " minutes")
# better way to do concatenate string and int
# where f = format
# print(f"20 days and {50} minutes")

# another example
# print(f"20 days is {20 * 24 * 60} minutes")

# better example
# print(f"20 days are {20 * calculation_to_units} {name_of_units}")

# ---- function ----
# def day_to_units():
#     print(f"20 days are {20 * calculation_to_units} {name_of_units}")
#     print("All good!")

# ---- function with one parameter ----
# def day_to_units(number_of_days):
#     print(f"{number_of_days} days are {number_of_days * calculation_to_units} {name_of_units}")
#     print("All good!")

# ---- calling function ----
# days_to_units(10, "Nice")
# days_to_units(20, "Let's gooo!")

# ---- input ----
# user_input = input("Enter a number of days to convert it into hours\n")

# ---- variables ----
# calculation_to_units = 24
# name_of_units = "hours"

# # ---- function ----
# def days_to_units(number_of_days):
#     if number_of_days > 0:
#         return f"{number_of_days} days are {number_of_days * calculation_to_units} {name_of_units}"
#     elif number_of_days == 0:
#         return "You have entered zero, please enter a positve number!"
#
# # ---- function for input checking ----
# def  validate_and_execute():
#     if user_input.isdigit():
#         #  ---- casting ----
#         user_input_converted = int(user_input)
#         # ---- return variable ----
#         my_var = days_to_units(user_input_converted)
#         print(my_var)
#     else:
#         print("Enter a valid number. Stop ruining my program!")

# ---- cleaning - Look above for the previous version ----
# def days_to_units(number_of_days):
#     return f"{number_of_days} days are {number_of_days * calculation_to_units} {name_of_units}"
#
# # ---- function for input checking w/ nested if...else ----
# def  validate_and_execute():
#     if user_input.isdigit():
#         #  ---- casting ----
#         user_input_converted = int(user_input)
#         if user_input_converted > 0:
#             # ---- return variable ----
#             my_var = days_to_units(user_input_converted)
#             print(my_var)
#         elif user_input_converted == 0:
#             print("You have entered zero, please enter a positve number!")
#     else:
#         print("Enter a valid number. Stop ruining my program!")

# ---- cleaning - Look above for the previous version ----
# def days_to_units(number_of_days):
#     return f"{number_of_days} days are {number_of_days * calculation_to_units} {name_of_units}"
#
# # ---- function for input checking w/ try/except (catch) ----
# def  validate_and_execute():
#     try:
#         #  ---- casting ----
#         user_input_converted = int(num_of_days_element)
#         if user_input_converted > 0:
#             # ---- return variable ----
#             my_var = days_to_units(user_input_converted)
#             print(my_var)
#         elif user_input_converted == 0:
#             print("You have entered zero, please enter a postive number!")
#         else:
#             print("You have entered a negative number, please enter a postive number!")
#     except ValueError:
#         print("Enter a valid number. Stop ruining my program!")
#
# # ---- input ----
# user_input = ""
#
# # ---- adding While loop ----
# # while user_input != "x":
# #     user_input = input("Enter a number of days to convert it into hours, write 'x' to exit:\n")
# #     validate_and_execute()
#
# # ---- adding for loop to have list ----
# while user_input != "x":
#     user_input = input("Enter a number of days to convert it into hours, write 'x' to exit:\n")
#     # split() to convert strings into list. You can define the separator, like in the example
#     # set() to filter out duplicates
#     for num_of_days_element in set(user_input.split(", ")):
#         validate_and_execute()

# ------- NEW chapter, implementing dictionary data type

# ---- variables ----
calculation_to_units = 24
name_of_units = "hours"
user_input = ""

# ---- cleaning - Look above for the previous version ----
def days_to_units(number_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{number_of_days} days are {number_of_days * 24} hours"
    elif conversion_unit == "minutes":
        return f"{number_of_days} days are {number_of_days * 24 * 60} minutes"
    else:
        return "Unsupported unit, try again!"

# ---- function for input checking w/ try/except (catch) ----
def  validate_and_execute():
    try:
        #  ---- casting string into int - dictionary uses "key" - "days": "int"
        user_input_converted = int(days_and_unit_dictionary["days"])
        if user_input_converted > 0:
            my_var = days_to_units(user_input_converted, days_and_unit_dictionary["unit"])
            print(my_var)
        elif user_input_converted == 0:
            print("You have entered zero, please enter a postive number!")
        else:
            print("You have entered a negative number, please enter a postive number!")
    except ValueError:
        print("Enter a valid number. Stop ruining my program!")

# ---- adding for loop to have list ----
while user_input != "x":
    user_input = input("Hey user, enter number of days and conversion unit! Write 'x' to exit:\n")
    # split() to convert strings into list. You can define the separator, like in the example
    days_and_unit = user_input.split(":")
    print(days_and_unit)
    days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    print(days_and_unit_dictionary)
    print(type(days_and_unit_dictionary))
    validate_and_execute()