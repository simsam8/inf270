# Problem 1

## a)

$$
\begin{aligned}
\underset{x}{\max}\quad 2x_1 + (1- \alpha)x_2 + x_3 & \\
3x_1 + x_2 + (2-\alpha)x_3 &\leq 6\\
x_1 + 2x_2 + x_3 &\leq 4\beta\\
x_1,x_2,x_3 \geq 0 &
\end{aligned}
$$

$$
\begin{aligned}
\zeta &= 0 + 2x_1 + (1-\alpha)x_2 + x_3\\
w_1 &= 6 - 3x_1 - x_2 - (2-\alpha)x_3\\
w_2 &= 4\beta - x_1 - 2x_2 - x_3\\
\end{aligned}
$$

$$
\begin{aligned}
\zeta &= 0 + 2x_1 + x_2 + x_3\\
w_1 &= 6 - 3x_1 - x_2 - 2x_3\\
w_2 &= 4 - x_1 - 2x_2 - x_3\\
\end{aligned}
$$

$$
\begin{aligned}
\zeta &= 4 - \frac{2}{3}w_1 + \frac{1}{3}x_2 - \frac{1}{3}x_3\\
x_1 &= 2 - \frac{1}{3}w_1 - \frac{1}{3}x_2 -\frac{2}{3}x_3\\
w_2 &= 2 + \frac{1}{3}w_1 - \frac{5}{3}2x_2 - \frac{1}{3}x_3\\
\end{aligned}
$$

$$
\begin{aligned}
\zeta &= \frac{22}{5} - \frac{3}{5}w_1 - \frac{1}{5}w_2 - \frac{2}{5}x_3\\
x_1 &= \frac{8}{5} - \frac{2}{5}w_1 + \frac{1}{5}w_2 - \frac{3}{5}x_3\\
x_2 &= \frac{6}{5} + \frac{1}{5}w_1 - \frac{3}{5}2w_2 - \frac{1}{5}x_3\\
\end{aligned}
$$


$x_1=\frac{8}{5}, x_2=\frac{6}{5}, x_3=0$

\newpage

## b)

$$
\begin{aligned}
\underset{y}{\min}\quad 6y_1 + 4\beta y_2 & \\
3y_1 + y_2 & \geq 2\\
y_1 + 2 y_2 & \geq (1-\alpha)\\
(2-\alpha)y_1 + y_2 & \geq 1\\
y_1,y_2 \geq 0 &\\
\end{aligned}
$$

We find the optimal values for the dual from the primal solution.

$$
\begin{aligned}
-\xi &= -\frac{22}{5} -\frac{8}{5}z_1 -\frac{6}{5}z_2\\
y_1 &= \frac{3}{5} + \frac{2}{5}z_1 - \frac{1}{5}z_2\\
y_2 &= \frac{1}{5} - \frac{1}{5}z_1 + \frac{3}{5}z_2\\
z_3 &= \frac{2}{5} + \frac{3}{5}z_1 + \frac{1}{5}z_2\\
\end{aligned}
$$

$y_1=\frac{3}{5}, y_2=\frac{1}{5}, z_1=0, z_2=0, z_3=\frac{2}{5}$

\newpage

## c)

Finding range for $\alpha$ in objective function:

