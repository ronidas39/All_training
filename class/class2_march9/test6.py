#find if hello is present or not
sample="hello"
cl=["yes","ok","k"]
k=0
for i in cl:
    if(i==sample):
        print("match found")
        k=1
        break
if(k==0):
    print("not found")
    
