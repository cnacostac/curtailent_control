# -*- coding: utf-8 -*-

__author__      = "Clarissa Nallely Acosta Campas"
__copyright__   = "Instituto Tecnológico de Morelia"
__credits__     = ["Clarissa Acosta","ITM"]
__description__ = " Script principal para ejecutar estudios"
__email__       = "cnacsotac@gmail.com"
__status__      = "En desarrollo, última actualizacion Junio / 2021"

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
import datetime as dt
opendss = opendss.opendss()
import datetime
import matplotlib as mpl
import matplotlib as mpl


currentDT = datetime.datetime.now()
print (str(currentDT))

t = time.process_time()
## Define the path where files are located

mydir = 'D:/open/casos/Carga_Aumentada'
Read_excel = 'D:\\open\\casos\\Carga_Aumentada\\'
PVprofiles = '(file=D:\\open\\casos\\Profiles\\LCTProfiles\\Norm_PV_Prof\\Nprofile_'
Loadprofiles = '(file=D:\\open\\casos\\Profiles\\LCTProfiles\\Norm_Load_Prof\\Nprofile_'


LoadMult=1 # multiplicador de demanda 
GenMult1=1 # multiplicador de generación
gencur_adj=0.0 # reducción mttp Redmttp
gencur_adjup=0.0 # aumento mttp Incmttp
gen_min=0.8 # mínimo mttp mttpmin

vpu_tol=0.03 # banda Vbt
case_name='Case_Control'+str(LoadMult)

Data_Case=dict([\
                ['SE_CAP', 10.5],\
                ['hours', 288],\
                ['PVSize_data', np.divide([1, 5, 10, 30, 50,100,250,500],3)],\
                ['PerPVSize_data', np.divide([32,14,13,7,5,8,10,11],100)],\
                ['Vlimit_pu', [0.93, 1.05]],\
                ['Resolution_std-data', [10, 5]],\
                ['%-Cumplimiento-Tension', 95],\
                ['OverCurrentLimit', np.divide(60,100)],\
                ['CurrentLimit_%', 80],\
                ['SubestationSLimit_%', np.divide(80,100)],\
                ['TransformerSLimit_%', np.divide(80,100)],\
                ['Buses(0)_Nodes(1)', [0]],\
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
                ])

exec(open(mydir +'/'+'Read_Circuit_info.py').read())
exec(open(mydir +'/'+'Call_Dict2.py').read())

Data_Impact=dict([\
                ['Pmax', 100],\
                ['itera', 0],\
                ['Per_actual', 0],\
                ['PerPen', [0]],\
                ['MonteCarlo_Iterations',1],\
                ])
# Cada iteracion de monte carlo genera en promedio 20 escenarios diferentes. 
# para simular 1000 escenarios, por ejemplo, 'MonteCarlo_Iterations' debe tener
# un valor de 50.
   

#%%
## ****************************************************************************
#                              Initialize OpenDSS
# *****************************************************************************

import DSSStartup as dsss
DSSStartOK, DSSObj, DSSText = dsss.DSSStartup()
if not DSSStartOK:
    print('Unable to start the OpenDSS Engine')
    import sys
    sys.exit()

DSSText = DSSObj.Text                                                          #   Set up the Text
DSSText.Command = 'set DefaultBaseFrequency=60'
DSSText.Command = 'clear'   
DSSCircuit = DSSObj.ActiveCircuit                                              #   Set up the Circuit
DSSSolution = DSSCircuit.Solution                                              #   Set up the Solution
ControlQueue = DSSCircuit.CtrlQueue                                            #   Set up the Control
DSSObj.AllowForms = 0 

