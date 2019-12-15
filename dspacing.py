import csv
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib import pyplot as plt
from scipy.signal import find_peaks
import numpy as np

def get_column_data(numcol, numrows, datacsv):
    datatotal = []
    for i in range(1, numrows):
        data = datacsv[i][numcol]
        if data != '':
            data = float(data)
            datatotal.append(data)
    return np.asarray(datatotal).astype(float)

datacsv = []
csvfile = open('values.csv')
reader = csv.reader(csvfile, delimiter=',')
for row in reader:
    datacsv.append(row)
csvfile.close()
numrows = len(datacsv)
numcolumns = len(datacsv[1])

xdata = get_column_data(0, numrows, datacsv)
ydata = get_column_data(1, numrows, datacsv)

peaks, _ = find_peaks(ydata, height=3)

print(peaks)
print(xdata[peaks])
maxspacings = xdata[peaks]

dspacings = [x - maxspacings[i - 1] for i, x in enumerate(maxspacings)][1:]
print("d spacing (nm): ", np.nanmedian(dspacings))

plt.plot(xdata, ydata)
plt.plot(xdata[peaks], ydata[peaks], "x")
plt.tight_layout()
plt.show()

