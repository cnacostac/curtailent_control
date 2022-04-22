# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 14:25:53 2019

@author: lanal
"""
# Disctionaries
Data_ABB_iMC=dict([\
                   ['ABB_iMC', []],\
                   ['ABB', []],\
                   ['AB', []],\
                   ['BusVarray', []],\
                   ])

Data_Vmax_location=dict([\
                         ['Vmax_location', []],\
                         ['Distance_vmax_loc', []],\
                         ['Vmax_location_history', []],\
                         ])

Data_ABB_std=dict([\
                   ['ABB_iMC_std', []],\
                   ['ABB_iMC_std_pen', []],\
                   ['ABB_iMC_std_1', []],\
                   ['ABB_iMC_std_average', []],\
                   ])   

Data_ABB_iMC_custom_perquant=dict([\
                                   ['Quant_history', []],\
                                   ['Quant_history_min', []],\
                                   ['Percen_history', []],\
                                   ['Percen_history_min', []],\
                                   ['Index_history', []],\
                                   ['Index_history_min', []],\
                                   ['customers_problems', []],\
                                   ['index_daily', []],\
                                   ['day_problems', []],\
                                   ['index_2', []],\
                                   ['problems_quant', []],\
                                   ['problems_percen', []],\
                                   ['index_1', []],\
                                   ])    

Data_ABB_iMC_custom=dict([\
                          ['ABB_iMC_custom_problems', []],\
                          ['ABB_iMC_custom_problems-min', []],\
                          ['ABB_iMC_custom_issues', []],\
                          ['ABB_iMC_custom_issues-min', []],\
                          ['problems_quant', []],\
                          ['problems_quant-min', []],\
                          ['customer_compliment_issues', []],\
                          ['customer_compliment_issues_1', []],\
                          ['customer_compliment_issues_1-min', []],\
                          ['customer_compliance_1', []],\
                          ['customer_compliance_1-min', []],\
                          ['customer_compliance_zero', []],\
                          ['customer_compliance_zero-min', []],\
                          ['customer_compliance', []],\
                          ['customer_compliance-min', []],\
                          ['day_problems', []],\
                          ['day_problems-min', []],\
                          ['average_daily', []],\
                          ['average_daily-min', []],\
                          ['customers_problems', []],\
                          ['customers_problems-min', []],\
                          ['no_compliment', []],\
                          ['no_compliment-min', []],\
                          ['customer_nocompliment_arg', []],\
                          ['ABB_iMC_custom_index', []],\
                          ['ABB_iMC_custom_index-min', []],\
                          ['customer_nocompliment_arg_1', []],\
                          ['customer_nocompliment_arg_1-min', []],\
                          ['nocompliment_arg', []],\
                          ['nocompliment_arg-min', []],\
                          ])   

Data_HC=dict([\
              ['Current_Flags', []],\
              ['HC_V_history', []],\
              ['HC_Vav_history', []],\
              ['HC_perstd_max_history', []],\
              ['HC_perstdav_max_history', []],\
              ['HC_V_history_min', []],\
              ['HC_Vav_history_min', []],\
              ['HC_perstd_max_history_min', []],\
              ['HC_perstdav_max_history_min', []],\
              ['HC_voltage', []],\
              ['HC_voltage_av', []],\
              ['HC_percen_max_custom', []],\
              ['HC_percen_max_custom_av', []],\
              ['HC_voltage', []],\
              ['HC_voltage_Impact', []],\
              ['HC_voltage_Impact_min', []],\
              ['HC_current_Impact', []],\
              ['HC_Substation_Impact', []],\
              ])    
Data_HC['HC_voltage_Impact']=dict([\
                              ['Total GD installed', []],\
                              ['GD average per customer', []],\
                              ['Maximum Voltage (pu)', []],\
                              ['% GD Penetration', []],\
                              ['Index Time Issue', []],\
                              ['Maximum % customer with issues', []],\
                              ['Index Customer Issue', []],\
                              ['Customer Distance from Substation', []],\
                              ])  
Data_HC['HC_voltage_Impact_min']=dict([\
                              ['Total GD installed', []],\
                              ['GD average per customer', []],\
                              ['Maximum Voltage (pu)', []],\
                              ['% GD Penetration', []],\
                              ['Index Time Issue', []],\
                              ['Maximum % customer with issues', []],\
                              ['Index Customer Issue', []],\
                              ['Customer Distance from Substation', []],\
                              ])  
Data_HC['Current_Flags']=dict([\
                              ['% Line Utilization', []],\
                              ['MC Case', []],\
                              ['% GD penetration', []],\
                              ['Index Time', []],\
                              ['Index Customer', []],\
                              ])  

Data_HC['Voltage_Flags']=dict([\
                              ['MC Case', []],\
                              ['% GD penetration', []],\
                              ['Index Time', []],\
                              ]) 

#%% save just the customers voltages
for irf in range(len(Data_Voltage['Vprof_all'])):
    Data_ABB_iMC['ABB'] = []
    for irt in range(len(Data_Voltage['Vprof_all'][irf])):
        Data_ABB_iMC['AB'] = []
        for iry in range(len(Data_Voltage['Vprof_all'][irf][irt])):
            Data_ABB_iMC['BusVarray'] = []
            for ii in range(len(Data_Customers['NodeNames_BusV'])):
                Data_ABB_iMC['BusVarray'].append(Data_Voltage['Vprof_all'][irf][irt][iry][Data_Customers['NodeNames_BusV'][ii]])                
            Data_ABB_iMC['AB'].append(Data_ABB_iMC['BusVarray'])
        Data_ABB_iMC['ABB'].append(Data_ABB_iMC['AB'])
    Data_ABB_iMC['ABB_iMC'].append(Data_ABB_iMC['ABB'])
    
# save customers voltage issues distances    
for i in range(len(Data_Voltage['VMax_mag_MC_loc_history'])):
    Data_Vmax_location['Vmax_location'] = []
    for ii in range(len(Data_Voltage['VMax_mag_MC_loc_history'][i])):
        Data_Vmax_location['Distance_vmax_loc'] = []
        for iii in range(len(Data_Voltage['VMax_mag_MC_loc_history'][i][ii])):
            Data_Vmax_location['Distance_vmax_loc'].append(Data_Customers['all_node_distances'][Data_Voltage['VMax_mag_MC_loc_history'][i][ii][iii]])
        Data_Vmax_location['Vmax_location'].append(Data_Vmax_location['Distance_vmax_loc'])
    Data_Vmax_location['Vmax_location_history'].append(Data_Vmax_location['Vmax_location'])
    
#%% change resolution for EN STD EN 50160 this code depends from the country std   
for i in range(len(Data_ABB_iMC['ABB_iMC'])):    
    Data_ABB_std['ABB_iMC_std_pen'] = []
    for ii in range(len(Data_ABB_iMC['ABB_iMC'][i])):
        Data_ABB_std['ABB_iMC_std_1'] = []
        for iii in range(0,len(Data_ABB_iMC['ABB_iMC'][i][ii]),int(Data_Case['Resolution_std-data'][0]/Data_Case['Resolution_std-data'][1])):             
            Data_ABB_std['ABB_iMC_std_average'] = []
            for iv in range(0,len(Data_ABB_iMC['ABB_iMC'][i][ii][iii])):  
                if iv < len(Data_ABB_iMC['ABB_iMC'][i][ii][iii]):
                    Data_ABB_std['ABB_iMC_std_average'].append((Data_ABB_iMC['ABB_iMC'][i][ii][iii][iv]+Data_ABB_iMC['ABB_iMC'][i][ii][iii+1][iv])/int(Data_Case['Resolution_std-data'][0]/Data_Case['Resolution_std-data'][1]))
            Data_ABB_std['ABB_iMC_std_1'].append(Data_ABB_std['ABB_iMC_std_average'])
        Data_ABB_std['ABB_iMC_std_pen'].append(Data_ABB_std['ABB_iMC_std_1'])
    Data_ABB_std['ABB_iMC_std'].append(Data_ABB_std['ABB_iMC_std_pen'])
    
#%% customers issues compliment and no compliment
for i in range(len(Data_ABB_std['ABB_iMC_std'])):
    Data_ABB_iMC_custom['customer_compliment_issues'] = [] 
    Data_ABB_iMC_custom['no_compliment'] = [] 
    Data_ABB_iMC_custom['problems_quant'] = []
    Data_ABB_iMC_custom['customer_compliment_issues-min'] = [] 
    Data_ABB_iMC_custom['no_compliment-min'] = [] 
    Data_ABB_iMC_custom['problems_quant-min'] = []
    Data_ABB_iMC_custom['customer_compliment_issues_1-min'] = [0]*(len(Data_Customers['PVS_n']))            
    for ii in range(len(Data_ABB_std['ABB_iMC_std'][i])):
        Data_ABB_iMC_custom['day_problems'] = []
        Data_ABB_iMC_custom['average_daily'] = []
        Data_ABB_iMC_custom['customer_compliment_issues_1'] = [0]*(len(Data_Customers['PVS_n']))  
        Data_ABB_iMC_custom['day_problems-min'] = []
        Data_ABB_iMC_custom['average_daily-min'] = []
        Data_ABB_iMC_custom['customer_compliment_issues_1-min'] = [0]*(len(Data_Customers['PVS_n']))  
        for iii in range(len(Data_Customers['NodeNames_BusV'])):
            Data_ABB_iMC_custom['customers_problems'] = 0
            Data_ABB_iMC_custom['customers_problems-min'] = 0
            for iv in range(len(Data_ABB_std['ABB_iMC_std'][i][ii])):
                if Data_ABB_std['ABB_iMC_std'][i][ii][iv][iii] >= Data_Case['Vlimit_pu'][1]:
                    Data_ABB_iMC_custom['customers_problems'] += 1
                    Data_ABB_iMC_custom['customer_compliment_issues_1'][iii] = 1
                if Data_ABB_std['ABB_iMC_std'][i][ii][iv][iii] <= Data_Case['Vlimit_pu'][0]:
                    Data_ABB_iMC_custom['customers_problems-min'] += 1
                    Data_ABB_iMC_custom['customer_compliment_issues_1-min'][iii] = 1
            Data_ABB_iMC_custom['day_problems'].append(Data_ABB_iMC_custom['customers_problems'])
            Data_ABB_iMC_custom['day_problems-min'].append(Data_ABB_iMC_custom['customers_problems-min'])
        Data_ABB_iMC_custom['customer_compliment_issues'].append(Data_ABB_iMC_custom['customer_compliment_issues_1'])
        Data_ABB_iMC_custom['customer_compliment_issues-min'].append(Data_ABB_iMC_custom['customer_compliment_issues_1-min'])
        Data_ABB_iMC_custom['problems_quant'].append(Data_ABB_iMC_custom['day_problems'])
        Data_ABB_iMC_custom['problems_quant-min'].append(Data_ABB_iMC_custom['day_problems-min'])
        Data_ABB_iMC_custom['no_compliment'].append(np.multiply(Data_ABB_iMC_custom['problems_quant'][ii],100/len(Data_ABB_std['ABB_iMC_std'][i][ii])))
        Data_ABB_iMC_custom['no_compliment-min'].append(np.multiply(Data_ABB_iMC_custom['problems_quant-min'][ii],100/len(Data_ABB_std['ABB_iMC_std'][i][ii])))
    Data_ABB_iMC_custom['ABB_iMC_custom_problems'].append(Data_ABB_iMC_custom['no_compliment'])
    Data_ABB_iMC_custom['ABB_iMC_custom_problems-min'].append(Data_ABB_iMC_custom['no_compliment-min'])
    Data_ABB_iMC_custom['ABB_iMC_custom_issues'].append(Data_ABB_iMC_custom['customer_compliment_issues'])
    Data_ABB_iMC_custom['ABB_iMC_custom_issues-min'].append(Data_ABB_iMC_custom['customer_compliment_issues-min'])

#%%
# extract index customer with problems   
for i in range(len(Data_ABB_iMC_custom['ABB_iMC_custom_issues'])):
    Data_ABB_iMC_custom['customer_nocompliment_arg_1'] = []
    Data_ABB_iMC_custom['customer_nocompliment_arg_1-min'] = []
    for ii in range(len(Data_ABB_iMC_custom['ABB_iMC_custom_issues'][i])):
        Data_ABB_iMC_custom['nocompliment_arg'] = []
        Data_ABB_iMC_custom['customer_compliance_zero'] = [0]*(len(Data_Customers['PVS_n']))
        Data_ABB_iMC_custom['nocompliment_arg-min'] = []
        Data_ABB_iMC_custom['customer_compliance_zero-min'] = [0]*(len(Data_Customers['PVS_n']))
        for iii in range(len(Data_ABB_iMC_custom['ABB_iMC_custom_problems'][i][ii])):
            if Data_ABB_iMC_custom['ABB_iMC_custom_issues'][i][ii][iii] == 1:
                Data_ABB_iMC_custom['nocompliment_arg'].append(iii)
            if Data_ABB_iMC_custom['ABB_iMC_custom_problems'][i][ii][iii] >= (100-Data_Case['%-Cumplimiento-Tension']):
                Data_ABB_iMC_custom['customer_compliance_zero'][iii] = 1
            if Data_ABB_iMC_custom['ABB_iMC_custom_issues-min'][i][ii][iii] == 1:
                Data_ABB_iMC_custom['nocompliment_arg-min'].append(iii)
            if Data_ABB_iMC_custom['ABB_iMC_custom_problems-min'][i][ii][iii] >= (100-Data_Case['%-Cumplimiento-Tension']):
                Data_ABB_iMC_custom['customer_compliance_zero-min'][iii] = 1
        Data_ABB_iMC_custom['customer_nocompliment_arg_1'].append(Data_ABB_iMC_custom['nocompliment_arg'])
        Data_ABB_iMC_custom['customer_compliance_1'].append(Data_ABB_iMC_custom['customer_compliance_zero'])
        Data_ABB_iMC_custom['customer_nocompliment_arg_1-min'].append(Data_ABB_iMC_custom['nocompliment_arg-min'])
        Data_ABB_iMC_custom['customer_compliance_1-min'].append(Data_ABB_iMC_custom['customer_compliance_zero-min'])
    Data_ABB_iMC_custom['ABB_iMC_custom_index'].append(Data_ABB_iMC_custom['customer_nocompliment_arg_1'])
    Data_ABB_iMC_custom['customer_compliance'].append(Data_ABB_iMC_custom['customer_compliance_1'])
    Data_ABB_iMC_custom['ABB_iMC_custom_index-min'].append(Data_ABB_iMC_custom['customer_nocompliment_arg_1-min'])
    Data_ABB_iMC_custom['customer_compliance-min'].append(Data_ABB_iMC_custom['customer_compliance_1-min'])

#%%
for i in range(len(Data_ABB_std['ABB_iMC_std'])):
    Data_ABB_iMC_custom_perquant['problems_quant'] = []
    Data_ABB_iMC_custom_perquant['problems_quant_min'] = []
    Data_ABB_iMC_custom_perquant['problems_percen'] = []
    Data_ABB_iMC_custom_perquant['problems_percen_min'] = []
    Data_ABB_iMC_custom_perquant['index_1'] = []
    Data_ABB_iMC_custom_perquant['index_1_min'] = []
    for ii in range(len(Data_ABB_std['ABB_iMC_std'][i])):
        Data_ABB_iMC_custom_perquant['day_problems'] = []
        Data_ABB_iMC_custom_perquant['day_problems_min'] = []
        Data_ABB_iMC_custom_perquant['index_daily'] = []
        Data_ABB_iMC_custom_perquant['index_daily_min'] = []
        for iii in range(len(Data_ABB_std['ABB_iMC_std'][i][ii])):
            Data_ABB_iMC_custom_perquant['customers_problems'] = 0
            Data_ABB_iMC_custom_perquant['customers_problems_min'] = 0
            Data_ABB_iMC_custom_perquant['index_2'] = []
            Data_ABB_iMC_custom_perquant['index_2_min'] = []
            for iv in range(len(Data_ABB_std['ABB_iMC_std'][i][ii][iii])):
                if Data_ABB_std['ABB_iMC_std'][i][ii][iii][iv] >= Data_Case['Vlimit_pu'][1]:
                    Data_ABB_iMC_custom_perquant['customers_problems'] += 1
                    Data_ABB_iMC_custom_perquant['index_daily'].append(iv)
                if Data_ABB_std['ABB_iMC_std'][i][ii][iii][iv] <= Data_Case['Vlimit_pu'][0]:
                    Data_ABB_iMC_custom_perquant['customers_problems_min'] += 1
                    Data_ABB_iMC_custom_perquant['index_daily_min'].append(iv)
            Data_ABB_iMC_custom_perquant['day_problems'].append(Data_ABB_iMC_custom_perquant['customers_problems'])
            Data_ABB_iMC_custom_perquant['day_problems_min'].append(Data_ABB_iMC_custom_perquant['customers_problems_min'])
            Data_ABB_iMC_custom_perquant['index_2'].append(Data_ABB_iMC_custom_perquant['index_daily'])
            Data_ABB_iMC_custom_perquant['index_2_min'].append(Data_ABB_iMC_custom_perquant['index_daily_min'])
        Data_ABB_iMC_custom_perquant['problems_quant'].append(Data_ABB_iMC_custom_perquant['day_problems'])
        Data_ABB_iMC_custom_perquant['problems_quant_min'].append(Data_ABB_iMC_custom_perquant['day_problems_min'])
        Data_ABB_iMC_custom_perquant['problems_percen'].append(np.multiply(Data_ABB_iMC_custom_perquant['problems_quant'][ii],100/len(Data_ABB_std['ABB_iMC_std'][i][ii][iii])))
        Data_ABB_iMC_custom_perquant['problems_percen_min'].append(np.multiply(Data_ABB_iMC_custom_perquant['problems_quant_min'][ii],100/len(Data_ABB_std['ABB_iMC_std'][i][ii][iii])))    
        Data_ABB_iMC_custom_perquant['index_1'].append(Data_ABB_iMC_custom_perquant['index_2'])
        Data_ABB_iMC_custom_perquant['index_1_min'].append(Data_ABB_iMC_custom_perquant['index_2_min'])
    Data_ABB_iMC_custom_perquant['Quant_history'].append(Data_ABB_iMC_custom_perquant['problems_quant'])
    Data_ABB_iMC_custom_perquant['Quant_history_min'].append(Data_ABB_iMC_custom_perquant['problems_quant_min'])
    Data_ABB_iMC_custom_perquant['Percen_history'].append(Data_ABB_iMC_custom_perquant['problems_percen'])
    Data_ABB_iMC_custom_perquant['Percen_history_min'].append(Data_ABB_iMC_custom_perquant['problems_percen_min'])
    Data_ABB_iMC_custom_perquant['Index_history'].append(Data_ABB_iMC_custom_perquant['index_1'])
    Data_ABB_iMC_custom_perquant['Index_history_min'].append(Data_ABB_iMC_custom_perquant['index_1_min'])

#%% HC estimation   
    
for i in range(len(Data_Voltage['Vmax_bus_history'])):
    Data_HC['HC_voltage'] = []
    Data_HC['HC_voltage_av'] = []
    Data_HC['HC_percen_max_custom'] = []
    Data_HC['HC_percen_max_custom_av'] = []
    Data_HC['HC_voltage_min'] = []
    Data_HC['HC_voltage_av_min'] = []
    Data_HC['HC_percen_max_custom_min'] = []
    Data_HC['HC_percen_max_custom_av_min'] = []
    for ii in range(len(Data_Voltage['Vmax_bus_history'][i])):
            if Data_Voltage['Vmax_bus_history'][i][ii] >= Data_Case['Vlimit_pu'][1] and np.max(Data_ABB_iMC_custom['ABB_iMC_custom_problems'][i][ii]) > 0:
                Data_HC['HC_voltage'].append([ii,Data_Voltage['Vmax_bus_history'][i][ii],\
                                             Data_PV['PV_average_history'][i][ii],Data_PV['PV_average_history'][i][ii]*len(Data_Customers['PVS_n']),\
                                             Data_PV['PerPen_history'][i][ii],np.argmax(Data_ABB_iMC_custom['ABB_iMC_custom_problems'][i][ii]),\
                                             np.max(Data_ABB_iMC_custom['ABB_iMC_custom_problems'][i][ii]),\
                                             Data_Voltage['Vmax_bus_location_history'][i][ii],\
                                             Data_Customers['all_node_distances'][Data_Voltage['Vmax_bus_location_history'][i][ii]],i,ii,np.max(Data_Current['Iut_normamps_history'][i][ii])])
                Data_HC['HC_voltage_av'].append([Data_PV['PV_average_history'][i][ii]])
                
            if np.max(Data_ABB_iMC_custom['ABB_iMC_custom_problems'][i][ii]) >= (100-Data_Case['%-Cumplimiento-Tension']):
                Data_HC['HC_percen_max_custom'].append([ii,Data_Voltage['Vmax_bus_history'][i][ii],\
                                             Data_PV['PV_average_history'][i][ii],Data_PV['PV_average_history'][i][ii]*len(Data_Customers['PVS_n']),\
                                             Data_PV['PerPen_history'][i][ii],np.argmax(Data_ABB_iMC_custom['ABB_iMC_custom_problems'][i][ii]),\
                                             np.max(Data_ABB_iMC_custom['ABB_iMC_custom_problems'][i][ii]),\
                                             Data_Voltage['Vmax_bus_location_history'][i][ii],\
                                             Data_Customers['all_node_distances'][Data_Voltage['Vmax_bus_location_history'][i][ii]],i,ii,np.max(Data_Current['Iut_normamps_history'][i][ii]),\
                                             np.max(Data_ABB_iMC_custom_perquant['Quant_history'][i][ii]),np.argmax(Data_ABB_iMC_custom_perquant['Quant_history'][i][ii]),Data_Voltage['Vmin_bus_history'][i][ii]])
                Data_HC['HC_percen_max_custom_av'].append([Data_PV['PV_average_history'][i][ii]])
                
            if Data_Voltage['Vmin_bus_history'][i][ii] <= Data_Case['Vlimit_pu'][0] and np.max(Data_ABB_iMC_custom['ABB_iMC_custom_problems-min'][i][ii]) > 0:
                Data_HC['HC_voltage_min'].append([ii,Data_Voltage['Vmin_bus_history'][i][ii],\
                                             Data_PV['PV_average_history'][i][ii],Data_PV['PV_average_history'][i][ii]*len(Data_Customers['PVS_n']),\
                                             Data_PV['PerPen_history'][i][ii],np.argmax(Data_ABB_iMC_custom['ABB_iMC_custom_problems-min'][i][ii]),\
                                             np.max(Data_ABB_iMC_custom['ABB_iMC_custom_problems-min'][i][ii]),\
                                             Data_Voltage['Vmin_bus_location_history'][i][ii],\
                                             Data_Customers['all_node_distances'][Data_Voltage['Vmin_bus_location_history'][i][ii]],i,ii,np.max(Data_Current['Iut_normamps_history'][i][ii]),\
                                             np.max(Data_ABB_iMC_custom_perquant['Quant_history_min'][i][ii]),np.argmax(Data_ABB_iMC_custom_perquant['Quant_history_min'][i][ii])])
                Data_HC['HC_voltage_av_min'].append([Data_PV['PV_average_history'][i][ii]])
                
            if np.max(Data_ABB_iMC_custom['ABB_iMC_custom_problems-min'][i][ii]) >= (100-Data_Case['%-Cumplimiento-Tension']):
                Data_HC['HC_percen_max_custom_min'].append([ii,Data_Voltage['Vmin_bus_history'][i][ii],\
                                             Data_PV['PV_average_history'][i][ii],Data_PV['PV_average_history'][i][ii]*len(Data_Customers['PVS_n']),\
                                             Data_PV['PerPen_history'][i][ii],np.argmax(Data_ABB_iMC_custom['ABB_iMC_custom_problems-min'][i][ii]),\
                                             np.max(Data_ABB_iMC_custom['ABB_iMC_custom_problems-min'][i][ii]),\
                                             Data_Voltage['Vmin_bus_location_history'][i][ii],\
                                             Data_Customers['all_node_distances'][Data_Voltage['Vmin_bus_location_history'][i][ii]],i,ii,np.max(Data_Current['Iut_normamps_history'][i][ii]),\
                                             np.max(Data_ABB_iMC_custom_perquant['Quant_history_min'][i][ii]),np.argmax(Data_ABB_iMC_custom_perquant['Quant_history_min'][i][ii]),Data_Voltage['Vmax_bus_history'][i][ii]])
                Data_HC['HC_percen_max_custom_av_min'].append([Data_PV['PV_average_history'][i][ii]])
                
    Data_HC['HC_V_history'].append(Data_HC['HC_voltage'])
    Data_HC['HC_Vav_history'].append(Data_HC['HC_voltage_av'])
    Data_HC['HC_perstd_max_history'].append(Data_HC['HC_percen_max_custom'])
    Data_HC['HC_perstdav_max_history'].append(Data_HC['HC_percen_max_custom_av'])
    Data_HC['HC_V_history_min'].append(Data_HC['HC_voltage_min'])
    Data_HC['HC_Vav_history_min'].append(Data_HC['HC_voltage_av_min'])
    Data_HC['HC_perstd_max_history_min'].append(Data_HC['HC_percen_max_custom_min'])
    Data_HC['HC_perstdav_max_history_min'].append(Data_HC['HC_percen_max_custom_av_min'])    
    
#%%
xcurr=[]
Data_HC['Current_Flags']=[]
lines_names=opendss.DSSCircuit.Lines.AllNames
for i in range(len(Data_Current['Iut_normamps_history'])):
    for ii in range(len(Data_Current['Iut_normamps_history'][i])): 
        for iii in range(len(Data_Current['Iut_normamps_history'][i][ii])):
            for iv in range(len(Data_Current['Iut_normamps_history'][i][ii][iii])):
                if (Data_Current['Iut_normamps_history'][i][ii][iii][iv] >= Data_Case['CurrentLimit_%'] and (Data_Current['Iut_normamps_history'][i][ii][iii][iv] <= Data_Case['CurrentLimit_%']+10)):
                    PerUtil=Data_Current['Iut_normamps_history'][i][ii][iii][iv]
#                    xcurr.append([PerUtil,i,ii,iii,iv])
                    xcurr.append([ii,PerUtil,i,iii,iv])

if xcurr == []:
    CurrentFlag=[]
else:
    CurrentFlag=min(xcurr)                  

#%%
     
xvolmax=[]
xvolmin=[]
Data_HC['Voltage_Flags']=[]
for i in range(len(Data_Voltage['Vprof_all'])): #MC CASE
    for ii in range(len(Data_Voltage['Vprof_all'][i])):#PENETRATION CASE
        for iii in range(len(Data_Voltage['Vprof_all'][i][ii])): #TIME STEPS
            for iv in range(len(Data_Voltage['Vprof_all'][i][ii][iii])): #NODES
                if (Data_Voltage['Vprof_all'][i][ii][iii][iv] >= Data_Case['Vlimit_pu'][1] and Data_Voltage['Vprof_all'][i][ii][iii][iv] <= (Data_Case['Vlimit_pu'][1]+0.15)):
                    PerUtil=Data_Voltage['Vprof_all'][i][ii][iii][iv]
#                    xvolmax.append([PerUtil,i,ii,iii,iv])
                    xvolmax.append([ii,PerUtil,i,iii,iv])
                if (Data_Voltage['Vprof_all'][i][ii][iii][iv] <= Data_Case['Vlimit_pu'][0]):# and Data_Voltage['Vprof_all'][i][ii][iii][iv] >= (Data_Case['Vlimit_pu'][0]-0.001)):
                    PerUtil=Data_Voltage['Vprof_all'][i][ii][iii][iv]
#                    xvolmin.append([PerUtil,i,ii,iii,iv])
                    xvolmin.append([ii,PerUtil,i,iii,iv])
#,np.max(Data_Current['Iut_normamps_history'][i][ii])                    
#,np.max(Data_Current['Iut_normamps_history'][i][ii])
if xvolmax == []:
    VoltageFlagmax=[]
else:
    VoltageFlagmax=min(xvolmax) 


if xvolmin == []:
    VoltageFlagmin=[]
else:
    VoltageFlagmin=min(xvolmin) 

#VoltageFlagmax=min(xvolmax)
#VoltageFlagmin=min(xvolmin)



#%% Generate report
HCmin=[]
if max(Data_HC['HC_perstd_max_history']) == []:
    Data_HC['HC_voltage_Impact']=dict([\
                                  ['Circuito', case_name],\
                                  ['Total Customers', len(Data_Customers['PVS_n'])],\
                                  ['Limit', 'No voltage impact with % of customers with voltage issues'],\
                                  ])  

else: 
    while([] in Data_HC['HC_perstd_max_history']) : 
        Data_HC['HC_perstd_max_history'].remove([]) 
    
#    if min(Data_HC['HC_perstd_max_history']) == []:
#        Data_HC['HC_perstd_max_history'].remove([])       
#        HC_V=  min(min(Data_HC['HC_perstd_max_history']))
#    HC_V=  (min(Data_HC['HC_V_history']))  
#    if HC_V == []:
#        HC_V=  min(max(Data_HC['HC_V_history']))
    else:
        HC_V=  min(min(Data_HC['HC_perstd_max_history']))
        Data_HC['HC_voltage_Impact']=dict([\
                                      ['Circuito', case_name],\
                                      ['Total Customers', len(Data_Customers['PVS_n'])],\
                                      ['% GD Penetration (CAP. SE MAX 80%)', HC_V[3]/1000/Data_Case['SE_CAP']*100],\
                                      ['Total GD installed in kW', HC_V[3]],\
                                      ['Customers with PV', len(Data_PV['pv_list_history'][HC_V[9]][HC_V[10]])],\
                                      ['GD average per customer in kW', HC_V[2]],\
                                      ['Maximum Voltage (pu)', HC_V[1]],\
                                      ['Minimum Voltage (pu)', HC_V[14]],\
                                      ['MC Case', HC_V[9]],\
                                      ['% GD Penetration (NUM. CURSTOMERS)', HC_V[4]],\
                                      ['Index Time Issue', HC_V[13]],\
                                      ['Time Issue Hours', str(int(HC_V[13]*Data_Case['Resolution_std-data'][0]/60))+\
                                       ':'+str("{:02d}".format(int(round((abs(HC_V[13]*Data_Case['Resolution_std-data'][0]/60)\
                                               -abs(int(HC_V[13]*Data_Case['Resolution_std-data'][0]/60)))*60,0))))],\
                                      ['Maximum % customer with issues', HC_V[6]],\
                                      ['Index Customer Issue', HC_V[7]],\
                                      ['Node Name Customer Issue', Data_Customers['all_node_names'][HC_V[7]]],\
                                      ['Customer Distance from Substation in km' , HC_V[8]],\
                                      ['Max Feeder Utilization %', HC_V[11]],\
                                      ])  
        HCmin.append([HC_V[4],HC_V[9],HC_V[0]])



if max(Data_HC['HC_perstd_max_history_min']) == []:
    Data_HC['HC_voltage_Impact_min']=dict([\
                                  ['Circuito', case_name],\
                                  ['Total Customers', len(Data_Customers['PVS_n'])],\
                                  ['Limit', 'No voltage impact with % of customers with voltage issues'],\
                                  ])  

else: 
    
    while([] in Data_HC['HC_perstd_max_history_min']) : 
        Data_HC['HC_perstd_max_history_min'].remove([])
#    if min(Data_HC['HC_perstd_max_history_min']) == []:
#        Data_HC['HC_perstd_max_history_min'].remove([])       
#        HC_V=  min(min(Data_HC['HC_perstd_max_history_min']))
#    else:
    HC_V=  min(min(Data_HC['HC_perstd_max_history_min']))
    Data_HC['HC_voltage_Impact_min']=dict([\
                                      ['Circuito', case_name],\
                                      ['Total Customers', len(Data_Customers['PVS_n'])],\
                                      ['% GD Penetration (CAP. SE MAX 80%)', HC_V[3]/1000/Data_Case['SE_CAP']*100],\
                                      ['Total GD installed in kW', HC_V[3]],\
                                      ['Customers with PV', len(Data_PV['pv_list_history'][HC_V[9]][HC_V[10]])],\
                                      ['GD average per customer in kW', HC_V[2]],\
                                      ['Minimum Voltage (pu)', HC_V[1]],\
                                      ['Maximum Voltage (pu)', HC_V[14]],\
                                      ['MC Case', HC_V[9]],\
                                      ['% GD Penetration (NUM. CURSTOMERS)', HC_V[4]],\
                                      ['Index Time Issue', HC_V[13]],\
                                      ['Time Issue Hours', str(int(HC_V[13]*Data_Case['Resolution_std-data'][0]/60))+\
                                       ':'+str("{:02d}".format(int(round((abs(HC_V[13]*Data_Case['Resolution_std-data'][0]/60)\
                                               -abs(int(HC_V[13]*Data_Case['Resolution_std-data'][0]/60)))*60,0))))],\
                                      ['Maximum % customer with issues', HC_V[6]],\
                                      ['Index Customer Issue', HC_V[7]],\
                                      ['Node Name Customer Issue', Data_Customers['all_node_names'][HC_V[7]]],\
                                      ['Customer Distance from Substation in km' , HC_V[8]],\
                                      ['Max Feeder Utilization %', HC_V[11]],\
                                      ])
    HCmin.append([HC_V[4],HC_V[9],HC_V[0]])


if CurrentFlag == []:
    Data_HC['Current_Flags']=dict([\
                                  ['Circuito', case_name],\
                                  ['Total Customers', len(Data_Customers['PVS_n'])],\
                                  ['Limit', 'No current issues over 80% ES capacity'],\
                                  ]) 
else:
    Data_HC['Current_Flags']=dict([\
                              ['Circuito', case_name],\
                              ['Total Customers', len(Data_Customers['PVS_n'])],\
                              ['% GD Penetration (CAP. SE MAX 80%)', \
                               Data_PV['PV_average_history'][CurrentFlag[2]][CurrentFlag[0]-1]\
                               *len(Data_Customers['PVS_n'])/1000/Data_Case['SE_CAP']*100],\
                              ['Total GD installed in kW', Data_PV['PV_average_history'][CurrentFlag[2]]\
                               [CurrentFlag[0]-1]*len(Data_Customers['PVS_n'])],\
                              ['Customers with PV', len(Data_PV['pv_list_history'][CurrentFlag[2]][CurrentFlag[0]-1])],\
                              ['% GD penetration', Data_PV['PerPen_history'][CurrentFlag[2]][CurrentFlag[0]-1]],\
                              ['% Line Utilization '+str(Data_PV['PerPen_history'][CurrentFlag[2]][CurrentFlag[0]-1]), CurrentFlag[1]],\
                              ['Minimum Voltage (pu)', Data_Voltage['Vmin_bus_history'][CurrentFlag[2]][CurrentFlag[0]-1]],\
                              ['Maximum Voltage (pu)', Data_Voltage['Vmax_bus_history'][CurrentFlag[2]][CurrentFlag[0]-1]],\
                              ['MC Case', CurrentFlag[2]],\
                              ['Index Time', CurrentFlag[3]],\
                              ['Time Issue Hours', str(int(CurrentFlag[3]*Data_Case['Resolution_std-data'][1]/60))+\
                               ':'+str("{:02d}".format(int(round((abs(CurrentFlag[3]*Data_Case['Resolution_std-data']\
                                       [1]/60)-abs(int(CurrentFlag[3]*Data_Case['Resolution_std-data'][1]/60)))*60))))],\
                              ['Index Section', CurrentFlag[4]],\
                              ['Feeder Name', lines_names[CurrentFlag[4]]],\
                              ['Feeder [Bus1,Bus2]', [opendss.DSSCircuit.SetActiveElement(str("line.")+\
                               str(lines_names[CurrentFlag[4]])),opendss.DSSCircuit.ActiveCktElement.BusNames]],\
                              ['Total Number of Customer Served', [opendss.DSSCircuit.Lines.TotalCust,\
                                                                   str(int(round(np.multiply(opendss.DSSCircuit.Lines.TotalCust/\
                                                                       len(Data_Customers['PVS_n']),100))))+str("%")]],\
                              ['Number of Customers on this Line Section', opendss.DSSCircuit.Lines.NumCust],\
                              ['Max Feeder Utilization %', np.max(Data_Current['Iut_normamps_history'][CurrentFlag[2]][CurrentFlag[0]-1])],\
                              ])  
    HCmin.append([Data_PV['PerPen_history'][CurrentFlag[2]][CurrentFlag[0]-1],CurrentFlag[2],CurrentFlag[0]-1])



if VoltageFlagmax == []:
    Data_HC['Voltage_Flags_Sup']=dict([\
                                  ['Circuito', case_name],\
                                  ['Total Customers', len(Data_Customers['PVS_n'])],\
                                  ['Limit', 'No voltage issues'],\
                                  ])  
else:
    Data_HC['Voltage_Flags_Sup']=dict([\
                                  ['Circuito', case_name],\
                                  ['Total Customers', len(Data_Customers['PVS_n'])],\
                                  ['% GD Penetration (CAP. SE MAX 80%)', Data_PV['PV_average_history']\
                                   [VoltageFlagmax[2]][VoltageFlagmax[0]]*len(Data_Customers['PVS_n'])\
                                   /1000/Data_Case['SE_CAP']*100],\
                                  ['Total GD installed in kW', Data_PV['PV_average_history'][VoltageFlagmax[2]]\
                                   [VoltageFlagmax[0]]*len(Data_Customers['PVS_n'])],\
                                  ['Customers with PV', len(Data_PV['pv_list_history'][VoltageFlagmax[2]]\
                                                            [VoltageFlagmax[0]])],\
                                  ['% GD penetration', Data_PV['PerPen_history'][VoltageFlagmax[2]][VoltageFlagmax[0]]],\
                                  ['Voltage Issue (pu)', VoltageFlagmax[1]],\
                                  ['Index Node', VoltageFlagmax[4]],\
                                  ['Node Name', Data_Customers['all_node_names'][VoltageFlagmax[4]]],\
                                  ['Node Distance from Substation in km', Data_Customers['all_node_distances']\
                                   [VoltageFlagmax[4]]],\
                                  ['MC Case', VoltageFlagmax[2]],\
                                  ['Index Time', VoltageFlagmax[3]],\
                                  ['Time Issue Hours', str(int(VoltageFlagmax[3]*Data_Case['Resolution_std-data'][1]/60))\
                                   +':'+str("{:02d}".format(int(round((abs(VoltageFlagmax[3]\
                                            *Data_Case['Resolution_std-data'][1]/60)-abs(int(VoltageFlagmax[3]\
                                                      *Data_Case['Resolution_std-data'][1]/60)))*60))))],\
                                  ['Max Feeder Utilization %', np.max(Data_Current['Iut_normamps_history'][VoltageFlagmax[2]][VoltageFlagmax[0]])],\
                                  ])


if VoltageFlagmin == []:
    Data_HC['Voltage_Flags_Min']=dict([\
                                  ['Circuito', case_name],\
                                  ['Total Customers', len(Data_Customers['PVS_n'])],\
                                  ['Limit', 'No voltage issues'],\
                                  ]) 
else:                                      
    Data_HC['Voltage_Flags_Min']=dict([\
                              ['Circuito', case_name],\
                              ['Total Customers', len(Data_Customers['PVS_n'])],\
                              ['% GD Penetration (CAP. SE MAX 80%)', Data_PV['PV_average_history'][VoltageFlagmin[2]][VoltageFlagmin[0]]*len(Data_Customers['PVS_n'])/1000/Data_Case['SE_CAP']*100],\
                              ['Total GD installed in kW', Data_PV['PV_average_history'][VoltageFlagmin[2]]\
                               [VoltageFlagmin[0]]*len(Data_Customers['PVS_n'])],\
                              ['Customers with PV', len(Data_PV['pv_list_history'][VoltageFlagmin[2]]\
                                                        [VoltageFlagmin[0]])],\
                              ['% GD penetration', Data_PV['PerPen_history'][VoltageFlagmin[2]][VoltageFlagmin[0]]],\
                              ['Voltage Issue (pu)', VoltageFlagmin[1]],\
                              ['Index Node', VoltageFlagmin[4]],\
                              ['Node Name', Data_Customers['all_node_names'][VoltageFlagmin[4]]],\
                              ['Node Distance from Substation in km', Data_Customers['all_node_distances'][VoltageFlagmin[4]]],\
                              ['MC Case', VoltageFlagmin[2]],\
                              ['Index Time', VoltageFlagmin[3]],\
                              ['Time Issue Hours', str(int(VoltageFlagmin[3]*Data_Case['Resolution_std-data'][1]/60))\
                               +':'+str("{:02d}".format(int(round((abs(VoltageFlagmin[3]\
                                        *Data_Case['Resolution_std-data'][1]/60)-abs(int(VoltageFlagmin[3]\
                                                  *Data_Case['Resolution_std-data'][1]/60)))*60))))],\
                              ['Max Feeder Utilization %', np.max(Data_Current['Iut_normamps_history'][VoltageFlagmin[2]][VoltageFlagmin[0]])],\
                              ])
