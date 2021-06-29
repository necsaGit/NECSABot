# nsfw_file = open("nsfw.txt", "r")
# nsfw_words = nsfw_file.readlines()
# nsfw_words = [x.strip('\n') for x in nsfw_words]

# import os
# from cryptography.fernet import Fernet

# decryptKey = os.environ['enc-key']
# decryptKey = str.encode(decryptKey[2:-1])
# fernet = Fernet(decryptKey)
# class warden:

#     def __init__(self):
#         pass

#     def encrypt(self, message):
#         return fernet.encrypt(message.encode())

#     def decrypt(self, message):
#         return fernet.decrypt(message).decode()

#     def strToByte(self, message):
#         message = message[2:-1]
#         return str.encode(message)
    
#     def nsfwCheck(self, message):
#         for words in nsfw_words:
#             new = self.strToByte(words)
#             if  self.decrypt(new) in message:
#                 return True
                                        
#     def censorMessage(self, message):
#         for words in nsfw_words:
#             new = self.strToByte(words)
#             ndec = self.decrypt(new)
#             if ndec in message:
#                 message = message.replace(ndec, '\*'*(len(ndec)-1)+'\*')
#         return message
