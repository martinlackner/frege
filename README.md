# A Python implementation of Frege's voting method

For a detailed description of Frege's voting method as well as the modified Frege method, see the paper by Harrenstein, Lackner, and Lackner [1].

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


## Comments

* This module requires Python 2.7.
* This module requires [gmpy2](https://gmpy2.readthedocs.io/).


## References

[1] Paul Harrenstein, Marie-Louise Lackner, and Martin Lackner. *A Mathematical Analysis of an Election System Proposed by Gottlob Frege*. 2019.
