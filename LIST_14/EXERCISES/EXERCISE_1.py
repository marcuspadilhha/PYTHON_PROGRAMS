test= list()
test.append('Marcus')
test.append(31)
guys=list()
guys.append(test[:])
test[0]='Maria'
test[1]=22
guys.append(test)
print(guys)