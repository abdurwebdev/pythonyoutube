print("Hello");
#this is a comment
"""hello this is a multi line
comment
"""

sher = "Student"

SgeryiansSchool = "Student"

sheryiansScholl = "Student"

sheryians_scholl = "Student"

print(sher);

sher = -10
sher2 = 10.9
sher3 = 12/4

sher4 = True
sher5 = False

sher6 = 'hello'
sher6 = "hello"

sher7 = 14j

a="A"

print(ord(a))

b=65

print(chr(b));

c="Hello"

print(c[2],c[-3]);

d="SHER CODER"
print(d[0:4:1]);

e="SHER CODER"
print(e[5::1])

f="SHER CODER"
print(e[::])

g=12
g=str(g)
print(type(g))

h="12"
h=int(h)
print(type(h))

# 0 false "" 0.0 [] {} () Falsy

age = 12
name ="Abdurrehman"

print(f"hello my name is {name} and my age is {age}");

name2=input("Enter your name ");
age2=int(input("Enter your age "));

print(f"my name is {name2} and my age is {age2}");

i=10
j=20

print(i+j)
print(i-j)
print(i*j)
print(5**2)
print(20/5)
print(20//5)
print(32%5)

#assignment operators

k=20
k+=20
k+=40
k+=60
print(k)
"""
+=
-=
*=
/=
//=
%=
**=
"""
print(12==12)
print(23>10)
print(10<30)
print(23<=23)
print(45>=45)
print(12!=11)

print("A"=="A")
print("ABC"<"ACD");
#not done print("A">34)

print(12<1 and 12>2 and 30<60)
print(12<3 or 12>20 or 89<40)
print(not 12==12)


m=6
if m>10:
  print("I will do Task A")
else:
  print("I will do Task B")
money = int(input("Please Provide me the money "))

if money==10:
  print("I will have a chocobar icecream")
else:
  print("I will have a mango dolly")


choice = int(input("Please Provide me the Money -:>"))

if choice==10:
  print("I will have a chocobar icecream")
elif choice==20:
  print("I will have a mango dolly")
elif choice==30:
  print("I will have a chocobar icecream and a mango dolly")
else:
  print("You provided me more money")

num1=int(input("Enter Fistr number: "))
num2=int(input("Enter Second Number: "))

if num1>num2:
  print(f"{num1} is greater than {num2}")
elif num2>num1:
  print(f"{num2} is greater than {num1}")
else:
  print(f"{num1} is equal to {num2}")

gender = input("Enter Your Gender (M/F): ")
if gender=='M' or gender=='m':
  print("Good morning Sir!")
elif gender=='F' or gender=='f':
  print("Good Morning Mam")
else:
  print("Please enter (M/F)")

evenorodd = int(input("Enter a number: "))
if evenorodd % 2 == 0:
  print(f"{evenorodd} is Even Number")
else:
  print(f"{evenorodd} is Odd Number")

voter = input("Enter your name: ")
ages = int(input("Enter your age: "))

if ages >= 18:
     print(f"Hello {voter}, you are a valid voter");
else:
     print(f"Hello {voter}, you are not a valid voter")
leap = int(input("Enter a year: "))
if leap%100==0 and leap%400==0:
  print(f"{leap} is a leap year")
elif leap%100!=0 and leap%4==0:
  print(f"{leap} is a leap year")
else:
  print(f"{leap} is not a leap year")

temperature = int(input("Enter temperature in Celcius (35): "))

if temperature<0:
  print(f"The temperature is {temperature} and its freezing cold❄.")
elif temperature>=0 and temperature<=10:
  print(f"The temperature is {temperature} and its very cold🥶.")
elif temperature>=10 and temperature<=20:
  print(f"The temperature is {temperature} and its cold🧥.")
elif temperature>=20 and temperature<=30:
  print(f"The temperature is {temperature} and its normal🌞.")
elif temperature>=30 and temperature<=40:
  print(f"The temperature is {temperature} and its hot☀️.")
else:
  print(f"The temperature is {temperature} and its very hot🔥.")

x=range(1,21,1)

for i in a:
  print(i)

for j in range(1,101,1):
  print(j)

for n in range(21):
  print(n)

for m in range(16,0,-1):
  print(m)
for k in range(-5,-16,-1):
  print(k)

for i in range(1,11,1):
  print(f"5 * {i} = {5*i}")
for l in range(5,51,5):
  print(l)

p = int(input("Which table you want : "))

for o in range(p,(p*10)+1,p):
  print(o)

i ="SHERYIANS"

for elem in range(len(i)):
  print(i[elem])

for j in range(1,21,1):
  if j==15:
    break
  print(j)
for g in range(1,21,1):
  if g==15:
    continue
  print(g)

for f in range(1,21,1):
  if f==15:
    print("Break statement executed")
    break
else:
  print("Break statement not executed")

for d in range(1,21,1):
  if d==50:
    print("Break statement executed")
    break
else:
  print("Break statement not executed")

s=int(input("Enter how may time you want to print the hellow world!: "))

for z in range(1,s+1,1):
  print("Hello World!")

c = int(input("Enter how much upto you want to print the natural numbers"))

for v in range(1,c+1,1):
  print(v);

ab = int(input("Please enter from which to 1 you want to print: "))

for th in range(ab,0,-1):
  print(th)

sume = int(input("Enter and sum upto n terms"))
actsum=0
for fg in range(1,sume+1,1):
  actsum+=fg
print(f"Your sum of upto {sume} is {actsum}")