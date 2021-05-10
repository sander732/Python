catName= []
while True:
    print("enter the name of cat" + str(len(catName)+ 1)+ '(or enter to stop)')
    name=input()
    if name =='':
        break
    catName.append(name)
print('the cat names are')
for name in catName:
    print(''+ name)