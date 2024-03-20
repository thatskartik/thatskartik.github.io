

### Some results in Convex Optimization

---


Consider the function $f$ that is closed convex and $\beta$ smooth, then the following inequalities can be used to bound the change in the function across two points $x$ and $y$.

$$
\begin{gather}
    f(x) - f(y) \le g_x^T (x - y) - \frac{1}{2 \beta} \| g_x - g_y \|_*^2 
    \\
    f(x) - f(y) \le g_y^T(x - y) + \frac{\beta}{2} \|x - y \|^2
\end{gather}
$$

Note how the results are dual in nature. One of the results bounds the change in the function in terms of the "distance" between the points $x$ and $y$, while the other measures the distance after a linear map $\partial f$.

Maps under the set of subgradients are congenial to us, it follows from the Conjugate subgradient theorem



