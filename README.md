# A Python implementation of Frege's voting method

For a detailed description of Frege's voting method as well as the modified Frege method, see the research paper by Harrenstein, Lackner, and Lackner [1].

## How-to
For a fixed electorate:

```python
from frege import frege, modfrege 
profile = [1, 1, 1, 1, 1, 5]
k = 10
frege(profile, k, verbose=True)
modfrege(profile, k, verbose=True)
```

For a variable electorate:

```python
from frege import frege, modfrege
profiles = [[3, 2, 1], [3, 1, 1], [1, 2, 2]]
frege(profiles, verbose=True)
modfrege(profiles, verbose=True)
```

## Further examples

Further examples can be found in [examples.py](examples.py), all of which are described in [1].


## Comments

* Requires Python 2.7 or 3.6+. The module [gmpy2](https://gmpy2.readthedocs.io/) is optional. If gmpy2 is not available, the much slower Python module [fractions](https://docs.python.org/2/library/fractions.html) is used to compute fractions.
* The file [bias.py](bias.py) contains the code for the experiments in "A Mathematical Analysis of an Election System Proposed by Gottlob Frege" [1], Section 5.3.

## References

[1] Paul Harrenstein, Marie-Louise Lackner, and Martin Lackner. *A Mathematical Analysis of an Election System Proposed by Gottlob Frege*. To appear in Erkenntnis. 2020. Preprint: https://arxiv.org/abs/1907.03643
