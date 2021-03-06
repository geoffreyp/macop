# Minimalist And Customisable Optimisation Package

![](https://img.shields.io/github/workflow/status/jbuisine/macop/build?style=flat-square) ![](https://img.shields.io/pypi/v/macop?style=flat-square) ![](https://img.shields.io/pypi/dm/macop?style=flat-square)

<p align="center">
    <img src="https://github.com/jbuisine/macop/blob/master/logo_macop.png" alt="" width="50%">
</p>


## Description

`macop` is an optimisation Python package which not implement the whole available algorithms in the literature but let you the possibility to quickly develop and test your own algorithm and strategies. The main objective of this package is to be the most flexible as possible and hence, to offer a maximum of implementation possibilities.

## Modules

- **algorithms:** generic and implemented OR algorithms
- **evaluator:** example of an evaluation function to use (you have to implement your own evaluation function)
- **solutions:** solutions used to represent problem data
- **operators:** mutators, crossovers update of solution. This folder also has `policies` folder to manage the way of update and use solution.
- **callbacks:** callbacks folder where `Callback` class is available for making callback instructions every number of evaluations.
  
**Note:** you can pass a custom `validator` function to the algorithm in order to check if a solution is always correct for your needs after an update.

## How to use ?

Fully documentation of package with examples is [available](https://jbuisine.github.io/macop). 

You can also see examples of use:
-  in the [knapsackExample.py](https://github.com/jbuisine/macop/blob/master/examples/knapsackExample.py) python file for mono-objective.
-  in the [knapsackMultiExample.py](https://github.com/jbuisine/macop/blob/master/examples/knapsackMultiExample.py) python file for multi-objective.

## Add as dependency

```bash
git submodule add https://github.com/jbuisine/macop.git
```

## License

[The MIT License](LICENSE)