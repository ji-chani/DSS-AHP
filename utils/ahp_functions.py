import numpy as np

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
