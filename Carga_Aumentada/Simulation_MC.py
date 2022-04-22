# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 14:01:32 2020

@author: lanal
"""

# Randomize
Data_Customers['Customers_quant'] = []
Data_Voltage['Voltage_Profile_all'] = []
Data_Voltage['VMax_mag_MC'] = []
Data_Voltage['VMax_mag_MC_loc'] = []
Data_Voltage['Vmax_bus'] = []
Data_Voltage['Vmax_bus_location'] = []
Data_Voltage['Vmin_bus'] = []
Data_Voltage['Vmin_bus_location'] = []
Data_Meters_SE['EM_se'] = []
Data_PV['PVquant_save'] = []
Data_PV['baxe_save'] = []
Data_PV['Bb_loc'] = []
Data_PV['pv_list_all'] = []
Data_Current['Iut_maxim_save'] = []
Data_Current['Iut_mag_save'] = []
Data_Current['Iut_normamps_save'] = []
Data_Current['I_customer_save'] = []
Data_Current['I_net_amps_save'] = []
Data_Meters_SE['Tap_change']= []
Data_Current['Line_Losses_wq_mc'] = []
Data_Meters_SE['FPa_GENM_all'] = []
Data_Meters_SE['EMeters'] = []
for iep in range(len(Data_Impact['PerPen'])):
    
    DSSText = DSSObj.Text                                                          #   Set up the Text
    DSSText.Command = 'set DefaultBaseFrequency=60'
    DSSText.Command = 'clear'   
    #DSSText.Command = 'Compile '+mydir+'/'+'Las_Americas-3.dss'    #   In Python strings are concatenated with the operator "+" e.g. 'Hello,' + ' World!' = 'Hello, World!'
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
    #%%
    
    Data_PV['bax'] = []
    Data_PV['baxe'] = []
    Data_PV['PV_list'] =[]
    Data_PV['PV_list2'] =[]
    Data_PV['PVShape_list'] =[]
    seed(1)
    Data_Customers['Customers_quant'].append(math.ceil(len(Data_Customers['PVS_n'])*Data_Impact['PerPen'][iep]/100))
    Data_PV['PVquant'] = (np.around(Data_Case['PerPVSize_data']*round(len(Data_Customers['PVS_n'])*Data_Impact['PerPen'][iep]/100)))
    Data_PV['PVquantnr'] = Data_Case['PerPVSize_data']*math.ceil(len(Data_Customers['PVS_n'])*Data_Impact['PerPen'][iep]/100)
    Data_PV['Bb'] = sample(sequence, math.ceil(len(Data_Customers['PVS_n'])*Data_Impact['PerPen'][iep]/100))#.astype(numpy.int64))
    Data_PV['indmaxnr'] = []
    Data_PV['PVqtt'] = [0]*len(Data_PV['PVquant'])
    if sum(Data_PV['PVquant']) > sum(Data_PV['PVquantnr']) or sum(Data_PV['PVquant']) < sum(Data_PV['PVquantnr']):    
        for ier in range(1,len(Data_PV['PVquantnr'])+1):
            Data_PV['indmaxnr'].append(heapq.nlargest(ier, range(len(Data_PV['PVquantnr'])), Data_PV['PVquantnr'].__getitem__))
            if sum(Data_PV['PVqtt']) < math.ceil(len(Data_Customers['PVS_n'])*Data_Impact['PerPen'][iep]/100):
                for iet in range(len(Data_PV['indmaxnr'][ier-1])):
                    Data_PV['PVqtt'][Data_PV['indmaxnr'][ier-1][iet]]=math.ceil(Data_PV['PVquantnr'][Data_PV['indmaxnr'][ier-1][iet]])                
            if sum(Data_PV['PVqtt']) == math.ceil(len(Data_Customers['PVS_n'])*Data_Impact['PerPen'][iep]/100):
                continue
        Data_PV['PVquant']=Data_PV['PVqtt']           
    if sum(Data_PV['PVquant']) > len(Data_Customers['PVS_n']) or sum(Data_PV['PVquant']) > math.ceil(len(Data_Customers['PVS_n'])*Data_Impact['PerPen'][iep]/100):
        for ier in range(len(Data_PV['PVquant'])):
            if sum(Data_PV['PVquant']) > math.ceil(len(Data_Customers['PVS_n'])*Data_Impact['PerPen'][iep]/100):
                Data_PV['indmaxnr']=np.argmax(Data_PV['PVquant'])
                Data_PV['PVquant'][Data_PV['indmaxnr']] -= 1  
    Data_PV['PVquant'] = numpy.uint64(Data_PV['PVquant'])         
    for ti in range(len(Data_PV['PVquant'])):
         Data_PV['bax'].extend([Data_Case['PVSize_data'][ti]]*Data_PV['PVquant'][ti])  
    Data_PV['PVquant_save'].append(Data_PV['PVquant'])             
    Data_PV['baxe'].append([Data_PV['Bb'],Data_PV['bax']])
    Data_PV['baxe_save'].append(Data_PV['baxe'])
    Data_PV['Bb_loc'].append(Data_PV['Bb']) 
    Data_Customers['Custom_history'].append(Data_Customers['Customers_quant'])
    for ipv in range(len(Data_PV['baxe'][0][1])):
        DSSText.Command = 'New Loadshape.PVShape_' + str(Data_PV['baxe'][0][0][ipv]) +' npts='+ str(Data_Case['hours'])+ ' interval=0.0833 mult='+\
        str(PVprofiles)+ str(Data_PV['baxe'][0][0][ipv]) +'.csv) useactual=false'
        Data_PV['PVShape_list'].append('New Loadshape.PVShape_' + str(Data_PV['baxe'][0][0][ipv]) +' npts='+ str(Data_Case['hours'])+\
               ' interval=0.0833 mult='+str(PVprofiles) + str(Data_PV['baxe'][0][0][ipv]) +'.csv) useactual=false')
        DSSText.Command = 'New Generator.PV' + str(Data_PV['baxe'][0][0][ipv]) + ' ' + str(Data_Customers['PVS_n'][3][Data_PV['baxe'][0][0][ipv]]) +\
        ' ' + str(Data_Customers['PVS_n'][4][Data_PV['baxe'][0][0][ipv]]) + ' ' + str(Data_Customers['PVS_n'][2][Data_PV['baxe'][0][0][ipv]]) +\
        ' kw='+str(Data_PV['baxe'][0][1][ipv]) +' pf=1'+' model=7 status=variable daily=PVShape_' +str(Data_PV['baxe'][0][0][ipv])   
    
        Data_PV['PV_list'].append('Generator.PV' + str(Data_PV['baxe'][0][0][ipv])+ ' ' + str(Data_Customers['PVS_n'][3][Data_PV['baxe'][0][0][ipv]]) +\
               ' ' + str(Data_Customers['PVS_n'][4][Data_PV['baxe'][0][0][ipv]]) + ' ' + str(Data_Customers['PVS_n'][2][Data_PV['baxe'][0][0][ipv]]) +\
               ' kw='+str(Data_PV['baxe'][0][1][ipv]) +' pf=1'+' model=7 status=variable daily=PVShape_' +str(Data_PV['baxe'][0][0][ipv]))
        
    Data_PV['pv_list_all'].append(Data_PV['PV_list'])
    
    #%%
   
    #% Mode and reset
    DSSText.Command = 'set voltagebases=[115,69,34.5,13.8,7.9674]'  #calcular voltajes en pu
    DSSText.Command = 'calcv'
    #control mode
    DSSText.Command = 'Set ControlMode = time'
    DSSText.Command = 'Reset'                                                      #    resetting all energy meters and monitors
    DSSText.Command = 'set mode = daily stepsize=300s number=1'
#        
    import ExtractMonitorData as emd        
    ##solve
    Data_Voltage['Buses_VmagPu'] = []
    Data_Voltage['Vmax_Buses_VmagPu'] = []
    Data_Voltage['Vmax_Buses_VmagPu_loc'] = []
    Data_Current['Iut_maxim'] = []
    Data_Current['Line_Losses_wq'] = []
    Data_Current['Iut_mag'] = []
    Data_Current['Iut_normamps'] = []
    Data_Current['I_customer_amps'] = []
    Data_Current['I_net_amps'] = []
    Data_Meters_SE['EMvalues'] = []
    Data_Meters_SE['Emeter_v'] = []
    Data_Meters_SE['EM'] = []
    Data_Meters_SE['Tap_1'] = []
    Data_Meters_SE['FPa_GENM'] = []
    GenMult=GenMult1
    
    for ie in range(0,Data_Case['hours']):
        
        if GenMult > 1:
            GenMult=1
        DSSText.Command = 'Set Loadmult='+str(LoadMult)
        DSSText.Command = 'Set Genmult='+str(GenMult)
        
        DSSObj.ActiveCircuit.Solution.Solve()  #
        
        Data_Meters_SE['FPa_GENM'].append(GenMult)            
        Data_Current['Iut_max_normamps'] = []
        
        for ilines in range(len(Data_Customers['Lines_n'])):
            opendss.DSSCircuit.SetActiveElement(str(Data_Customers['Lines_n'][1][ilines]))
            opendss.DSSCircuit.ActiveCktElement.CurrentsMagAng
            Ia = DSSCircuit.ActiveCktElement.CurrentsMagAng[0]
            Ib = DSSCircuit.ActiveCktElement.CurrentsMagAng[2]
            Ic = DSSCircuit.ActiveCktElement.CurrentsMagAng[4]
            line_normamps=opendss.DSSCircuit.Lines.EmergAmps
            Data_Current['Iut_max_normamps'].append(np.multiply(max([Ia,Ib,Ic]),100/line_normamps))
        
        exec(open(mydir +'/'+'Control_rating.py').read()) #control de generación


        Data_Current['Iut_normamps'].append(Data_Current['Iut_max_normamps'])
        Data_Voltage['Buses_VmagPu'].append(opendss.DSSCircuit.AllBusVmagPu)
        Data_Voltage['Vmax_Buses_VmagPu'].append(max(max(Data_Voltage['Buses_VmagPu'])))
        Data_Voltage['Vmax_Buses_VmagPu_loc'].append(np.argmax(max(Data_Voltage['Buses_VmagPu'])))
        Data_Meters_SE['Emeter_v'].append(DSSCircuit.Meters.RegisterValues)
        MS=emd.ExtractMonitorData(DSSCircuit, 'SE')
        Y=MS[:,3]+MS[:,5]+MS[:,7]
        X=MS[:,2]+MS[:,4]+MS[:,6]
        Z=np.sqrt(X**2+Y**2)

    Data_Meters_SE['Tap_change'].append([emd.ExtractMonitorData(DSSCircuit, 'TapTR1')[:,2],\
                  (np.diff(emd.ExtractMonitorData(DSSCircuit, 'TapTR1')[:,2])!=0).sum()])
    Data_Meters_SE['EM_se'].append([Z,X,Y]) 
    Data_Meters_SE['FPa_GENM_all'].append(Data_Meters_SE['FPa_GENM'])
    Data_Current['Iut_normamps_save'].append(Data_Current['Iut_normamps'])
    Data_Meters_SE['EMvalues'].append(DSSCircuit.Meters.RegisterValues)
    Data_Voltage['Voltage_Profile_all'].append(Data_Voltage['Buses_VmagPu'])
    Data_Voltage['VMax_mag_MC'].append(Data_Voltage['Vmax_Buses_VmagPu'])  
    Data_Voltage['VMax_mag_MC_loc'].append(Data_Voltage['Vmax_Buses_VmagPu_loc'])
    Data_Voltage['Vmax_bus'].append(np.max(Data_Voltage['Buses_VmagPu']))
    Data_Voltage['Vmax_bus_location'].append(np.argmax(max(Data_Voltage['Buses_VmagPu']))) 
    Data_Voltage['Vmin_bus'].append(np.min(Data_Voltage['Buses_VmagPu']))
    Data_Voltage['Vmin_bus_location'].append(np.argmin(min(Data_Voltage['Buses_VmagPu']))) 
    Data_Meters_SE['EMeters'].append(Data_Meters_SE['EMvalues'])
    Data_Meters_SE['Emeter_v_prin'].append(Data_Meters_SE['Emeter_v'])
Data_Meters_SE['EMeters_history'].append(Data_Meters_SE['EMeters'])
Data_Current['Iut_normamps_history'].append(Data_Current['Iut_normamps_save'])
Data_PV['PVquant_history'].append(Data_PV['PVquant_save'])  
Data_PV['Baxe_history'].append(Data_PV['baxe_save'])
Data_Voltage['Vprof_all'].append(Data_Voltage['Voltage_Profile_all'])
Data_Voltage['VMax_mag__MC_history'].append(Data_Voltage['VMax_mag_MC'])
Data_Voltage['VMax_mag_MC_loc_history'].append(Data_Voltage['VMax_mag_MC_loc'])
Data_Voltage['Vmax_bus_history'].append(Data_Voltage['Vmax_bus'])
Data_Voltage['Vmax_bus_location_history'].append(Data_Voltage['Vmax_bus_location'])
Data_Voltage['Vmin_bus_history'].append(Data_Voltage['Vmin_bus'])
Data_Voltage['Vmin_bus_location_history'].append(Data_Voltage['Vmin_bus_location'])
Data_PV['Bb_loc_history'].append(Data_PV['Bb_loc'])
Data_PV['pv_list_history'].append(Data_PV['pv_list_all'])    
Data_PV['PerPen_history'].append(Data_Impact['PerPen'])
DSSCircuit.Meters.Name = 'TR1'
Data_Meters_SE['Tap_history'].append(Data_Meters_SE['Tap_change'])   
Data_Meters_SE['FPa_GENM_history'].append(Data_Meters_SE['FPa_GENM_all'])
   