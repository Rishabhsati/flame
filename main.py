def disp(n):
  if n=="f":
    print("Friends")
  elif n=="l":
    print("Lovers")
  elif n=="a":
    print("Affection")
  elif n=="m":
    print("Marriage")
  else:
    print("Enemy")
def fun1(x,y):
  i=0
  for k in range(i,len(x)):
    for j in range(0,len(y)):
      if x[i]==y[j]:
        x.pop(i)
        y.pop(j)
        i=i-1
        break
    i+=1
  return x,y
x=list(input("enter first name : "))
y=list(input("enter second name : "))
a,b=fun1(x,y)
num= len(a)+len(b)
l=["f","l","a","m","e"]
c=0
while(len(l)!= 1):
  for i in range(0,num):
    if c>= len(l):
      c=0
    c+=1
  c=c-1
  l.pop(c) 
disp(l[0])
