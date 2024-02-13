# Boolean Values - represent one of two values: True or False.

print(10 > 9)  #True
print(10 == 9) #False
print(10 < 9)  #False

print(bool("Hello"))  #True
print(bool(15))       #True
print(bool(0))        #False
print(bool(1))        #True

# many values that evaluate to False, except empty values, such as (), [], {}, "", the number 0, and the value None. And of course the value False evaluates to False.
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})


# Functions can Return a Boolean

# def myFunction() :
#   return True  

# print(myFunction())


def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")
