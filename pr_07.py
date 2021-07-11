post=input("enter any post: ")

if("harry" in post):
    flag=True
elif("Harry" in post):
    flag=True
elif("HaRRy" in post):
    flag=True
elif("HarRY" in post):
    flag=True
else:
    flag=False

if(flag):
    print("harry is in the post")
else:
    print("not in post")