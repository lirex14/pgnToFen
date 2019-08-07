import pgntofen
pgnConverter = pgntofen.PgnToFen()
with open("/Users/rli233/myApps/lichess/game1.txt","r+") as file: # Use file to refer to the file object
    data = file.read()
# PGNMoves = 'd4 d5'
# temp=PGNMoves.split(' ')
# pgnConverter.pgnToFen(temp)
# fen = pgnConverter.getFullFen()
# print(fen)

stats = pgnConverter.pgnFile("/Users/rli233/myApps/lichess/game1.txt");


print(stats[1:])

