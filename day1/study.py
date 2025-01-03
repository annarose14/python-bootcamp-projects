a= "helloworld"
print("wor" in a)
count=0
for letter in 'helloworld':
    if(letter=='l'):
        count+=1
print(count,'letters found')

str1 = list(enumerate(a))
print(str1)
print(id(a))

