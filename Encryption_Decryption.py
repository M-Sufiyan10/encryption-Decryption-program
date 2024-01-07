import random as r
import string as s
import time as t

#encoding fucntion
def encoding(encode):    
    '''this function will help you to encode the message so no other person can read your data'''
    if len(encode) >= 3:
            a=encode[1:]
            a=''.join([a,encode[0]])
            characters = s.ascii_letters
            r1 = ''.join(r.choice(characters) for _ in range(4))
            r2 = ''.join(r.choice(characters) for _ in range(4))
            a=r1+a+r2   
            return a
    else:

        print(''.join(reversed(encode)))
        return encode
#decoding fucntion
def decoding(decode):
    '''this function will help you to decode the encoded string of your message'''
    if len(decode)>=3:
         d=decode[4:len(decode)-4]
         copy=d[len(d)-1]
         d="".join([copy,d[:-1]])
         return d

    else:
        decode="".join(reversed(decode))
        return decode


encode=input("enter your message : ")
print("do you want to see your data in encrypted form or decrypted form? ")
flag=False
while(flag == False):
    try:
        t.sleep(2)
        choice=int(input("press 1 for encryption mode\npress 2 for decryption mode : "))
        if choice <=0 or choice >=3:
            raise ValueError
        flag=True
    except ValueError:
        t.sleep(2)
        print("wrong input!!!! try again...")
        flag=False
   
decode=(encoding(encode))
while True:
    if choice == 1:    
        print("your message in encrypted form is : ", encoding(encode))
        option= input("do you want to see in decrypted form? press 'Y' for yes or 'N' for no : ")
        if option.upper() == 'Y':
            print("your message in decrypted form : ", decoding(decode))   
            break;
        else:
            print("program has terminated!!!")
            break  
    else:
        
        print("your message in decrypted form : ", decoding(decode))
        option= input("do you want to see in encrypted form? press 'Y' for yes or 'N' for no: ")
        if option.upper() == 'Y':
            print("your message in encrypted form : ", encoding(encode))   
            break;
        else:
            print("program has terminated!!!")
            break  




