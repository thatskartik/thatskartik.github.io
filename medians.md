### On Medians


The following are three nice problems on medians, along  with their solutions


[Problem 1]() : Find the minimum amount of stick to be cut or added  to create $n$ sticks of equal length when given an array of
$n$ sticks $a_i$.

The problem boils down to finding an optimal stick length $p$ such that the sum 
$$
    f(p, a) = \sum_{i = 1}^{i = n} | p - a_i| 
$$
is minimized over the discrete space $p \in \{\min(a_i), \max(a_i) \}$


The solution is to of course look at this as an optimization problem, and somehow understand the curvature of this loss
function as a function of $p$.

Of course, let us start with lower values of $p$, starting from the minimum value in the array and work our way upwards.

Suppose that the sorted values of the array are represented as the array $b_i$.
Since the optimization objective $f(p)$ is invariant of the order of the sticks, $f(p,a) = f(p, b)$
Now, notice that if $p \in \{b_1, b_2\}$ and we perturb the value of $p$ by $\epsilon$, the function value changes
(decreases) by $(n - 1)\epsilon$ .
This means that the function is initially decreasing when we move to the right, and due to symmetry, will be increasing
when we move to the right towards the right end of the array.

This would suggest that there is a minimum in between, and the shape of a function is like a "cup" (convex).



