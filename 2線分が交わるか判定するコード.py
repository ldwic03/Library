def check(line,point1,point2):
    #line:どちらか一方の線分の2端点をそれぞれ(x1,y1),(x2,y2)としたときに、line=[x1,x2,y1,y2]の形式のリスト
    #point1:もう一方の線分の端点1
    #point2:もう一方の線分の端点2
    A,B,C=line[3]-line[1],line[0]-line[2],line[2]*line[1]-line[0]*line[3]
    if A*(point1[0]-point2[0])+B*(point1[1]-point2[1])==0:return 0
    t=(A*point1[0]+B*point1[1]+C)/(A*(point1[0]-point2[0])+B*(point1[1]-point2[1]))
    if 0<=t<=1 and line[0] < point1[0]+t*(point2[0]-point1[0]) < line[2]:return 1
    return 0
