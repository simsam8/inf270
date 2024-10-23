# 1

a)

$$
\begin{align}
\underset{x}{\max}\quad 2x_1 + (1- \alpha)x_2 + x_3 & \\
3x_1 + x_2 + (2-\alpha)x_3 &\leq 6\\
x_1 + 2x_2 + x_3 &\leq 4\beta\\
x_1,x_2,x_3 \geq 0 &
\end{align}
$$

$$
\begin{align}
\zeta &= 0 + 2x_1 + (1-\alpha)x_2 + x_3\\
w_1 &= 6 - 3x_1 - x_2 - (2-\alpha)x_3\\
w_2 &= 4\beta - x_1 - 2x_2 - x_3\\
\end{align}
$$

$$
\begin{align}
\zeta &= 0 + 2x_1 + x_2 + x_3\\
w_1 &= 6 - 3x_1 - x_2 - 2x_3\\
w_2 &= 4 - x_1 - 2x_2 - x_3\\
\end{align}
$$

$$
\begin{align}
\zeta &= 4 - \frac{2}{3}w_1 + \frac{1}{3}x_2 - \frac{1}{3}x_3\\
x_1 &= 2 - \frac{1}{3}w_1 - \frac{1}{3}x_2 -\frac{2}{3}x_3\\
w_2 &= 2 + \frac{1}{3}w_1 - \frac{5}{3}2x_2 - \frac{1}{3}x_3\\
\end{align}
$$

$$
\begin{align}
\zeta &= \frac{22}{5} - \frac{3}{5}w_1 - \frac{1}{5}w_2 - \frac{2}{5}x_3\\
x_1 &= \frac{8}{5} - \frac{2}{5}w_1 + \frac{1}{5}w_2 - \frac{3}{5}x_3\\
x_2 &= \frac{6}{5} + \frac{1}{5}w_1 - \frac{3}{5}2w_2 - \frac{1}{5}x_3\\
\end{align}
$$


$x_1=\frac{8}{5}, x_2=\frac{6}{5}, x_3=0$

b)

$$
\begin{align}
\underset{y}{\min}\quad 6y_1 + 4\beta y_2 & \\
3y_1 + y_2 & \geq 2\\
y_1 + 2 y_2 & \geq (1-\alpha)\\
(2-\alpha)y_1 + y_2 & \geq 1\\
y_1,y_2 \geq 0 &\\
\end{align}
$$

We find the optimal values for the dual from the primal solution.

$$
\begin{align}
-\xi &= -\frac{22}{5} -\frac{8}{5}z_1 -\frac{6}{5}z_2\\
y_1 &= \frac{3}{5} + \frac{2}{5}z_1 - \frac{1}{5}z_2\\
y_2 &= \frac{1}{5} - \frac{1}{5}z_1 + \frac{3}{5}z_2\\
z_3 &= \frac{2}{5} + \frac{3}{5}z_1 + \frac{1}{5}z_2\\
\end{align}
$$

$y_1=\frac{3}{5}, y_2=\frac{1}{5}, z_1=0, z_2=0, z_3=\frac{2}{5}$


c)

