# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 19:04:50 2020

@author: lanal
"""

#Data_Voltage=dict([\
#                ['Vprof_all', []],\
#                ['VMax_mag__MC_history', []],\
#                ['VMax_mag_MC_loc_history', []],\
#                ['Vmax_bus_history', []],\
#                ['Vmax_bus_location_history', []],\
#                ['Vmax_bus', []],\
#                ['Vmax_bus_location', []],\
#                ['Vmin_bus_history', []],\
#                ['Vmin_bus_location_history', []],\
#                ['Vmin_bus', []],\
#                ['Vmin_bus_location', []],\
#                ['VMax_mag_MC', []],\
#                ['VMax_mag_MC_loc', []],\
#                ['Voltage_Profile_all', []],\
#                ['Buses_VmagPu', []],\
#                ['Vmax_Buses_VmagPu', []],\
#                ['Vmax_Buses_VmagPu_loc', []],\
#                ])
#
#Data_Current=dict([\
#                ['Iut_maxim_history', []],\
#                ['Iut_mag_history', []],\
#                ['I_PV_amps_history', []],\
#                ['Iut_normamps_history', []],\
#                ['I_net_amps_history', []],\
#                ['I_customer_history', []],\
#                ['Iut_maxim_save', []],\
#                ['Iut_mag_save', []],\
#                ['Iut_normamps_save', []],\
#                ['I_customer_save', []],\
#                ['I_PV_amps_save', []],\
#                ['I_net_amps_save', []],\
#                ['Iut_maxim', []],\
#                ['Iut_mag', []],\
#                ['Iut_normamps', []],\
#                ['I_customer_amps', []],\
#                ['I_PV_amps', []],\
#                ['I_net_amps', []],\
#                ['Iut_max', []],\
#                ['Iut', []],\
#                ['Iut_max_normamps', []],\
#                ['I_customer_node', []],\
#                ['I_customer', []],\
#                ['I_PV', []],\
#                ['I_net_amps_history', []],\
#                ['I_custom_prof', []],\
#                ['I_custom_prof_amps', []],\
#                ['I_custom_prof_save', []],\
#                ['I_custom_prof_history', []],\
#                ['Line_Losses_history', []],\
#                ])
#
#Data_PV=dict([\
#                ['pv_list_history', []],\
#                ['PVquant_history', []],\
#                ['Bb_loc_history', []],\
#                ['PerPen_history', []],\
#                ['Baxe_history', []],\
#                ['baxe_save', []],\
#                ['pv_list_all', []],\
#                ['Bb_loc', []],\
#                ['PVquant_save', []],\
#                ['Bb', []],\
#                ['PVquant', []],\
#                ['PVquantnr', []],\
#                ['indmaxnr', []],\
#                ['PVqtt', []],\
#                ['bax', []],\
#                ['baxe', []],\
#                ['PV_list', []],\
#                ['PVShape_list', []],\
#                ['PV_average_history', []],\
#                ['PV_average', []],\
#                ])
#
#Data_Meters_SE=dict([\
#                ['EM_history', []],\
#                ['EMeters', []],\
#                ['Emeter_v_prin', []],\
#                ['EM_se', []],\
#                ['EMvalues', []],\
#                ['Emeter_v', []],\
#                ['EM', []],\
#                ['Tap_history', []],\
#                ])
#
#Data_Customers=dict([\
#                ['Custom_history', []],\
#                ['PVS_n', []],\
#                ['Customers_quant', []],\
#                ['NodeNames_BusV', []],\
#                ['BusNames_BusV', []],\
#                ['NodeNames_Locations', []],\
#                ['BusNames_Locations', []],\
#                ['all_node_names', []],\
#                ['all_bus_names', []],\
#                ['all_node_distances', []],\
#                ['all_bus_distances', []],\
#                ['Lines_n', []],\
#                ])
#
#x_seed=[]


#Data_Impact=dict([\
#                ['Pmax', 100],\
#                ['itera', 0],\
#                ['Per_actual', 0],\
##                ['PerPen', [50]],\
#                ['PerPen', [100]],\
#                ['MonteCarlo_Iterations',1],\
#                ])


Data_Voltage=dict([\
                ['Vprof_all', []],\
                ['VMax_mag__MC_history', []],\
                ['VMax_mag_MC_loc_history', []],\
                ['Vmax_bus_history', []],\
                ['Vmax_bus_location_history', []],\
                ['Vmax_bus', []],\
                ['Vmax_bus_location', []],\
                ['Vmin_bus_history', []],\
                ['Vmin_bus_location_history', []],\
                ['Vmin_bus', []],\
                ['Vmin_bus_location', []],\
                ['VMax_mag_MC', []],\
                ['VMax_mag_MC_loc', []],\
                ['Voltage_Profile_all', []],\
                ['Buses_VmagPu', []],\
                ['Vmax_Buses_VmagPu', []],\
                ['Vmax_Buses_VmagPu_loc', []],\
                ])

Data_Current=dict([\
                ['Iut_maxim_history', []],\
                ['Iut_mag_history', []],\
                ['I_PV_amps_history', []],\
                ['Iut_normamps_history', []],\
                ['I_net_amps_history', []],\
                ['I_customer_history', []],\
                ['Iut_maxim_save', []],\
                ['Iut_mag_save', []],\
                ['Iut_normamps_save', []],\
                ['I_customer_save', []],\
                ['I_PV_amps_save', []],\
                ['I_net_amps_save', []],\
                ['Iut_maxim', []],\
                ['Iut_mag', []],\
                ['Iut_normamps', []],\
                ['I_customer_amps', []],\
                ['I_PV_amps', []],\
                ['I_net_amps', []],\
                ['Iut_max', []],\
                ['Iut', []],\
                ['Iut_max_normamps', []],\
                ['I_customer_node', []],\
                ['I_customer', []],\
                ['I_PV', []],\
                ['I_net_amps_history', []],\
                ['I_custom_prof', []],\
                ['I_custom_prof_amps', []],\
                ['I_custom_prof_save', []],\
                ['I_custom_prof_history', []],\
#                ['Line_Losses_history', []],\
                ])

Data_PV=dict([\
                ['pv_list_history', []],\
                ['PVquant_history', []],\
                ['Bb_loc_history', []],\
                ['PerPen_history', []],\
                ['Baxe_history', []],\
                ['baxe_save', []],\
                ['pv_list_all', []],\
                ['Bb_loc', []],\
                ['PVquant_save', []],\
                ['Bb', []],\
                ['PVquant', []],\
                ['PVquantnr', []],\
                ['indmaxnr', []],\
                ['PVqtt', []],\
                ['bax', []],\
                ['baxe', []],\
                ['PV_list', []],\
                ['PVShape_list', []],\
                ['PV_average_history', []],\
                ['PV_average', []],\
                ['Hierarchical_history', []],\
                ['Bess_SoC_history', []],\
                ])

Data_Meters_SE=dict([\
                ['EM_history', []],\
                ['EMeters', []],\
                ['Emeter_v_prin', []],\
                ['EM_se', []],\
                ['EMvalues', []],\
                ['Emeter_v', []],\
                ['EM', []],\
                ['Tap_history', []],\
                ['FPa_GENM_history', []],\
                ['EMeters_history', []],\
                ])

Data_Customers=dict([\
                ['Custom_history', []],\
                ['PVS_n', []],\
                ['Customers_quant', []],\
                ['NodeNames_BusV', []],\
                ['BusNames_BusV', []],\
                ['NodeNames_Locations', []],\
                ['BusNames_Locations', []],\
                ['all_node_names', []],\
                ['all_bus_names', []],\
                ['all_node_distances', []],\
                ['all_bus_distances', []],\
                ['Lines_n', []],\
                ])

x_seed=[]
