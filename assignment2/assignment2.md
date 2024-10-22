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

$y_1=\frac{3}{5}, y_2=\frac{1}{5}, z_3=\frac{2}{5}$


c)

We first apply our solution and find $\alpha$ for each constraint in the primal and dual.

Primal constraints:

$$
\begin{align}
\frac{22}{5} &\leq 2x_1 + (1-\alpha) x_2 + x_3\\
\frac{22}{5} &\leq \frac{16}{5} + \frac{6}{5} - \frac{6}{5}\alpha\\
\frac{6}{5}\alpha &\leq \frac{22}{5} - \frac{22}{5}\\
\alpha &\leq 0\\
\end{align}
$$


$\alpha$ has no effect, as $x_3$ is $0$:

$$
3x_1 + x_2 + (2-\alpha)x_3 \leq 6\\
$$


Dual constraints:

$$
\begin{align}
y_1 + 2y_2 \geq (1-\alpha)

\end{align}
$$




d)

e)

The LP is bounded, as there exists constraints that have opposite inequalities.

