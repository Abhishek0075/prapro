import numpy as np
import matplotlib.pyplot as plt

def gDescent(x,y,learning_rate = 0.01, iterations = 100):
    # Initial slope and intercept
    slope = 0
    intercept = 0

    # Perform gradient descent
    for i in range(iterations):
        # Calculate predictions with current slope and intercept
        y_pred = slope * x + intercept
        
        # Calculate gradients for slope and intercept
        gradient_slope = (-2 / len(x)) * np.sum(x * (y - y_pred))
        gradient_intercept = (-2 / len(x)) * np.sum(y - y_pred)
        
        oldSlope = slope
        oldIntercept = intercept
        
        # Update slope and intercept
        slope -= learning_rate * gradient_slope
        intercept -= learning_rate * gradient_intercept
        
        print(f"Difference : {oldSlope - slope}  {oldIntercept - intercept}")
        
        if(np.allclose([slope, intercept], [oldSlope, oldIntercept], atol = 1e-2)):
            print("All close")
            break
        
        # Clear the plot to remove the old line
        plt.clf()
        
        # Plot the updated data points
        plt.scatter(x, y, label='Data Points')
        # Plot the line with the current slope and intercept
        plt.plot(x, slope * x + intercept, label=f'Iteration {i+1}')

        # Add labels and legend
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.legend()

        # Draw the updated plot
        plt.draw()
        
        # Pause briefly to observe the plot update
        plt.pause(0.5)

    plt.close()
    return (slope, intercept)

