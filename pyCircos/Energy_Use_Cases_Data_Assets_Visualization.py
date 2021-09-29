import sys 
import numpy as np
from pandas.core.dtypes.missing import isnull
sys.path.append("../../")
from pycircos import * 
import pandas as pd

df = pd.read_csv("C:\\Users\\chris\\Google Drive\\Data Science\\Projects\\Circos\\pyCircos\\Energy_Use_Cases_Data_Assets_Relationships.csv", encoding='unicode_escape')

data_sources = df['Data_Sources'].tolist()

use_cases = df.columns.tolist()
use_cases.pop(0)

relations = df.drop('Data_Sources', axis=1).to_numpy()

colors = pd.read_csv("C:\\Users\\chris\\Google Drive\\Data Science\\Projects\\Circos\\pyCircos\\colors.csv", encoding='unicode_escape')
color_codes = colors['Color_Code'] # color codes to be used for data sources


if __name__ == "__main__":
    gcircle = Gcircle()
    for i in range(len(use_cases)): #create a locus for each use case
        if (i == len(use_cases)-1): #change interspace between use cases and data sources
            gcircle.add_locus(use_cases[i], 1000, bottom=900, height=100, facecolor="#ED665D", interspace = 0.3) #name, length, bottom (0<=bottom<=1000), height (0<=bottom<=1000)
        else: 
            gcircle.add_locus(use_cases[i], 1000, bottom=900, height=100, facecolor="#ED665D") #name, length, bottom (0<=bottom<=1000), height (0<=bottom<=1000)

    for i in range(len(data_sources)): # create a locus for each data source   
        if (i == len(data_sources)-1): #change interspace between use cases and data sources
            gcircle.add_locus(data_sources[i], 1000, bottom=900, height=100, facecolor=color_codes[i], interspace = 0.3) #name, length, bottom (0<=bottom<=1000), height (0<=bottom<=1000)    
        else: 
            gcircle.add_locus(data_sources[i], 1000, bottom=900, height=100, facecolor=color_codes[i]) #name, length, bottom (0<=bottom<=1000), height (0<=bottom<=1000)    
    gcircle.set_locus(figsize = (12, 12)) #Create figure object


    # add relations in form of a chord_plot
    for u in range(relations[0,:].size): # for each use case
        for d in range(relations[:,0].size): # for each data source
            if relations[d,u] != 0: #add relations chord in case data source is needed for this use case
                locus_size_use_case = len(gcircle.locus_dict[use_cases[u]]["positions"])-2
                locus_size_data_source = len(gcircle.locus_dict[data_sources[d]]["positions"])-2
                line_width = 0.2 # width of relations chords as a percentage of locus width (0.2 = 20% of locus width)

                gcircle.chord_plot(
                    (use_cases[u], round((locus_size_use_case)*(0.5-line_width/2)),round((locus_size_use_case)*(0.5+line_width/2))), 
                    (data_sources[d], round((locus_size_data_source)*(0.5-line_width/2)),round((locus_size_data_source)*(0.5+line_width/2))), 
                    bottom=900, alpha=0.5,color = color_codes[d])
    
    gcircle.save(format = 'svg')  