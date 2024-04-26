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

def generate_dp_table(graph, start_city):
    # Step 1: Initialize the DP table for the start city
    dp_table = {start_city: {other_city: float('inf') for other_city in graph}}

    # Step 2: Initialize the entry in the DP table for the start city
    dp_table[start_city][start_city] = 0

    # Step 3: Update the cost in the DP table for the adjacent cities of the start city
    for adj_city, cost1, cost2 in graph[start_city]:
        dp_table[start_city][adj_city] = cost1 + cost2

    # Step 4: For each city in the graph
    for city in graph:
        # If it's not the start city and there's a direct path from the start city to this city
        if city != start_city and dp_table[start_city][city] != float('inf'):
            # Update the cost in the DP table for all its adjacent cities
            for adj_city, cost1, cost2 in graph[city]:
                dp_table[start_city][adj_city] = min(dp_table[start_city][adj_city], dp_table[start_city][city] + cost1 + cost2)

    return dp_table


def main():
    file_path = 'input.txt'
    num_cities, start_city, end_city, city_data = read_data(file_path)
    print(num_cities)
    print(start_city)
    print(end_city)
    print(city_data)
    dp_table = generate_dp_table(city_data, start_city)
    print(dp_table)


if __name__ == '__main__':
    main()