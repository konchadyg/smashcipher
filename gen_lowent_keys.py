from cryptography.hazmat.primitives import serialization
from smashcipher.util import rsa as rsa_utils
import primefac

p = 111785135995915694872879065655450100824399060915246858692368272101498809780789
q = 95426003088967587203385239828634342249572881536732227152898005772259369509063
r = 115610435786510485451946829452875827768560089514770425913213861099648595711893

public = 65537

private1 = primefac.modinv(public, (p - 1) * (q - 1))
private2 = primefac.modinv(public, (q - 1) * (r - 1))

private_key1 = rsa_utils.build_rsa_private(p * q, public, private1, p, q)
private_key2 = rsa_utils.build_rsa_private(q * r, public, private2, q, r)

private_file1 = private_key1.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption())
file1 = open("test_keys/lowent/private-lowent1.key", "w")
file1.write(private_file1)
file1.close()

private_file2 = private_key2.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption())
file2 = open("test_keys/lowent/private-lowent2.key", "w")
file2.write(private_file2)
file2.close()
