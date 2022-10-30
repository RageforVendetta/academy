num = 23
real_num = 4.5
answer = "False"
name = "John"
print(f"{num} " + f"{real_num} " + f"{answer} " + name)
print("{} {} {} {}".format(23, 4.5 , False , "John")) # po lesen nachin
print(f"{23} {4.5} {False} {'John'}") # nai dobre


ft = "football"
name = "Atanas"
h = "his"
print(f"{name} favorite sport is {ft}")
print(f"{name} is working on {h} programming")
print(f"{'Atanas'} favorite sport is {'football'}") # direktno izpolzvane na {}
print(f"{'Atanas'} is working on {'his'} programming ") # direktno {}

paragraph = '"Python is a great language"' ",Said Fred." '"I don\'t ever remember having this much fun before"'
print(paragraph)
# Change ur str
school = '"EG Peyo Yavorov"'
print(school.replace("Yavorov", "Yonkov"))
# UPPER CASE STRING
country = "usa"
print(country)
correct_country = country.upper()
print(correct_country)
# find index , check if
filename = '"hello.py"'
print(filename.endswith("java"))
print(filename.find("py"))
print(filename.startswith("world"))
print(filename[:filename.find(".py")])
# print string only with capital leters
print("its verry funny to be funny".upper())
# strip $$ from ""
name = "$$John Smith$$"
print(name.strip("$"))
print(name.lstrip("$"))
print(name.rstrip("$"))
# make proggram
width = 60
print("*" * width)
print("Coding Temple,Inc.".center(width))
print("283 Fraklin St.".center(width))
print("Boston,MA".center(width))
#print(width - broi bukvi = x ~ x/2
#print(" " * 21, "Coding Temple,Inc."
width2 = 60
print("=" * width2)
print("Product Name".rjust(25), " Product Price")
print("Books".rjust(25), " $49.95")
print("Computer".rjust(25), " $579.99")
print("Monitor".rjust(25), " $124.89")
print("=" * width2)
header = "Total"
num_of_intervals = (width2 - 33)
print(f"{' '* (num_of_intervals)}{header}")
print(f"{' '* (num_of_intervals)}{'$754.73'}")
print("=" * width2)
thanks = "Thanks for shopping with us today"
print("\n" + thanks.center(width2) + "\n")
print("*" * width)
