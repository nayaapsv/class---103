import csv
import statistics
with open ('SOCR-HeightWeight.csv',newline='')as f:
    reader = csv.reader(f)
    data = list(reader)
    
data.pop(0)
newdata = []

for i in range(len(data)):
    num = data[i][2]
    newdata.append(float(num))
    
n = len(newdata)

if n%2 ==0:
    median1 = float(newdata[n//2])
    median2 = float(newdata[n//2-1])
    median = (median1+median2)/2

else:
    median = newdata[n//2]

print(median)
print(statistics.median(newdata))