Finding range for $\alpha$ in objective function:
$$
\newcommand\mycolv[1]{\begin{bmatrix}#1\end{bmatrix}}\\
\newcommand\m[1]{\begin{pmatrix}#1\end{pmatrix}} 
\mathcal{B} = \{1,2\},\quad \mathcal{N} = \{4,5,3\}\\
\mathcal{c_{\mathcal{B}}} = \mycolv{2\\1},\quad \mathcal{c_{\mathcal{N}}} = \mycolv{0\\0\\1}\\
\Delta \mathcal{c_{\mathcal{B}}} = \mycolv{0\\1}, \Delta \mathcal{c_{\mathcal{N}}} = \mycolv{0\\0\\0}\\
B^{-1}N = \frac{1}{5}\mycolv{2&-1&3\\-1&3&1}\\
\begin{align*}\\
\Delta \mathcal{z}_{\mathcal{N}} &= (B^{-1}N)^{T}\Delta \mathcal{c_{\mathcal{B}}} - \Delta \mathcal{c_{\mathcal{N}}}\\
\Delta \mathcal{z}_{\mathcal{N}} &= \frac{1}{5}\mycolv{2&-1\\-1&3\\3&1}\mycolv{0\\1}-\mycolv{0\\0\\0}\\
\Delta \mathcal{z}_{\mathcal{N}} &= \frac{1}{5}\mycolv{-1\\3\\1}\\
\end{align*}\\
\mathcal{z}_{\mathcal{N}}^* = \frac{1}{5}\mycolv{3&1&2}^T\\
\mathcal{z}_{\mathcal{N}}^* + t \Delta \mathcal{z}_{\mathcal{N}} \geq 0\\
\frac{1}{5}\mycolv{3\\1\\2}+t\frac{1}{5}\mycolv{-1\\3\\1} \geq 0\\
3\geq t,\quad t\geq -\frac{1}{3}, \quad t\geq -2\\
-\frac{1}{3} \leq t \leq 3\\
x_2 \quad range \to \mycolv{\frac{2}{3}&4}\\
\begin{align*}\\
1-\alpha = \frac{2}{3}, &\quad 1-\alpha = 4\\
\alpha = \frac{1}{3}, &\quad \alpha = -3
\end{align*}\\
$$

Checking for values of $\alpha$ in the dual:

$$
y_1 + 2y_2 - z_2 \leq 1-\alpha\\
\frac{3}{5} + 2\frac{1}{5} - 0 \leq 1-\alpha\\
\alpha \leq 0
\\~\\
(2-\alpha)y_1 + y_2 - z_3 \leq 1\\
(2-\alpha)\frac{3}{5} + \frac{1}{5} - \frac{2}{5} \leq 1\\
\frac{6}{5} - \frac{3}{5}\alpha + \frac{1}{5} - \frac{2}{5} \leq 1\\
-\frac{3}{5}\alpha \leq 0\\
\alpha \geq 0\\
?????
$$

The tighest bound on $\alpha$ then becomes: $-3 \leq \alpha \leq 0$

Thus these are the values for $\alpha$ where the solution in a) remains optimal.


d)

e)

The LP is a linear combination of the Primal and Dual found previous in the task,
where $\alpha =0,\quad \beta = 1$.
The objective functions are added together as another constraint, 
and the objective function is the sum of all variables.

The first 5 constraints are feasible, as they are feasible in the Primal and Dual,
but the last constraint is not feasible, as it is the sum of the objective functions 
of the Primal and Dual, which sums to 0.


# 2

a)

$$
\begin{align}
\underset{u,v}{\max}\quad \sum^{n}_{j=1}{z_j} &- \sum^{m}_{i=1}{k_iu_i}\\
\sum^{m}_{i=1}{u_i} &\leq c_{in}\\
\sum^{n}_{j=1}{v_i} &\leq c_{out}\\
v_j - \sum^{m}_{i=1}{a_{ij}u_i} &= 0 \quad j = 1,\dots , n\\
v_{jk} \leq b_{jk} &\quad j = 1,\dots,n\quad k=1,\dots,T-1\\
v_j = \sum^{T}_{k=1}{v_{jk}}&\quad j = 1,\dots,n\\
z_j = \sum^{T}_{k=1}{p_{jk}v_{jk}} &\quad j = 1,\dots,n\\
u_1,\dots,u_m &\geq 0\\
v_1,\dots,v_n &\geq 0\\
v_{11},\dots,v_{jT}&\geq 0\\
\end{align}
$$



# 3 

a) 

$$
\begin{align}
\underset{y}{\min}\quad y_1 b + \sum^{n}_{j=2}{y_j} &\\
y_1a_j + y_{j+1} &\geq c_j \quad j=1,\dots,n\\
y_1,\dots,y_n &\geq 0\\
\end{align}
$$

b)

- terminates before sum of a reaches b.
- min function assures xj never exceeds 1


c) 


