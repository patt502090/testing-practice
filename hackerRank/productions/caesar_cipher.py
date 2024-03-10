def caesarCipher(s, k):
    encrypted = ''
    for char in s:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            encrypted += chr((ord(char) - base + k) % 26 + base)
        else:
            encrypted += char
    return encrypted