# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 13:07:12 2018

@author: Andreas T. Procopiou
"""

class opendss(object):                           
    def __init__(self):
        DSSStartOK, DSSObj, DSSText = self.DSSStartup()
        if not DSSStartOK:
            print('Unable to start the OpenDSS Engine')
            import sys
            sys.exit()
            
        self.DSSText = DSSObj.Text                 #Set up the Text
        self.DSSCircuit = DSSObj.ActiveCircuit     #Set up the Circuit
        self.DSSSolution = self.DSSCircuit.Solution     #Set up the Solution
        self.ControlQueue = self.DSSCircuit.CtrlQueue   #Set up the Control
        self.DSSOBJ = DSSObj
        DSSObj.AllowForms = 1 
    
    def DSSStartup(self): # Function for starting up the DSS
        # In Python we need to import all the libraries besides the standard library before we use their functions.
        # "win32com" is one possible library to use a COM object from Python
        import win32com.client
        from comtypes import client as cc
        import sys
        from win32com.client import makepy
        sys.argv = ["makepy", "OpenDSSEngine.DSS"]
        makepy.main()
        # instantiate the DSS Object
        Obj = cc.CreateObject('OpenDSSEngine.DSS')
        # Start the DSS. Only needs to be executed the first time within a Python session
        Start = Obj.Start(0)
        # Define the text interface
        Text = Obj.Text
        # In Python the output(s) of the functions need to be explicitely returned when the function finishes
        return Start, Obj, Text
    
    