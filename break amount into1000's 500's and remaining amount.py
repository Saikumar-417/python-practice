amount=int(input("enter amount:"))
notes_1000=amount//1000
print(notes_1000)
remaining_change=amount-(notes_1000*1000)
notes_500=remaining_change//500
print(notes_500)
remaining_amount=remaining_change-(notes_500*500)
print(remaining_amount)
