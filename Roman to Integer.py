
string=input("Enter a Roman Number")
romanletter = ["I", "V" , "X" , "L" , "C" , "D" , "M" ]

roman=[]
for i in string:
    roman.append(i)
print(roman)

if set(roman).issubset(set(romanletter))==True:
    for i in range(len(roman)):
        if roman[i]=="I":
            roman[i]="1"
        if roman[i]=="V":
            roman[i]="5"
        if roman[i]=="X":
            roman[i]="10"
        if roman[i]=="L":
            roman[i]="50"
        if roman[i]=="C":
            roman[i]="100"
        if roman[i]=="D":
            roman[i]="500"
        if roman[i]=="M":
            roman[i]="1000"
    #print(roman)
    romannumber=[]
    for i in range(len(roman)):
        romannumber.append(int(roman[i]))
    #print(romannumber)
    #print(len(romannumber))
    x = len(romannumber)-1
    num = 0
    #print(x)
    for i in range(x):
        if romannumber[i] >= romannumber[i+1] :
            num += romannumber[i]
            #print(romannumber[i])
            #print("num",num)

        else:
            num -= romannumber[i]
        if i + 1 == x:
            num += romannumber[i + 1]
            #print("num2", num)
    print("Integer is:",num)





else:
    print("Invalid input")