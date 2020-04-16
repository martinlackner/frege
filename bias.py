""" Bias experiments from
Paul Harrenstein, Marie-Louise Lackner, and Martin Lackner.
*A Mathematical Analysis of an Election System Proposed by
Gottlob Frege*. To appear in Erkenntnis. 2020.
 Preprint: https://arxiv.org/abs/1907.03643
"""

from __future__ import print_function
import apportionment
import random
import frege
from statsmodels.stats.proportion import proportion_confint


def bias_exp():
    runs = 1000000
    num_parties = 5
    random.seed(17091743)
    distributions = []
    for _ in range(runs):
        distributions.append([random.randrange(1, 1000)
                              for _ in range(num_parties)])

    print("bias means with 95% confidence intervals")

    for method in ["quota", "lrm", "dhondt", "saintelague",
                   "huntington", "adams", "modfrege"]:
        small = 0
        for r in range(runs):
            seats = 100
            if method == "frege":
                rep = frege.frege(
                    distributions[r], seats,
                    modifiedfrege=False, verbose=False)
            elif method == "modfrege":
                rep = frege.frege(
                    distributions[r], seats, modifiedfrege=True, verbose=False)
            else:
                rep = apportionment.compute(
                    method, distributions[r], seats, verbose=False)
            largest = distributions[r].index(max(distributions[r]))
            smallest = distributions[r].index(min(distributions[r]))
            if ((1. * rep[largest] / distributions[r][largest]
                 < 1. * rep[smallest] / distributions[r][smallest])):
                small += 1

        aver = 100. * small / runs
        conf1, conf2 = proportion_confint(small, runs,
                                          alpha=0.05, method='wilson')

        print(method + " " + "." * (25 - len(method)), end=" ")
        print("{:6.3f}% ({:6.3f}%, {:6.3f}%)".format(
            aver, 100. * conf1, 100. * conf2))


bias_exp()
