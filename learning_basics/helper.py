user_input_message = "Hey user, enter number of days and conversion unit! Write 'x' to exit:\n"

def days_to_units(number_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{number_of_days} days are {number_of_days * 24} hours"
    elif conversion_unit == "minutes":
        return f"{number_of_days} days are {number_of_days * 24 * 60} minutes"
    else:
        return "Unsupported unit, try again!"

# ---- function for input checking w/ try/except (catch) ----
def  validate_and_execute(days_and_unit_dictionary):
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