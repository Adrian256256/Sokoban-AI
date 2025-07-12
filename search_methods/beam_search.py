import random
from typing import Callable, List, Tuple
from sokoban.map import Map
import random

# Source: https://medium.com/biased-algorithms/introduction-to-beam-search-algorithm-d598a77a4b4d

def beam_search(start_node: Map, beam_width: int, heuristic: Callable[[Map], int], max_restarts: int = 10000, max_iterations: int = 10000) -> Tuple[List[Map], int, int]:
    """
    Beam Search algorithm for Sokoban with stochasticity and restart mechanism.
    """
    random.seed(0)  # seed for reproducibility
    restart_count = 0

    import time
    start_time = time.time()
    # set maximum time for the search
    maximum_time = 120
    import time
    while time.time() - start_time < maximum_time:
        # beam with the start node
        beam = [(start_node, [start_node])]  # (current state, path to state)
        visited_states = set()
        iteration_count = 0
        total_pushes = 0
        total_pulls = 0

        while beam:
            next_beam = []

            # explore each node in the current beam
            for node, path in beam:
                # check if the goal is reached
                if node.is_solved():
                    return path, total_pushes, total_pulls  # goal is reached
                
                # Generate successors (neighbors) and add them to the next beam
                for successor in node.get_neighbours():
                    state_str = str(successor)
                    if state_str not in visited_states:  # avoid revisiting states
                        visited_states.add(state_str)
                        next_beam.append((successor, path + [successor]))

                        # Count pushes and pulls
                        total_pushes += successor.push_count
                        total_pulls += successor.pull_count

            # stochasticity: select successors probabilistically based on heuristic
            if next_beam:
                weights = [1 / (1 + heuristic(x[0])) for x in next_beam]  # inverse proportional to heuristic
                beam = random.choices(next_beam, weights=weights, k=min(beam_width, len(next_beam)))
            else:
                beam = []

            iteration_count += 1
            if iteration_count >= max_iterations:
                # if no solution is found in this iteration, break and restart
                break

        # increment restart count
        restart_count += 1

    return None, total_pushes, total_pulls  # no solution found
