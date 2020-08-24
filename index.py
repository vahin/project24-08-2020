from pandas import read_csv as rc;import statistics as sts;
def x(csv, column):
    listX = [float(x)for x in rc(csv)[column].to_list()]
    listXMean, listXMedian, listXMode, listXStd = sts.mean(listX), sts.median(listX), sts.mode(listX), sts.stdev(listX)
    x1s, x1e = listXMean-listXStd, listXMean+listXStd
    x2s, x2e = listXMean-(2*listXStd), listXMean+(2*listXStd)
    x3s, x3e = listXMean-(3*listXStd), listXMean+(3*listXStd)
    y1 = [x for x in listX if x>listXMean-listXStd and x<listXMean+listXStd]
    y2 = [x for x in listX if x>listXMean-(2*listXStd) and x<listXMean+(2*listXStd)]
    y3 = [x for x in listX if x>listXMean-(3*listXStd) and x<listXMean+(3*listXStd)]
    return [listX, listXMean, listXMedian, listXMode, listXStd, y1, y2, y3]
csv,col = "studentPerformance.csv","reading score"
print("Mean of Reading Score:", x(csv, col)[1])
print("Meadian of Reading Score:", x(csv, col)[2])
print("Mode of Reading Score:", x(csv, col)[3])
print("Standard Deviation of Reading Score:", x(csv, col)[4]);print();print()
print("Percentage of data within First Standard Deviation of Reading Score:", len(x(csv, col)[5])*100/len(x(csv, col)[0]));print()
print("Data within First Standard Deviation of Reading Score:", x(csv, col)[5]);print()
print("Percentage of data within Second Standard Deviation of Reading Score:", len(x(csv, col)[6])*100/len(x(csv, col)[0]));print()
print("Data within Second Standard Deviation of Reading Score:", x(csv, col)[6]);print()
print("Percentage of data within Third Standard Deviation of Reading Score:", len(x(csv, col)[7])*100/len(x(csv, col)[0]));print()
print("Data within Third Standard Deviation of Reading Score:", x(csv, col)[7]);print()
