from cplex import Cplex
def solve_linear_problem(senses =[] , obj = [] , constraintCoefficient = [[]] , values = [] , minimze = False):
    # Create a CPLEX model
    var = len(obj)
    names = []
    for i in range(var):
        names.append(f'x{i+1}')
    # Run the solver
    model = Cplex()
    # Set the problem type to Maximization
    if minimze:
        model.objective.set_sense(model.objective.sense.minimize)
    else:  
        model.objective.set_sense(model.objective.sense.maximize)

    # Add decision variables with their coefficients in the objective function
    # The variable type is "C" for continuous
    model.variables.add(
        obj=obj,  # Coefficients in the objective function
        lb=[0] * var,   # Lower bounds of variables (x, y >= 0)
        names=names  # Use global names array
    )

    # Add constraints => [names, [1 , 0.9 , 0,0,0, 0.05 , 0 , 0.02]] = [[x1,x2 , ..... , xn], [1 , 0.9 , 0,0,0, 0.05 , 0 , 0.02]]
    constraints = []
    for i in range(len(constraintCoefficient)):
        constraints.append([names, constraintCoefficient[i]])
 
    rhs = values # Right-hand sides of constraints like expression <= values[0] = 2
    senses = senses  # "L" indicates <= constraint

    model.linear_constraints.add(lin_expr=constraints, senses=senses, rhs=rhs)

    # Solve the problem
    model.solve()

    # Get the results
    solution = model.solution.get_values()
    for i in range(len(solution)):
        print(f' X{i+1} = {solution[i]}')
    return (solution , model.solution.get_objective_value() )

# Global variable names for decision variables
def getResult():
    senses = ["L", "L" , 'L' , 'L']
    obj = [9 , 7 , 6.5 , 5 , 4 , 3.5 , 2 , 0.5]
    constraints = [
       [1 , 0.9 , 0,0,0, 0.05 , 0 , 0.02],  # First constraint
        [0 , 0.1,1 , 0.5 , 0 , 0.1 , 0 , 0] ,   # Second constraint
        [0 , 0 , 0 , 0.4 , 1 , 0.6 , 0.8 , 0.6] ,   # Second constraint
        [0 , 0 , 0 , 0.1 , 0 , 0.25 , 0.2 , 0.38]   # Second constraint
    ]
    values = [2 , 4 , 5 , 7]
    s = solve_linear_problem(senses , obj , constraints , values)
