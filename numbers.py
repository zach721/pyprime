#Python prime number script
#Author: Zakarias

def generate(num:int):
    
  list = []
  for x in range(num):
     x+=1
     list.append(x)

  list.pop(0)
  list.pop(num-2)
  mssg=""
  for x in list:
  
    while num%x!=0:
      mssg = str(num)+" is prime"

      break
      return mssg
    else:
       #mssg = str(num)+" isn't prime"
       break
       #return mssg
  
  print(mssg)
  


def printnumber(numb:int):

  print("/$$$$$$$           /$$                                                                 /$$                                          \n"
"| $$__  $$         |__/                                                                | $$                                          \n"
"| $$  \ $$ /$$$$$$  /$$ /$$$$$$/$$$$   /$$$$$$        /$$$$$$$  /$$   /$$ /$$$$$$/$$$$ | $$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$$   \n"   
"| $$$$$$$//$$__  $$| $$| $$_  $$_  $$ /$$__  $$      | $$__  $$| $$  | $$| $$_  $$_  $$| $$__  $$ /$$__  $$ /$$__  $$ /$$_____/      \n"   
"| $$____/| $$  \__/| $$| $$ \ $$ \ $$| $$$$$$$$      | $$  \ $$| $$  | $$| $$ \ $$ \ $$| $$  \ $$| $$$$$$$$| $$  \__/|  $$$$$$    \n"
"| $$     | $$      | $$| $$ | $$ | $$| $$_____/      | $$  | $$| $$  | $$| $$ | $$ | $$| $$  | $$| $$_____/| $$       \____  $$   \n"   
"| $$     | $$      | $$| $$ | $$ | $$|  $$$$$$$      | $$  | $$|  $$$$$$/| $$ | $$ | $$| $$$$$$$/|  $$$$$$$| $$       /$$$$$$$/    \n"  
"|__/     |__/      |__/|__/ |__/ |__/ \_______/      |__/  |__/ \______/ |__/ |__/ |__/|_______/  \_______/|__/      |_______/     \n")

  print('1 is prime\n')

  print('2 is prime\n')

  for x in range(numb):
    if x == 0:
        continue
    if x == 1:
        continue
    if x == 2:
        continue
    generate(x)
    

printnumber(30)