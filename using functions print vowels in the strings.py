def listiterate(x):
    vowels="aeiouAEIOU"
    for i in x:
        if type(i)==str:
           for char in i:
               if char in vowels:
                  print(char)
listiterate(["sai","indu",2,5,6])
