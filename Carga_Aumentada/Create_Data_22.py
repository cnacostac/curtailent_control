# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 10:25:04 2019

@author: Nallely Acosta
"""

import statistics
import matplotlib
import numpy as np
import numpy
import matplotlib.pyplot as plt #abrir figuras en ventanas
import math
import re
import pandas as pd
import random
from matplotlib import collections  as mc
import opendss_class as opendss
from random import seed
from random import choice
from random import sample
import matplotlib.cm as cm
import time
import os
import heapq
from IPython import get_ipython


opendss = opendss.opendss()

t = time.process_time()
## Define the path where files are located
mydir = 'D:/open/casos/Carga_Aumentada'
Read_excel = 'D:\\open\\casos\\Carga_Aumentada\\'
PVprofiles = '(file=D:\\open\\casos\\Profiles\\LCTProfiles\\Norm_PV_Prof\\Nprofile_'
Loadprofiles = '(file=D:\\open\\casos\\Profiles\\LCTProfiles\\Norm_Load_Prof\\Nprofile_'

## Basic definitions
Data_Case=dict([\
                ['Conexiones', pd.read_excel(Read_excel + 'Lines.xlsx', header=None)],\
                ['WiresCatalogue', pd.read_excel(Read_excel + 'WiresCatalogue.xlsx', header=None)],\
                ['CableCatalogue', pd.read_excel(Read_excel + 'CableCatalogue.xlsx', header=None)],\
                ['LineGeometry', pd.read_excel(Read_excel + 'Geometry_Catalogue.xlsx', header=None)],\
                ['DistributedLoad', pd.read_excel(Read_excel + 'DistributedLoad.xlsx', header=None)],\
                ['LargeCustomers', pd.read_excel(Read_excel + 'Large_Customers.xlsx', header=None)],\
                ['WiresData', []],\
                ['CableData', []],\
                ['Lines', []],\
                ['Geometries', []],\
                ['Loads', []],\
                ['Loads_Daily', []],\
                ['Large_Customers', []],\
                ['Large_Customers_Daily', []],\
                ['Load_Shapes', []],\
                ['PV_Shapes', []],\
                ['hours', 288],\
                ])

 
#%%
for i in range(1,len(Data_Case['DistributedLoad'])):
    for ii in range(1,len(Data_Case['Conexiones'])):
        if str(Data_Case['DistributedLoad'][0][i]) == str(Data_Case['Conexiones'][0][ii]):
                if Data_Case['DistributedLoad'][6][i] or Data_Case['DistributedLoad'][9][i] != 0:
                    Data_Case['Loads'].append('New Load.Load_A_' + str(Data_Case['DistributedLoad'][0][i].lower()) + ' Phases=1 Bus1=' + str(Data_Case['Conexiones'][6][ii].lower()) +'.1 kv='+ str(Data_Case['DistributedLoad'][2][i]) +\
                             ' kw=' + str(Data_Case['DistributedLoad'][6][i]) + ' kvar=' + str(Data_Case['DistributedLoad'][9][i]*-1)+\
                             ' model=' + str(Data_Case['DistributedLoad'][12][i]) + ' conn=' + str(Data_Case['DistributedLoad'][13][i]))
                    Data_Case['Load_Shapes'].append('New Loadshape.LoadShape_Load_A_' + str(Data_Case['DistributedLoad'][0][i].lower()) +' npts='+ str(Data_Case['hours']) + \
                     ' interval=0.0833 mult=' + str(Loadprofiles) + str(i) + '.csv) useactual=false')
                    Data_Case['PV_Shapes'].append('New Loadshape.PVShape_Load_A_' + str(Data_Case['DistributedLoad'][0][i].lower()) +' npts='+ str(Data_Case['hours']) + \
                     ' interval=0.0833 mult=' + str(PVprofiles) + str(i) + '.csv) useactual=false')
                if Data_Case['DistributedLoad'][7][i] or Data_Case['DistributedLoad'][10][i] != 0:
                    Data_Case['Loads'].append('New Load.Load_B_' + str(Data_Case['DistributedLoad'][0][i].lower()) + ' Phases=1 Bus1=' + str(Data_Case['Conexiones'][6][ii].lower()) +'.2 kv='+ str(Data_Case['DistributedLoad'][2][i]) +\
                             ' kw=' + str(Data_Case['DistributedLoad'][7][i]) + ' kvar=' + str(Data_Case['DistributedLoad'][10][i]*-1)+\
                             ' model=' + str(Data_Case['DistributedLoad'][12][i]) + ' conn=' + str(Data_Case['DistributedLoad'][13][i]))
                    Data_Case['Load_Shapes'].append('New Loadshape.LoadShape_Load_B_' + str(Data_Case['DistributedLoad'][0][i].lower()) +' npts='+ str(Data_Case['hours']) + \
                     ' interval=0.0833 mult=' + str(Loadprofiles) + str(i) + '.csv) useactual=false')
                    Data_Case['PV_Shapes'].append('New Loadshape.PVShape_Load_B_' + str(Data_Case['DistributedLoad'][0][i].lower()) +' npts='+ str(Data_Case['hours']) + \
                     ' interval=0.0833 mult=' + str(PVprofiles) + str(i) + '.csv) useactual=false')
                if Data_Case['DistributedLoad'][8][i] or Data_Case['DistributedLoad'][11][i] != 0:
                    Data_Case['Loads'].append('New Load.Load_C_' + str(Data_Case['DistributedLoad'][0][i].lower()) + ' Phases=1 Bus1=' + str(Data_Case['Conexiones'][6][ii].lower()) +'.3 kv='+ str(Data_Case['DistributedLoad'][2][i]) +\
                             ' kw=' + str(Data_Case['DistributedLoad'][8][i]) + ' kvar=' + str(Data_Case['DistributedLoad'][11][i]*-1)+\
                             ' model=' + str(Data_Case['DistributedLoad'][12][i]) + ' conn=' + str(Data_Case['DistributedLoad'][13][i]))
                    Data_Case['Load_Shapes'].append('New Loadshape.LoadShape_Load_C_' + str(Data_Case['DistributedLoad'][0][i].lower()) +' npts='+ str(Data_Case['hours']) + \
                     ' interval=0.0833 mult=' + str(Loadprofiles) + str(i) + '.csv) useactual=false')
                    Data_Case['PV_Shapes'].append('New Loadshape.PVShape_Load_C_' + str(Data_Case['DistributedLoad'][0][i].lower()) +' npts='+ str(Data_Case['hours']) + \
                     ' interval=0.0833 mult=' + str(PVprofiles) + str(i) + '.csv) useactual=false')



for i in range(1,len(Data_Case['DistributedLoad'])):
    for ii in range(1,len(Data_Case['Conexiones'])):
        if str(Data_Case['DistributedLoad'][0][i]) == str(Data_Case['Conexiones'][0][ii]):
                if Data_Case['DistributedLoad'][6][i] or Data_Case['DistributedLoad'][9][i] != 0:
                    Data_Case['Loads_Daily'].append('New Load.Load_A_' + str(Data_Case['DistributedLoad'][0][i].lower()) + ' Phases=1 Bus1=' + str(Data_Case['Conexiones'][6][ii].lower()) +'.1 kv='+ str(Data_Case['DistributedLoad'][2][i]) +\
                             ' kw=' + str(Data_Case['DistributedLoad'][6][i]) + ' kvar=' + str(Data_Case['DistributedLoad'][9][i]*-1)+\
                             ' model=' + str(Data_Case['DistributedLoad'][12][i]) + ' conn=' + str(Data_Case['DistributedLoad'][13][i]) +' Daily=LoadShape_Load_A_'+str(Data_Case['DistributedLoad'][0][i].lower()))
                    
                if Data_Case['DistributedLoad'][7][i] or Data_Case['DistributedLoad'][10][i] != 0:
                    Data_Case['Loads_Daily'].append('New Load.Load_B_' + str(Data_Case['DistributedLoad'][0][i].lower()) + ' Phases=1 Bus1=' + str(Data_Case['Conexiones'][6][ii].lower()) +'.2 kv='+ str(Data_Case['DistributedLoad'][2][i]) +\
                             ' kw=' + str(Data_Case['DistributedLoad'][7][i]) + ' kvar=' + str(Data_Case['DistributedLoad'][10][i]*-1)+\
                             ' model=' + str(Data_Case['DistributedLoad'][12][i]) + ' conn=' + str(Data_Case['DistributedLoad'][13][i]) +' Daily=LoadShape_Load_B_'+str(Data_Case['DistributedLoad'][0][i].lower()))
                  
                if Data_Case['DistributedLoad'][8][i] or Data_Case['DistributedLoad'][11][i] != 0:
                    Data_Case['Loads_Daily'].append('New Load.Load_C_' + str(Data_Case['DistributedLoad'][0][i].lower()) + ' Phases=1 Bus1=' + str(Data_Case['Conexiones'][6][ii].lower()) +'.3 kv='+ str(Data_Case['DistributedLoad'][2][i]) +\
                             ' kw=' + str(Data_Case['DistributedLoad'][8][i]) + ' kvar=' + str(Data_Case['DistributedLoad'][11][i]*-1)+\
                             ' model=' + str(Data_Case['DistributedLoad'][12][i]) + ' conn=' + str(Data_Case['DistributedLoad'][13][i]) +' Daily=LoadShape_Load_C_'+str(Data_Case['DistributedLoad'][0][i].lower()))
#'New Generator.PV' + str(Data_PV['baxe'][0][0][ipv]) + ' ' + str(Data_Customers['PVS_n'][3][Data_PV['baxe'][0][0][ipv]]) +' ' + str(Data_Customers['PVS_n'][4][Data_PV['baxe'][0][0][ipv]]) + ' ' + str(Data_Customers['PVS_n'][2][Data_PV['baxe'][0][0][ipv]]) +' kw='+str(Data_PV['baxe'][0][1][ipv]) +' pf=1 model=7 status=variable daily=PVShape_' +str(Data_PV['baxe'][0][0][ipv])                    


for i in range(2,len(Data_Case['LargeCustomers'])):
    for ii in range(1,len(Data_Case['Conexiones'])):
        if str(Data_Case['LargeCustomers'][2][i]) == str(Data_Case['Conexiones'][0][ii]):
                if Data_Case['LargeCustomers'][3][i] != 'Large Customer (Off)':
                    Data_Case['Large_Customers'].append('New Load.Load_' + str(Data_Case['LargeCustomers'][1][i].lower()) + ' Phases='+str(Data_Case['LargeCustomers'][4][i])+' Bus1=' + str(Data_Case['Conexiones'][7][ii].lower()) +' kv='+ str(Data_Case['LargeCustomers'][5][i]) +\
                             ' kw=' + str(Data_Case['LargeCustomers'][6][i]) + ' kvar=' + str(Data_Case['LargeCustomers'][7][i])+\
                             ' model=' + str(Data_Case['LargeCustomers'][9][i]) + ' conn=' + str(Data_Case['LargeCustomers'][10][i]))
                    Data_Case['Load_Shapes'].append('New Loadshape.LoadShape_Load_' + str(Data_Case['LargeCustomers'][1][i].lower()) +' npts='+ str(Data_Case['hours']) + \
                     ' interval=0.0833 mult=' + str(Loadprofiles) + str(i) + '.csv) useactual=false')
                    Data_Case['Large_Customers_Daily'].append('New Load.Load_' + str(Data_Case['LargeCustomers'][1][i].lower()) + ' Phases='+str(Data_Case['LargeCustomers'][4][i])+' Bus1=' + str(Data_Case['Conexiones'][7][ii].lower()) +' kv='+ str(Data_Case['LargeCustomers'][5][i]) +\
                             ' kw=' + str(Data_Case['LargeCustomers'][6][i]) + ' kvar=' + str(Data_Case['LargeCustomers'][7][i])+\
                             ' model=' + str(Data_Case['LargeCustomers'][9][i]) + ' conn=' + str(Data_Case['LargeCustomers'][10][i]) +' Daily=LoadShape_Load_' + str(Data_Case['LargeCustomers'][1][i].lower()))
                    




#%%    
#file = open('Line_Data-2.txt','w') 
#for i in range(len(Data_Case['Lines'])):
#    file.write(Data_Case['Lines'][i]) 
#    file.write('\n') 
#file = open('Geometry_Data-2.txt','w') 
#for i in range(len(Data_Case['Geometries'])):
#    file.write(Data_Case['Geometries'][i]) 
#    file.write('\n')    
#file = open('Wire_Data-2.txt','w') 
#for i in range(len(Data_Case['WiresData'])):
#    file.write(Data_Case['WiresData'][i]) 
#    file.write('\n')   
#file = open('Load_Data-2.txt','w') 
#for i in range(len(Data_Case['Loads'])):
#    file.write(Data_Case['Loads'][i]) 
#    file.write('\n')  
                    
file = open('LargeCustomer_Data-33.txt','w') 
for i in range(len(Data_Case['Large_Customers'])):
    file.write(Data_Case['Large_Customers'][i]) 
    file.write('\n')  

file = open('LargeCustomer_Daily-33.txt','w') 
for i in range(len(Data_Case['Large_Customers_Daily'])):
    file.write(Data_Case['Large_Customers_Daily'][i]) 
    file.write('\n') 
#
#file = open('Cable_Data-2.txt','w') 
#for i in range(len(Data_Case['CableData'])):
#    file.write(Data_Case['CableData'][i]) 
#    file.write('\n') 
#
#file = open('BusCoords-2.txt','w') 
#for i in range(1,len(Data_Case['Conexiones'])):
#    file.write(str(Data_Case['Conexiones'][6][i].lower())+', '+str(Data_Case['Conexiones'][13][i])+', '+str(Data_Case['Conexiones'][14][i])) 
#    file.write('\n')
#    file.write(str(Data_Case['Conexiones'][7][i].lower())+', '+str(Data_Case['Conexiones'][13][i])+', '+str(Data_Case['Conexiones'][14][i])) 
#    file.write('\n')
#
file = open('LoadShapes-33.txt','w') 
for i in range(len(Data_Case['Load_Shapes'])):
    file.write(Data_Case['Load_Shapes'][i]) 
    file.write('\n')  
#
file = open('PVhapes-33.txt','w') 
for i in range(len(Data_Case['PV_Shapes'])):
    file.write(Data_Case['PV_Shapes'][i]) 
    file.write('\n')      
#
#
#
#file = open('LoadDailys-2.txt','w') 
#for i in range(len(Data_Case['Loads_Daily'])):
#    file.write(Data_Case['Loads_Daily'][i]) 
#    file.write('\n')  
#    
#
#file = open('Master-1.txt','w') 
#file.write('Wire_Data.txt'+\
#           '\nGeometry_Data.txt'+\
#           '\nLine_Data.txt'+\
#           '\nLoad_Data.txt') 
    
    #%%
print('listo')
##
get_ipython().magic('reset -sf')
