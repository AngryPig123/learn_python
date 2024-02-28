answer_1 = "Welcome to the tip calculator."
answer_2 = "What was the total bill?$"
answer_3 = "What percentage tip should you like to give? 10, 12, or 15?"
answer_4 = "How many people to split the bill?"

print(answer_1)
bill = float(input(answer_2))
tip = int(input(answer_3))
people = int(input(answer_4))

pay = (bill / people) * (1 + round(tip / 100, 2))

print(f"Each person should pay: ${'{:.2f}'.format(pay)}")
