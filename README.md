# ACO Application for Food Delivery Routes
A Python implementation for a simple ant colony optimization (ACO) algorithm that solves the Traveling Salesman Problem in order to help food delivery drivers find the most optimal food delivery route when given a list of `n` restaurants.

Built using NumPy, Matplotlib, and GeoPy libraries.
 
# How to Setup
Fill in the following input parameters (lines 103-121) in `aco.py`:\
    `num_ants`: the number of computer-generated ants in an iteration’s colony\
    `num_iterations`: the number of iterations that the ACO will be run on the graph\
    `restaurants`: an array of the names of the restaurant locations on the graph\
    `restaurantCoordinates`: an array of coordinates for the corresponding restaurants in `restaurants`. Can be gathered from Google Maps.\
    `distances`: an array of the distances between each restaurant, using the latitude and longitude coordinates of each restaurant, received from Google Maps\
    `pheromone_evaporation_rate`: the rate at which pheromones laid down by ants decays, decreasing the pheromone level of a given graph edge\
    `pheromone_deposit_rate`: the rate at which pheromones are laid down by ants, increasing the pheromone level of a given graph edge\
    `alpha`: the influence of pheromones on decision-making\
    `beta`: the influence of distance on decision-making\

## How the Application Works
After setup, running `aco.py` will output the most optimal order in which locations should be visited, and generate a graph showing the relationship between # of iterations ran and % of ants using the shortest path.
