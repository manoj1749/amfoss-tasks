n=int(input())
y=0
for i in range(1,int(n**(0.5))+1):
  if n%i==0  :
    if n/i==i:
      y+=1
    else:
      y+=2
print(y)