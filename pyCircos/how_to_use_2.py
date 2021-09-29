import sys 
import numpy as np
sys.path.append("../../")
from pycircos import * 
import pandas as pd

df = pd.read_csv("C:\\Users\\chris\\Google Drive\\Data Science\\Projects\\Circos\\pyCircos\\Energy_Use_Cases_Data_Assets_Relationships.csv", encoding='unicode_escape')

data_sources = df['Data_Sources'].tolist()

use_cases = df.columns.tolist()
use_cases.pop(0)

relations = df.drop('Data_Sources', axis=1).to_numpy()

if __name__ == "__main__":
    gcircle = Gcircle()
    for i in range(len(use_cases)): #create a locus for each use case
        gcircle.add_locus(use_cases[i], 1000, bottom=900, height=100, facecolor="#ED665D") #name, length, bottom (0<=bottom<=1000), height (0<=bottom<=1000)
    for i in range(len(data_sources)): # create a locus for each data source   
        gcircle.add_locus(data_sources[i], 1000, bottom=900, height=100, facecolor="#6DCCDA") #name, length, bottom (0<=bottom<=1000), height (0<=bottom<=1000)    
    gcircle.set_locus() #Create figure object


    for u in range(relations[0,:].size): # for each use case
        for d in range(relations[:,0].size): # for each data source
            if relations[d,u] != 0:
                locus_size_use_case = len(gcircle.locus_dict[use_cases[u]]["positions"])-2
                locus_size_data_source = len(gcircle.locus_dict[data_sources[d]]["positions"])-2
                line_width = 0.2 # width of relations chords as a percentage of locus width (0.2 = 20% of locus width)

                gcircle.chord_plot(
                    (use_cases[u], round((locus_size_use_case)*(0.5-line_width/2)),round((locus_size_use_case)*(0.5+line_width/2))), 
                    (data_sources[d], round((locus_size_data_source)*(0.5-line_width/2)),round((locus_size_data_source)*(0.5+line_width/2))), 
                    bottom=900, alpha=0.1)
    
    gcircle.save(format = 'svg')        


'''    gcircle.add_locus("1", 1000, bottom=900, height=100) #name, length, bottom (0<=bottom<=1000), height (0<=bottom<=1000)
    gcircle.add_locus("2", 2000, bottom=900, height=100, facecolor="#ED665D")
    gcircle.add_locus("3", 3000, bottom=900, height=100, facecolor="#6DCCDA")
#    gcircle.add_locus("4", 2000, bottom=900, height=100, facecolor="#ED97CA")
#    gcircle.add_locus("5", 5000, bottom=900, height=50, facecolor="#EDC948")
    gcircle.set_locus() #Creat figure object
    gcircle.save()        
  
    data = np.random.rand(100)
    gcircle.scatter_plot("1", data, bottom=900, height=-100)
   
    data = np.random.rand(100)
    gcircle.line_plot("2", data, bottom=600, height=100)
   
    data = np.random.rand(100)
    gcircle.line_plot("2", data, bottom=600, height=100)
    
    data = np.random.rand(50)
    gcircle.heatmap("3", data, bottom=600, height=100)

    gcircle.chord_plot(["4", 1000, 1100], ["1", 200, 400], bottom=400)
    gcircle.chord_plot(["5", 1000, 1100, 950], ["3", 1000, 2000, 600], color="#FF0000")
    gcircle.chord_plot(["5", 4000, 4500, 950], ["2", 500, 1000, 400], color="#F2BE2B")

    data = np.random.rand(50)
    gcircle.bar_plot("4", data, bottom=600, height=-200)
    
    data = np.random.rand(50)
    gcircle.bar_plot("4", data, bottom=600, height=200)
''' 
    