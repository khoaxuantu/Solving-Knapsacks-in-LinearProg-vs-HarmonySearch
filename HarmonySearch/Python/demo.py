import random
from multiprocessing import cpu_count
from pyharmonysearch import ObjectiveFunctionInterface, harmony_search
import time


class ObjectiveFunction(ObjectiveFunctionInterface):
    # Implement the objective function
    def __init__(self):
        # Set the bound of each item (or decision variable)
        # Upper bound is the limited duplicate item
        # Lower bound is 0 for the item
        # The limited amount of each item is required due to the stochastic property of the Harmony Search
        nitem = 20
        items_num = 10
        self.lower_bound = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.upper_bound = list(nitem for i in range(items_num))

        # Set value and size
        self.value = [90, 36, 54, 108, 45, 18, 50, 80, 210, 150]
        self.size = [
            [10, 4, 6, 12, 5, 2, 7, 9, 18, 15],
            [9, 3, 9, 10, 6, 2, 5, 6, 25, 12]
        ]

        # Maximum weight
        self.max_weight = 1500

        # Maximum volume
        self.max_volume = 2500

        # Declare decision variables
        self.variable = [True, True, True, True, True, True, True, True, True, True]

        # Define all hyper parameters
        self._maximize = True
        self._max_imp = 30000
        self._hms = 1
        self._hmcr = 0.8
        self._par = 0.15
        self._bw = 0.2

    def get_fitness(self, vector):
        '''
            Return the objective function value given a solution vector containing each decision variable.
            :param vector:
        '''
        # Default constraint for the knapsack problem only consists of maximum weight
        # You may need to update more constraints depends on the problems
        # Objective function and total capacity
        # obj: objective value
        # w: total weight
        # v: total volume
        obj = 0
        w = 0
        v = 0
        for i in range(len(self.variable)):
            w += vector[i] * self.size[0][i]
            v += vector[i] * self.size[1][i]
            obj += vector[i] * self.value[i]

        # Do not return value if the objective size is larger than the maximum capacity
        if w <= self.max_weight and v <= self.max_volume:
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

    # Get harmony memory consider rate
    def get_hmcr(self):
        return self._hmcr

    # Get harmony memory size
    def get_hms(self):
        return self._hms

    # Get the bandwidth
    def get_mpap(self):
        return self._bw

    # Get pitch adjusting rate
    def get_par(self):
        return self._par

    def maximize(self):
        return self._maximize


if __name__ == '__main__':
    start_time = time.time()
    obj_fun = ObjectiveFunction()

    # use number of logical CPUs
    num_processes = cpu_count()

    # each process does 5 iterations
    num_iterations = num_processes * 5
    results = harmony_search(obj_fun, num_processes, num_iterations)

    total_weight, total_volume = 0, 0
    # Round the final decision variables
    list_items = results.best_harmony
    for x in range(len(list_items)):
        list_items[x] = round(list_items[x])
        total_weight += list_items[x] * obj_fun.size[0][x]
        total_volume += list_items[x] * obj_fun.size[1][x]

    print('Elapsed time: %s seconds\n'
          'Best harmony (Selected items): %s\n'
          'Best fitness (Maximum value): %s\n' % (results.elapsed_time, list_items, results.best_fitness))
    print(f"Weight: {total_weight}")
    print(f"Volume: {total_volume}")
    print("Time per iteration: %f milliseconds" % ((time.time() - start_time) * 1000 / obj_fun.get_max_imp()))
