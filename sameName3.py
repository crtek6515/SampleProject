def spam():
    global eggs
    eggs = 'spam'  #this is a global variable

def bacon():
    eggs = 'bacon'  #this is a local variable

def ham():
    print(eggs)  #this is the global

eggs = 42 #this is the global
spam()
print(eggs)