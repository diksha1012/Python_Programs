text=input("enter text: ")
# spam=False
if("make a lot if money" in text):
    spam=True
elif("buy now" in text):
    spam=True
elif("click this" in text):
    spam=True
elif("subscribe this" in text):
    spam=True
else:
    spam=False

if(spam):
    print("this is spam")
else:
    print("not a spam")
