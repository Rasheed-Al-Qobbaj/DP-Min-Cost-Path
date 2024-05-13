def read_data(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Remove newline characters
    lines = [line.strip() for line in lines]

    # Get the number of cities
    num_cities = int(lines[0])

    # Get the start and end cities
    start_city, end_city = lines[1].split(', ')

    # Initialize an empty dictionary to hold the city data
    city_data = {}

    # Parse the city data
    for line in lines[2:]:
        # Split the line by ', ' and unpack the result into city and adjacent_cities
        city, *adjacent_cities = line.split(', ')
        # removes the square brackets from the start and end of the element, splits it at each comma
        adjacent_cities = [tuple(adj_city[1:-1].split(',')) for adj_city in adjacent_cities]
        # checks if the length of the element is 3, if it is, it adds it to the city_data dictionary
        city_data[city] = [(adj_city[0], int(adj_city[1]), int(adj_city[2])) for adj_city in adjacent_cities if len(adj_city) == 3]

    # Add a key for the end city to the city_data dictionary
    city_data[end_city] = []

    return num_cities, start_city, end_city, city_data

def generate_dp_table(graph):
    # Initialize the DP table for all cities
    dp_table = {city: {other_city: float('inf') if other_city != city else 0 for other_city in graph} for city in graph}

    # Update the cost in the DP table for the adjacent cities of each city
    for city in graph:
        for adj_city, cost1, cost2 in graph[city]:
            dp_table[city][adj_city] = cost1 + cost2

    # For each pair of cities in the graph
    for city in graph:
        for other_city in graph:
            # If there's a direct path from the city to the other city
            if dp_table[city][other_city] != float('inf'):
                # Update the cost in the DP table for all its adjacent cities
                for adj_city, cost1, cost2 in graph[other_city]:
                    dp_table[city][adj_city] = min(dp_table[city][adj_city], dp_table[city][other_city] + cost1 + cost2)

    return dp_table


def display_dp_table(dp_table):
    # Get all cities
    cities = list(dp_table.keys())

    # Print header
    print(" " * 7, end="")
    for city in cities:
        print(f"{city:>5}", end="")
    print()

    # Print each row
    for city in cities:
        print(f"{city:>5}", end="")
        for other_city in cities:
            cost = dp_table[city][other_city]
            # Print 'inf' if the cost is infinity, otherwise print the cost
            print(f"{cost if cost != float('inf') else 'inf':>5}", end="")
        print()


def find_optimal_path(dp_table, start_city, end_city):
    # Initialize the previous city dictionary
    prev_city = {city: None for city in dp_table}

    # For each city, find the city from which we can arrive at the current city with the minimum cost
    for city in dp_table:
        for other_city in dp_table:
            if city != other_city and dp_table[start_city][city] == dp_table[start_city][other_city] + dp_table[other_city][city]:
                prev_city[city] = other_city

    # Start from the end city and backtrack to the start city
    path = []
    current_city = end_city
    while current_city is not None:
        path.append(current_city)
        current_city = prev_city[current_city]

    # Reverse the path
    path = path[::-1]

    # Get the minimum cost
    min_cost = dp_table[start_city][end_city]

    return min_cost, path

def find_alternate_paths(dp_table, start_city, end_city):
    paths = []
    for _ in range(3):  # find three paths
        # Initialize the previous city dictionary
        prev_city = {city: None for city in dp_table}

        # For each city, find the city from which we can arrive at the current city with the minimum cost
        for city in dp_table:
            for other_city in dp_table:
                if city != other_city and dp_table[start_city][city] == dp_table[start_city][other_city] + dp_table[other_city][city]:
                    prev_city[city] = other_city

        # Start from the end city and backtrack to the start city
        path = []
        current_city = end_city
        while current_city is not None:
            path.append(current_city)
            current_city = prev_city[current_city]

        # Reverse the path
        path = path[::-1]

        # Get the cost
        cost = dp_table[start_city][end_city]

        # Add the path and its cost to the paths list
        paths.append((cost, path))

        # Remove the last edge in the path from the dp_table to find an alternate path in the next iteration
        if len(path) > 1:
            dp_table[path[-2]][path[-1]] = float('inf')

    # Sort the paths by cost
    paths.sort()

    return paths  # returns a list of tuples, where each tuple is (cost, path)

def main():
    file_path = 'input.txt'
    num_cities, start_city, end_city, city_data = read_data(file_path)
    print(num_cities)
    print(start_city)
    print(end_city)
    print(city_data)
    dp_table = generate_dp_table(city_data)
    print(dp_table)
    display_dp_table(dp_table)
    min_cost, path = find_optimal_path(dp_table, start_city, end_city)
    print(f"Minimum cost: {min_cost}")
    print(f"Optimal path: {' -> '.join(path)}")


if __name__ == '__main__':
    main()