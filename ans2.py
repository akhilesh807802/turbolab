upper= ord('A')
size= 25
def rem(number):
    while number:
        number, remainder = divmod(number - 1, size)
        yield remainder
def alphabet(firstnumber, secondnumber):
    string1 = ''.join(chr(upper+ part) for part in rem(firstnumber))[::-1]
    string2 = ''.join(chr(upper+ part) for part in rem(secondnumber))[::-1]
    return string1 + string2
def number(string):
    return sum(
        (ord(letter) - upper+ 1) * size** i for i, letter in enumerate(reversed(string.upper()))
    )
string = "petpan"
first_base10 = number(string[:int(len(string) / 2)])
second_base10 = number(string[int(len(string) / 2):])
total = first_base10 + second_base10
print(total)
print(alphabet(10145, 10039))
