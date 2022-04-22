# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 10:25:04 2019

@author: Nallely Acosta
"""


#%%
for i in range(1,len(Data_Case['LineGeometry'])):
    if Data_Case['LineGeometry'][2][i] == 4:
        Data_Case['Geometries'].append('New LineGeometry.'+str(Data_Case['LineGeometry'][0][i])+' nconds='+str(Data_Case['LineGeometry'][2][i])+\
             ' nphases='+str(Data_Case['LineGeometry'][3][i])+' reduce='+str(Data_Case['LineGeometry'][4][i].lower())+\
             ' cond='+str(Data_Case['LineGeometry'][5][i])+' '+str(Data_Case['LineGeometry'][6][i].lower())+\
             ' x='+str(Data_Case['LineGeometry'][7][i])+' h='+str(Data_Case['LineGeometry'][8][i])+' units='+str(Data_Case['LineGeometry'][9][i].lower())+\
             ' cond='+str(Data_Case['LineGeometry'][10][i])+' '+str(Data_Case['LineGeometry'][11][i].lower())+\
             ' x='+str(Data_Case['LineGeometry'][12][i])+' h='+str(Data_Case['LineGeometry'][13][i])+' units='+str(Data_Case['LineGeometry'][14][i].lower())+\
             ' cond='+str(Data_Case['LineGeometry'][15][i])+' '+str(Data_Case['LineGeometry'][16][i].lower())+\
             ' x='+str(Data_Case['LineGeometry'][17][i])+' h='+str(Data_Case['LineGeometry'][18][i])+' units='+str(Data_Case['LineGeometry'][19][i].lower())+\
             ' cond='+str(Data_Case['LineGeometry'][20][i])+' '+str(Data_Case['LineGeometry'][21][i].lower())+\
             ' x='+str(Data_Case['LineGeometry'][22][i])+' h='+str(Data_Case['LineGeometry'][23][i])+' units='+str(Data_Case['LineGeometry'][24][i].lower()))
    if Data_Case['LineGeometry'][2][i] == 3:
        Data_Case['Geometries'].append('New LineGeometry.'+str(Data_Case['LineGeometry'][0][i])+' nconds='+str(Data_Case['LineGeometry'][2][i])+\
             ' nphases='+str(Data_Case['LineGeometry'][3][i])+' reduce='+str(Data_Case['LineGeometry'][4][i].lower())+\
             ' cond='+str(Data_Case['LineGeometry'][5][i])+' '+str(Data_Case['LineGeometry'][6][i].lower())+\
             ' x='+str(Data_Case['LineGeometry'][7][i])+' h='+str(Data_Case['LineGeometry'][8][i])+' units='+str(Data_Case['LineGeometry'][9][i].lower())+\
             ' cond='+str(Data_Case['LineGeometry'][10][i])+' '+str(Data_Case['LineGeometry'][11][i].lower())+\
             ' x='+str(Data_Case['LineGeometry'][12][i])+' h='+str(Data_Case['LineGeometry'][13][i])+' units='+str(Data_Case['LineGeometry'][14][i].lower())+\
             ' cond='+str(Data_Case['LineGeometry'][15][i])+' '+str(Data_Case['LineGeometry'][16][i].lower())+\
             ' x='+str(Data_Case['LineGeometry'][17][i])+' h='+str(Data_Case['LineGeometry'][18][i])+' units='+str(Data_Case['LineGeometry'][19][i].lower()))
    if Data_Case['LineGeometry'][2][i] == 2:
        Data_Case['Geometries'].append('New LineGeometry.'+str(Data_Case['LineGeometry'][0][i])+' nconds='+str(Data_Case['LineGeometry'][2][i])+\
             ' nphases='+str(Data_Case['LineGeometry'][3][i])+' reduce='+str(Data_Case['LineGeometry'][4][i].lower())+\
             ' cond='+str(Data_Case['LineGeometry'][5][i])+' '+str(Data_Case['LineGeometry'][6][i].lower())+\
             ' x='+str(Data_Case['LineGeometry'][7][i])+' h='+str(Data_Case['LineGeometry'][8][i])+' units='+str(Data_Case['LineGeometry'][9][i].lower())+\
             ' cond='+str(Data_Case['LineGeometry'][10][i])+' '+str(Data_Case['LineGeometry'][11][i].lower())+\
             ' x='+str(Data_Case['LineGeometry'][12][i])+' h='+str(Data_Case['LineGeometry'][13][i])+' units='+str(Data_Case['LineGeometry'][14][i].lower()))
    if Data_Case['LineGeometry'][2][i] == 1:
        Data_Case['Geometries'].append('New LineGeometry.'+str(Data_Case['LineGeometry'][0][i])+' nconds='+str(Data_Case['LineGeometry'][2][i])+\
             ' nphases='+str(Data_Case['LineGeometry'][3][i])+' reduce='+str(Data_Case['LineGeometry'][4][i].lower())+\
             ' cond='+str(Data_Case['LineGeometry'][5][i])+' '+str(Data_Case['LineGeometry'][6][i].lower())+\
             ' x='+str(Data_Case['LineGeometry'][7][i])+' h='+str(Data_Case['LineGeometry'][8][i])+' units='+str(Data_Case['LineGeometry'][9][i].lower()))
    
for i in range(1,len(Data_Case['WiresCatalogue'])):
    Data_Case['WiresData'].append('New WireData.'+str(Data_Case['WiresCatalogue'][0][i].lower())+' DIAM='+str(Data_Case['WiresCatalogue'][4][i])+\
             ' GMRac='+str(Data_Case['WiresCatalogue'][5][i])+' Rdc='+str(Data_Case['WiresCatalogue'][3][i])+\
             ' Runits='+str(Data_Case['WiresCatalogue'][8][i])+' Radunits='+str(Data_Case['WiresCatalogue'][7][i])+\
             ' gmrunits='+str(Data_Case['WiresCatalogue'][6][i])+' Normamps='+str(Data_Case['WiresCatalogue'][2][i])+\
             ' emergamps='+str(Data_Case['WiresCatalogue'][1][i]))
            
for i in range(1,len(Data_Case['CableCatalogue'])):    
    for ii in range(1,len(Data_Case['WiresCatalogue'])):
        if Data_Case['CableCatalogue'][9][i] == Data_Case['WiresCatalogue'][0][ii]:
            for iii in range(1,len(Data_Case['WiresCatalogue'])):
                if Data_Case['CableCatalogue'][10][i] == Data_Case['WiresCatalogue'][0][iii]:             
                    Data_Case['CableData'].append('New CNData.'+str(Data_Case['CableCatalogue'][12][i].lower())+\
                             ' k='+str(Data_Case['CableCatalogue'][6][i])+' DiaStrand='+str(Data_Case['WiresCatalogue'][4][iii])+\
                             ' Rstrand='+str(Data_Case['WiresCatalogue'][3][iii]/Data_Case['CableCatalogue'][6][i])+\
                             ' epsR='+str(Data_Case['CableCatalogue'][11][i])+' InsLayer='+str(Data_Case['CableCatalogue'][8][i])+\
                             ' DiaIns='+str(Data_Case['CableCatalogue'][3][i])+' DiaCable='+str(Data_Case['CableCatalogue'][4][i])+\
                             ' Rac='+str(Data_Case['WiresCatalogue'][3][ii])+' GMRac='+str(Data_Case['WiresCatalogue'][5][ii])+\
                             ' Normamps='+str(Data_Case['WiresCatalogue'][1][ii])+' emergamps='+str(Data_Case['WiresCatalogue'][2][ii])+\
                             ' diam='+str(Data_Case['WiresCatalogue'][4][ii])+' Runits='+str(Data_Case['WiresCatalogue'][8][ii])+\
                             ' Radunits='+str(Data_Case['WiresCatalogue'][7][ii])+' GMRunits='+str(Data_Case['WiresCatalogue'][6][ii]))

for i in range(1,len(Data_Case['Conexiones'])):
    Data_Case['Lines'].append('New Line.'+str(Data_Case['Conexiones'][0][i].lower())+' Bus1='+str(Data_Case['Conexiones'][6][i].lower())+\
             ' Bus2='+str(Data_Case['Conexiones'][7][i].lower())+' Phases='+str(Data_Case['Conexiones'][2][i])+\
             ' Length='+str(Data_Case['Conexiones'][5][i])+' Units=m Geometry='+str(Data_Case['Conexiones'][15][i]))  
#%%
for i in range(1,len(Data_Case['DistributedLoad'])):
    for ii in range(1,len(Data_Case['Conexiones'])):
        if str(Data_Case['DistributedLoad'][0][i]) == str(Data_Case['Conexiones'][0][ii]):
                if Data_Case['DistributedLoad'][6][i] or Data_Case['DistributedLoad'][9][i] != 0:
                    Data_Case['Loads'].append('New Load.Load_A_' + str(Data_Case['DistributedLoad'][0][i].lower()) + ' Phases=1 Bus1=' + str(Data_Case['Conexiones'][6][ii].lower()) +'.1 kv='+ str(Data_Case['DistributedLoad'][2][i]) +\
                             ' kw=' + str(Data_Case['DistributedLoad'][6][i]) + ' kvar=' + str(Data_Case['DistributedLoad'][9][i])+\
                             ' model=' + str(Data_Case['DistributedLoad'][12][i]) + ' conn=' + str(Data_Case['DistributedLoad'][13][i]))
                    Data_Case['Load_Shapes'].append('New Loadshape.LoadShape_Load_A_' + str(Data_Case['DistributedLoad'][0][i].lower()) +' npts='+ str(Data_Case['hours']) + \
                     ' interval=0.0833 mult=' + str(Loadprofiles) + str(i) + '.csv) useactual=false')
                    Data_Case['PV_Shapes'].append('New Loadshape.PVShape_Load_A_' + str(Data_Case['DistributedLoad'][0][i].lower()) +' npts='+ str(Data_Case['hours']) + \
                     ' interval=0.0833 mult=' + str(PVprofiles) + str(i) + '.csv) useactual=false')
                if Data_Case['DistributedLoad'][7][i] or Data_Case['DistributedLoad'][10][i] != 0:
                    Data_Case['Loads'].append('New Load.Load_B_' + str(Data_Case['DistributedLoad'][0][i].lower()) + ' Phases=1 Bus1=' + str(Data_Case['Conexiones'][6][ii].lower()) +'.2 kv='+ str(Data_Case['DistributedLoad'][2][i]) +\
                             ' kw=' + str(Data_Case['DistributedLoad'][7][i]) + ' kvar=' + str(Data_Case['DistributedLoad'][10][i])+\
                             ' model=' + str(Data_Case['DistributedLoad'][12][i]) + ' conn=' + str(Data_Case['DistributedLoad'][13][i]))
                    Data_Case['Load_Shapes'].append('New Loadshape.LoadShape_Load_B_' + str(Data_Case['DistributedLoad'][0][i].lower()) +' npts='+ str(Data_Case['hours']) + \
                     ' interval=0.0833 mult=' + str(Loadprofiles) + str(i) + '.csv) useactual=false')
                    Data_Case['PV_Shapes'].append('New Loadshape.PVShape_Load_B_' + str(Data_Case['DistributedLoad'][0][i].lower()) +' npts='+ str(Data_Case['hours']) + \
                     ' interval=0.0833 mult=' + str(PVprofiles) + str(i) + '.csv) useactual=false')
                if Data_Case['DistributedLoad'][8][i] or Data_Case['DistributedLoad'][11][i] != 0:
                    Data_Case['Loads'].append('New Load.Load_C_' + str(Data_Case['DistributedLoad'][0][i].lower()) + ' Phases=1 Bus1=' + str(Data_Case['Conexiones'][6][ii].lower()) +'.3 kv='+ str(Data_Case['DistributedLoad'][2][i]) +\
                             ' kw=' + str(Data_Case['DistributedLoad'][8][i]) + ' kvar=' + str(Data_Case['DistributedLoad'][11][i])+\
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
                             ' kw=' + str(Data_Case['DistributedLoad'][6][i]) + ' kvar=' + str(Data_Case['DistributedLoad'][9][i])+\
                             ' model=' + str(Data_Case['DistributedLoad'][12][i]) + ' conn=' + str(Data_Case['DistributedLoad'][13][i]) +' Daily=LoadShape_Load_A_'+str(Data_Case['DistributedLoad'][0][i].lower()))
                    
                if Data_Case['DistributedLoad'][7][i] or Data_Case['DistributedLoad'][10][i] != 0:
                    Data_Case['Loads_Daily'].append('New Load.Load_B_' + str(Data_Case['DistributedLoad'][0][i].lower()) + ' Phases=1 Bus1=' + str(Data_Case['Conexiones'][6][ii].lower()) +'.2 kv='+ str(Data_Case['DistributedLoad'][2][i]) +\
                             ' kw=' + str(Data_Case['DistributedLoad'][7][i]) + ' kvar=' + str(Data_Case['DistributedLoad'][10][i])+\
                             ' model=' + str(Data_Case['DistributedLoad'][12][i]) + ' conn=' + str(Data_Case['DistributedLoad'][13][i]) +' Daily=LoadShape_Load_B_'+str(Data_Case['DistributedLoad'][0][i].lower()))
                  
                if Data_Case['DistributedLoad'][8][i] or Data_Case['DistributedLoad'][11][i] != 0:
                    Data_Case['Loads_Daily'].append('New Load.Load_C_' + str(Data_Case['DistributedLoad'][0][i].lower()) + ' Phases=1 Bus1=' + str(Data_Case['Conexiones'][6][ii].lower()) +'.3 kv='+ str(Data_Case['DistributedLoad'][2][i]) +\
                             ' kw=' + str(Data_Case['DistributedLoad'][8][i]) + ' kvar=' + str(Data_Case['DistributedLoad'][11][i])+\
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
            