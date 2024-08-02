string=input("")
t=""
for i in range(len(string)):
    if i%3!=0:
        t=t+string[i]
print(t)