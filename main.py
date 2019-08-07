import pgntofen
from anytree import Node, RenderTree

pgnConverter = pgntofen.PgnToFen()
with open("/Users/rli233/myApps/lichess/game1.txt","r+") as file: # Use file to refer to the file object
    data = file.read()
# PGNMoves = 'd4 d5'
# temp=PGNMoves.split(' ')
# pgnConverter.pgnToFen(temp)
# fen = pgnConverter.getFullFen()
# print(fen)

#get the fen list for a given game
stats = pgnConverter.pgnFile("/Users/rli233/myApps/lichess/game1.txt")[1:];
gameMoves = pgnConverter.gameMoves[1:];
# print(gameMoves)

white = Node("white", parent=None)
iter = 1
nodeIter = white
moveCounter = 1
for i in range(len(gameMoves)):
    if iter % 2 is not 0:
        j = gameMoves[i]
        temp = Node(str(moveCounter)+"."+gameMoves[i])
        temp.parent = nodeIter
        nodeIter = temp
    else:
        temp = Node(str(moveCounter)+".."+gameMoves[i])
        temp.parent = nodeIter
        nodeIter = temp
        moveCounter+=1
    iter+=1

print(RenderTree(white))


