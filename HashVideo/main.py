from Crypto.Hash import SHA256
from binascii import a2b_hex, b2a_hex


def getFile(file, sizeNum):
    # Open file for reading as binary data
    f = open(file, 'rb')
    data = f.read()
    f.close()

    # Chunked 1KB
    bytes = len(data)
    blocks = []
    for i in range(0, bytes, sizeNum):
        blocks.append(data[i:i + sizeNum])

    return blocks


def getHash(file):
    sizeNum = 1024
    res_hash = b''

    # Retrieve block content
    blocks = getFile(file, sizeNum)

    for i in range(len(blocks) - 1, -1, -1):
        # Compute block content = block content + hash value of the next block
        blocks[i] = blocks[i] + res_hash

        # Generate new hash
        hash = SHA256.new(blocks[i])

        # Update hash value
        res_hash = hash.digest()

    return b2a_hex(res_hash)


if __name__ == '__main__':
    test_file = "birthday.mp4"
    print("Chain hash for {} is:\n {}".format(test_file, getHash(test_file)))

# https://github.com/madison-freeman/HMAC-SHA256