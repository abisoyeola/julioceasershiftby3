lstChar = [' ','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
def encrypt(plaintext=' '):
   cypherText = []
   for c in plaintext:
      if c == ' ':
         cypherText.append(c)               
      elif lstChar.index(c)+3 > 26:
         cypherText.append(lstChar[(lstChar.index(c)+3)-26])
      else:
         cypherText.append(lstChar[lstChar.index(c)+3])

   #returning cypherText       
   return cypherText

def decrypt(cypherText=' '):
   plaintext = []
   for c in cypherText:
      if c == ' ':
         plaintext.append(c)               
      elif lstChar.index(c) <= 3:
         plaintext.append(lstChar[(lstChar.index(c)+26)-3])
      else:
         plaintext.append(lstChar[lstChar.index(c)-3])

   #returning cypherText       
   return plaintext


# enc = encrypt('JOHN')
# denc = decrypt(enc)
# print("Encryption: " + str(enc) + " Decryprion" + str(denc))

print("WELCOME TO MY SHIFT BY 3 ALGORITHM")
print("Enter your text: ")
text = input()

enc = encrypt(text)
print("Encryption: " + str(enc))

print("Enter your cypher text: ")
ctext = input()

denc = decrypt(ctext)
print("Decryprion" + str(denc))





