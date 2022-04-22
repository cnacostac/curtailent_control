# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 13:15:13 2020

@author: lanal
"""

file = open(mydir +'/'+'Report/'+'Report_'+str(case_name)+'_'+str(Data_Impact['MonteCarlo_Iterations'])+'MC-'+str(int(gencur_adj*100))+str(int(gen_min*100))+str(int(Data_Case['OverCurrentLimit']*100))+'.txt','w')
file.write('\n       HC IMPACT STUDY (VOLTAGE LIMITS COMPLIANCE)')
file.write('\n----------------------------------------------------')
file.write('\n')
for key,value in Data_HC['HC_voltage_Impact'].items():
    file.write("Key : {} , Value : {}".format(key,value))
    file.write('\n')
    
file.write('\n       HC IMPACT STUDY (VOLTAGE min LIMITS COMPLIANCE)')
file.write('\n----------------------------------------------------')
file.write('\n')
for key,value in Data_HC['HC_voltage_Impact_min'].items():
    file.write("Key : {} , Value : {}".format(key,value))
    file.write('\n')

file.write('\n')
file.write('\n       HC IMPACT STUDY (CURRENT LIMITS)')
file.write('\n----------------------------------------------------')
file.write('\n')
for key,value in Data_HC['Current_Flags'].items():
    file.write("Key : {} , Value : {}".format(key,value))
    file.write('\n')

file.write('\n')
file.write('\n       HC IMPACT STUDY (VOLTAGE LIMITS SUP)')
file.write('\n----------------------------------------------------')
file.write('\n')
for key,value in Data_HC['Voltage_Flags_Sup'].items():
    file.write("Key : {} , Value : {}".format(key,value))
    file.write('\n')

file.write('\n')
file.write('\n       HC IMPACT STUDY (VOLTAGE LIMITS INF)')
file.write('\n----------------------------------------------------')
file.write('\n')
for key,value in Data_HC['Voltage_Flags_Min'].items():
    file.write("Key : {} , Value : {}".format(key,value))
    file.write('\n')

    

 
file.close()