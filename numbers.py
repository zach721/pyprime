#Python prime number script
#Author: Zakarias
#You can use this software for free
#and modify it in your own projects

def generate(num:int):
    
  list = []

  for x in range(num):
     x+=1
     list.append(x)

  list.pop(0)
  list.pop(num-2)
  
  mssg2 = []
  for x in list:
    mssg=""  

    while num%x!=0:
      mssg = str(num)+" is prime"

      break
    else:
       break

  if mssg!='':
   mssg2.append(mssg)  
   for z in mssg2:
    print(z)
   
  

def printnumber(numb:int):

 
  print('1 is prime')

  print('2 is prime')

  for x in range(numb):
    if x == 0:
        continue
    if x == 1:
        continue
    if x == 2:
        continue
    generate(x)
    

printnumber(300)

