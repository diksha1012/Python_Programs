# use open function to read the content of a file!
# f=open('sample.txt','r') by default the mode is r
f=open('sample.txt')
# data = f.read()
data = f.read(5) #read first 5 characters
print(data)
f.close()