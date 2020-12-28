#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Date        : 
Autor       : Leonid Burmistrov
Description : Simple reminder-training example.
'''

import matplotlib.pyplot as plt
import seaborn as sns
from optparse import OptionParser

sns.set_theme()

iris = sns.load_dataset("iris")
tips = sns.load_dataset("tips")

print(' iris ',type(iris),' ',len(iris))
print(' tips ',type(tips),' ',len(tips))

def firstSeabornPlot():
    sns.relplot(data=tips,
                x="total_bill", y="tip", col="time",
                hue="smoker", style="smoker", size="size")
    plt.show()

def pairGridPlot():
    g = sns.PairGrid(iris, hue="species")
    g.map_diag(sns.histplot)
    g.map_offdiag(sns.scatterplot)
    g.add_legend()
    plt.show()
    
parser = OptionParser()
parser.add_option('-p', '--plot',
                  dest='plotID', type="int",default=1,
                  help="plot type")
(options, args) = parser.parse_args()
    
if __name__ == "__main__":
    if options.plotID == 1:
        firstSeabornPlot()
    elif options.plotID == 2:
        pairGridPlot()
    else :
        parser.print_help()
