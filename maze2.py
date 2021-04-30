from random import shuffle, randrange

 
def make_maze(w = 5, h = 5):
    vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]
    ver = [["|  "] * w + ['|'] for _ in range(h)] + [[]]
    hor = [["+--"] * w + ['+'] for _ in range(h + 1)]
 
    def walk(x, y):     # The walk inside this maze starting from the cell x,y
        vis[y][x] = 1   # First mark the starting cell as visited

        d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)] # describe the walk directions sequence (1 step to the Left, Down, Right, Up)
        shuffle(d)              # and change the directions order in this one-step sequence randomly
        
        for (xx, yy) in d:      # check out all the neighbour cells step by step in a random sequence
            if vis[yy][xx]: continue    # if the checking cell already visited, then just continue with a next one
                                        # else:
            if xx == x: hor[max(y, yy)][x] = "+  " # replace initial "+--" to "+  " and open the vertically throupath if it was nonvisited neibour along y-coordinate (the x is not changed)
            if yy == y: ver[y][max(x, xx)] = "   " # replace initial "|" to " " and open horisontally throupath if it was nonvisited neibour along x-coordinate (the y is not changed)
            walk(xx, yy)                           # and go far recursively
 
    walk(randrange(w), randrange(h)) #Start the walk from a random cell inside the maze
 
    s = ""
    for (a, b) in zip(hor, ver):
        s += ''.join(a + ['\n'] + b + ['\n'])
    return s
 
if __name__ == '__main__':
    print(make_maze())
