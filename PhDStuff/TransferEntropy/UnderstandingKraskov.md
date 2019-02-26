# Understanding Kraskov w.r.t to [TE_compute.cpp](https://github.com/ikegwukc/TransEnt/blob/master/src/compute_TE.cpp)


- **Note:**  I see that the main algorithm in [TE_compute.cpp](https://github.com/ikegwukc/TransEnt/blob/master/src/compute_TE.cpp) comes from this paper. However, This paper does not discuss the embedding (or look back values) that Jeff talks about and that's in [TE_compute.cpp](https://github.com/ikegwukc/TransEnt/blob/master/src/compute_TE.cpp) so some things are implemented differently in TE_compute.cpp. I need to review the paper(s) that talk about that.

### The basic idea
This paper estimates Mutual Information (MI) from k-nearest neighbor statistics.

Let `X` represent the security prices and `Y` represent the option prices. The basic idea is to estimate Shannon's entropy H() from the average distance to the k-nearest neighbor averaged over all points  for `X` and `Y`.

Mutual information could be obtained by estimating Shannon Entropy for `X` H(X), the Shannon Entropy for `Y` H(Y), and H􏰒(X,Y) and then performing the following calculation:  H(X) + H(Y) - H(X,Y).

- **Note:** There's a paper that talk about how to compute H(X,Y) but I have not reviewed it yet.


### The algorithm used in [Compute_TE.cpp](https://github.com/ikegwukc/TransEnt/blob/master/src/compute_TE.cpp)
The algorithm used in [Compute_TE.cpp](https://github.com/ikegwukc/TransEnt/blob/master/src/compute_TE.cpp) is the first algorithm described in the Kraskov paper (with some modifications) which states:

>In the first algorithm, we count the number $n_x(􏰒i)$􏰇 of points $x_j$ whose distance from $x_i$ is strictly less than 􏰠$\epsilon(􏰒i)􏰇/2$, and similarly for y instead of x.
>
> The estimate for MI is then: I$􏰒^{(1)}􏰇(X,Y)􏰇 = \digamma(􏰞􏰒k)􏰇 − \digamma(􏰎􏰞􏰒n_x) + 1)􏰇 + \digamma(􏰞􏰒n_y +1) + \digamma(N)$

- $\epsilon(􏰒i)􏰇/2$ is the distance to the nearest neighbor. $x_j$ contains the observation for the nearest neighbor $x_i$ contains the observation for the current point.
-

How I interpreted the pseudocode looking like is:
``` python
from scipy.special import digamma  # to compute log derivative of gamma function

X = ...  # numpy array with security prices
Y = ...  # numpy array with option prices
N = ...  # Number of Points in X and Y which should be the same.
k = ...  # number of neighbors

n_x = 0
n_y = 0
kdTreeX = sklearn.neighbors.KDTree(X)  # KD Tree for X space
kdTreeY = sklearn.neighbors.KDTree(Y)  # KD Tree for Y space


for i in range(N):
  # # nearest neighbors to X[i], Get dist and index of NN
  # Assume that X[i] is diregarded from query
  dist, idx  = kdTreeX.query(X, k=k)  

  # Obtain distance from nearest neighbor
  dist_x = X[i] - X[idx]

  # Get Counts of all neighbors within that distance.
  counts = kdTreeX.query_radius(X[i], dist_x)  # Assume I get back a integer
  n_x += counts

  # Repeat above for Y

TransferEntropy = digamma(k) - maxnorm(digamma(n_x + 1) + digamma(n_y +1)) + digamma(N)
```

I see that the above is being done in compute_TE however there are 4 subspaces instead of just 2 for X and Y.
