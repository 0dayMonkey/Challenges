import itertools

def decrypt(ciphertext, key):
    plaintext = ""
    for i in range(0, len(ciphertext), 2):
        pair = ciphertext[i:i+2]
        if pair in key:
            plaintext += key[pair]
        else:
            plaintext += "?"
    return plaintext

ciphertext = "lmcnsyfbpffbftybftfbncpminad ahncbhin ybercnwo xtcnpfxyfbdldllvcn pfcn hkcnininybmocn ybercnpf inbhpfpfcninad lncn pmcn dlbhft ktybin ftlvnckt xtfbdldlfbpffbsycn dlfbpmybsysycnhkcnpmftju anfbcnpm edncbhcnlvhg rhncpm ftlvyberybfbsyad zppmftlvcnlv pfcn hkncft pfsycndl pfnchkhkcn inncsybhftfbncpmlt molvyblvpmlvpmmoktrhpmxtad"
letters = "abcdefghijklmnopqrstuvwxyz"
pairs = [a + b for a in letters for b in letters]
possibilities = itertools.permutations(pairs)

for possibility in possibilities:
    key = dict(zip(possibility, letters*2))
    plaintext = decrypt(ciphertext, key)
    with open("plaintexts.txt", "a") as f:
        f.write(str(possibility) + "\n" + plaintext + "\n\n")
