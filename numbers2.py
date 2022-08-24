#Python prime number script
#Author: Zakarias

def generate(num:int):
    
  list = []
  
  for x in range(num):
     x+=1
     list.append(x)

  list.pop(0)
  list.pop(num-2)
   
  for x in list:
    mssg=""
    while num%x!=0:
      mssg = str(num)+" es primo"

      break
      return mssg
    else:
       mssg = str(num)+" no es primo"
       break
       return mssg
  
  
  print(mssg)
  

generate(15)