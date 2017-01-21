from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from util import rsa as rsa_utils


def factor_pubkey(infile, outfile):
    with open(infile, "rb") as key_file:
        pub_key = serialization.load_pem_public_key(key_file.read(),
                                                    backend=default_backend())
        priv_key = rsa_utils.factor(pub_key)
        priv_file = priv_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption())
        privkey_file = open(outfile, "w")
        privkey_file.write(priv_file)
        privkey_file.close()


def lowentropy(infile1, infile2, outfile1, outfile2):
    with open(infile1, "rb") as key_file1:
        with open(infile2, "rb") as key_file2:
            pub_key1 = serialization.load_pem_public_key(
                key_file1.read(),
                backend=default_backend())
            pub_key2 = serialization.load_pem_public_key(
                key_file2.read(),
                backend=default_backend())
            priv_key1, priv_key2 = rsa_utils.gcd(pub_key1, pub_key2)
            priv_file1 = priv_key1.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption())
            privkey_file1 = open(outfile1, "w")
            privkey_file1.write(priv_file1)
            privkey_file1.close()
            priv_file2 = priv_key2.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption())
            privkey_file2 = open(outfile2, "w")
            privkey_file2.write(priv_file2)
            privkey_file2.close()

