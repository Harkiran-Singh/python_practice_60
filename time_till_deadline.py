from  datetime import datetime

user_input = input("Enter the goal and deadline separated by colon e.g. task:dd.mm.yy\n")
user_input_list = user_input.split(':')
goal = user_input_list[0]
deadline = user_input_list[1]

deadline_date = datetime.strptime(deadline, '%d.%m.%y')
today_date = datetime.today()
time_till_deadline = deadline_date - today_date

print(f"Dear  user! Time remaining for your goal: {goal} is {time_till_deadline.days} days")