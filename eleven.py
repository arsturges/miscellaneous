import pprint
solutions=[]
for a in range(12):
    for b in range(12):
        for c in range(12):
            for d in range(12):
                if a+b+c+d==11:
                    solution = [a,b,c,d]
                    solution.sort()
                    if solution not in solutions:
                        solutions.append(solution)
pprint.pprint(solutions)
print len(solutions)
