import enchant
d = enchant.Dict("en_GB") 

class Caesar:
    def __init__(self, message: str = ''):
        self.message = message.upper()
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    def encrypt(self, shift : int) -> str:
        '''
            Caesar Shift Cipher Encrypter:
                Encrypts given plaintext message using the Caesar Shift Cipher by moving 
                each letter across the alphabet by specified shift value.
        '''
        output_string = ''
        for char in self.message:
            if char not in self.alphabet:
                output_string += char
            else:
                output_string += self.alphabet[(self.alphabet.index(char)+shift)%26]

        return output_string
    
    def decrypt_brute(self) -> str:
        '''
            Caesar Shift Cipher Decrypter: Brute force
                Decrypts given ciphertext and outputs the most likely plaintext using brute force.
        '''
        # create list of all 26 possible plaintexts
        possible_outputs = [self.message]
        for shift in range(1, 26):
            possible_outputs.append(self.encrypt(shift))
            
        # check to see if word in shifted ciphertext is an english word, skip to next if not
        valid = True
        for i in possible_outputs:
            list_of_words = i.split()
            for word in list_of_words:
                if d.check(word) == False:
                    valid = False
                    break
                else:
                    valid = True
            if valid == True:
                return i
        return possible_outputs
        

    def decrypt_fast(self) -> str:
        '''
            Caesar Shift Cipher Decrypter: Frequency Analysis
                Decrypts given ciphertext and outputs the most likely plaintext using the uniform
                distribution of each character in the alphabet. i.e. how frequently each character
                appears.
        '''
        pass
    
    
    @classmethod
    def winston_churchill(cls):
        quote = cls('L FDQQRW IRUHFDVW WR BRX WKH DFWLRQ RI UXVVLD LW LV D ULGGOH ZUDSSHG LQ D PBVWHUB LQVLGH DQ HQLJPD ZLQVWRQ FKXUFKLOO')
        return quote.decrypt_brute()
    

    
x = Caesar('qeb pefm pxfip qljloolt')
        
x.decrypt_brute()
