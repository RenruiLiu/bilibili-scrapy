#计算皇子
f = open('YeyinfuVideoTitles.txt','r')
lines = f.readlines()
total = 0
j4 = 0
for line in lines:
    j4 += line.count('皇子')
    total += line.count(':')
print('“皇子”俩字在总共',total,'p内出现了',j4,'次,占比',j4/total)
f.close()
