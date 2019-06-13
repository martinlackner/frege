import random
import math
import string
from gmpy2 import mpq as mpq
 

# print formated latex table
def print_latex(aggrscore,population,cands,r,representative,modifiedfrege):
    string = str(r+1) + " & "
    for score in aggrscore:
        string += str(score) + " & "
    if modifiedfrege:
        string += cands[representative] 
    else:
        string += cands[representative]  + " & "
        string += str(sum(aggrscore) // len(population))
    string += "\\\\"
    print string


# Frege's voting method
# population .......... either a list of (not necessarily normalized) plurality scores (for a fixed electorate),
#                       or a list of k such lists (variable electorate)
# k ................... (optional) number of rounds [default: len(poulation)]
# cands ............... (optional) names of candidates
# verbose ............. (optional) method outputs scores and chosen representatives
# latextable .......... (optional) method prints latex table with scores and chosen representatives
# modifiedfrege ....... (optional) use Frege's modfied method instead
# checkquota .......... (optional) output if lower or upper quota violated at any point
# tiebreakingallowed .. (optional) if False, return None if tie-breaking is required in any round
def frege(population, k=0, cands=string.ascii_lowercase, verbose=False, latextable=False, modifiedfrege=False, checkquota=False, tiebreakingallowed=True):
    if k == 0:
		k = len(population)
	
    variable = False
    if isinstance(population[0], list):
		variable = True
	
    if variable:
        aggrscore = [0] * len(population[0])
        victories = [0] * len(population[0])
        if checkquota:
            print "checkquota=True not compatible with variable electorate"
            print "(i.e., variable population is a list of lists)"
            #quit()
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
            aggrscore = [a + mpq(b,sum(p)) for a, b in zip(aggrscore, p)]
        else:
            aggrscore = [a + b for a, b in zip(aggrscore, p)]
        maximum = max(aggrscore)
        representative = aggrscore.index(maximum)
        victories[representative] += 1
        if latextable:
            print_latex(aggrscore,p,cands,r,representative,modifiedfrege)
        
        if not tiebreakingallowed:      
            if len([x for x in aggrscore if x == max(aggrscore)])>1:
                return
                
        if verbose:
            if modifiedfrege:
                if r == 0:
                    print "round : chosen representative | aggregated scores"    
                print r+1,":",  cands[representative], '|', ', '.join(map(str, aggrscore))
            else:
                if r == 0:
                    print "round : chosen representative | aggregated scores | cost of winning"    
                print r+1,":", cands[representative], '|', ', '.join(map(str, aggrscore)), '|', int(sum(aggrscore) // len(p))

        if checkquota:
            n = sum(p)
            for i in range(len(p)):
                if victories[i] > math.ceil(float(p[i]) * (r+1) / n) or victories[i]+1 < math.floor(float(p[i]) * (r+1) / n):
                    print "round", r+1,"for profile",p,":" 
                    print "   quota of candidate",cands[i],"is", float(p[i])*(r+1)/n,"but won in", victories[i],"rounds"
        
        if modifiedfrege:
            aggrscore[representative] -= 1
        else:
            aggrscore[representative] -= int(sum(aggrscore) // len(p))
        
    return victories

# modified Frege method
def modfrege(population, k=0, cands=string.ascii_lowercase, verbose=False, latextable=False, checkquota=False, tiebreakingallowed=True):
	return frege(population, k, cands, verbose, latextable, True, checkquota, tiebreakingallowed)