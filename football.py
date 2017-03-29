for i in range(int(input())):
    array=[]
    n,c=map(int,input().split())
    array.append(c)
    for j in range(n):
        s=input().split()
        if s[0]=='P':
            array.append(s[1])
        if s[0]=='B':
            array[len(array)-1],array[len(array)-2]=array[len(array)-2],array[len(array)-1]
    print("Player",array[len(array)-1])
