time=int(input("enter seconds:"))
hours=time//3600
print(hours)
remaining_seconds=time-(hours*3600)
minutes=remaining_seconds//60
print(minutes)
remaining_seconds=remaining_seconds-(minutes*60)
print(remaining_seconds)
