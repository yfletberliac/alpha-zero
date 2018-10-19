#### SELF PLAY
EPISODES = 50
MCTS_SIMS = 100
MEMORY_SIZE = 9000
TURNS_UNTIL_TAU0 = 10 # turn on which it starts playing deterministically
CPUCT = 1
EPSILON = 0.2
ALPHA = 0.8


#### RETRAINING
BATCH_SIZE = 256
EPOCHS = 2
REG_CONST = 0.0001
LEARNING_RATE = 0.1
MOMENTUM = 0.9
TRAINING_LOOPS = 10

HIDDEN_CNN_LAYERS = [
	{'filters':128, 'kernel_size': (4,4)}
	 , {'filters':128, 'kernel_size': (4,4)}
	]

#### EVALUATION
EVAL_EPISODES = 5
SCORING_THRESHOLD = 1.3