from pyper import *
import matplotlib.pyplot as plt
tempnew = []
bc = []
r = R(RCMD="C:\\Program Files\\R\\R-3.4.3\\bin\\x64\\R")
r('Sys.setenv(JAVA_HOME="C:\\Program Files\\Java\\jre1.8.0_112")')
r('library(RNetLogo)')
r('nl.path <- "C:/Program Files/NetLogo 6.0.2/app"')
r('nl.jarname <- "netlogo-6.0.2.jar"')
r('NLStart(nl.path, nl.jarname=nl.jarname)')
r('model.path <- "/models/Sample Models/demo/Heat Diffusion.nlogo"')
r('NLLoadModel(paste(nl.path,model.path,sep=""))')
for i in range(1, 10):
 print( '----------------', i*10, '---------------------')
 bc.append(i*10)
 r('NLCommand("set thickness-of-layer ' + str(i*0.10) + '")')
 r('NLCommand("setup")')
 r('NLDoCommand(500, "go")')
 r('temperate <- NLReport("heat-diffusivity")')
 print(r.temperate)
 tempnew.append(r.temperate)
plt.figure(figsize=(8,4))
plt.ylabel("heat diffusion across the material")
plt.xlabel("thickness of the layer")
plt.plot(bc, tempnew)
plt.show()
r('NLQuit()')
