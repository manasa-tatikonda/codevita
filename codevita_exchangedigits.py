from itertools import permutations
number_list=[int(a) for a in input().split()]
number1=str(number_list[0])
number2=number_list[1]
diff_combinations=sorted(["".join(a) for a in permutations(number1,len(number1))])
result=-1
if(len(number1))<len(str(number2)):
  print(result)
else:
  for i in diff_combinations:
    if(int(i)>number2):
      result=int(i)
      break
  if(result!=-1):    
      print(result) 
  else:
      print(result)
