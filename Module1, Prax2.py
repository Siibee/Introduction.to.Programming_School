#! python3
#PRAX 1
a=("X")
b=("|")
c=("-")

print("          ",a)
print("        ",a,a,a)
print("      ",a,a,a,a,a)
print("     ",b,"       ",b)
print("     ",b,"  abc  ",b)
print("      ",c,c,c,c,c)

#PRAX 2
print()
print()
a = input("Enter Name: ")
b = input("Home address: ")
c = input("Phone number: ")
d = input("Email Address: ")

#Old code, (first time coding ever):
#print("Your home address is,", b)
#print("Your number is,", c)
#print("Your email is,", d)
#print("Thank you!")
#print("Output complete!")

#Updated code:
print ()
print("\t","Good Morning,", a,"\n","\t","Your home address is,", b,"\n", "\t", "Your number is,", c, "\n", "\t", "Your email is,", d,"\n", "\t", "Thank you!")
print ()
print("\t","Output complete!")
