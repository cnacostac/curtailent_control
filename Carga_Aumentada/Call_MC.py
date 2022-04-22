# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 19:22:11 2020

@author: lanal
"""

Data_Impact['PerPen'] = []
Data_Impact['Per_actual'] = 0
Data_Impact['itera'] = 0
seed(x_seed[iMC])
while(Data_Impact['Pmax'] >= Data_Impact['Per_actual']):
    Pinc_rand=random.randrange(1,10)
    Data_Impact['Per_actual'] += Pinc_rand
    Data_Impact['PerPen'].append(np.array(Data_Impact['Per_actual']))    
    Data_Impact['itera'] += 1
    if Data_Impact['PerPen'][len(Data_Impact['PerPen'])-1] > Data_Impact['Pmax']:
        Data_Impact['PerPen'][len(Data_Impact['PerPen'])-1]=Data_Impact['Pmax']
        Data_Impact['PerPen']=np.asarray(Data_Impact['PerPen'])
        print(Data_Impact['PerPen'], len(Data_Impact['PerPen']), x_seed[iMC], iMC)
        
        MC_simulations.append(len(Data_Impact['PerPen']))