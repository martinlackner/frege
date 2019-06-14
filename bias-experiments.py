import apportionment   # https://github.com/martinlackner/apportionment
import random
import frege

def exp1():
    runs = 1000000
    num_parties = 5
    random.seed(17091743)
    distributions = []
    for _ in range(runs):
        distributions.append([random.randrange(1,1000) for _ in range(num_parties)])

    for method in ["quota", "lrm", "dhondt","saintelague","huntington","adams","frege", "modfrege"]:
        small = 0
        for r in range(runs):
            seats=100
            if method == "frege":
                rep = frege.frege(distributions[r], seats, modifiedfrege=False, verbose=False)
            elif method == "modfrege":
                rep = frege.frege(distributions[r], seats, modifiedfrege=True, verbose=False)
            else:
                rep = apportionment.method(method, distributions[r], seats, verbose=False)
            largest = distributions[r].index(max(distributions[r]))
            smallest = distributions[r].index(min(distributions[r]))
            if 1. * rep[largest] / distributions[r][largest] < 1. * rep[smallest] / distributions[r][smallest]:
                small += 1

        print method, "."*(25 - len(method)), 100.*small / runs, "%"

exp1()
