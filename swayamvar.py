number=int(input())
bride_groom=input().split()
bride=[]
for i in bride_groom[0]:
  bride.append(i)
groom=[]
for i in bride_groom[1]:
  groom.append(i)
for i in bride:
  if i in groom:
    groom.remove(i)
  else:
    break
print(len(groom),end="") 
