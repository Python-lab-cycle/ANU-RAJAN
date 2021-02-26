fn = open('test2.txt', 'r')
#read the content of the file line by line
list = fn.readlines()
print("content of file\n\n",list)
fn.close()
