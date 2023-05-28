import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()
fig.set_facecolor('pink')

# INTIAL GRID
axis = 50
grid = np.zeros((axis, axis))
# INITIALIZES GRID CELLS TO 0S AND 1S
grid[25, 26:29] = 1
grid[26:28, 24:27] = np.array([[1, 0, 1], [1, 0, 1]])

def update(frame_number, grid, axis):
  """
  Copies current grid, counts neighbors, applies rules, and updates grid.
  """
  new_grid = grid.copy()

  for i in range(axis):
    for j in range(axis):

      # LIVE NEIGHBOR COUNT!
      num_neighbors = int(
        (grid[(i - 1) % axis, (j - 1) % axis] + grid[(i - 1) % axis, j] +
         grid[(i - 1) % axis, (j + 1) % axis] + grid[i, (j - 1) % axis] +
         grid[i, (j + 1) % axis] + grid[(i + 1) % axis, (j - 1) % axis] +
         grid[(i + 1) % axis, j] + grid[(i + 1) % axis, (j + 1) % axis]))

      # RULES OF THE GAME!
      # if cell is ON...
      if grid[i, j] == 1:
        # if cell has fewer than 2 neighbors...
        # if cell has more than 3 neighbors...
        if num_neighbors < 2 or num_neighbors > 3:
          # it turns OFF!
          new_grid[i, j] = 0
        # if cell has 2 or 3 neighbors...
        else:
          # it turns ON!
          new_grid[i, j] = 1
      # if cell is OFF...
      else:
        # if cell is exactly 3 neighbors...
        if num_neighbors == 3:
          # it turns ON!
          new_grid[i, j] = 1

  # UPDATE GRID
  mat.set_data(new_grid)
  grid[:] = new_grid[:]

  return [mat]


# ANIMATION
mat = ax.matshow(grid, cmap='Pastel1')
ani = animation.FuncAnimation(fig,
                              update,
                              fargs=(grid, axis),
                              frames=100,
                              interval=100)

# Display the animation
plt.show()
