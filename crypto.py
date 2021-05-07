import os, hmac, hashlib
from bitstring import BitArray


def generate_prf_key(size : int):
    return os.urandom(size)


def prf(key, message):
    digest_maker = hmac.new(key, message.bin.encode('utf-8'), hashlib.sha256)
    digest = digest_maker.hexdigest()
    return BitArray(hex=digest)