###############################################################################
#  Llamar a los archivos txt
DSSText.Command = 'new circuit.example basekV=13.8 angle=0 frequency=60 phases=3' #   Clear text command
DSSText.Command = 'Edit Vsource.Source BasekV=13.8 pu=1.00 ISC3=3000 ISC1=2500 baseMVA=10'  #ISC3=3000  ISC1=2500'
DSSText.Command = 'New Transformer.TR1 Buses=[SourceBus, mrd04015] Conns=[delta, delta] kVs=[115, 13.8] kVAs=[20000, 10500] windings=2 phases=3' #red primaria
DSSText.Command = 'Redirect Wire_Data-2.txt'
DSSText.Command = 'Redirect Cable_Data-2.txt'
DSSText.Command = 'Redirect Geometry_Data-2.txt'
DSSText.Command = 'Redirect LargeCustomer_Data-33.txt'
DSSText.Command = 'Redirect Line_Data-2.txt'
DSSText.Command = 'Redirect Loads.txt'
DSSText.Command = 'New Capacitor.Cap_OH_135923 Bus1=nd_137372 phases=3 kvar=298 kV=13.8 states=1'
DSSText.Command = 'New monitor.SE Transformer.TR1 1 mode=1 ppolar=no'
DSSText.Command = 'New energymeter.TR1 element=Transformer.TR1 term= 1'
DSSText.Command = 'set voltagebases=[115,69,34.5,13.8,7.9674]'  #calcular voltajes en pu
DSSText.Command = 'calcv'
DSSText.Command = 'solve mode = snap'

DSSObj.ActiveCircuit.Solution.Solve()  #

Data_Customers['all_node_names']=opendss.DSSCircuit.AllNodeNames
Data_Customers['all_bus_names']=opendss.DSSCircuit.AllBusNames
Data_Customers['all_node_distances']=opendss.DSSCircuit.AllNodeDistances
Data_Customers['all_bus_distances']=opendss.DSSCircuit.AllBusDistances
Data_Customers['PVS_n']=pd.read_csv("Loads.txt",header=None, sep=' ') 
Data_Customers['PVS_n2']=pd.read_csv("Loads.txt",header=None, sep='.')
Data_Customers['Lines_n']=pd.read_csv("Line_Data-2.txt",header=None, sep=' ')
#%%

if Data_Case['Buses(0)_Nodes(1)'] == [0]: #buses
    for ie in range(0,1):
        for i in range(len(Data_Customers['all_bus_names'])):
            for ii in range(len(Data_Customers['PVS_n'])):
                if ('Bus1='+str(Data_Customers['all_bus_names'][i])) == str(Data_Customers['PVS_n'][3][ii])\
                or ('Bus1='+str(Data_Customers['all_bus_names'][i])+'.1') == str(Data_Customers['PVS_n'][3][ii])\
                or ('Bus1='+str(Data_Customers['all_bus_names'][i])+'.2') == str(Data_Customers['PVS_n'][3][ii])\
                or ('Bus1='+str(Data_Customers['all_bus_names'][i])+'.3') == str(Data_Customers['PVS_n'][3][ii]):
                    Data_Customers['NodeNames_BusV'].append(i)   
    for i in range(len(Data_Customers['NodeNames_BusV'])):
        Data_Customers['NodeNames_Locations'].append(Data_Customers['all_bus_distances'][Data_Customers['NodeNames_BusV'][i]])                  
elif Data_Case['Buses(0)_Nodes(1)'] == [1]: #nodos
    for ie in range(0,1):
        for i in range(len(Data_Customers['all_node_names'])):
            for ii in range(len(Data_Customers['PVS_n'])):
                if ('Bus1='+str(Data_Customers['all_node_names'][i])) == str(Data_Customers['PVS_n'][3][ii]):
                    Data_Customers['NodeNames_BusV'].append(i)
        for i in range(len(Data_Customers['all_bus_names'])):
                for ii in range(len(Data_Customers['PVS_n'])):
                    if ('Bus1='+str(Data_Customers['all_bus_names'][i])) == str(Data_Customers['PVS_n'][3][ii]):
                        Data_Customers['NodeNames_BusV'].append(i)
    for i in range(len(Data_Customers['NodeNames_BusV'])):
        Data_Customers['NodeNames_Locations'].append(Data_Customers['all_node_distances'][Data_Customers['NodeNames_BusV'][i]])

