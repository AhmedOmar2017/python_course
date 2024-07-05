# -----------------------------------
# -------string_methode2-------------
# -----------------------------------


a=  "I love python so much"
b=  "I-love-python-so-much"

# [2] split =>return list of words defult is space
print(a.split())
print(len(a.split()))
print("#######################################")
print(a.rsplit())
print(len(a.rsplit()))
print("#######################################")
# [3] split =>return list of words defult is space  number of element  
print(b.split("-",2))
print(len(b.split("-",2)))
print("#######################################")
# [4] rsplit =>return list of words defult is space  number of element  but from right
print(b.rsplit("-",2))
print(len(b.rsplit("-",2)))
print("#######################################")

# [5] center => center string between spcial char defult value space
e= "osama"
print(e.center(9))
print(e.center(9,"@"))
print("#######################################")


# [6] count => rturn number repeated element take start, end 
print(b.count("-"))
print("#######################################")
print(b.count("-", 0, 7))
print("#######################################")


# [7] swapcase => swap between capital and small
g = "I Love Programming"
print(g.swapcase())
print("#######################################")

# [7] startwith => which start with this char take start, end 
print(g.startswith("I",7, 12))
print("#######################################")
print(g.startswith("I"))
print("#######################################")

# [8] endwith => which end with this char take start, end 
print(g.startswith("I",7, 12))
print("#######################################")
print(g.startswith("g"))
print("#######################################")

