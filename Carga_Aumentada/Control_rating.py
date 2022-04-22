# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 11:20:19 2020

@author: lanal
"""

if np.max(opendss.DSSCircuit.AllBusVmagPu) >= (Data_Case['Vlimit_pu'][1]-vpu_tol) or \
    np.min(opendss.DSSCircuit.AllBusVmagPu) <= (Data_Case['Vlimit_pu'][0]+vpu_tol) or \
    np.max(Data_Current['Iut_max_normamps']) >= Data_Case['OverCurrentLimit']*100:
        if GenMult <= 1 and GenMult >= gencur_adj:
            GenMult2=GenMult-gencur_adj
            GenMult=GenMult2
        if GenMult <= gen_min:
            GenMult2 = gen_min+gencur_adjup
            GenMult=GenMult2
                
if (np.min(opendss.DSSCircuit.AllBusVmagPu) > (Data_Case['Vlimit_pu'][0]+vpu_tol) and \
    np.max(opendss.DSSCircuit.AllBusVmagPu) < (Data_Case['Vlimit_pu'][1]-vpu_tol)) and \
    np.max(Data_Current['Iut_max_normamps']) >= Data_Case['OverCurrentLimit']*100:
        if GenMult <= 1 and GenMult >= gencur_adj:
            GenMult2=GenMult-gencur_adj
            GenMult=GenMult2
        if GenMult <= gen_min:
            GenMult2 = gen_min+gencur_adjup
            GenMult=GenMult2
        
if (np.min(opendss.DSSCircuit.AllBusVmagPu) > (Data_Case['Vlimit_pu'][0]+vpu_tol) and \
    np.max(opendss.DSSCircuit.AllBusVmagPu) < (Data_Case['Vlimit_pu'][1]-vpu_tol)) and \
    np.max(Data_Current['Iut_max_normamps']) < Data_Case['OverCurrentLimit']*100:
        if GenMult < 1-gencur_adjup:
            GenMult2=GenMult+gencur_adjup
            GenMult=GenMult2
        if GenMult >= 1:
            GenMult2=1 
            GenMult=GenMult2        
            
if GenMult > 1:
    GenMult=1