from ortools.linear_solver import pywraplp
import time


def data_model():
    # Store the data
    """Size: [Weight, Volume]"""
    data = {
        # 'size': [
        #     [5, 7, 9, 2, 1],
        #     [18, 4, -9, 10, 12],
        #     [4, 7, 3, 8, 5],
        #     [5, 13, 16, 3, -7],
        # ],
        # 'max_weight': [250, 285, 211, 315],
        # 'value': [7, 8, 2, 9, 6],
        # 'num_vars': 5,
        # 'num_constraints': 4

        'size': [
            [10, 4, 6, 12, 5, 2, 7, 9, 18, 15],
            [9, 3, 9, 10, 6, 2, 5, 6, 25, 12]
        ],
        'max_weight': [1500, 2500],
        'value': [90, 36, 54, 108, 45, 18, 50, 80, 210, 150],
        'num_vars': 10,
        'num_constraints': 2
    }
    return data


def main():
    start_time = time.time()

    '''Instantiate data'''
    data = data_model()
    max_weight_achieve = 0
    max_volume_achieve = 0

    '''Instantiate the solver'''
    # Using Google's open source linear programming solver (GLOP)
    # For the item whose requirement cannot be duplicated,
    # or typical Mixed Integer Linear Programming, try using SCIP solver
    solver = pywraplp.Solver.CreateSolver("GLOP")

    '''Define the variables'''
    # Limit of duplicate item
    # If unlimited: Use solver.infinity()
    r = 20

    x = {}
    for i in range(data['num_vars']):
        # Use IntVar() for Mixed Integer Linear Programming
        x[i] = solver.IntVar(0.0, r, 'x[%i]' % i)

    print("Number of variables = ", solver.NumVariables())
    print(x)

    '''Define the constraints'''
    '''For Multidimensional Knapsacks'''
    for i in range(data['num_constraints']):
        constraint = solver.Constraint(0, data['max_weight'][i], '')
        for j in range(data['num_vars']):
            constraint.SetCoefficient(x[j], data['size'][i][j])
    print("Number of constraints = ", solver.NumConstraints())

    '''For Knapsacks'''
    # for i in range(data['num_constraints']):
    #     constraint_expr = [data['size'][j] * x[j] for j in range(data['num_vars'])]
    #     solver.Add(sum(constraint_expr) <= data['max_weight'])

    '''Define the objective function'''
    obj = solver.Objective()
    for i in range(data['num_vars']):
        obj.SetCoefficient(x[i], data['value'][i])
    obj.SetMaximization()

    '''Call the solver'''
    status = solver.Solve()

    '''Display the solution'''
    print()
    # Check that the problem has an optimal solution
    if status == pywraplp.Solver.OPTIMAL:
        print("Solution:")
        print("Objective value =", solver.Objective().Value())
        for i in range(data['num_vars']):
            if x[i].solution_value() != 0:
                # Compute the final weight achieved
                max_weight_achieve += (data['size'][0][i] * x[i].solution_value())
                max_volume_achieve += (data['size'][1][i] * x[i].solution_value())
            print(x[i].name(), " = ", round(x[i].solution_value()))
        print(f"Maximum weight reached: {max_weight_achieve}")
        print(f"Maximum volume reached: {max_volume_achieve}")
        print()
        print('Problem solved in %f milliseconds' % solver.wall_time())
        print('Problem solved in %d iterations' % solver.iterations())
    else:
        print("The problem does not have an optimal solution")

    time_elapse = ((time.time() - start_time) * 1000)
    print("--- %f milliseconds ---" % time_elapse)
    print()
    if solver.iterations() != 0:
        print("Time per iteration: %f milliseconds" % (time_elapse / solver.iterations()))


if __name__ == "__main__":

    main()
