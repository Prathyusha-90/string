#string conversions
#string datatype to another datatype


#implicit
a ="Welcome to VKC"
print(a)
print(type(a))

#explicit
a = str("Pratyusha")
print(a)
print(type(a))

#Data type /variable annotation
a: str = "VKC"
print(a)
print(type(a))

#binary
a = str(0b100001)
print(a)
print(type(a))

#octal
a = str(0o67)
print(a)
print(type(a))

#hexa
a = str(0x1467)
print(a)
print(type(a))

#boolean
a = str(True)
print(a)
print(type(a))

#b00lean conversion
a = bool(0)
print(a)
print(type(a))

#hexa conversion
a = hex(0x46)
print(a)
print(type(a))

#octal conversion
a = oct(0o67)
print(a)
print(type(a))

#binary conversion
a = bin(0b111000)
print(a)
print(type(a))