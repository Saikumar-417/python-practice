names = ['sai','manoj','ganesh','kisore','sarath']
l=len(names)
newlist=[]
for name in range(l-1,-1,-1): 
  if len(names[name])>3:
       print(names[name])
       newlist.append(names[name])
print(newlist)
       
