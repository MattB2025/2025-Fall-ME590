# Project 2

This project directory includes a python script `example_vector_plots.py` that plots a set of streamlines for two representative flows from the lecture. Those scripts were output by ChatGPT, given the following two vector fields:
$$
\begin{align}
\begin{bmatrix}u\\v\end{bmatrix}
 &= \begin{bmatrix}y/R\\-x/R\end{bmatrix}
 \\
 \begin{bmatrix}u\\v\end{bmatrix}
 &= \begin{bmatrix}x\\-y\end{bmatrix}\
 \end{align}
$$

where $R = \sqrt{x^2 + y^2}$. The velocity fields correspond to circular and hyperbolic flows. Some edits were made for the output plots to better visualize the vectors and streamlines.

A few notes regarding implementing a 3D vector field.

- The mesh grid currently shown is linearly spaced in $x,y$ and for a 3D field, doing the same is simply a matter of adding $x,y,z$ where now a mesh grid will be in 3D
  `X, Y, Z = np.meshgrid(x,y,z)` where the variable `z` is now another linear space, `z = np.linspace(-0.5, 0.5, 10)`
- This holds true for the vector field and streamline plots of the droplet, however, I would encourage you to drop the points outside of the radius of the droplet. The velocity vector field has no meaning there.
- Writing the velocity field equation `def velocity_field_1(X,Y)` now will take a third argument, `Z` as defined from the output of `numpy`'s `meshgrid` function.
- I would encourage you to write the function with additional input parameters ($\beta$ for example), in order to make your code a little cleaner.