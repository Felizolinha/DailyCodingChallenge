import collections

board = [[0, 0, 0, 0],
         [-1,-1,0,-1],
         [0, 0, 0, 0],
         [0, 0, 0, 0]]

Coordinate = collections.namedtuple("Coordinate", "y x")
start = input().split()
start = Coordinate(y=int(start[0]), x=int(start[1]))

end = input().split()
end = Coordinate(y=int(end[0]), x=int(end[1]))

def floodfill(pos, target, value):
    if board[pos.y][pos.x] == -1:
        return
    if value < board[pos.y][pos.x]: