#from carlsim import * 
from carlsim import *

import time 

TRAINING_TIME_IN_SEC = 50
TEST_TIME_IN_SEC = 50

DEBUG_ENABLE = 0

N_IN = 49
N_TOT = 80
N_EXC = 0
N_INH = 0
EXC_INH_RATIO = 80

EXCITATORY_PYRAMIDAL_NEURONS = 0

ENABLE_SPK_MONITOR = True
ENABLE_CON_MONITOR = True


sim = CARLsim("CHF", CPU_MODE, USER, 0, 42)

time.sleep(1)

nNeurIn = N_IN
nNeurExc = N_EXC
nNeurInh = N_INH

if N_EXC == 0:
	nNeurExc = EXC_INH_RATIO * N_TOT / 100
	print "Hello N_EXC" , nNeurExc
if N_INH == 0:
	nNeurInh = (100 - EXC_INH_RATIO) * N_TOT / 100

nSynPerNeur = 4                               # number of synpases per neuron


wtExc = 6.0                                 # synaptic weight magnitude if pre is exc
wtInh = 5.0                                 # synaptic weight magnitude if pre is inh (no negative sign)
wtMax = 10.0                                # maximum synaptic weight magnitude
pConn = nSynPerNeur * 1.0 / N_TOT           # connection probability

alphaPlusE = 0.0
tauPlusE = 20.0 
alphaMinusE = 0.1
tauMinusE = 20.0
alphaPlusI = 0.01
tauPlusI = 20.0
alphaMinusI = 0.001
tauMinusI = 20.0

###################################################################################
				###########  Neuron  Grouping #################				
###################################################################################


gIn = []

for nin1 in range(nNeurIn):
	neurGrpName = "gin"+str(nin1)
	gIn.append(sim.createSpikeGeneratorGroup(neurGrpName, 1, EXCITATORY_NEURON))

#print gIn

gExc = sim.createGroup("gexc", nNeurExc, EXCITATORY_NEURON)
sim.setNeuronParameters(gExc, 0.02, 0.2, -65.0, 8.0)

gInh = sim.createGroup("ginh", nNeurInh, INHIBITORY_NEURON)
sim.setNeuronParameters(gInh, 0.1,  0.2, -65.0, 2.0)



for nin2 in range(nNeurIn):
	po = sim.connect(gIn[nin2], gExc, "random", RangeWeight(0.0, wtExc, wtMax), 0.4, RangeDelay(1,20), RadiusRF(-1), SYN_PLASTIC)
	yo = sim.connect(gIn[nin2], gInh, "random", RangeWeight(0.0, wtInh, wtMax), 0.4, RangeDelay(1,20), RadiusRF(-1), SYN_PLASTIC)
#	print "going into the loop", yo
#	print "this is po ", po
#	sim.setConnectionMonitor(gIn[nin2],gExc,"DEFAULT");
sim.connect(gExc, gExc, "random", RangeWeight(0.0, wtExc, wtMax), pConn, RangeDelay(1,20), RadiusRF(-1), SYN_PLASTIC)
sim.connect(gInh, gExc, "random", RangeWeight(0.0, wtInh, wtMax), pConn, RangeDelay(1,20), RadiusRF(-1), SYN_PLASTIC)

spikeTimes = []
with open('spikeFile.txt','r') as file:
	for nin3 in file:
		nin3 = nin3.strip()
		nin3 = float(nin3)
		spikeTimes.append(int(nin3))
	
file.close()
#spikeTimes = map(int, spikeTimes)
SGV = SpikeGeneratorFromVector(spikeTimes)
for i in range(len(gIn)):
	sim.setSpikeGenerator(i, SGV)
	#print i

sim.setESTDP(gExc, True, STANDARD, ExpCurve(alphaPlusE, tauPlusE, -alphaMinusE, tauMinusE))
sim.setISTDP(gExc, True, STANDARD, ExpCurve(-alphaPlusI, tauPlusI, alphaMinusI, tauMinusI))
sim.setESTDP(gInh, True, STANDARD, ExpCurve(alphaPlusE, tauPlusE, -alphaMinusE, tauMinusE))
sim.setISTDP(gInh, True, STANDARD, ExpCurve(-alphaPlusI, tauPlusI, alphaMinusI, tauMinusI))
sim.setHomeostasis(gExc, True, 1.0, 10.0)
sim.setHomeoBaseFiringRate(gExc, 35.0, 0.0)
sim.setHomeostasis(gInh, True, 1.0, 10.0)
sim.setHomeoBaseFiringRate(gInh, 50.0, 0.0)


sim.setConductances(True);

sim.setupNetwork();	

SMin = []
if (ENABLE_SPK_MONITOR == True):
	
	for nin4 in range(nNeurIn):
		SMin.append(sim.setSpikeMonitor(nin4, "DEFAULT"))
	SMexc = sim.setSpikeMonitor(gExc, "DEFAULT")
	SMinh = sim.setSpikeMonitor(gInh, "DEFAULT")

CMine = []
CMini = []
if (ENABLE_CON_MONITOR == True):

	for nin5 in range(nNeurIn):
		CMine.append(sim.setConnectionMonitor(nin5, gExc, "DEFAULT"))
		CMini.append(sim.setConnectionMonitor(nin5, gInh, "DEFAULT"))	
	CMee = sim.setConnectionMonitor(gExc, gExc, "DEFAULT")
	CMie = sim.setConnectionMonitor(gInh, gExc, "DEFAULT")


if (ENABLE_SPK_MONITOR == True):
	for i in range(nNeurIn):
		SMin[i].startRecording()
	SMexc.startRecording()
	SMinh.startRecording()


sim.runNetwork(TRAINING_TIME_IN_SEC,0)

sim.startTesting()

sim.runNetwork(TEST_TIME_IN_SEC,0)


if (ENABLE_SPK_MONITOR == True):
	for i in range(nNeurIn):
		SMin[i].stopRecording()
	SMexc.stopRecording()
	SMinh.stopRecording()

SMexc._print()
SMinh._print()



