#// GENERAL PARAMETERS //#

POP_SIZE = 50
TIME_LIMIT = 5

TRAIN_START_TIME = 0

#// CAR PARAMETERS //#

STEER_STRENGTH = 0.05 #0.06
ACC_FORCE = 0.2#0.5
SENSOR_NUM = 7
MAX_VEL = 5
initpos = PVector(422, 727)

#// NEURAL NETWORK PARAMETERS //#

NN_TOPOLOGY = (SENSOR_NUM, 5, 5, 2)

#// GENETIC ALGORITHM PARAMETERS //#

MUTATION_CONSTANT = 0.5

MUTATION_RATE = 0.4
SAVED_CARS = 5

#// VISUALISATION PARAMETERS //#

NODE_DIAMETER = 25
VIS_DIM = (len(NN_TOPOLOGY)*4*NODE_DIAMETER, (2*max(NN_TOPOLOGY)+1)*NODE_DIAMETER)
VIS_OFFSET = (1250-VIS_DIM[0]/2,90)
