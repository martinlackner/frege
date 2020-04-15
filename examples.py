from __future__ import print_function
from frege import frege, modfrege
import apportionment


print("************************************************")
print("Example 1 (Frege's original method)")
profile = [5, 3, 2]
k = 10
print("input (fixed electorate):    ", profile)
print("rounds:                      ", k)
print("representatives distribution:", frege(profile, k))
print("details (verbose=True):")
frege(profile, k, verbose=True)
print()

print("************************************************")
print("Example 2 (Frege's original method)")
profile = [1, 1, 1, 1, 1, 5]
k = 10
print("input (fixed electorate):    ", profile)
print("rounds:                      ", k)
print("representatives distribution:", frege(profile, k))
print("details (verbose=True):")
frege(profile, k, verbose=True)
print()

print("************************************************")
print("Example 3 (Frege's original method)")
print("Frege's original method with variable electorate")
print("  may not converge to quota")
profiles = []
k = 100
for i in range(k):
    profiles.append([2**(i + 1), 2**i])
print("rounds:                      ", k)
print("representatives distribution:", frege(profiles))
print()

print("************************************************")
print("Example 4 (Frege's modified method)")
profile = [1, 1, 1, 1, 1, 5]
k = 10
print("input (fixed electorate):    ", profile)
print("rounds:                      ", k)
print("representatives distribution:", modfrege(profile, k))
print("details (verbose=True):")
modfrege(profile, k, verbose=True)
print()

print("************************************************")
print("Example 4 (Frege's modified method)")
print("Frege's modified method violates variable lower quota")
print(" for m=6")
profile = [1001, 1000, 161, 151, 146, 141]
k = 13
print("input (fixed electorate):    ", profile)
print("rounds:                      ", k)
print("representatives distribution:", modfrege(profile, k))
print("details (verbose=True):")
modfrege(profile, k, verbose=True, checkquota=True)
print()

print("************************************************")
print("Example 5 (Frege's modified method)")
print("Frege's modified method violates variable lower quota")
print(" for m=5")
profile = [1001, 1000, 300, 107, 92]
k = 15
print("input (fixed electorate):    ", profile)
print("rounds:                      ", k)
print("representatives distribution:", modfrege(profile, k))
print("details (verbose=True):")
modfrege(profile, k, verbose=True, checkquota=True)
print()

print("************************************************")
print("Example 5 (Frege's modified method)")
print("Frege's modified method violates variable lower quota")
print(" for m=4")
profile = [1001, 1000, 115, 26]
k = 30
print("input (fixed electorate):    ", profile)
print("rounds:                      ", k)
print("representatives distribution:",
      modfrege(profile, k, tiebreakingallowed=False))
print("details (verbose=True):")
modfrege(profile, k, verbose=True, checkquota=True)
print()

print("************************************************")
print("Example 8 (apportionment)")
print("all apportionment methods yield different results")

methods = ["quota", "largest_remainder", "dhondt",
           "saintelague", "huntington", "adams", "modfrege"]
distribution = (79, 7, 6, 3, 2, 1)
seats = 20

print("vote distribution :     ", distribution)
print("seats:                  ", k)

print("\nresults:                      ")
for method in methods:
    if method == "frege":
        rep = frege(
            distribution, seats, modifiedfrege=False, verbose=False)
    elif method == "modfrege":
        rep = frege(
            distribution, seats, modifiedfrege=True, verbose=False)
    else:
        rep = apportionment.compute(
            method, distribution, seats, tiesallowed=False, verbose=False)
    print(method, "." * (25 - len(method)), rep)
