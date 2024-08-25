import math


class NeuralNetwork:
    def __init__(self, genome):
        self.genome = genome
        self.weights = self.genome_to_weights()

    def genome_to_weights(self):
        return [
            int(self.genome[i: i + 8], 16) / (2**32 - 1)
            for i in range(0, len(self.genome), 8)
        ]

    def activate(self, inputs):
        hidden = math.tanh(inputs[0] * self.weights[0] + self.weights[1])
        output1 = math.tanh(hidden * self.weights[2] + self.weights[2])
        output2 = math.tanh(hidden * self.weights[3] + self.weights[3])
        return [output1, output2]
