num = int(input())
son = 0
while num>0:
    if num%2 == 0:
            num//=2
    else:
            num-=1
    son+=1    
print(son)