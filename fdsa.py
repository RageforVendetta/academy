x = 8 #Integer
print(type(x))
pi = 3.141592 #float
print(type(pi))

overflow = 3.12345667891011121314
print(overflow)

is_user_logged_in = True #Boolean

print(is_user_logged_in)

comment = "Hello" #str
print(comment)

text = '"hello"'
print(text) # ' i posle " za slagavene v "

prazen = '"hello"\n\n\n' #\n za prazen red
print(prazen)

prazno_mqsto = "hello\t" # ostava prazno mqsto sled dumata
print(prazno_mqsto)

print(4+3)
print(4-2)
print(4*3)
print(4/3) #Float division
print(4//3) #Integer division
print(5 % 3) #remainder #ostatuk
print(2%5)
print(2 ** 3) # power stepenuvane
print(4+3*2) #aretmetichni operacii , () za otdelqne kato v matematika

print(3 == 3) #ravno li e ==
print(3 != 3) # razlichno li e !=

x = 3
print(x < 5)
print(x < 5 and x >= 2 and x >=4) #kombinaciq na usloviq s AND
# s OR operatora go interesuva dali edno ot usloviqta e izpulneno i otgovarq s TRUE ili FAlse
print(x <= 20 and x>=10) # check if x in [10;20]
print(not x >3) # not gleda uslovieto i obrushta krainata stoinost

x = 3
x = x +3
print(x)