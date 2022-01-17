def TowerHanoi(n,a,b,c):
    #Base Case
    if n == 1:
        print("Move disk 1 from %s to %s"%(a,c))
        return
    
    #Move n-1 disks from A to B using C
    TowerHanoi(n-1,a,c,b)

    #Move nth disk from A to C
    print("Move disk %d from %s to %s"%(n,a,c))

    #Move n-1 disks from B to C using A
    TowerHanoi(n-1,b,a,c)

TowerHanoi(2,'A','B','C')

