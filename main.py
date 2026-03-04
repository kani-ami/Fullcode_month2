import re
# number = "Number: +996342452353"
# pattern = r".\d+"
# print(re.findall(pattern, number))

# password0 = "32423423Lsrewrfddsf"
# password1 = "fskjdkFfjklds21324"
# password2 = "423ewrewrfsUf23424@@@"
# def is_password(password):
#     pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$"
#     if re.fullmatch(pattern, password):
#         return True
#     else:
#         return False
#
#
# print(is_password(password0))
# print(is_password(password1))
# print(is_password(password2))


def validate_pin(pin):
    n = 4
    m = pin.isdigit()
    pin = int(pin)
    b = pin = len(pin)
    for i in pin:
        if (b == n) and (pin == m):
            return True
        else:
            return False
print(validate_pin('123456'))



print(validate_pin('123456'))

print(validate_pin('123456'))


n = 8
m = 9
print(n+m)

