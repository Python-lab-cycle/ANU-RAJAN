list=[105,20,305,40]
result=[ ]
for i in list:
    if i > 100:
        result.append('Over')
    else:
        result.append(i)
for i in result:
    print(i)
