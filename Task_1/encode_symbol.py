def encode_cesar(message, key):
    result = ''.join([chr((ord(ch) - ord('a') + key) % (ord('z') - ord('a') + 1) + ord('a')) for ch in message])
    return result
