from pyspark import SparkContext

sc=SparkContext(appName='test')
lines = sc.textFile("E:\pythonProject\pysparktest.txt")