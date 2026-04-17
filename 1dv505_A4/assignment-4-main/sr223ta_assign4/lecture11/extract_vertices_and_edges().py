def read_adjacency_list(file_path):
    adjacency_list = {}
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            animal, interactions = line.split(":")
            animal = animal.strip()  
            animal_interactions = []
            for interaction in interactions.split(","):
                neighbor, weight = interaction.strip().split()
                weight = int(weight)  
                animal_interactions.append((neighbor, weight))
            adjacency_list[animal] = animal_interactions

    return adjacency_list


def extract_vertices_and_edges(adjacency_list):
    vertices = list(adjacency_list.keys())

    animal_to_index = {animal: idx for idx, animal in enumerate(vertices)}

    edges = []
    for animal, interactions in adjacency_list.items():
        start_index = animal_to_index[animal]
        
        for neighbor, weight in interactions:
            end_index = animal_to_index[neighbor]
            edges.append([start_index, end_index, weight])

    print("Vertices (Animals):")
    print(vertices)
    print("\nEdges (Start Index, End Index, Weight):")
    for edge in edges:
        print(edge)

    return vertices, edges
adjacency_list = {
    'Lion': [('Tiger', 3), ('Elephant', 2), ('Zebra', 4)],
    'Tiger': [('Lion', 3), ('Monkey', 5), ('Panda', 2)],
    'Elephant': [('Lion', 2), ('Giraffe', 4), ('Rhino', 6), ('Hippo', 3)],
    'Giraffe': [('Elephant', 4), ('Zebra', 5), ('Flamingo', 2)],
    'Zebra': [('Lion', 4), ('Giraffe', 5), ('Kangaroo', 3)],
    'Monkey': [('Tiger', 5), ('Panda', 4), ('Penguin', 3)],
    'Panda': [('Tiger', 2), ('Monkey', 4), ('Kangaroo', 6), ('Flamingo', 1)],
    'Kangaroo': [('Zebra', 3), ('Panda', 6), ('Penguin', 5)],
    'Penguin': [('Monkey', 3), ('Kangaroo', 5), ('Flamingo', 4)],
    'Flamingo': [('Giraffe', 2), ('Panda', 1), ('Penguin', 4)],
    'Rhino': [('Elephant', 6), ('Hippo', 5)],
    'Hippo': [('Elephant', 3), ('Rhino', 5)]
}
vertices, edges = extract_vertices_and_edges(adjacency_list)
