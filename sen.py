while true:
print("Enter 'x' for exit.")
string = input("Enter any string: ")
if string == 'x':
break
else :
word_length = len(string.split())
print("Number of words =",word_length,"\n")
