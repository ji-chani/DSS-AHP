import numpy as np

# perceived difficulty
difficulty = {
    'BS AMAT':[2.8, 2.9, 4.2, 3.6, 4.2, 3.6, 3.4, 4.8, 4.6, 4.4, 4.6, 
               4.3, 4.7, 4.3, 4.2, 4.3, 4.5, 4.4, 4.2, 4.6, 4.7],
    'BS MATH': [4.2, 3.6, 2.9, 4.4, 4.3, 3.4,
                4.6, 3.8, 3.6, 4.0, 4.2, 2.7]
}

# peer pressure
pressure = {
    'BS AMAT': [0.3, 0.1, 0.1, 0.4, 0.2, 0.3, 0.3, 0.3, 0.3, 0.2, 0.2,
                0.1, 0.2, 0.0, 0.3, 0.1, 0.0, 0.0, 0.0, 0.0, 0.3],
    'BS MATH': [0.1, 0.2, 0.3, 0.1, 0.1, 0.4, 
                0.1, 0.1, 0.4, 0.2, 0.2, 0.2]
}

# availability
np.random.seed(21)
options = [15, 20, 25, 30, 35]
availability = {
    'BS AMAT': np.random.choice(options, size=21),
    'BS MATH': np.random.choice(options, size=12)
}



