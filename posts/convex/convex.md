---
title: Convex
author: Kartik Srinivas
---


### Some results in Convex Optimization

---

<b> Duality of the conjugates </b>

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


<b>Proximal Descent</b>

The fundamental inequality is derived as follows for $F = f + g$ [^cvx]

$$
 F(x) - F(y^+) \ge \frac{L}{2} \| x - y^+ \|^2 - \frac{L}{2} \| x - y \|^2 + B_f(x, y)
$$


From this two results follow, both of which help us in showing the convergence

The first is the descent lemma

$$
    F(x) - F(x^+) \ge \frac{L}{2} \| x - x^+ \|^2 = \frac{1}{2L} \| G(x) \|^2 
$$
This shows convergence of Convex-case[^cvx]
The second can be used to show the distance is decreasing 

$$
    F(x_*) - F(x^+) \ge \frac{L}{2} (\| x_* - x^+ \|^2  - \|x_*- x^2 \| ) + B_f(x*, x)
$$

This second inequality helps use prove the convergence of convex, strongly-convex and smooth $f$, proximal descent [^scvx]

[^scvx]: It is clear that the right side is a recursion isn the distances, and the left side is lesser than zero. Moreover the final term can be bounded using  the fundamental equation of strong convexity.
There are 2 cases
    $$
        B_f(x^*, x) \ge \frac{\mu}{2} \| x - x^* \|^2 ,  0
    $$

[^cvx]: To see this use the strong convexity of the objective of proximal gradient descent, and that the optimal is at $y^+$. 