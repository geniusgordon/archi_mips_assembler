import sys

with open(sys.argv[1], "rb") as f:
    byte = f.read(1)
    while byte != "":
        word = []
        for i in range(4):
            word.append("%02x" % ord(byte))
            byte = f.read(1)
        print ''.join(word)

