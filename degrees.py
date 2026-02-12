from util import Node, QueueFrontier

def shortest_path(source, target):
    """
    Returns the shortest list of (movie_id, person_id) pairs
    that connect the source to the target.

    If no possible path, returns None.
    """

    # Initialize frontier with the source node
    start = Node(state=source, parent=None, action=None)
    frontier = QueueFrontier()
    frontier.add(start)

    # Keep track of explored nodes
    explored = set()

    while not frontier.empty():
        node = frontier.remove()

        # Check neighbors
        for movie_id, person_id in neighbors_for_person(node.state):
            if person_id not in explored and not frontier.contains_state(person_id):
                child = Node(state=person_id, parent=node, action=movie_id)

                # If child is target, build path
                if person_id == target:
                    path = []
                    while child.parent is not None:
                        path.append((child.action, child.state))
                        child = child.parent
                    path.reverse()
                    return path

                frontier.add(child)

        explored.add(node.state)

    # If no path found
    return None