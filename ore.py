import crypto
from bitstring import BitArray


def encrypt(key: bytearray, message: int):
    ciphertext = []
    message_bitArray = BitArray(bin=bin(message))

    # For each bit in the message
    for i in range(0, len(message_bitArray.bin)):
        # get the prefix
        prefix = message_bitArray.bin[0:i]

        # Get the PRF output with the key and prefix
        prf_output = crypto.prf(key, BitArray(bin=prefix))
        # Add the current bit from the message to the prf_output
        block = (prf_output.uint + int(message_bitArray.bin[i])) % 3

        # add block to the final ciphertext
        ciphertext = ciphertext + [block]

    return ciphertext


# compare ciphertext 1 and ciphertext 2
# if : ctx1 < ctx2 return -1
# if : ctx1 > ctx2 return 1
# if : ctx1 = ctx2 return 0
def compare(ctx1, ctx2):
    if len(ctx1) > len(ctx2):
        return 1
    if len(ctx2) > len(ctx1):
        return -1
    else:
        for i in range(0, len(ctx1)):
            if ctx1[i] != ctx2[i]:
                if int(ctx2[i]) == (int(ctx1[i]) + 1) % 3:
                    return -1
                elif int(ctx2[i]) == (int(ctx1[i]) -1) % 3:
                    return 1
        return 0
