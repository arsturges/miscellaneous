from pprint import pprint
abc_set = [1, 2, 3] 
letter_array = []
for a in abc_set:
    for b in abc_set:
        for c in abc_set:
            for d in abc_set:
                for e in abc_set:
                    potential_set = [a, b, c, d, e]
                    letter_array.append(potential_set)
                    for column in range(len(potential_set)):
                        if potential_set[column] != 1: #find first non-1 column
                            subset = potential_set[column:len(potential_set)]
                            for column in range(len(subset)):
                                if subset[column] != 1: #find first non-1 column:
                                    print potential_set, potential_set[column:5] 
                                    break

#pprint(letter_array)
print len(letter_array)
