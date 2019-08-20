<p align="center">
  <br>
  <a href="https://github.com/SimonBlanke/Hyperactive"><img src="./images/hyperactive_logo_alt.png" height="210"></a>
  <br>
</p>

<br>

<h2 align="center">A hyperparameter optimization toolbox for convenient and fast prototyping</h3>

<div align="center">
  
![Build Status][img-travis-ci-badge] ![img-coveralls-badge] ![img-codacy-badge] ![img-codeclimate-badge] ![img-codefactor-badge]

</div>


<br>

---

<div align="center"><a name="menu"></a>
  <h4>
    <a href="https://github.com/SimonBlanke/Hyperactive#overview">Overview</a> |
    <a href="https://github.com/SimonBlanke/Hyperactive#performance">Performance</a> |
    <a href="https://github.com/SimonBlanke/Hyperactive#installation">Installation</a> |
    <a href="https://github.com/SimonBlanke/Hyperactive#examples">Examples</a> |
    <a href="https://github.com/SimonBlanke/Hyperactive#hyperactive-api">Hyperactive API</a> |
    <a href="https://github.com/SimonBlanke/Hyperactive#license">License</a>
  </h4>
</div>

---

<br>

## Overview

- Optimize hyperparameters of [machine- or deep-learning models](https://github.com/SimonBlanke/Hyperactive/tree/master/hyperactive/model#supported-packages
), using a simple API.
- Choose from a variety of different [optimization techniques](https://github.com/SimonBlanke/Hyperactive/tree/master/hyperactive/optimizers#optimization-techniques) to improve your model.
- Utilize [advanced features](https://github.com/SimonBlanke/Hyperactive/tree/master/hyperactive#advanced-features) to improve the performance of all optimization techniques.


<table>
  <tbody>
    <tr align="center" valign="center">
      <td>
        <strong>Optimization Techniques</strong>
        <img src="images/blue.jpg"/>
      </td>
      <td>
        <strong>Supported Packages</strong>
        <img src="images/blue.jpg"/>
      </td>
      <td>
        <strong>Advanced Features</strong>
        <img src="images/blue.jpg"/>
      </td>
    </tr>
    <tr/>
    <tr valign="top">
      <td>
        <a><b>Local Search:</b></a>
          <ul>
            <li><a href="https://github.com/SimonBlanke/Hyperactive/tree/master/hyperactive/optimizers#hill-climbing">Hill Climbing</a></li>
            <li><a href="https://github.com/SimonBlanke/Hyperactive/tree/master/hyperactive/optimizers#stochastic-hill-climbing">Stochastic Hill Climbing</a></li>
            <li><a href="https://github.com/SimonBlanke/Hyperactive/tree/master/hyperactive/optimizers#tabu-search">Tabu Search</a></li>
         </ul>
        <a><b>Random Methods:</b></a>
          <ul>
            <li><a href="https://github.com/SimonBlanke/Hyperactive/tree/master/hyperactive/optimizers#random-search">Random Search</a></li>
            <li><a href="https://github.com/SimonBlanke/Hyperactive/tree/master/hyperactive/optimizers#random-restart-hill-climbing">Random Restart Hill Climbing</a></li>
            <li><a href="https://github.com/SimonBlanke/Hyperactive/tree/master/hyperactive/optimizers#random-annealing">Random Annealing</a></li>
         </ul>
        <a><b>Markov Chain Monte Carlo:</b></a>
          <ul>
            <li><a href="https://github.com/SimonBlanke/Hyperactive/tree/master/hyperactive/optimizers#simulated-annealing">Simulated Annealing</a></li>
            <li><a href="https://github.com/SimonBlanke/Hyperactive/tree/master/hyperactive/optimizers#stochastic-tunneling">Stochastic Tunneling</li>
            <li><a href="https://github.com/SimonBlanke/Hyperactive/tree/master/hyperactive/optimizers#parallel-tempering">Parallel Tempering</a></li>
          </ul>
        <a><b>Population Methods:</b></a>
          <ul>
            <li><a href="https://github.com/SimonBlanke/Hyperactive/tree/master/hyperactive/optimizers#particle-swarm-optimization">Particle Swarm Optimizer</li>
            <li><a href="https://github.com/SimonBlanke/Hyperactive/tree/master/hyperactive/optimizers#evolution-strategy">Evolution Strategy</a></li>
          </ul>
        <a><b>Sequential Methods:</b></a>
          <ul>
            <li><a href="https://github.com/SimonBlanke/Hyperactive/tree/master/hyperactive/optimizers#bayesian-optimization">Bayesian Optimization</a></li>
          </ul>
      </td>
      <td>
        <a><b>Machine Learning:</b></a>
          <ul>
              <li><a href="https://github.com/SimonBlanke/Hyperactive/tree/master/hyperactive/model#scikit-learn">Scikit-learn</a></li>
              <li><a href="https://github.com/SimonBlanke/Hyperactive/tree/master/hyperactive/model#xgboost">XGBoost</a></li>
              <li><a href="https://github.com/SimonBlanke/Hyperactive/tree/master/hyperactive/model#lightgbm">LightGBM</a></li>
              <li><a href="https://github.com/SimonBlanke/Hyperactive/tree/master/hyperactive/model#catboost">CatBoost</a></li>
          </ul>
        <a><b>Deep Learning:</b></a>
          <ul>
              <li><a href="https://github.com/SimonBlanke/Hyperactive/tree/master/hyperactive/model#keras">Keras</a></li>
          </ul>
        <a><b>Distribution:</b></a>
          <ul>
              <li><a href="https://github.com/SimonBlanke/Hyperactive/tree/master/hyperactive/model#multiprocessing">Multiprocessing</a></li>
          </ul>
      </td>
      <td>
        <a><b>Position initialization:</b></a>
          <ul>
              <li><a href="https://github.com/SimonBlanke/Hyperactive/tree/master/hyperactive#scatter-initialization">Scatter-Initialization</a></li>
              <li><a href="https://github.com/SimonBlanke/Hyperactive/tree/master/hyperactive#warm-start">Warm-start</a></li>
          </ul>
        <a><b>Resource allocation:</b></a>
          <ul>
            <li><a href="https://github.com/SimonBlanke/Hyperactive/tree/master/hyperactive#memory">Memory</a></li>
          </ul>
        <a><b>Weight initialization:</b></a>
          <ul>
            <li><a href="https://github.com/SimonBlanke/Hyperactive/tree/master/hyperactive#transfer-learning">Transfer-learning</a></li>
          </ul>
      </td>
    </tr>
  </tbody>
</table>

<br>


## Installation

Hyperactive is developed and tested in python 3:

[![pyversions](https://img.shields.io/pypi/pyversions/hyperactive.svg?style=for-the-badge&logo=python&logoColor=white)](https://pypi.org/project/hyperactive)
[![commit-activity](https://img.shields.io/github/commit-activity/w/SimonBlanke/Hyperactive?style=for-the-badge)](https://github.com/SimonBlanke/Hyperactive/graphs/contributors)
[![last-commit](https://img.shields.io/github/last-commit/SimonBlanke/Hyperactive?style=for-the-badge)](https://github.com/SimonBlanke/Hyperactive/commits/master)

<br>

Hyperactive is available on PyPi:

[![PyPI version](https://badge.fury.io/py/hyperactive.svg)](https://badge.fury.io/py/hyperactive)
[![Downloads](https://pepy.tech/badge/hyperactive)](https://pepy.tech/project/hyperactive)

```console
pip install hyperactive
```

<br>


## Examples

<details><summary>Scikit-learn:</summary>
<p>

```python
from sklearn.datasets import load_iris
from hyperactive import RandomSearchOptimizer

iris_data = load_iris()
X = iris_data.data
y = iris_data.target

# this defines the model and hyperparameter search space
search_config = {
    'sklearn.neighbors.KNeighborsClassifier': {
        'n_neighbors': range(1, 100),
        'weights': ["uniform", "distance"],
        'p': [1, 2]
    }
}

opt = RandomSearchOptimizer(search_config, n_iter=1000, n_jobs=2, cv=3)

# search best hyperparameter for given data
opt.fit(X, y)
```

</p>
</details>



<details><summary>XGBoost:</summary>
<p>

```python
import numpy as np

from sklearn.datasets import load_breast_cancer
from hyperactive import RandomAnnealingOptimizer

breast_cancer_data = load_breast_cancer()
X = breast_cancer_data.data
y = breast_cancer_data.target

# this defines the model and hyperparameter search space
search_config = {
    "xgboost.XGBClassifier": {
        "n_estimators": range(3, 50, 1),
        "max_depth": range(1, 21),
        "learning_rate": [1e-3, 1e-2, 1e-1, 0.5, 1.0],
        "subsample": np.arange(0.1, 1.01, 0.1),
        "min_child_weight": range(1, 21),
        "nthread": [1],
    }
}

opt = RandomAnnealingOptimizer(search_config, n_iter=100, n_jobs=4, cv=3)

# search best hyperparameter for given data
opt.fit(X, y)
```

</p>
</details>




<details><summary>LightGBM:</summary>
<p>

```python
import numpy as np
from sklearn.datasets import load_breast_cancer
from hyperactive import RandomSearchOptimizer

breast_cancer_data = load_breast_cancer()
X = breast_cancer_data.data
y = breast_cancer_data.target

# this defines the model and hyperparameter search space
search_config = {
    "lightgbm.LGBMClassifier": {
        "boosting_type": ["gbdt"],
        "num_leaves": range(2, 20),
        "learning_rate": np.arange(0.01, 0.1, 0.01),
        "feature_fraction": np.arange(0.1, 0.95, 0.1),
        "bagging_fraction": np.arange(0.1, 0.95, 0.1),
        "bagging_freq": range(2, 10, 1),
    }
}

opt = RandomSearchOptimizer(search_config, n_iter=10, n_jobs=4, cv=3)

# search best hyperparameter for given data
opt.fit(X, y)
```

</p>
</details>



<details><summary>CatBoost:</summary>
<p>

```python
import numpy as np
from sklearn.datasets import load_breast_cancer
from hyperactive import RandomSearchOptimizer

breast_cancer_data = load_breast_cancer()
X = breast_cancer_data.data
y = breast_cancer_data.target

# this defines the model and hyperparameter search space
search_config = {
    "catboost.CatBoostClassifier": {
        "iterations": [3],
        "learning_rate": np.arange(0.01, 0.1, 0.01),
        "depth": range(2, 20),
        "verbose": [0],
        "thread_count": [1],
    }
}

opt = RandomSearchOptimizer(search_config, n_iter=10, n_jobs=4, cv=3)

# search best hyperparameter for given data
opt.fit(X, y)
```

</p>
</details>



<details><summary>Keras:</summary>
<p>

```python
import numpy as np
from keras.datasets import mnist
from keras.utils import to_categorical
from hyperactive import RandomSearchOptimizer

(X_train, y_train), (X_test, y_test) = mnist.load_data()

X_train = X_train.reshape(60000, 28, 28, 1)
X_test = X_test.reshape(10000, 28, 28, 1)

y_train = to_categorical(y_train)
y_test = to_categorical(y_test)


# this defines the structure of the model and the search space in each layer
search_config = {
    "keras.compile.0": {"loss": ["categorical_crossentropy"], "optimizer": ["adam"]},
    "keras.fit.0": {"epochs": [10], "batch_size": [500], "verbose": [2]},
    "keras.layers.Conv2D.1": {
        "filters": [32, 64, 128],
        "kernel_size": range(3, 4),
        "activation": ["relu"],
        "input_shape": [(28, 28, 1)],
    },
    "keras.layers.MaxPooling2D.2": {"pool_size": [(2, 2)]},
    "keras.layers.Conv2D.3": {
        "filters": [16, 32, 64],
        "kernel_size": [3],
        "activation": ["relu"],
    },
    "keras.layers.MaxPooling2D.4": {"pool_size": [(2, 2)]},
    "keras.layers.Flatten.5": {},
    "keras.layers.Dense.6": {"units": range(30, 200, 10), "activation": ["softmax"]},
    "keras.layers.Dropout.7": {"rate": list(np.arange(0.4, 0.8, 0.1))},
    "keras.layers.Dense.8": {"units": [10], "activation": ["softmax"]},
}

Optimizer = RandomSearchOptimizer(search_config, n_iter=10)

# search best hyperparameter for given data
Optimizer.fit(X_train, y_train)
```

</p>
</details>

<br>

## Hyperactive API

### Classes:
```python

HillClimbingOptimizer(search_config, n_iter, metric="accuracy", n_jobs=1, cv=3, verbosity=1, random_state=None, warm_start=False, memory=True, scatter_init=False, eps=1, r=1e-6)
StochasticHillClimbingOptimizer(search_config, n_iter, metric="accuracy", n_jobs=1, cv=3, verbosity=1, random_state=None, warm_start=False, memory=True, scatter_init=False)
TabuOptimizer(search_config, n_iter, metric="accuracy", n_jobs=1, cv=3, verbosity=1, random_state=None, warm_start=False, memory=True, scatter_init=False, eps=1, tabu_memory=[3, 6, 9])

RandomSearchOptimizer(search_config, n_iter, metric="accuracy", n_jobs=1, cv=3, verbosity=1, random_state=None, warm_start=False, memory=True, scatter_init=False)
RandomRestartHillClimbingOptimizer(search_config, n_iter, metric="accuracy", n_jobs=1, cv=3, verbosity=1, random_state=None, warm_start=False, memory=True, scatter_init=False, n_restarts=10)
RandomAnnealingOptimizer(search_config, n_iter, metric="accuracy", n_jobs=1, cv=3, verbosity=1, random_state=None, warm_start=False, memory=True, scatter_init=False, eps=100, t_rate=0.98)

SimulatedAnnealingOptimizer(search_config, n_iter, metric="accuracy", n_jobs=1, cv=3, verbosity=1, random_state=None, warm_start=False, memory=True, scatter_init=False, eps=1, t_rate=0.98)
StochasticTunnelingOptimizer(search_config, n_iter, metric="accuracy", n_jobs=1, cv=3, verbosity=1, random_state=None, warm_start=False, memory=True, scatter_init=False, eps=1, t_rate=0.98, n_neighbours=1, gamma=1)
ParallelTemperingOptimizer(search_config, n_iter, metric="accuracy", n_jobs=1, cv=3, verbosity=1, random_state=None, warm_start=False, memory=True, scatter_init=False, eps=1, t_rate=0.98, n_neighbours=1, system_temps=[0.1, 0.2, 0.01], n_swaps=10)

ParticleSwarmOptimizer(search_config, n_iter, metric="accuracy", n_jobs=1, cv=3, verbosity=1, random_state=None, warm_start=False, memory=True, scatter_init=False, n_part=4, w=0.5, c_k=0.5, c_s=0.9)
EvolutionStrategyOptimizer(search_config, n_iter, metric="accuracy", n_jobs=1, cv=3, verbosity=1, random_state=None, warm_start=False, memory=True, scatter_init=False, individuals=10, mutation_rate=0.7, crossover_rate=0.3)

BayesianOptimizer(search_config, n_iter, metric="accuracy", n_jobs=1, cv=3, verbosity=1, random_state=None, warm_start=False, memory=True, scatter_init=False)

```

<br>

### General positional argument:

| Argument | Type | Description |
| ------ | ------ | ------ |
| search_config  | dict | hyperparameter search space to explore by the optimizer |
| n_iter | int | number of iterations to perform |

<br>

### General keyword arguments:

| Argument | Type | Default | Description |
| ------ | ------ | ------ | ------ |
| metric  | str | "accuracy" | metric for model evaluation |
| n_jobs | int | 1 | number of jobs to run in parallel (-1 for maximum) |
| cv | int | 3 | cross-validation |
| verbosity | int | 1 | Shows model and metric information |
| random_state | int | None | The seed for random number generator |
| warm_start | dict | None | Hyperparameter configuration to start from |
| memory  |  bool | True  |  Stores explored evaluations in a dictionary to save computing time |
| scatter_init  |  int | False  |  Chooses better initial position by training on multiple random positions with smaller training dataset (split into int subsets)  |

<br>

### Specific keyword arguments:

#### [Hill Climbing](https://github.com/SimonBlanke/Hyperactive/blob/master/hyperactive/optimizers/local/hill_climbing_optimizer.py)

| Argument | Type | Default | Description |
| ------ | ------ | ------ | ------ |
| eps  | int | 1 | epsilon |


#### [Stochastic Hill Climbing](https://github.com/SimonBlanke/Hyperactive/blob/master/hyperactive/optimizers/local/stochastic_hill_climbing.py)

| Argument | Type | Default | Description |
| ------ | ------ | ------ | ------ |
| eps  | int | 1 | epsilon |
|  r | float  |  1e-6 | acceptance factor  |


#### [Tabu Search](https://github.com/SimonBlanke/Hyperactive/blob/master/hyperactive/optimizers/local/tabu_search.py)

| Argument | Type | Default | Description |
| ------ | ------ | ------ | ------ |
| eps  | int | 1 | epsilon |
|  tabu_memory | list  |  [3, 6, 9] | length of short/mid/long-term memory  |

#### [Random Restart Hill Climbing](https://github.com/SimonBlanke/Hyperactive/blob/master/hyperactive/optimizers/random/random_restart_hill_climbing.py)

| Argument | Type | Default | Description |
| ------ | ------ | ------ | ------ |
| eps  | int | 1 | epsilon |
| n_restarts  | int  | 10  | number of restarts  |


#### [Random Annealing](https://github.com/SimonBlanke/Hyperactive/blob/master/hyperactive/optimizers/random/random_annealing.py)


| Argument | Type | Default | Description |
| ------ | ------ | ------ | ------ |
| eps  | int | 100 | epsilon |
| t_rate | float | 0.98 | cooling rate  |

#### [Simulated Annealing](https://github.com/SimonBlanke/Hyperactive/blob/master/hyperactive/optimizers/monte_carlo/simulated_annealing.py)

| Argument | Type | Default | Description |
| ------ | ------ | ------ | ------ |
| eps  | int | 1 | epsilon |
| t_rate | float | 0.98 | cooling rate  |

#### [Stochastic Tunneling](https://github.com/SimonBlanke/Hyperactive/blob/master/hyperactive/optimizers/monte_carlo/stochastic_tunneling.py)

| Argument | Type | Default | Description |
| ------ | ------ | ------ | ------ |
| eps  | int | 1 | epsilon |
| t_rate | float | 0.98 | cooling rate  |
| gamma  | float  |  1 | tunneling factor  |


#### [Parallel Tempering](https://github.com/SimonBlanke/Hyperactive/blob/master/hyperactive/optimizers/monte_carlo/parallel_tempering.py)

| Argument | Type | Default | Description |
| ------ | ------ | ------ | ------ |
| eps  | int | 1 | epsilon |
| t_rate | float | 0.98 | cooling rate  |
| system_temps  | list  |  [0.1, 0.2, 0.01] | initial temperatures (number of elements defines number of systems)  |
|  n_swaps | int  | 10  | number of swaps  |


#### [Particle Swarm Optimization](https://github.com/SimonBlanke/Hyperactive/blob/master/hyperactive/optimizers/population/particle_swarm_optimization.py)

| Argument | Type | Default | Description |
| ------ | ------ | ------ | ------ |
| n_part  | int | 1 | number of particles |
| w | float | 0.5 | intertia factor |
| c_k | float | 0.8 | cognitive factor |
| c_s | float | 0.9 | social factor |

#### [Evolution Strategy](https://github.com/SimonBlanke/Hyperactive/blob/master/hyperactive/optimizers/population/evolution_strategy.py)

| Argument | Type | Default | Description |
| ------ | ------ | ------ | ------ |
| individuals  | int | 10 | number of individuals |
| mutation_rate | float | 0.7 | mutation rate |
| crossover_rate | float | 0.3 | crossover rate |

#### [Bayesian Optimization](https://github.com/SimonBlanke/Hyperactive/blob/master/hyperactive/optimizers/sequence_model/bayesian_optimization.py)

| Argument | Type | Default | Description |
| ------ | ------ | ------ | ------ |
| kernel  | class | Matern | Kernel used for the gaussian process |

<br>

### General methods:
```
fit(self, X_train, y_train)
```
| Argument | Type | Description |
| ------ | ------ | ------ |
| X_train  | array-like | training input features |
| y_train | array-like | training target |

```
predict(self, X_test)
```
| Argument | Type | Description |
| ------ | ------ | ------ |
| X_test  | array-like | testing input features |

```
score(self, X_test, y_test)
```
| Argument | Type | Description |
| ------ | ------ | ------ |
| X_test  | array-like | testing input features |
| y_test | array-like | true values |

```
export(self, filename)
```
| Argument | Type | Description |
| ------ | ------ | ------ |
| filename  | str | file name and path for model export |

<br>

### Available Metrics:

|  Scores |  Losses |
| ------ | ------ |
| accuracy_score | brier_score_loss |
| balanced_accuracy_score | log_loss |
| average_precision_score | max_error |
| f1_score | mean_absolute_error |
| recall_score | mean_squared_error |
| jaccard_score | mean_squared_log_error |
| roc_auc_score | median_absolute_error |
| explained_variance_score |  |


<br>

## License

![https://github.com/SimonBlanke/Hyperactive/blob/master/LICENSE](https://img.shields.io/github/license/SimonBlanke/Hyperactive?style=for-the-badge)




[img-travis-ci-badge]:https://img.shields.io/travis/SimonBlanke/Hyperactive.svg?style=for-the-badge&logo=appveyor
[img-coveralls-badge]:https://img.shields.io/coveralls/github/SimonBlanke/Hyperactive?style=for-the-badge&logo=codecov
[img-codacy-badge]:https://img.shields.io/codacy/grade/acb6989093c44fb08cc3be1dd2df1be7?style=for-the-badge&logo=codacy
[img-codeclimate-badge]:https://img.shields.io/codeclimate/maintainability/SimonBlanke/Hyperactive?style=for-the-badge&logo=code-climate
[img-codefactor-badge]:https://img.shields.io/codefactor/grade/github/SimonBlanke/Hyperactive?label=code%20factor&style=for-the-badge
