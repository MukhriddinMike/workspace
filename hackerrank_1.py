if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
list=[]
list2=[]
for i in range(x+1):
    for k in range(y+1):
        for j in range(z+1):
            if(i+j+k!=n):
                list2=[i,k,j]
                list.append(list2)
print(list)







