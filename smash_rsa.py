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
