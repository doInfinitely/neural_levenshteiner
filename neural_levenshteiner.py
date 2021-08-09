import torch
from torch import nn
class NeuralLevenshteiner:
    def __init__(self, max_length, key_size, cross_penalty):
        self.binarizer =
        self.internal_models =
        self.cross_penaly
        self.pdist = nn.PairwiseDistance()
        pass
    def token_distance_function(self, x, y):
        if x != y:
            return 1
        return 0
    def forward(self, x):
        sequence1 = x[0]
        sequence2 = x[1]
        links = dict()
        keys = dict()
        loss = 0
        for j,y in enumerate(sequence1):
            for k,z in enumerate(sequence2):
                key1 = self.internal_models[0,j](y)
                key2 = self.internal_models[1,k](z)
                loss += self.pdist(key1,key2)*token_distance_function(y,z)
                links[frozenset({j,k})] = self.pdist(key1,key2)
                keys[y] = key1
                keys[z] = key2
        for i in range(self.max_length):
            for j in range(self.max_length):
                for k in range(self.max_length):
                    for l in range(self.max_length):
                        if i < k and j < l:
                            if i < j and k < l:
                                sign = 1
                            else:
                                sign = -1
                        if sign == -1:
                            loss += self.cross_penalty*self.pdist(keys[sequence1[i]],keys[sequence2[k]])*token_distance_function(sequence1[i],sequence2[k])
        return loss
