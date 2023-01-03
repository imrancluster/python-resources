#
# We will see Symmetric-key Encryption using cryptography package.
# Here, we will use Fernet class
#

from cryptography.fernet import Fernet


class MyEncryption:
    def __init__(self, fernet: Fernet):
        """
        constructor define fernet object

        :param fernet:
        """
        self.__fernet = fernet

    def get_encrypted_message(self, plain_text: str) -> bytes:
        """
        get_encrypted_message returns encrypted message in bytes format

        param plain_text: string input
        :return: bytes of string
        """
        enc_message = self.__fernet.encrypt(plain_text.encode("utf-8"))
        return enc_message

    def get_decrypted_message(self, encrypted_message: bytes) -> str:
        """
        get_decrypted_message returns string after decoding the encrypted message

        param encrypted_message:
        :return: decoded string
        """
        dec_message = self.__fernet.decrypt(encrypted_message).decode()
        return dec_message


def main():
    # instantiate Fernet object,
    # in this example, we will be able to use one key for encryption & decryption
    # Fernet.generate_key() function will create new 32 base64 hash
    # we can also use our own custom key using following
    # imran_key = base64.urlsafe_b64encode(bytes("12345678901234567890123456789012".encode("utf-8")))
    key = Fernet.generate_key()
    fernet = Fernet(key)

    # instantiate My object
    my_encryption = MyEncryption(fernet)

    # get encrypted message using plain text
    message = "Hello World!"
    encrypted_message = my_encryption.get_encrypted_message(plain_text=message)
    decrypted_message = my_encryption.get_decrypted_message(encrypted_message=encrypted_message)

    print("Actual message: ", message)
    print("Encrypted message: ", encrypted_message)
    print("Decrypted message: ", decrypted_message)


if __name__ == "__main__":
    main()
