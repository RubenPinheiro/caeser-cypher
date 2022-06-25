import caesar_logo

print(caesar_logo.logo)
launch = 'yes'
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def crypt(alphabet, text, shift, direction, launch):

      crypt_word = ""

      for char in range(0,len(text)):
          
          while shift >= len(alphabet):
              shift -= len(alphabet)
          
          if text[char] in alphabet:
              position = alphabet.index(text[char]) + shift
              
              if position >= len(alphabet):
                  position -= len(alphabet)
              elif position < 0:
                  position += len(alphabet)
                  
              crypt_word += alphabet[position]
              
          else:
              crypt_word += text[char]

      print(f'The {direction} message is: {crypt_word}')

while launch != 'no':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == 'encode':
        crypt(alphabet, text, shift, direction, launch)
    elif direction == 'decode':
        crypt(alphabet, text, -shift, direction, launch)
        
    launch = input('Would you like to launch the program again? Type "yes" or "no":\n')
