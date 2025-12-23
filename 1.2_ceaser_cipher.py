import random

shift_key_string = input("What is your desired shift( if you have no preference plz input 'none' ): ")
shift_key_int = 0
if shift_key_string == "none":
    shift_key_int = random.randint(0, 26)
else:
    shift_key_int = int(shift_key_string)

def encode(message):
    encoded_message = ""
    for i in range(len(message)):
        if message[i] == " ":
            encoded_message += " "
            
        elif message[i] != " ":
            encoded_message += chr(ord(message[i])+shift_key_int)
       
    return encoded_message
    
def decode(message):
    decoded_message = ""
    for i in range(len(message)):
        if message[i] == " ":
            decoded_message += " "
            
        elif message != " ":
            decoded_message += chr(ord(message[i])-shift_key_int)
    return decoded_message

user_mess = input("What message would you like to encode: ")
print(encode(user_mess))
print(decode(encode(user_mess)))
        
        