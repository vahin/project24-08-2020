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

print("Mean of Reading Score:", x("studentPerformance.csv", "reading score")[1])
print("Meadian of Reading Score:", x("studentPerformance.csv", "reading score")[2])
print("Mode of Reading Score:", x("studentPerformance.csv", "reading score")[3])
print("Standard Deviation of Reading Score:", x("studentPerformance.csv", "reading score")[4]);print();print()
print("Percentage of data within First Standard Deviation of Reading Score:", len(x("studentPerformance.csv", "reading score")[5])*100/len(x("studentPerformance.csv", "reading score")[0]));print()
print("Data within First Standard Deviation of Reading Score:", x("studentPerformance.csv", "reading score")[5]);print()
print("Percentage of data within Second Standard Deviation of Reading Score:", len(x("studentPerformance.csv", "reading score")[6])*100/len(x("studentPerformance.csv", "reading score")[0]));print()
print("Data within Second Standard Deviation of Reading Score:", x("studentPerformance.csv", "reading score")[6]);print()
print("Percentage of data within Third Standard Deviation of Reading Score:", len(x("studentPerformance.csv", "reading score")[7])*100/len(x("studentPerformance.csv", "reading score")[0]));print()
print("Data within Third Standard Deviation of Reading Score:", x("studentPerformance.csv", "reading score")[7]);print()
