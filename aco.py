# https://stackoverflow.com/questions/65309403/on-the-implementation-of-a-simple-ant-colony-algorithm

import matplotlib.pyplot as plt
import numpy as np
import geopy.distance

# https://stackoverflow.com/questions/19412462/getting-distance-between-two-points-based-on-latitude-longitude
def generateDistances(coordinates):
    distances = []
    for i in coordinates:
        temp = []
        for j in coordinates:
            temp.append(geopy.distance.distance(i, j).m)
        distances.append(temp)
    return distances

def ACO(num_ants, num_iterations, restaurants, distances, pheromone_evaporation_rate, pheromone_deposit_rate):
  # Initialize the pheromone trails on the edges of the graph to a low value
  pheromones = np.ones((num_cities, num_cities)) / num_cities
  
  # Initialize the best solution and best solution cost found so far
  best_solution = None
  best_solution_cost = float('inf')
  solution_costs_history = []
  
  # Iterate over the number of iterations
  for i in range(num_iterations):
    # Initialize the solutions for this iteration
    solutions = []
    solution_costs = []

    # Construct solutions for each ant
    for j in range(num_ants):
      # Initialize the current solution
      solution = []

      # Set the starting restaurant to index 0 
      current_restaurant = 0
      solution.append(current_restaurant)

      # Construct the solution by sequentially visiting the restaurants
      while len(solution) < num_cities:
        # Find the next restaurant to visit based on the pheromone trails
        next_restaurant = choose_next_restaurant(pheromones, current_restaurant, solution)
        solution.append(next_restaurant)
        current_restaurant = next_restaurant

      # Calculate the cost of the solution
      solution_cost = calculate_solution_cost(solution, distances)

      # Store the solution and its cost
      solutions.append(solution)
      solution_costs.append(solution_cost)

      # Update the best solution found so far
      if solution_cost < best_solution_cost:
        best_solution = solution
        best_solution_cost = solution_cost

    # Update the pheromone trails based on the solutions
    for j in range(num_ants):
      pheromones = update_pheromones(pheromones, solutions[j], solution_costs[j], pheromone_evaporation_rate, pheromone_deposit_rate)
      
    solution_costs_history.append(solution_costs)
  return [best_solution, solution_costs_history, best_solution_cost]

def choose_next_restaurant(pheromones, current_restaurant, solution):
  # Calculate the transition probabilities for each restaurant
  transition_probs = []
  for i in range(num_cities):
    if i in solution:
      transition_probs.append(0)
    else:
      transition_probs.append(pheromones[current_restaurant][i] ** alpha * ((1 / distances[current_restaurant][i]) ** beta))

  # Normalize the transition probabilities
  transition_probs = [x / sum(transition_probs) for x in transition_probs]

  # Choose the next restaurant based on the transition probabilities
  next_restaurant = np.random.choice(num_cities, p=transition_probs)
  return next_restaurant

def update_pheromones(pheromones, solution, solution_cost, pheromone_evaporation_rate, pheromone_deposit_rate):
  # Calculate the amount of pheromone to deposit on the edges
  delta_pheromones = np.zeros((num_cities, num_cities))
  for i in range(num_cities - 1):
    delta_pheromones[solution[i]][solution[i + 1]] = 1 / solution_cost

  # Update the pheromone trails by evaporating the old pheromones and depositing the new pheromones
  pheromones = (1 - pheromone_evaporation_rate) * pheromones + pheromone_deposit_rate * delta_pheromones
  return pheromones

def calculate_solution_cost(solution, distances):
    cost = 0
    for i in range(len(solution) - 1):
        cost += distances[solution[i]][solution[i + 1]]
    return cost

# Input Parameters
num_ants = 20
num_iterations = 100
restaurants = ["O'Bagel", 
               "Fiore's House of Quality", 
               "Chango Kitchen", 
               "Shake Shack Hoboken", 
               "Hot House Pizza"
               ]
restaurantCoordinates = [(-74.0292149, 40.7436045),
                         (-74.03618360000002, 40.7430165),
                         (-74.0335348, 40.74069799999999),
                         (-74.0305393, 40.7377453),
                         (-74.0401013, 40.7405219)]
distances = generateDistances(restaurantCoordinates)
pheromone_evaporation_rate = 0.1
pheromone_deposit_rate = 1
num_cities = len(restaurants)
alpha = 1 # influence of pheromones on decision-making
beta = 1 # influence of distance on decision-making

def report_results(success):
  plt.xlabel("iteration")
  plt.ylabel("% of ants using the shortest path")
  plt.ylim(0.0, 1.05)
  plt.xlim(0, 100)
  plt.plot(success)
  plt.show()

# Output
path = ACO(num_ants, num_iterations, restaurants, distances, pheromone_evaporation_rate, pheromone_deposit_rate)[0]
costs = np.array(ACO(num_ants, num_iterations, restaurants, distances, pheromone_evaporation_rate, pheromone_deposit_rate)[1])
best_sol_cost = ACO(num_ants, num_iterations, restaurants, distances, pheromone_evaporation_rate, pheromone_deposit_rate)[2]

success = []
for i in costs:
  successCount = 0
  for j in i:
    if j == best_sol_cost:
      successCount += 1       
  success.append(successCount/i.size)
        
pathNames = []
for i in path:
  pathNames.append(restaurants[i])

print(pathNames)

report_results(success)