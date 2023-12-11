from itertools import permutations
from collections import deque
import kakuro

l = list(permutations(range(1, 10)))

def perm(length, sum_needed):
    if length == 1:
        return [sum_needed]
    possible = set()
    for tup in l:
        temp = list(tup)
        if sum(temp[0:length]) == sum_needed:
            possible.add(tup[0:length])
    possible = list(possible)
    return possible

singlevariable = {}
variables = set()
unassigned_variable = []
neighbours = {}
assignment = {}
domain = {}
constraint = {}

row_constraints = kakuro.row_constraint
col_constraints = kakuro.column_constraint
row_sums = kakuro.row_sum
col_sums = kakuro.column_sum

for row_constraint in row_constraints:
    for var in row_constraint:
        variables.add(var)
for col_constraint in col_constraints:
    for var in col_constraint:
        variables.add(var)

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

i = 0
for row_constraint in row_constraints:
    for var in row_constraint:
        domain[var] = list(range(1, min(row_sums[i] + 1, 10)))
    i += 1

i = 0
for col_constraint in col_constraints:
    for var in col_constraint:
        if var not in domain.keys():
            domain[var] = list(range(1, col_sums[i] + 1))
        else:
            lst = domain[var][-1]
            x = min(9, col_sums[i])
            if lst > x:
                while domain[var][-1] > x:
                    domain[var].pop()
    i += 1

c1 = []
c2 = []
i = 0

for row_constraint in row_constraints:
    if len(row_constraint) == 1:
        singlevariable[row_constraint[0]] = row_sums[i]
    c = perm(len(row_constraint), row_sums[i])
    i += 1
    c1.append(c)

i = 0
for col_constraint in col_constraints:
    if len(col_constraint) == 1:
        singlevariable[col_constraint[0]] = col_sums[i]
    c = perm(len(col_constraint), col_sums[i])
    i += 1
    c2.append(c)

for k in range(len(c1)):
    for possible_assignment in c1[k]:
        for i in range(len(row_constraints[k])):
            for j in range(len(row_constraints[k])):
                if i != j:
                    constraint[(row_constraints[k][i], possible_assignment[i], row_constraints[k][j], possible_assignment[j])] = 1

for k in range(len(c2)):
    for possible_assignment in c2[k]:
        for i in range(len(col_constraints[k])):
            for j in range(len(col_constraints[k])):
                if i != j:
                    constraint[(col_constraints[k][i], possible_assignment[i], col_constraints[k][j], possible_assignment[j])] = 1

unassigned_variable = list(variables)

def remove_inconsistent_values(Xi, Xj, domain):
    ok = False
    to_remove = []
    for value1 in domain[Xi]:
        cnt = 0
        for value2 in domain[Xj]:
            if (Xi, value1, Xj, value2) in constraint.keys():
                cnt += 1
        if cnt == 0:
            ok = True
            to_remove.append(value1)
    for val in to_remove:
        domain[Xi].remove(val)
    return ok

def backtracking_search(assignment, constraint, domain, unassigned_variable, attempt_count=0):
    if len(assignment) == len(variables):
        return assignment, attempt_count  # Return the assignment dictionary
    if len(unassigned_variable):
        var = unassigned_variable[-1]
        for value in domain[var]:
            ok = True
            for var1 in neighbours[var]:
                if var1 in assignment.keys():
                    constraint1 = (var, value, var1, assignment[var1])
                    if constraint1 not in constraint.keys():
                        ok = False
            if ok:
                unassigned_variable.pop()
                assignment[var] = value
                if var in singlevariable.keys():
                    assignment[var] = singlevariable[var]
                result, attempt_count = backtracking_search(assignment, constraint, domain, unassigned_variable, attempt_count + 1)
                if result:
                    return result, attempt_count
                else:
                    assignment.pop(var)
                    unassigned_variable.append(var)
        return False, attempt_count

result, try_count = backtracking_search({}, constraint, domain, list(variables))

def print_solution(solution, row_constraints, col_constraints):
    if solution:
        assignments = {}
        for var, value in solution.items():
            assignments[var] = value

        print("Variable Assignments:")
        for i, row_constraint in enumerate(row_constraints):
            print(f" {i + 1}: {', '.join([f'{var}={assignments[var]}' for var in row_constraint])}")
    else:
        print("No solution found.")

# Print the solution
print_solution(result, row_constraints, col_constraints)
print('Number of Attempts: ', try_count)
