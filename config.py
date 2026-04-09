import numpy as np

# Pump parameter boundaries for spatial light modulation
PBOUNDS = {
    'a1': (0.0, 5.0),
    'a2': (0.0, 5.0),
    'phi1': (0.0, 2 * np.pi),
    'phi2': (0.0, 2 * np.pi)
}

# Environmental perturbation parameters
ABERRATION_ENV = 0.5

# Bayesian Optimization hyperparameters
BO_INIT_POINTS = 16
BO_N_ITER_IDEAL = 100
BO_N_ITER_COMP = 150