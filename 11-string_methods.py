# -------------------------------
# --- sting method --------------
# -------------------------------



a= "     I Love Python        "
b = "###########I Love Python##########"
c = "#@#@#@#@I Love Python#@@@###"
d = "I love 2d graphic and 3g technology and python "
# [1] count number of elements in string
print(len(a))

# [2] lstrip => remove space if you remove the printseces embty from left
print(a.lstrip())
print(len(a.lstrip()))

# [3] rstrip => remove space if you remove the printseces embty from right 
print(a.rstrip())
print(len(a.rstrip()))
# [4] strip => remove space if you remove the printseces embty from left and right
print(a.strip())
print(len(a.strip()))



print("#######################################")

# [2] lstrip => remove "#" if you add between  the printseces  from left
print(b.lstrip("#"))
print(len(b.lstrip("#")))

# [3] rstrip => remove "#" if you add between  the printseces from right 
print(b.rstrip("#"))
print(len(b.rstrip("#")))



# [4] strip => remove s"#" if you add between  the printseces from left bnd right
print(b.strip("#"))
print(len(b.strip("#")))


print("#######################################")


 #[2] lstrip => remove "#" if you add between  the printseces  from left
print(c.lstrip("@#"))
print(len(c.lstrip("@#")))

# [3] rstrip => remove "#" if you add between  the printseces from right 
print(c.rstrip("@#"))
print(len(c.rstrip("@#")))



# [4] strip => remove s"#" if you add between  the printseces from left bnd right
print(c.strip("@#"))
print(len(c.strip("@#")))



print("#######################################")
# [5] title()  convert first char capital and char after number

print(d.title())
print("#######################################")
# [6] capitalize()  convert char to capital 
print(d.capitalize())
print("#######################################")


# [7] capitalize()  convert char to capital 
print(d.capitalize())
print("#######################################")

# [8] zfill fill the number with zero to be in line 
q,w,e,r = "1","11","111", "1111"
print(q)
print(w)
print(e)
print(r)

print("#######################################")
print(q.zfill(4))
print(w.zfill(4))
print(e.zfill(4))
print(r.zfill(4))

print("#######################################")

# [9] upper conver all char to capital

y = "ahmed omar"

print(y.upper())


print("#######################################")

# [10] lower  convert all char  to small 

z="AHMED OMAR"

print(z.lower())
