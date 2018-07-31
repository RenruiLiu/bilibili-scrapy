#计算打野皇子
f = open('YeyinfuVideoTitles.txt','r')
lines = f.readlines()
total = 0
j4jg = 0
for line in lines:
    j4jg += line.count('打野皇子')
    total += line.count(':')
print('“打野皇子”四个字在总共267个视频内的一共',total,'p内出现了',j4jg,'次,占比',j4jg/total)
f.close()
