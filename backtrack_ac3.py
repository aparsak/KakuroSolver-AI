from itertools import permutations
from collections import deque
import kakuro

# Generating valid permutations for a given constraint
def valid_permutations(length, sum_needed):
    valid_perms = []
    for perm in permutations(range(1, 10), length):
        if sum(perm) == sum_needed and len(set(perm)) == length:
            valid_perms.append(perm)
    return valid_perms

# Initialize variables and constraints
singlevariable = {}
variables = set()
unassigned_variable = []
neighbours = {}
assignment = {}
domain = {}
constraint = {}

# Row and column constraints and sums
row_constraints = kakuro.row_constraint
col_constraints = kakuro.column_constraint
row_sums = kakuro.row_sum
col_sums = kakuro.column_sum

# Add variables taking part in row and column constraints
for row_constraint in row_constraints:
    for var in row_constraint:
        variables.add(var)
for col_constraint in col_constraints:
    for var in col_constraint:
        variables.add(var)

# Assign neighbors to variables
for row_constraint in row_constraints:
    for var in row_constraint:
        neighbours[var] = []
        for neighbour in row_constraint:
            if var != neighbour:
                neighbours[var].append(neighbour)
for col_constraint in col_constraints:
    for var in col_constraint:
        if var not in neighbours.keys():
            neighbours[var] = []
        for neighbour in col_constraint:
            if var != neighbour:
                neighbours[var].append(neighbour)

# Assign domain to variable with node consistency
i = 0
for row_constraint in row_constraints:
    for var in row_constraint:
        domain[var] = []
        for val in range(1, min(row_sums[i] + 1, 10)):
            domain[var].append(val)
    i += 1
i = 0
for col_constraint in col_constraints:
    for var in col_constraint:
        if var not in domain.keys():
            domain[var] = []
            for val in range(1, col_sums[i] + 1):
                domain[var].append(val)
        else:
            lst = domain[var][-1]
            x = min(9, col_sums[i])
            if lst > x:
                while domain[var][-1] > x:
                    domain[var].pop()
    i += 1

# Generate valid permutations for row and column constraints
c1 = []
c2 = []
i = 0
for row_constraint in row_constraints:
    if len(row_constraint) == 1:
        singlevariable[row_constraint[0]] = row_sums[i]
    c = valid_permutations(len(row_constraint), row_sums[i])
    i += 1
    c1.append(c)

i = 0
for col_constraint in col_constraints:
    if len(col_constraint) == 1:
        singlevariable[col_constraint[0]] = col_sums[i]
    c = valid_permutations(len(col_constraint), col_sums[i])
    i += 1
    c2.append(c)

# Generate constraints based on valid permutations
for k in range(len(c1)):
    for possible_assignment in c1[k]:
        for i in range(len(row_constraints[k])):
            for j in range(len(row_constraints[k])):
                if i != j:
                    constraint[(
                        row_constraints[k][i], possible_assignment[i], row_constraints[k][j], possible_assignment[j])] = 1

for k in range(len(c2)):
    for possible_assignment in c2[k]:
        for i in range(len(col_constraints[k])):
            for j in range(len(col_constraints[k])):
                if i != j:
                    constraint[(
                        col_constraints[k][i], possible_assignment[i], col_constraints[k][j], possible_assignment[j])] = 1

# Store unassigned variables
unassigned_variable = list(variables)

# AC-3 algorithm for arc consistency
def remove_inconsistent_values(Xi, Xj, domain):
    ok = False
    toremove = []
    for value1 in domain[Xi]:
        cnt = 0
        for value2 in domain[Xj]:
            if (Xi, value1, Xj, value2) in constraint.keys():
                cnt += 1
        if cnt == 0:
            ok = True
            toremove.append(value1)
    for val in toremove:
        domain[Xi].remove(val)
    return ok

def ac3(variables, domain):
    q = deque()
    for var in variables:
        if var not in singlevariable.keys():
            for neighbour in neighbours[var]:
                q.append([var, neighbour])
    while len(q):
        [Xi, Xj] = q.popleft()
        if remove_inconsistent_values(Xi, Xj, domain):
            for neighbour in neighbours[Xi]:
                q.append([neighbour, Xi])
    return domain


print('Reduce domain with ac-3: ' , ac3(variables, domain))
# Reduce domain with ac-3


# Initialize try_count
try_count = 0

# Generic backtracking search algorithm after performing node and arc consistency
# Generic backtracking search algorithm after performing node and arc consistency
def backtracking_search(assignment, constraint, domain, unassigned_variable):
    global try_count
    try_count += 1
    if len(assignment) == len(variables):
        return assignment
    if len(unassigned_variable):
        var = unassigned_variable[-1]
        if var in singlevariable.keys() and var not in assignment:
            assignment[var] = singlevariable[var]
            unassigned_variable.pop()
            print(f"Assigned {var} = {assignment[var]} (Single-variable assignment)")
            result = backtracking_search(assignment, constraint, domain, unassigned_variable)
            if result:
                return result
            else:
                assignment.pop(var)
                unassigned_variable.append(var)
        else:
            for value in domain[var]:
                ok = True
                for var1 in neighbours[var]:
                    if var1 in assignment.keys():
                        constraint_key = (var, value, var1, assignment[var1])
                        if constraint_key in constraint:
                            ok = ok and constraint[constraint_key] == 1
                        else:
                            ok = False

                if ok:
                    unassigned_variable.pop()
                    assignment[var] = value
                    print(f"Assigned {var} = {assignment[var]}")
                    result = backtracking_search(assignment, constraint, domain, unassigned_variable)
                    if result:
                        return result
                    else:
                        assignment.pop(var)
                        unassigned_variable.append(var)
            return False

# Run backtracking search
answer = backtracking_search({}, constraint, domain, list(variables))

def print_solution(solution, row_constraints, col_constraints):
    assignments = {}
    for var, value in solution.items():
        assignments[var] = value

    print("Variable Assignments:")
    for i, row_constraint in enumerate(row_constraints):
        print(f" {i + 1}: {', '.join([f'{var}={assignments[var]}' for var in row_constraint])}")

# Print the solution
if answer:
    print_solution(answer, row_constraints, col_constraints)
    print('Number of Attempts: ', try_count)
else:
    print("No solution found.")

