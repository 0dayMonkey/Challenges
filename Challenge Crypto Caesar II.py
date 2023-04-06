cipher = """4B 78 77 20 7D 7B 6A 7F 6A 72 75 35 20 7F 78 7E
7C 20 6A 7F 6E 03 20 7B 6E 7C 78 75 7E 20 7E 77
20 6C 71 6A 75 75 6E 77 70 6E 20 6D 6E 20 79 75
7E 7C 20 6D 6A 77 7C 20 7F 78 7D 7B 6E 20 73 78
7E 7B 77 6E 6E 37 20 4C 6E 75 7E 72 36 75 6A 20
6E 7D 6A 72 7D 20 7C 72 76 79 75 6E 20 6A 20 6C
7B 6A 6C 74 6E 7B 37 20 57 30 6E 7C 7D 36 6C 6E
20 79 6A 7C 48 20 3A 3B 41 20 6C 6A 7B 6A 6C 7D
6E 7B 6E 7C 20 6E 7C 7D 20 7E 77 20 6E 7C 79 6A
6C 6E 20 6A 7C 7C 6E 03 20 79 6E 7D 72 7D 35 20
6D 78 77 6C 20 6C 6A 20 77 6E 20 6D 6E 7F 7B 6A
72 7D 20 79 6A 7C 20 7F 78 7E 7C 20 79 7B 6E 77
6D 7B 6E 20 7D 7B 78 79 20 75 78 77 70 7D 6E 76
79 7C 20 79 78 7E 7B 20 6D 6E 6C 7B 02 79 7D 6E
7B 20 6C 6E 20 76 6E 7C 7C 6A 70 6E 37 20 4B 72
6E 77 20 73 78 7E 6E 35 20 75 6A 20 7C 78 75 7E
7D 72 78 77 20 6E 7C 7D 20 6F 6F 75 7C 79 71 6E
7C 7C 76 6B 71 37
"""

for shift in range(127):
    decoded = ''.join(chr((int(c, 16) + shift + 1) % 128) for c in cipher.split())
    print(f'{decoded}\n{shift + 1}')

# À l'itération 114 (dans mon cas, peu changer ), on voit le message suivant:
"""
Bontravail,vousavezresoluunchallengedeplusdansvotrejournee.Celui-laetaitsimpleacracker.N'est-cepas?128caracteresestunespaceassezpetit,donccanedevraitpasvousprendretroplongtempspourdecryptercemessage.Bienjoue,lasolutionestfflsphessmbh.
"""
