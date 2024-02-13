# Slicing Strings
txt = "12345678910"
print(str(len(txt))+"\n12345678910")
print(txt[3:9])
print(txt[-5:-2])

# Modify Strings
a = "  Jai Shree Ram!  "
print("\n"+a.upper()) #Lower Case
print("\n"+a.lower()) #Upper Case
print("\n"+a.strip()) #Remove Whitespace

# Replace String
print(a.replace("4", "8"))

# Split String
print(a.split(","))

# String Concatenation
a = "jai"
b = "shree"
c = "ram!"
d = a +" "+ b + c
print(d)

# String Format
age = 36
txt = "My name is Jhon snow, I am " + age
print(txt)

quantity = 5
itemno = 567
price = 80
myorder = "I want {} pieces of item no. {} for {} rupees."
print(myorder.format(quantity, itemno, price))

# Escape Character
txt = "We are the so-called \"Nagpurians\" from the Maharashtra, India."
print(txt)






