# # Escape sequance char
# \b => Back Space
# \newline => scape new line 
# \ => scape spaicial char
# \n => line feed -new line -
# \r => carriage return
# \t => horizontal Tab 
# \xhh => char hex value 
# ------------------------------------------


# back space
print ("hello\bworld") #will remove o character

# scape new line + back slash
print("hello\
 I love\
 python")

# scape back slach itself
print("scape back slash \\")

# scape single qoute 
print("i lave qoute \'test\'")


# print each sentance in a new line 
print("hello\nworld")

# carriage return
print("123456\rhello")


# horizontal Tab 
print("hello\tworld")


# char hex value 

print("\x4f")