
msg_decode = """meesage à decodé (int)"""

s = [int(x, 16) for x in msg_decode.split()]

a_deco, rr,n = '',{},0

for _ in s:
    if _ not in rr:
        rr[_] = chr(97 + n)
        n += 1
    a_deco += rr[_]

a_deco = a_deco.translate(str.maketrans('ml{}~', ' .m:l'))
print(a_deco)
