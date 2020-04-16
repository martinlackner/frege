""" Frege's method and the modified Frege method
as described in
Paul Harrenstein, Marie-Louise Lackner, and Martin Lackner.
*A Mathematical Analysis of an Election System Proposed by
Gottlob Frege*. To appear in Erkenntnis. 2020.
Preprint: https://arxiv.org/abs/1907.03643
"""

from __future__ import print_function
import math
import string
try:
    from gmpy2 import mpq as Fraction
except ImportError:
    # slower
    from fractions import Fraction


def print_latex(aggrscore, population, cands, r,
                representative, modifiedfrege):
    """print formated latex table"""
    string = str(r + 1) + " & "
    for score in aggrscore:
        string += str(score) + " & "
    if modifiedfrege:
        string += cands[representative]
    else:
        string += cands[representative] + " & "
        string += str(sum(aggrscore) // len(population))
    string += "\\\\"
    print(string)


def frege(population, k=0, cands=string.ascii_lowercase, verbose=False,
          latextable=False, modifiedfrege=False, checkquota=False,
          tiebreakingallowed=True):
    """
    Frege's voting method
    population .......... either a list of (not necessarily normalized)
                          plurality scores (for a fixed electorate),
                          or a list of k such lists (variable electorate)
    k ................... (optional) number of rounds [default: len(poulation)]
    cands ............... (optional) names of candidates
    verbose ............. (optional) method outputs scores and
                          chosen representatives
    latextable .......... (optional) method prints latex table with scores
                          and chosen representatives
    modifiedfrege ....... (optional) use Frege's modfied method instead
    checkquota .......... (optional) output if lower or upper quota
                          violated at any point
    tiebreakingallowed .. (optional) if False, return None if tie-breaking
                          is required in any round
    """
    if k == 0:
        k = len(population)

    variable = False
    if isinstance(population[0], list):
        variable = True

    if variable:
        aggrscore = [0] * len(population[0])
        victories = [0] * len(population[0])
        if checkquota:
            raise NotImplementedError("checkquota=True not compatible" +
                                      " with variable electorate" +
                                      "(i.e., variable population is" +
                                      " a list of lists)")
    else:
        aggrscore = [0] * len(population)
        victories = [0] * len(population)

    for r in range(k):
        if variable:
            p = population[r]
        else:
            p = population

        if modifiedfrege:
            # normalize
            aggrscore = [a + Fraction(b, sum(p)) for a, b in zip(aggrscore, p)]
        else:
            aggrscore = [a + b for a, b in zip(aggrscore, p)]
        maximum = max(aggrscore)
        representative = aggrscore.index(maximum)
        victories[representative] += 1
        if latextable:
            print_latex(aggrscore, p, cands, r,
                        representative, modifiedfrege)

        if not tiebreakingallowed:
            if len([x for x in aggrscore if x == max(aggrscore)]) > 1:
                return

        if verbose:
            if modifiedfrege:
                if r == 0:
                    print("round : chosen representative | aggregated scores")
                print(r + 1, ":", cands[representative], '|', end="")
                print(', '.join(map(str, aggrscore)))
            else:
                if r == 0:
                    print("round : chosen representative | aggregated scores",
                          end="")
                    print(" | cost of winning")
                print(r + 1, ":", cands[representative], '|', end="")
                print(', '.join(map(str, aggrscore)), '|', end="")
                print(int(sum(aggrscore) // len(p)))

        if checkquota:
            n = sum(p)
            for i in range(len(p)):
                upperquota = (
                    victories[i] <= math.ceil(float(p[i]) * (r + 1) / n))
                lowerquota = (
                    victories[i] + 1 >= math.floor(float(p[i]) * (r + 1) / n))
                if (not lowerquota or not upperquota):
                    print("round", r + 1, "for profile", p, ":")
                    print("   quota of candidate", cands[i], "is", end="")
                    print(float(p[i]) * (r + 1) / n, "but won in", end="")
                    print(victories[i], "rounds")

        if modifiedfrege:
            aggrscore[representative] -= 1
        else:
            aggrscore[representative] -= int(sum(aggrscore) // len(p))

    return victories


def modfrege(population, k=0, cands=string.ascii_lowercase, verbose=False,
             latextable=False, checkquota=False, tiebreakingallowed=True):
    """modified Frege method"""
    return frege(population, k, cands, verbose,
                 latextable, True, checkquota, tiebreakingallowed)
