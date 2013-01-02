"""
Consider 2 x 2 Grid

a -> b -> c (1)
|    |    |
d -> e -> f (2)
|    |    |
g -> h -> i (6)
(1)  (2)

The numbers in the brackets are the possible routes to reach the border elements in the grid
Upon analysis, the routes for border elements in different sized grids are as below :

2x2     3x3     4x4     5x5     6x6
1       1       1       1       1
3       4       5       6       7
6       10      15      21      28
        20      35      56       and so on..
                70      126
                        252

"""

l = []
l.append([1,2])
l.append([1,3,6])   #2 x 2 Matrix (Routes for reaching terminal elements

for i in range(3,21):   # Start from 3 * 3
    #Construct a new list.
    t = []
    j = 0
    while j < i:
        if j == 0:
            t.append(1)     #Single route possible to reach the outermost element on the same horizontal line.
            j = j + 1
            continue
        t.append(t[-1] + l[-1][j])
        j = j + 1
        
    t.append(t[-1] * 2)
    l.append(t)

print "\n".join([str(x) for x in l])

#The answer is 137846528820L !!!