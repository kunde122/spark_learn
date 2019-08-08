from pyspark import SparkContext

sc=SparkContext(appName='test')
lines = sc.textFile("./data/total00.txt")

gre=lines.count()
fsd=lines.first()
print(fsd.encode('utf-8'))
print('done')