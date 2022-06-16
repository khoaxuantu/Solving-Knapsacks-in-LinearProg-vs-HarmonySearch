import random
from multiprocessing import cpu_count
import sys
from pyharmonysearch import ObjectiveFunctionInterface, harmony_search


class ObjectiveFunction(ObjectiveFunctionInterface):
    # Implement the objective function
    def __init__(self):
        # Set the bound of each item (or decision variable)
        # For unlimited of duplicated items, you may use sys.maxsize for upper_bound
        # inf = sys.maxsize
        # self.upper_bound = [inf, inf, inf, inf, inf,
        #                     inf, inf, inf, inf, inf]
        self.upper_bound = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.lower_bound = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        # Set value and size
        self.value = [55, 10, 47, 60, 15, 50, 68, 61, 75, 90]
        self.size = [95, 4, 60, 44, 23, 72, 80, 62, 55, 42]

        # Max weight
        self.max_weight = 269

        # Declare decision variables
        self.variable = [True, True, True, True, True, True, True, True, True, True]

        # Define all hyper parameters
        self._maximize = True
        self._max_imp = 2500
        self._hms = 100
        self._hmcr = 0.8
        self._par = 0.15
        self._mpap = 0.5

    def get_fitness(self, vector):
        '''
            Return the objective function value given a solution vector containing each decision variable.
            :param vector:
        '''
        # Objective function and total weight
        obj = 0
        w = 0
        for i in range(len(self.variable)):
            w += vector[i] * self.size[i]
            obj += vector[i] * self.value[i]

        # Do not return value if the objective size is larger than max_weight
        if w <= self.max_weight:
            return obj
        else:
            return 0

    def get_value(self, i, j=None):
        # Random a number in range of decision variables
        return random.randint(self.lower_bound[i], self.upper_bound[i])

    def get_lower_bound(self, i):
        return self.lower_bound[i]

    def get_upper_bound(self, i):
        return self.upper_bound[i]

    def is_variable(self, i):
        return self.variable[i]

    def is_discrete(self, i):
        # Turn off solving discrete problems option
        return False

    def get_num_parameters(self):
        return len(self.variable)

    def use_random_seed(self):
        # Turn off random seed option
        return False

    def get_max_imp(self):
        return self._max_imp

    def get_hmcr(self):
        return self._hmcr

    def get_hms(self):
        return self._hms

    def get_mpai(self):
        return self._par

    def get_mpap(self):
        return self._mpap

    def get_par(self):
        return self._par

    def maximize(self):
        return self._maximize


if __name__ == '__main__':
    obj_fun = ObjectiveFunction()

    # use number of logical CPUs
    num_processes = cpu_count()

    # each process does 5 iterations
    num_iterations = num_processes * 5
    results = harmony_search(obj_fun, num_processes, num_iterations)
    print('Elapsed time: %s\n'
          'Best harmony (Selected items): %s\n'
          'Best fitness (Maximum value): %s' % (results.elapsed_time, results.best_harmony, results.best_fitness))
