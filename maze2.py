from random import shuffle, randrange
 
def make_maze(w = 5, h = 5):
    vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]
    ver = [["|  "] * w + ['|'] for _ in range(h)] + [[]]
    hor = [["+--"] * w + ['+'] for _ in range(h + 1)]
 
    def walk(x, y):     #The walk inside this maze starting from the cell x,y
        vis[y][x] = 1   # Mark the starting cell as visited
        
        d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)] # description of the 1-step direction choosing sequence (1 step to the Left, Down, Right, Up)
        for (xx, yy) in d:      # check out the each neighbour cell starting from a random direction
            if vis[yy][xx]: continue    # if this cell visited, then just continue with next one in a random direction
            if xx == x: hor[max(y, yy)][x] = "+  "
            if yy == y: ver[y][max(x, xx)] = "   "
            walk(xx, yy)
 
    walk(randrange(w), randrange(h)) #Start the walk from a random cell
 
    s = ""
    for (a, b) in zip(hor, ver):
        s += ''.join(a + ['\n'] + b + ['\n'])
    return s
 
if __name__ == '__main__':
    print(make_maze())
