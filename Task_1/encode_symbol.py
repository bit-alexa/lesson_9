def encode_cesar(message, key):
    result = ''.join([chr((ord(char) - ord('a') + key) % (ord('z') - ord('a') + 1) + ord('a')) for char in message])
    return result
