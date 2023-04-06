txt_encode = 'jghjwlqxfqkdcdlmzokdcdkchjwlzsob pnhjlm fkowxjfqjafzcdowfk cdlpkczs dxowzszskdqxow zslmxjxjowzszsxqlmzozojaob shkdzs wlhjcd cdhjhj fkkcxqxqkcxjlmzocd owkccdlpowfqxo xxkdzs kccdnp showzozoxo qxhjhjfk bihjhdob swwlcdowfq cdlpkczs piowjaxxhjfqfk kdzs zshjzolmcdkchjwlil qxfqkdfqwlfqwlqxfzhdwlfkob'

cle = []
msg_a_dec = []

for word in txt_encode.split(' '):
    word_msg_a_dec = ''
    for k in range(0, len(word), 2):
        pair = word[k:k+2]
        if pair not in cle:
            cle.append(pair)
        word_msg_a_dec += chr(cle.index(pair) + ord('a'))
    msg_a_dec.append(word_msg_a_dec)

msg_a_dec = ' '.join(msg_a_dec).translate(str.maketrans('alw~{|}', 'A.,:alw'))
print(msg_a_dec)
