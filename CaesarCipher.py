class CaesarCipher:
    def __init__(self, shift):
        self.shift = shift

    def encode(self, plaintext):
        ciphertext = ""
        for char in plaintext:
            if char.isalpha():
                shift_amount = (ord(char.lower()) - ord('a') + self.shift) % 26
                if char.isupper():
                    ciphertext += chr(ord('A') + shift_amount)
                else:
                    ciphertext += chr(ord('a') + shift_amount)
            else:
                ciphertext += char
        return ciphertext

    def decode(self, ciphertext):
        plaintext = ""
        for char in ciphertext:
            if char.isalpha():
                shift_amount = (ord(char.lower()) - ord('a') - self.shift) % 26
                if char.isupper():
                    plaintext += chr(ord('A') + shift_amount)
                else:
                    plaintext += chr(ord('a') + shift_amount)
            else:
                plaintext += char
        return plaintext


if __name__ == "__main__":
    plaintext = input("Enter the plaintext: ")
    shift = int(input("Enter the shift number: "))

    cipher = CaesarCipher(shift=shift)
    
    # Encoding
    encoded_text = cipher.encode(plaintext)
    print("Encoded text:", encoded_text)
    
    # Decoding
    decoded_text = cipher.decode(encoded_text)
    print("Decoded text:", decoded_text)