$$
\newcommand\mycolv[1]{\begin{bmatrix}#1\end{bmatrix}}\\
\newcommand\m[1]{\begin{pmatrix}#1\end{pmatrix}} 
\begin{aligned}\\
\mathcal{B} = \{1,2\},&\quad \mathcal{N} = \{4,5,3\}\\
c_{\mathcal{B}} = \mycolv{2\\1},&\quad c_{\mathcal{N}} = \mycolv{0\\0\\1}\\
\Delta c_{\mathcal{B}} = \mycolv{0\\1},&\quad \Delta c_{\mathcal{N}} = \mycolv{0\\0\\0}\\
B^{-1}N &= \frac{1}{5}\mycolv{2&-1&3\\-1&3&1}\\
\Delta z_{\mathcal{N}} &= (B^{-1}N)^{T}\Delta c_{\mathcal{B}} - \Delta c_{\mathcal{N}}\\
\Delta z_{\mathcal{N}} &= \frac{1}{5}\mycolv{2&-1\\-1&3\\3&1}\mycolv{0\\1}-\mycolv{0\\0\\0}\\
\Delta z_{\mathcal{N}} &= \frac{1}{5}\mycolv{-1\\3\\1}\\
z_{\mathcal{N}}^* &= \frac{1}{5}\mycolv{3&1&2}^T\\
z_{\mathcal{N}}^* + &t \Delta z_{\mathcal{N}} \geq 0\\
\frac{1}{5}\mycolv{3\\1\\2}+t&\frac{1}{5}\mycolv{-1\\3\\1} \geq 0\\
3\geq t,\quad t\geq &-\frac{1}{3}, \quad t\geq -2\\
-\frac{1}{3} \leq &t \leq 3\\
x_2 \quad range &\to \mycolv{\frac{2}{3}&4}\\
1-\alpha = \frac{2}{3}, &\quad 1-\alpha = 4\\
\alpha = \frac{1}{3}, &\quad \alpha = -3
\end{aligned}\\
$$

The tighest bound on $\alpha$ then becomes: $-3 \leq \alpha \leq \frac{1}{3}$

Thus these are the values for $\alpha$ where the solution in a) remains optimal.

\newpage

## d)

We solve $B^{-1}b \geq 0$:

$$
\newcommand\mycolv[1]{\begin{bmatrix}#1\end{bmatrix}}\\
\begin{aligned}
\frac{1}{5}\mycolv{2&-1\\-1&3}\mycolv{6\\4\beta} &\geq 0\\
\frac{1}{5}\mycolv{12-4\beta\\-6+12\beta}&\geq 0\\
\frac{12}{5} - \frac{4}{5}\beta \geq 0,&\quad -\frac{6}{5} + \frac{12}{5}\beta \geq 0\\
\frac{12}{5} \geq \frac{4}{5}\beta,&\quad  \frac{12}{5}\beta \geq \frac{6}{5}\\
3 \geq \beta, &\quad \beta \geq \frac{1}{2}\\
\frac{1}{2} \leq &\beta \leq 3
\end{aligned}
$$

These are the values of $\beta$ where $x_1$ and $x_2$ remains in the basis of
the optimal solution.


## e)

The LP is a linear combination of the Primal and Dual found previous in the task,
where $\alpha =0,\quad \beta = 1$.
The objective functions are added together as another constraint, 
and the objective function is the sum of all variables.

The first 5 constraints are feasible, as they are feasible in the Primal and Dual,
but the last constraint is not feasible, as it is the sum of the objective functions 
of the Primal and Dual, which sums to 0.

\newpage

# Problem 2

## a)

$$
\begin{aligned}
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
\end{aligned}
$$

\newpage

## c)

status: 1, Optimal

objective: 87.5

| Variable   | Value    |
|--------------- | --------------- |
|u0   | 0.0    |
|u1   | 0.0    |
|u2   | 100.0  |
|v0   | 30.0   |
|v01   | 10.0   |
|v02   | 10.0   |
|v0T   | 10.0   |
|v1   | 60.0   |
|v11   | 15.0   |
|v12   | 15.0   |
|v1T   | 30.0   |
|z0   | 105.0  |
|z1   | 82.5   |

\newpage

# Problem 3 

## a) 

$$
\begin{aligned}
\underset{y}{\min}\quad y_0 b + \sum^{n}_{j=1}{y_j} &\\
y_0a_j + y_{j+1} &\geq c_j \quad j=1,\dots,n\\
y_0,\dots,y_n &\geq 0\\
\end{aligned}
$$

## b)

The algorithm provides a Primal feasible solution,
as it terminates before the sum of $a$ exceeds $b$.
And the min function assures that $x^{*}_j$ never exceeds $1$.

With the numerical example we get that:

$x^{*} = (1,1,\frac{1}{4},0)$


## c) 


Given the fact that the algorithm in b) provides a primal feasible solution,
the slack variables $w_j$ will either be zero if $x_j=1$ and/or if 
the capacity $b$ is filled, or the remaining 
value to satisfy the constraint when $x_j$ is a fraction or 0.

By knowing this, we can find $z^*,y^*,w^*$ by solving the inequalities:

$A^Ty - z \geq c$ and $Ax + w \leq b$,

to find a feasible solution to the dual, which satisfies complementary slackness.

Once we find a feasible dual solution that satisfies complementary slackness,
we know that $x^*$ is an optimal solution.


Using the numerical example from b)

We start by writing down the Primal and Dual.

$$
\begin{aligned}
\underset{x}{\max}\quad 4x_1 + 9x_2 + 8x_3 + 2x_4&\\
x_1 + 3x_2 + 4x_3 + 2x_4 &\leq 5\\
x_2 &\leq 1\\
x_3 &\leq 1\\
x_4 &\leq 1\\
x_1,\dots,x_n &\geq 0\\
\end{aligned}
$$


$$
\begin{aligned}
\underset{y}{\min}\quad 5y_0 + y_1 + y_2 + y_3 + y_4&\\
y_0 + y_1 &\leq 4\\
3y_0 + y_2 &\leq 9\\
4y_0 + y_3 &\leq 8\\
2y_0 + y_4 &\leq 2\\
y_0,\dots,y_n &\geq 0\\
\end{aligned}
$$

With the given $x^{*} = (1,1,\frac{1}{4},0)$,


By using:

$A^Ty - z \geq c$ and $Ax + w \leq b$,

we find $z^*,y^*,w^*$:

$$
\begin{aligned}
x* = (1,1,\frac{1}{4},0)&\quad y^* = (2,2,3,0,0)\\
z^* = (0,0,0,2)&\quad w^* = (0,0,0,\frac{3}{4},1)
\end{aligned}
$$

and we can see that $x_jz_j=0$ and $y_jw_j=0$ for all $j$. 
