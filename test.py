# file = open("password,txt","r")
# data=file.readlines()
# print(data)

import maskpass  # importing maskpass library
import base64

# prompt msg = Password and
# masking password with hashtag(#)
pwd = maskpass.askpass(prompt="Password:", mask="#")
p="Aniruddha77777"
encodePassword = base64.b64encode(p.encode("utf-8"))
decodePassword = base64.b64decode('QW5pcnVkZGhh').decode("utf-8")
print(p)
print(encodePassword)
print(decodePassword)