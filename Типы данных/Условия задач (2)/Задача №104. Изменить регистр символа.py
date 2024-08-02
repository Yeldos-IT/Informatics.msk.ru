def ff(x):
   if x in 'asdfghjklqwertyuiopzxcvbnm':

       return x.upper()
   else:
       return x.lower()

k = input()
print(ff(k))