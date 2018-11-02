import csv
import plotSignal as plot
with open('aa_no infu.csv', 'r') as f:
    reader = csv.reader(f)
    ls = list(reader)
ls = [float(x[0]) for x in ls]

plot.signalStem(ls)