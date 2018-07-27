import numpy as np
import re
import pingparsing
import sys
import os
import matplotlib.pyplot as plt

path = "./Logs/MacOS/"
figures_path = "./Figures/"


def plotHistogram(title,x_label,y_label,values_list,name):
    #Histogram
    histrogram = plt.figure(1)
    plt.hist(values_list, align='left')
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    print "Saving Histogram plot in 'Figures' folder."
    #bins_labels(bins, fontsize = 5)
    histrogram.savefig(figures_path+name+'.Histogram.png',dpi = 300)
    plt.close()

    return 

RSSI_Values = []
Noise_Values = []
TxRate_Values = []
MaxTxRate_Values = []

files_list = os.listdir(path)

for filename in files_list:
    file_name = os.path.join(path,filename)
    print ("Processing File: "+file_name)
    with open(file_name) as f:
        data = f.readlines()

    for line in data:
        if "agrCtlRSSI: " in line:
            RSSI = float(re.findall("[-+]\d*",line)[0])
            RSSI_Values.append(RSSI)
        elif "agrCtlNoise: " in line:
            noise = float(re.findall('[-+]\d*',line)[0])
            Noise_Values.append(noise)
        elif "lastTxRate: " in line:
            TxRate = int(re.findall('\d+',line)[0])
            TxRate_Values.append(TxRate)
        elif "maxRate: " in line:
            MaxRate = int(re.findall('\d+',line)[0])
            MaxTxRate_Values.append(MaxRate)

plotHistogram("RSSI Histogram","RSSI [dB]","Number of Events",RSSI_Values,"RSSI")
plotHistogram("Noise Histogram","Noise [dB]","Number of Events",Noise_Values,"Noise")
plotHistogram("Last Tx Rate","Data Rate [Mbps]","Number of Events",TxRate_Values,"TxRate")
plotHistogram("Max Tx Rate","Data Rate [Mbps]","Number of Events",MaxTxRate_Values,"MaxTxRate")

RSSI_Values = np.column_stack([RSSI_Values])
Noise_Values = np.column_stack([Noise_Values])
TxRate_Values = np.column_stack([TxRate_Values])
MaxTxRate_Values = np.column_stack([MaxTxRate_Values])

np.savetxt("./Results/RSSI_Values.dat", RSSI_Values, fmt='%f')
np.savetxt("./Results/Noise_Values.dat", Noise_Values, fmt='%f')
np.savetxt("./Results/TxRate_Values.dat", TxRate_Values, fmt='%d')
np.savetxt("./Results/MaxTxRateValues.dat", MaxTxRate_Values, fmt='%d')

print ("End of the Script")