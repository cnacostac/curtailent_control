def DSSStartup(): # Function for starting up the DSS
    
    # In Python we need to import all the libraries besides the standard library before we use their functions.
    # "win32com" is one possible library to use a COM object from Python
    import win32com.client
    #from comtypes import client as cc
    
    # instantiate the DSS Object
    Obj = win32com.client.Dispatch('OpenDSSEngine.DSS')
    #Obj = cc.CreateObject('OpenDSSEngine.DSS')
    
    # Start the DSS. Only needs to be executed the first time within a Python session
    Start = Obj.Start(0)
    
    # Define the text interface
    Text = Obj.Text
    
    # In Python the output(s) of the functions need to be explicitely returned when the function finishes
    return Start, Obj, Text