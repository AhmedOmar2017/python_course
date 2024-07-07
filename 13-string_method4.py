# --------------------------------
# -----string_method4-------------
# --------------------------------

# index(substring, start, end)
# prblem in index is if the object you search for is not in range it will pumped out an error
a = "I love egypt"
print(a.index("g"))
print(a.index("g",0,9))
print("###############################")

# find(substring, start, end) like index but overcome error problem
print(a.find("g"))
print(a.find("g",0,9))
print("###############################")

# rjust, ljust  defult value space two argument spacial char and number
print(a.rjust(20))
print(a.rjust(20, "#"))
print("###############################")

# rjust, ljust  defult value space two argument spacial char and number
print(a.ljust(20))
print(a.ljust(20, "#"))
print("###############################")


# splitlines => convert lines in list 
e = """Frist
secand 
third"""

print(e.splitlines())
print(type(e.splitlines()))
print("###############################")

#expandtabs() => number of tabs

f= "hello\tworld\tpip\t"
print(f)
print(f.expandtabs(5))
print("###############################")

# istitle used for check is title or not

one = "I Love Technolgy 3G"
two = "i love technolgy 3g"
print(one.istitle())
print(two.istitle())
print("###############################")

four = " "
five = ""
# isspace check is space or not
print(four.isspace())
print(five.isspace())
print("###############################")

six = "ahmed"
Seven = "Ahmed"
# islower check is small or not
print(six.islower())
print(Seven.islower())
print("###############################")

qw = "Ahmed_omar"
we = "AhmedOmar100"
rt = "Ahmed--omar"

print(qw.isidentifier())
print(we.isidentifier())
print(rt.isidentifier())
print("###############################")

aws = "aaaaaaaaaaaddddddddd"
sd = "aaaaaaaasss010"
print(aws.isalpha())
print(sd.isalpha())
print("###############################")

print(aws.isalnum())
print(sd.isalnum())
print("###############################")


# replace (old value, newvalue, count)
print(aws.replace("a", "1",4))
print("###############################")

# join compine list to gether take sperator

myList = ["ahmed", "omar", "abou"]
print(" ".join(myList))   
print("_".join(myList))      
print(type(" ".join(myList)))