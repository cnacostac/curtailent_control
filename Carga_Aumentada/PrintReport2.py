# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 13:16:26 2020

@author: lanal
"""

Data_HC['HC_voltage_Impact']
print('\n       HC IMPACT STUDY (VOLTAGE LIMITS COMPLIANCE)')
print('----------------------------------------------------')
for key,value in Data_HC['HC_voltage_Impact'].items():
    print("Key : {} , Value : {}".format(key,value))


Data_HC['HC_perstd_max_history_min']
print('\n       HC IMPACT STUDY (VOLTAGE min LIMITS COMPLIANCE)')
print('----------------------------------------------------')
for key,value in Data_HC['HC_voltage_Impact_min'].items():
    print("Key : {} , Value : {}".format(key,value))
    
print('\n       HC IMPACT STUDY (CURRENT LIMITS)')
print('----------------------------------------------------')
for key,value in Data_HC['Current_Flags'].items():
    print("Key : {} , Value : {}".format(key,value))

print('\n       HC IMPACT STUDY (VOLTAGE LIMITS SUP)')
print('----------------------------------------------------')
for key,value in Data_HC['Voltage_Flags_Sup'].items():
    print("Key : {} , Value : {}".format(key,value))
    
print('\n       HC IMPACT STUDY (VOLTAGE LIMITS INF)')
print('----------------------------------------------------')
for key,value in Data_HC['Voltage_Flags_Min'].items():
    print("Key : {} , Value : {}".format(key,value))

