from typing import List, Tuple, Callable
from sokoban.map import Map
import time


class LRTA_star:
    """
    LRTA* algorithm for Sokoban.
    """
    @staticmethod
    def LRTA_star(initial_map: Map, heuristic: Callable[[Map], int]) -> Tuple[List[Map], int, int]:
        """
        LRTA* algorithm for Sokoban.
        """
        start_time = time.time()
        maximum_time = 30
        current_time = 0
        current_map = initial_map
        cost = {}  # heuristic values for visited states
        path = [current_map]  # path to win
        push_count = 0
        pull_count = 0

        while not current_map.is_solved():
            # check time
            current_time = time.time() - start_time
            if current_time > maximum_time:
                return None, push_count, pull_count
            # if the current state is not in visited, calculate its heuristic
            if str(current_map) not in cost:
                cost[str(current_map)] = heuristic(current_map)

            # get all neighbors of the current state
            neighbors = current_map.get_neighbours()

            # if no neighbors exist, return failure
            if not neighbors:
                return None, push_count, pull_count

            # find the neighbor with the lowest heuristic value
            best_neighbor = None
            best_cost = float('inf')
            for neighbor in neighbors:
                neighbor_str = str(neighbor)
                new_cost = cost.get(neighbor_str, heuristic(neighbor))
                if new_cost < best_cost:
                    best_cost = new_cost
                    best_neighbor = neighbor

            # when go from state A to state B, the cost of A is the cost of B + 1
            # Update the heuristic value of the current state
            cost[str(current_map)] = best_cost + 1 # algorithm "learns"

            # move to the best neighbor
            current_map = best_neighbor
            path.append(current_map)

            # Update push and pull counts
            push_count += current_map.push_count
            pull_count += current_map.pull_count

        return path, push_count, pull_count

