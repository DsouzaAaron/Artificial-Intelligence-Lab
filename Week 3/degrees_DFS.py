import csv
import sys

from util import Node, StackFrontier, QueueFrontier

# Maps names to a set of corresponding person_ids
names = {}

# Maps person_ids to a dictionary of: name, birth, movies (a set of movie_ids)
people = {}

# Maps movie_ids to a dictionary of: title, year, stars (a set of person_ids)
movies = {}


def load_data(directory):
    """
    Load data from CSV files into memory.
    """
    # Load people
    with open(f"{directory}/people.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            people[row["id"]] = {
                "name": row["name"],
                "birth": row["birth"],
                "movies": set()
            }
            if row["name"].lower() not in names:
                names[row["name"].lower()] = {row["id"]}
            else:
                names[row["name"].lower()].add(row["id"])

    # Load movies
    with open(f"{directory}/movies.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            movies[row["id"]] = {
                "title": row["title"],
                "year": row["year"],
                "stars": set()
            }

    # Load stars
    with open(f"{directory}/stars.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                people[row["person_id"]]["movies"].add(row["movie_id"])
                movies[row["movie_id"]]["stars"].add(row["person_id"])
            except KeyError:
                pass


def main():
    if len(sys.argv) > 2:
        sys.exit("Usage: python degrees.py [directory]")
    path = "C:\\Users\\User\\Desktop\\Aritificial Intelligence\\degrees\\large"
    directory = sys.argv[1] if len(sys.argv) == 2 else path

    # Load data from files into memory
    print("Loading data...")
    load_data(directory)
    print("Data loaded.")

    source = person_id_for_name(input("Source Name: "))
    if source is None:
        sys.exit("Person not found.")
    target = person_id_for_name(input("Destination Name: "))
    if target is None:
        sys.exit("Person not found.")

    path = shortest_path(source, target)

    if path is None:
        print("Not connected.")
    else:
        degrees = len(path)
        print(f"{degrees} degrees of separation.")
        path = [(None, source)] + path
        for i in range(degrees):
            person1 = people[path[i][1]]["name"]
            person2 = people[path[i+1][1]]["name"]
            movie = movies[path[i+1][0]]["title"]
            print(f"{i + 1}: {person1} and {person2} starred in {movie}")


def shortest_path(source, target):
    """
    Returns the shortest list of (movie_id, person_id) pairs
    that connect the source to the target.

    If no possible path, returns None.
    """

    stack = StackFrontier()
    temp = StackFrontier()
    stack.add(Node(source,None, 0, None))

    visited = set()
    shortest_path_len = 1000
    shortest_path = []

    while not stack.empty():
        # print("Iterating\n")
        # if stack.empty():
        #     return None

        node = stack.top()

        # print(str(node.state)+"\n")
        visited.add(node.state)

        child = False
        for movie_id, person_id in neighbors_for_person(node.state):
            # print("Inside For loop\n")
            if stack.depth() > 6:
                # print("Length Exceeded!\n")
                child = False
                break
            if person_id == target:
                path = [(movie_id,person_id)]
                original = node
                while node.parent is not None:
                    # temp = stack.clone()
                    path.append((node.movie,node.state))
                    node = stack.remove()
                    # node = node.parent
                node = original
                return path
                if len(path) < shortest_path_len:
                    shortest_path = path.copy()
                    shortest_path_len = len(shortest_path)
                    print("Found a Path of length\n"+str(shortest_path_len))
                    print(shortest_path)
                    print("\n")
                    
                else:
                    child = False
                    break
            elif person_id in visited:
                continue
            child = True
            if stack.contains_state(person_id) == False:
                stack.add(Node(person_id, node, 0, movie_id))
                break
                # print("Adding Node for " + str(person_id) + "\n")
        
        if not child:
            # print("Romoving Node\n")
            deleted = stack.remove()

    if len(shortest_path) == 0:
        return None
    shortest_path = shortest_path.reverse()
    return shortest_path

    # stack = StackFrontier()
    # stack.add(Node(source, None, 0, None))
    # while(stack.empty() == False):
    #     print("Entering while loop\n")
    #     node = stack.remove()
    #     if(node.state == target):
    #         path = []
    #         while(node.parent != None):
    #             path.append((node.movie, node.state, node.parent))
    #             node = node.parent
    #         path.reverse()
    #         return path
    #     for movie_id, person_id in neighbors_for_person(node.state):
    #         if(stack.contains_state(person_id) == False and node.action != 1):
    #             stack.add(Node(person_id, node, 1, movie_id))
    #             print("Adding Node for " + str(person_id) + "\n")
    # return None
    # TODO
    raise NotImplementedError


def person_id_for_name(name):
    """
    Returns the IMDB id for a person's name,
    resolving ambiguities as needed.
    """
    person_ids = list(names.get(name.lower(), set()))
    if len(person_ids) == 0:
        return None
    elif len(person_ids) > 1:
        print(f"Which '{name}'?")
        for person_id in person_ids:
            person = people[person_id]
            name = person["name"]
            birth = person["birth"]
            print(f"ID: {person_id}, Name: {name}, Birth: {birth}")
        try:
            person_id = input("Intended Person ID: ")
            if person_id in person_ids:
                return person_id
        except ValueError:
            pass
        return None
    else:
        return person_ids[0]


def neighbors_for_person(person_id):
    """
    Returns (movie_id, person_id) pairs for people
    who starred with a given person.
    """
    movie_ids = people[person_id]["movies"]
    neighbors = set()
    for movie_id in movie_ids:
        for person_id in movies[movie_id]["stars"]:
            neighbors.add((movie_id, person_id))
    return neighbors


if __name__ == "__main__":
    main()
