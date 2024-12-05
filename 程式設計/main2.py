import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Circle, Rectangle

def draw_face(ax, is_happy=True):
    # Draw face circle
    face = plt.Circle((0.5, 0.5), 0.4, color='yellow', ec='black')
    ax.add_patch(face)
    
    # Draw eyes
    eye1 = plt.Circle((0.35, 0.65), 0.05, color='black')
    eye2 = plt.Circle((0.65, 0.65), 0.05, color='black')
    ax.add_patch(eye1)
    ax.add_patch(eye2)
    
    # Draw mouth
    if is_happy:
        mouth = plt.Arc((0.5, 0.4), 0.5, 0.3, angle=0, theta1=0, theta2=180, color='black')
    else:
        mouth = plt.Arc((0.5, 0.35), 0.5, 0.3, angle=0, theta1=180, theta2=360, color='black')
    ax.add_patch(mouth)

    # Set axis limits and remove grid/axes
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    ax.axis('off')

# Create a figure with two subplots
fig, axes = plt.subplots(1, 2, figsize=(10, 5))

# Draw a happy face and a sad face
draw_face(axes[0], is_happy=True)
axes[0].set_title('Smiley Face')

draw_face(axes[1], is_happy=False)
axes[1].set_title('Sad Face')

# Show the plot
plt.show()
