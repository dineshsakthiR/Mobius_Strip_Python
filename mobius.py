import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

class MobiusStrip:
    def __init__(self, R, w, n):
        #Initialising the Radius, width and Resoultion form the user input
        self.R = R 
        self.w = w  
        self.n = n  
        self.u, self.v = np.meshgrid(
            np.linspace(0, 2 * np.pi, n),
            np.linspace(-w/2, w/2, n)
        )
        self.compute_mesh()

    def compute_mesh(self):
        #commputing the 3D coordinates
        u = self.u
        v = self.v
        R = self.R

        #parametric equatinons from the problem
        self.x = (R + v * np.cos(u / 2)) * np.cos(u)
        self.y = (R + v * np.cos(u / 2)) * np.sin(u)
        self.z = v * np.sin(u / 2)

    def surface_area(self):
        #Calculating the surface area
        du = (2 * np.pi) / (self.n - 1)
        dv = self.w / (self.n - 1)

        dx_du = - (self.R + self.v * np.cos(self.u / 2)) * np.sin(self.u) - 0.5 * self.v * np.sin(self.u / 2) * np.cos(self.u)
        dy_du = (self.R + self.v * np.cos(self.u / 2)) * np.cos(self.u) - 0.5 * self.v * np.sin(self.u / 2) * np.sin(self.u)
        dz_du = 0.5 * self.v * np.cos(self.u / 2)

        dx_dv = np.cos(self.u / 2) * np.cos(self.u)
        dy_dv = np.cos(self.u / 2) * np.sin(self.u)
        dz_dv = np.sin(self.u / 2)

        cx = dy_du * dz_dv - dz_du * dy_dv
        cy = dz_du * dx_dv - dx_du * dz_dv
        cz = dx_du * dy_dv - dy_du * dx_dv

        dA = np.sqrt(cx**2 + cy**2 + cz**2)
        return np.sum(dA) * du * dv

    def edge_length(self):
        #Calculating the length of the edge 
        edge_x = self.x[0, :]
        edge_y = self.y[0, :]
        edge_z = self.z[0, :]

        dx = np.diff(edge_x)
        dy = np.diff(edge_y)
        dz = np.diff(edge_z)
        edge_lengths = np.sqrt(dx**2 + dy**2 + dz**2)

        return np.sum(edge_lengths)

    def plot(self):
        #Visualising the created strip
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(self.x, self.y, self.z, cmap='plasma', edgecolor='k', linewidth=0.2, alpha=0.9)
        ax.set_title("3D Möbius Strip")
        plt.show()

if __name__ == "__main__":
    #Getting user input
    try:
        R = float(input("Enter Radius R (e.g., 5): "))
        w = float(input("Enter Width w (e.g., 2): "))
        n = int(input("Enter Resolution n (e.g., 100): "))

        mobius = MobiusStrip(R, w, n)
        print("\n--- Calculated Surface Area and Edge Length ---")
        print(f"Surface Area: {mobius.surface_area():.4f}")
        print(f"Edge Length : {mobius.edge_length():.4f}")

        #Displaying the plot
        show_plot = input("Do you want to see the 3D plot? (yes/no): ").strip().lower()
        if show_plot == "yes":
            mobius.plot()

    except ValueError:
        print("Invalid Input, Please Enter Number Only")
