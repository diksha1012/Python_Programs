sub1=int(input("enter subject 1: "))
sub2=int(input("enter subject 2: "))
sub3=int(input("enter subject 3: "))

if(sub1<33 or sub2<33 or sub3<33):
    print("fail")
elif((sub1+sub2+sub3)/3 <41):
    print("fail in total")
else:
    print("pass")