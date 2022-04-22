# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 14:11:40 2020

@author: lanal
"""

V=[]
P=[]
ESu=[]
E=[]
XYZ=[]
Vmin=[]
XYZmin=[]
I=[]
#NEMA=[]
for i in range(len(Data_Voltage['Vmax_bus_history'])):
    for ii in range(len(Data_Voltage['Vmax_bus_history'][i])):
        E.append(-1*Data_Meters_SE['EMeters_history'][i][ii][0][0]/1000)
        V.append(Data_Voltage['Vmax_bus_history'][i][ii])
        P.append(Data_PV['PerPen_history'][i][ii])
        XYZ.append([Data_PV['PerPen_history'][i][ii],-1*Data_Meters_SE['EMeters_history'][i][ii][0][0]/1000,Data_Voltage['Vmax_bus_history'][i][ii]])
        Vmin.append(Data_Voltage['Vmin_bus_history'][i][ii])
        I.append(np.max(Data_Current['Iut_normamps_history'][i][ii]))
        ESu.append(Data_PV['PV_average_history'][i][ii]*len(Data_Customers['PVS_n'])/(Data_Case['SE_CAP']*1000)*100)
        
V=np.array(V)
Vmin=np.array(Vmin)
P=np.array(P)
ESu=np.array(ESu)
E=np.array(E)
CP=[gencur_adj,gencur_adjup,gen_min,Data_Case['OverCurrentLimit']]
str_list=['V','I','Ene','P','Vmin','I','Ene','P','ESu%','ConPar']
df = pd.DataFrame ([V,I,E,P,Vmin,I,E,P,ESu,CP])
df = df.transpose()
filepath = 'PVE'+'_'+str(case_name)+'_'+str(Data_Impact['MonteCarlo_Iterations'])+'MC-'+str(int(gencur_adj*100))+str(int(gen_min*100))+str(int(Data_Case['OverCurrentLimit']*100))+'.xlsx'
df.to_excel(mydir +'/'+'Report/'+filepath, index=False, header=str_list)