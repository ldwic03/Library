def check(line,point1,point2):
    A,B,C=line[3]-line[1],line[0]-line[2],line[2]*line[1]-line[0]*line[3]
    if A*(point1[0]-point2[0])+B*(point1[1]-point2[1])==0:return 0
    t=(A*point1[0]+B*point1[1]+C)/(A*(point1[0]-point2[0])+B*(point1[1]-point2[1]))
    if 0<=t<=1 and line[0] < point1[0]+t*(point2[0]-point1[0]) < line[2]:return 1
    return 0
