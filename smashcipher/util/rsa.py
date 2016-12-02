from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
import primefac


def build_rsa_private(n, public, private,
                      p=-1, q=-1, dmp1=-1, dmq1=-1, iqmp=-1):
    """A wrapper function to create an RSA private key from given parameters.

    Keyword arguments:
    n -- the modulus
    public -- the public exponent
    private -- the private exponent
    p -- (optional) prime 1
    q -- (optional) prime 2
    dmp1 -- (optional) CRT exponent 1
    dmq1 -- (optional) CRT exponent 2
    iqmp --- (optional) CRT coefficient
    """
    if p == -1 or q == -1:
        p, q = rsa.recover_prime_factors(n, public, private)
    if dmp1 == -1:
        dmp1 = rsa.rsa_crt_dmp1(private, p)
    if dmq1 == -1:
        dmq1 = rsa.rsa_crt_dmq1(private, q)
    if iqmp == -1:
        iqmp = rsa.rsa_crt_iqmp(p, q)
    pubNum = rsa.RSAPublicNumbers(public, n)
    privNum = rsa.RSAPrivateNumbers(p, q, private, dmp1, dmq1, iqmp, pubNum)
    return default_backend().load_rsa_private_numbers(privNum)


def build_rsa_public(n, public):
    """A wrapper function to create an RSA public key from given parameters.

    Keyword arguments:
    n -- the modulus
    public -- the public exponent
    """
    pubNum = rsa.RSAPublicNumbers(public, n)
    return default_backend().load_rsa_private_numbers(pubNum)


def generate_rsa_private(public, keysize):
    """A wrapper function to generate a new RSA private key from given parameters.

    Keyword arguments:
    public -- the public exponent
    keysize -- size of modulus
    """

    return rsa.generate_private_key(
        public_exponent=public,
        key_size=keysize,
        backend=default_backend())


def factor(public_key):
    public = public_key.public_numbers().e
    n = public_key.public_numbers().n
    p = primefac.multifactor(n, verbose=False,
                             methods=(primefac.pollardRho_brent,
                                      primefac.pollard_pm1,
                                      primefac.williams_pp1,
                                      primefac.ecm,
                                      primefac.mpqs))
    q = n / p
    private = primefac.modinv(public, (p - 1) * (q - 1))
    return build_rsa_private(n, public, private, p, q)
