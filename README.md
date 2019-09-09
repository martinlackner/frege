# A Python implementation of Frege's voting method

For a detailed description of Frege's voting method as well as the modified Frege method, see the research paper by Harrenstein, Lackner, and Lackner [1].

## How-to
For a fixed electorate:

```python
from frege import frege, modfrege 
profile = [5,1,1,1,1,1]
k = 10
frege(profile , k, verbose=True)
modfrege(profile , k, verbose=True)
```

For a variable electorate:

```python
from frege import frege, modfrege 
profiles = [[3,2,1],[3,1,1],[1,2,2]]
frege(profiles, verbose=True)
modfrege(profiles, verbose=True)
```

## Further examples

Further examples can be found in frege/examples.py.


<<<<<<< HEAD
## Comments

* This module requires Python 2.7.
* This module requires [gmpy2](https://gmpy2.readthedocs.io/).

=======
## Bias experiments

The file [bias-experiments.py](bias-experiments.py) contains the code for the experiments in "A Mathematical Analysis of an Election System Proposed by Gottlob Frege" [1], Section 5.3. This code requires [apportionment.py](https://github.com/martinlackner/apportionment/blob/master/apportionment.py) from https://github.com/martinlackner/apportionment. 
>>>>>>> 321beafdf369fd3f5845045839f912d27f3aad1a

## References

[1] Paul Harrenstein, Marie-Louise Lackner, and Martin Lackner. *A Mathematical Analysis of an Election System Proposed by Gottlob Frege*. 2019.
