#
# We will see Asymmetric-key Encryption using rsa package.
#

import rsa


# key should be at least 16 chars
public_key, private_key = rsa.newkeys(512)

# original message
message = "Hello RSA!"

# encryption using public key
enc_message = rsa.encrypt(message.encode(), public_key)

# decryption using private key
dec_message = rsa.decrypt(enc_message, private_key).decode()

# message printing
print("Original message: ", message)
print("Encrypted message: ", enc_message)
print("Decrypted message: ", dec_message)
