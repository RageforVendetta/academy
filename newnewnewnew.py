comment = """atanas
e
nai
ludiq
"""
#""" se izpolzva za nqkolko reda
print(comment)
text = "\\"   # za printirane na \
print((text))
name = "Atanas"
num = 6
real_num = 7.2
print(f"String:{name}")
print(f"Integer:{num}")
print(f"Real_number:{real_num}")
# fstrings - format {} Place holder
chislo = 27.42424242
print(f"{chislo:.2f}") # za pokazvane na
#opredelen broi znamenatel
# fstring = vizualizirane na dani, F zakruglq
name = "Kaloqn Ivanov"
print(name[2])
# [] za index zapochva ot 0
# -1 e poslednat bukva >
print(name[0 : 3])
# Za slicing/ slice from start to 3
print(name[0 : 9 : 2])
# vtoroto : e za stupka ,  preskacha prez 2
print(name[-1:-6:-1])
#-1 nakraq obrushta stringa
last_name = name[7:-2]
print(last_name)
print(name[:5]) # : nachalo
last_name = name[7:] # : sled nachalo = krai
print(last_name)
print(last_name[::-1])# reverse a string

name = "atanas atanasov"
print(name.title())
name = name.title()
print(name)
print(name.upper())
print(name.lower())
# .tittle()  Za purvata bukva
# .upper() za glavni
# .lower() za malki

ban = "banana e golqm."
print(ban.replace(".", "!"))
print(ban.replace("golqm", "maluk"))
# .replace() zamenqne na duma/znak s drug

rrr = "Moreto i negovite sini vulni"
print(rrr.find("sini"))
# .find() namira indexa na posechenata duma

next = rrr.find(" sini")
print(rrr[next + 1:])
# moga da namerq indeksa i da go slice-na lesno
# print (help(text.fin))
# find vrushta -1 ako ne namira index
# index vrushta direktno greshka

name = "          Ivan"
name = "\n\tIvan"
name = "@@@@@@@@@@@@@Ivan"
print(name.strip("@"))
# Strip premahva SPACE , TAB i custom symbols
# lstrip , rstrip = l premahva ot lqvo r= ot dqsno

text = "hello world"
print(len("Hello World"))
print(text[len(text) // 2: ])
# len get string lenght
print("," in text)
# in checks if it exists in string

text = "helllo world"
print(text.split()) #split a string
print(text.split("o")) # razdelitelq e O

print(text.startswith("h"))
print(text.startswith("Z"))
print(text.endswith("d"))
print(text.endswith("z"))