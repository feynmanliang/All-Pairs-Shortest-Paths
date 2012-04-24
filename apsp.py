import sys

x = sys.maxint

G = [[  0, 11,  x,  9],
     [ 14,  0, 35,  2],
     [  x, 21,  0, 15],
     [  2,  x,  5,  0]]

def printGraph(G):
    for row in G:
        print row

def BadAPSP(G, show=0):
    assert len(G) == len(G[0])
    M = G
    n = len(M[0])
    for l in range(n-1):
        if show:
            print 'l=%d' % (l)
            printGraph(M)
            print '-'*10
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    M[i][j] = min([M[i][j], M[i][k]+M[k][j]])
    print "APSP:"
    printGraph(M)
    return M

def FloydWarshall(G, show=0):
    assert len(G) == len(G[0])
    M = G
    n = len(M[0])
    for k in range(n):
        if show:
            print 'k=%d' % (k-1)
            printGraph(M)
            print '-'*10
        for i in range(n):
            for j in range(n):
                M[i][j] = min([M[i][j], M[i][k]+M[k][j]])
    print "APSP (k=%d):" % k
    printGraph(M)
    return M

#BadAPSP(G, 1)
FloydWarshall(G, 1)