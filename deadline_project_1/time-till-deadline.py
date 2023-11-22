# Little project - "Countdown" - to implement the basics of Python🐍
from datetime import datetime

user_input = input("Enter your goal with a deadline separated by colon!\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

# To convert string into datetime (dd.mm.yyyy)
deadline_date = datetime.strptime(deadline, "%d.%m.%Y")

# today datetime
today_date = datetime.today()

# Calculate how many days from today till deadline
countdown_till_deadline = deadline_date - today_date

# Calculate how many hours from today till deadline
countdown_till_deadline_hours = int(countdown_till_deadline.total_seconds() / 60 / 60)

user_input_question = input("Do you want to know in days or hours?\n")

if user_input_question == "days":
    print(f"Dear user! Deadline for your goal -{goal}- : {countdown_till_deadline.days} day(s) remaining!")
elif user_input_question == "hours":
    print(f"Dear user! Deadline for your goal -{goal}- : {countdown_till_deadline_hours} hour(s) remaining!")
else:
    print("Please use either days or hours!")