# -----------------------------------------------
# string indexing & sliceing 
# [1] all data in python are objects
# [2] objects contain elements 
# [3] every element has it own Index 
# [4] python use zero based index (start from zero)
# [5] Use square Brackets to access element
# [6] Enable accessing part of strings, tuple or list
# ----------------------------------------------------


# indexing =>  access single element 

myString = "I love Python"
print(myString[0]) # print frist element => I
print(myString[8]) # print 9th element = > y

# negative sign make you cout from right 
print(myString[-1]) # print frist element => n
print(myString[-2]) # print frist element => o



# slicing => access multiple elements 
# [start: end]  end not included 
# [start: end: steps]


print(myString[8:11])   

print(myString[:11])   # if you don't add start it will assume you to begin from start
print(myString[5:])   # if you don't add end it will assume you to print to the end  
print(myString[:])   # if you don't add start or end it will  print whole string 



# sliceing

print(myString[: : ])   # if you don't add start or end and add stepsit will  print whole string  move step by step
print(myString[: :2])   # if you don't add start or end add steps it will move two step 
print(myString[: :3])   # if you don't add start or end add steps it will move three step 