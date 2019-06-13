from frege import * 

print "************************************************"
print "Example 1 (Frege's original method)"
profile = [5,3,2]
k = 10
print "input (fixed electorate):    ", profile
print "rounds:                      ", k
print "representatives distribution:", frege(profile , k)
print "details (verbose=True):"
frege(profile , k, verbose=True)
print

print "************************************************"
print "Example 2 (Frege's original method)"
profile = [5,1,1,1,1,1]
k = 10
print "input (fixed electorate):    ", profile
print "rounds:                      ", k
print "representatives distribution:", frege(profile , k)
print "details (verbose=True):"
frege(profile , k, verbose=True)
print

print "************************************************"
print "Example 3 (Frege's modified method)"
profile = [5,1,1,1,1,1]
k = 10
print "input (fixed electorate):    ", profile
print "rounds:                      ", k
print "representatives distribution:", modfrege(profile , k)
print "details (verbose=True):"
modfrege(profile , k, verbose=True)
print

print "************************************************"
print "Remark 2 (Frege's original method)"
print "Frege's original method with variable electorate"
print "  may not converge to quota"
profiles = []
k = 100
for i in range(k):
    profiles.append([2**(i+1),2**i])
print "rounds:                      ", k
print "representatives distribution:", frege(profiles)
#print "details (verbose=True):"
#frege(profiles, verbose=True)
print

print "************************************************"
print "Example 4 (Frege's modified method)"
print "Frege's modified method violates variable lower quota"
print " for m=6"
profile = [1001, 1000, 161, 151, 146, 141]
k = 13
print "input (fixed electorate):    ", profile
print "rounds:                      ", k
print "representatives distribution:", modfrege(profile , k)
print "details (verbose=True):"
modfrege(profile , k, verbose=True, checkquota=True)
print

print "************************************************"
print "Example 4 (Frege's modified method)"
print "Frege's modified method violates variable lower quota"
print " for m=5"
profile = [1001, 1000, 300, 107, 92]
k = 15
print "input (fixed electorate):    ", profile
print "rounds:                      ", k
print "representatives distribution:", modfrege(profile , k)
print "details (verbose=True):"
modfrege(profile , k, verbose=True, checkquota=True)
print

print "************************************************"
print "Example 4 (Frege's modified method)"
print "Frege's modified method violates variable lower quota"
print " for m=4"
profile = [1001, 1000, 115, 26]
k = 30
print "input (fixed electorate):    ", profile
print "rounds:                      ", k
print "representatives distribution:", modfrege(profile , k, tiebreakingallowed=False)
print "details (verbose=True):"
modfrege(profile , k, verbose=True, checkquota=True)
print
