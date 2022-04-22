def ExtractMonitorData(DSSCircuit, name_monitor):
    
    import numpy as np
    
    DSSMon = DSSCircuit.Monitors
    DSSMon.Name = name_monitor
    n = DSSMon.SampleCount
    d = DSSMon.ByteStream
    idata = np.array(d[0:16], dtype=np.uint8).view(np.int32)
    nrec = idata[2]
    sdata = np.array(d[272:], dtype=np.uint8).view(np.single)
    y = np.reshape(sdata, (n, nrec+2))
    
    return y