seed(1)
sequence = [i for i in range(len(Data_Customers['PVS_n']))]

for i in range(Data_Impact['MonteCarlo_Iterations']):
    x_seed.append(random.randrange(1,Data_Impact['MonteCarlo_Iterations']*1000))   
#x_seed=[15987]    
print(x_seed)

#%%    

MC_simulations=[]

for iMC in range(Data_Impact['MonteCarlo_Iterations']):
    DSSText = DSSObj.Text                                                          #   Set up the Text
    DSSText.Command = 'set DefaultBaseFrequency=60'
    DSSText.Command = 'clear'   
    DSSCircuit = DSSObj.ActiveCircuit                                              #   Set up the Circuit
    DSSSolution = DSSCircuit.Solution                                              #   Set up the Solution
    ControlQueue = DSSCircuit.CtrlQueue                                            #   Set up the Control
    DSSObj.AllowForms = 0 
    
    ###############################################################################
    #  Llamar a los archivos txt
    DSSText.Command = 'new circuit.example basekV=13.8 angle=0 frequency=60 phases=3' #   Clear text command
    DSSText.Command = 'Edit Vsource.Source BasekV=13.8 pu=1.00 ISC3=3000 ISC1=2500 baseMVA=10'  #ISC3=3000  ISC1=2500'
    DSSText.Command = 'New Transformer.TR1 Buses=[SourceBus, mrd04015] Conns=[delta, delta] kVs=[115, 13.8] kVAs=[20000, 10500] windings=2 phases=3 maxtap=1.05 mintap=0.93' #red primaria
    DSSText.Command = 'new regcontrol.TapTR1 transformer=TR1 winding=2 tapwinding=2 vreg=(100) ptratio=80 band=2 maxtapchange=1.05'  #1
    DSSText.Command = 'Redirect Wire_Data-2.txt'
    DSSText.Command = 'Redirect Cable_Data-2.txt'
    DSSText.Command = 'Redirect Geometry_Data-2.txt'
    DSSText.Command = 'Redirect Line_Data-2.txt'
    DSSText.Command = 'Redirect LoadShapes-33.txt'
    DSSText.Command = 'Redirect LargeCustomer_Daily-33.txt'
    DSSText.Command = 'Redirect LoadDailys-3.txt'
    DSSText.Command = 'New Capacitor.Cap_OH_135923 Bus1=nd_137372 phases=3 kvar=298 kV=13.8 states=1'
    DSSText.Command = 'New monitor.SE Transformer.TR1 1 mode=1 ppolar=no'
    DSSText.Command = 'new monitor.TapTR1 element=transformer.TR1 terminal=2 mode=2'
    DSSText.Command = 'New energymeter.TR1 element=Transformer.TR1 term= 1'
    
    exec(open(mydir +'/'+'Call_MC.py').read())
    exec(open(mydir +'/'+'Simulation_MC.py').read())
    
    

#%%   
elapsed_time = time.process_time() - t
print('Elapsed Time: '+str(elapsed_time)+ ' seg ||| '+str(elapsed_time/60)+ ' min')           

currentDT = datetime.datetime.now()
print (str(currentDT))

print('Stochastic total simulations: '+str(np.sum(MC_simulations)))
#%%
for i in range(len(Data_PV['PVquant_history'])):
    Data_PV['PV_average'] = []
    for ii in range(len(Data_PV['PVquant_history'][i])):    
        Data_PV['PV_average'].append(np.sum(Data_Case['PVSize_data']*np.array(Data_PV['PVquant_history'][i][ii]))/len(Data_Customers['PVS_n']))
    Data_PV['PV_average_history'].append(Data_PV['PV_average'])


#%%
    
exec(open("Data_HC_estimate_lite.py").read())
exec(open("PrintReport2.py").read())
#exec(open("ReportTXT2.py").read())
#exec(open("ordenarPVE.py").read())


