# Implementing Analytic Hierarchy Process using Python

import numpy as np
import pandas as pd

class Hierarchy:
    def __init__(self) -> None:
        """
        Initializes a hierarchy framework instance.
        """
        self.layers = []
        self.connections = []

    # connect new layer
    def connect_layer(self, layer=None):
        if len(self.layers) == 1:
            self.connections.extend([('goal', lab) for lab in layer.labels])
        else:
            prev_layer_labels = self.layers[-2].labels
            self.connections.extend([(prev_lab, lab) for prev_lab in prev_layer_labels for lab in layer.labels])

    # add new hierarchy level
    def add(self, layer=None):
        self.layers.append(layer)
        self.connect_layer(layer)

    # shows current layers and corresponding weights of hierarchy
    def report(self):
        n_layers = len(self.layers)
        print(f'The Hierarchy consists of {n_layers+1} layers: goal, ' + ', '.join(layer.id for layer in self.layers))
        
        for layer in self.layers:
            print(f'\n ------- {layer.id} weights ------- ')
            for idx, lab in enumerate(layer.labels):
                if len(layer.weights.shape) == 1:
                    print(f'{lab}: {layer.weights[idx]}')
                else:
                    print(f'{lab}: {layer.weights[:, idx]}')

    # compute the decision values based on current weights
    def compute_decision(self) -> np.ndarray:
        self.decision_weights = self.layers[0].weights
        for layer in self.layers[1:]:
            self.decision_weights = np.matmul(self.decision_weights, layer.weights)

        # construct ranking
        print()
        print('AHP is solved --------------')
        final_result = np.array([[self.layers[-1].labels[idx], self.decision_weights[idx]] for idx in range(len(self.decision_weights))])
        ranking = np.array([sorted(self.decision_weights, reverse=True).index(x)+1 for x in self.decision_weights])  # descending order (reverse = True)
        ranking = ranking.reshape(len(ranking), 1)
        final_result = np.append(final_result, ranking, axis=1)
        print(pd.DataFrame(final_result, columns=[self.layers[-1].id, 'decision weights', 'rank']))

        return self.decision_weights, ranking.flatten()

class Layer(Hierarchy):
    """
    Creates a hierarchy layer.
    :param: num_input - nodes from previous layer
    :param: num_output - nodes from new layer
    :param: unique_id - identification of layer
    :param: labels - labels of nodes of new layer
    """

    def __init__(self, num_input:int=None, num_output:int=None, unique_id:str=None, labels:list=None):
        self.weights = np.random.rand(num_output) if num_input == 1 else np.random.rand(num_input, num_output)
        self.labels = labels
        self.id = unique_id

    # update weights of layer (input_type options: matrix, values, or rank)
    def update_weights(self, layer_idx:int=None, input_type:str=None, values:list=None, comparison_matrix:np.ndarray=None, ranking:list=None, reverse:bool=False):

        if input_type == 'matrix':
            if layer_idx is None:
                self.weights = get_weights(normalize_matrix(comparison_matrix))
                # self.weights = np.reshape(new_weights, newshape=(1, len(new_weights)))
            else:
                self.weights[layer_idx] = get_weights(normalize_matrix(comparison_matrix))

        if input_type == 'values':
            if reverse:
                values = np.max(values)/np.array(values)
            if layer_idx is None:
                self.weights = values / np.sum(values)
            else:
                self.weights[layer_idx] = values / np.sum(values)

        if input_type == 'rank':
            rank_matrix = rank_difference(ranking)
            if layer_idx is None:
                self.weights = get_weights(normalize_matrix(rank_matrix))
            else:
                self.weights[layer_idx] = get_weights(normalize_matrix(rank_matrix))

# -------- HELPER FUNCTIONS
def normalize_matrix(pairwise_matrix:np.ndarray) -> np.ndarray:
    """ Computes for the corresponding normalized matrix of a given pairwise comparison matrix"""
    column_sum = np.sum(pairwise_matrix, axis=0)
    return pairwise_matrix/column_sum

def get_weights(pairwise_matrix:np.ndarray) -> np.ndarray:
    """ Computes the weights of a pairwise comparison matrix"""
    return np.mean(normalize_matrix(pairwise_matrix), axis=1)

def get_consistency_ratio(pairwise_matrix:np.ndarray):
    n = len(pairwise_matrix)
    matrix_x_weights = np.matmul(pairwise_matrix, get_weights(pairwise_matrix))
    nmax = np.sum(matrix_x_weights)
    consistency_index = (nmax-n)/(n-1)
    random_consistency = (1.98 * (n-2))/n

    consistency_ratio = consistency_index/random_consistency
    inconsistency = 'unacceptable'
    if consistency_ratio < 0.1:
        inconsistency = 'acceptable'
    return consistency_ratio, inconsistency

def rank_difference(rankings:list):
    
    num_ranks = len(rankings)
    num_weights = int(np.max(rankings))

    # create matrix placeholder
    rank_matrix = np.ones(shape=(num_ranks, num_ranks))

    # create rank corresponding weights
    unrounded_rank_weights = np.ones(num_weights)
    if num_weights != 1:
        unrounded_rank_weights[-1] = 9
    for i in range(1, num_weights-1):
        unrounded_rank_weights[i] = unrounded_rank_weights[i-1] + 8/(num_weights-1)
    rank_weights = [round(unrounded_rank_weights[i]) for i in range(num_weights)]

    # update matrix based on ranking
    for i in range(rank_matrix.shape[0]):
        for j in range(rank_matrix.shape[1]):
            diff = rankings[i] - rankings[j]
            if diff <= 0:
                rank_matrix[i,j] = rank_weights[-int(diff)]
            else:
                rank_matrix[i,j] = 1/rank_weights[int(diff)]
    return rank_matrix
