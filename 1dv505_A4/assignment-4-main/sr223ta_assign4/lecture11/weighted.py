import os
print("Filer i aktuell katalog:", os.listdir())

file_path = r"C:\Users\saidh\Desktop\1DT910_4\sr223ta_assign4\lecture11\zoo_network.txt"
def read_adjacency_list(file_path):
    adjacency_list = {}

    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()  
                if not line:  
                    continue

                animal, interactions = line.split(":")
                animal = animal.strip()  
                interaction_list = []  

                
                interactions = interactions.split(",")
                for interaction in interactions:
                    neighbor, frequency = interaction.strip().split(" ")
                    interaction_list.append((neighbor, int(frequency)))  

                adjacency_list[animal] = interaction_list

    except FileNotFoundError:
        print(f"Filen {file_path} kunde inte hittas.")
    except Exception as e:
        print(f"Ett fel inträffade: {e}")

    return adjacency_list
adjacency_list = read_adjacency_list(file_path)
print("Adjacenslista:", adjacency_list)
