import os
from sokoban.map import Map
from typing import List, Tuple
from search_methods.heuristics import Heuristic
from search_methods.lrta_star import LRTA_star
from search_methods.beam_search import beam_search


class Solver:
    def run_search_algorithm(self, algorithm: str, heuristic: str, map_name: str, generate_gif: bool = False) -> Tuple[int, float]:
        """
        Run the search algorithm with the given heuristic and map name.
        Returns the number of nodes visited and the time taken.
        """
        heuristic_map = {
            'manhattan_heuristic': Heuristic.manhattan_heuristic,
            'euclidian_heuristic': Heuristic.euclidian_heuristic,
            'minimum_euclidian': Heuristic.minimum_euclidian,
            'minimum_manhattan': Heuristic.minimum_manhattan,
            'combined_heuristic': Heuristic.combined_heuristic,
        }

        if heuristic not in heuristic_map:
            raise ValueError(f"Unknown heuristic: {heuristic}")

        heuristic_function = heuristic_map[heuristic]

        map = Map.from_yaml(map_name)
        import time
        start_time = time.time()
        if algorithm == 'LRTA_star':
            path, push_count, pull_count = LRTA_star.LRTA_star(map, heuristic_function)
        elif algorithm == 'Beam_Search':
            path, push_count, pull_count = beam_search(map, 50, heuristic_function)
        else:
            raise ValueError(f"Unknown algorithm: {algorithm}")
        end_time = time.time()
        time_taken = end_time - start_time
        if path is None:
            return 0, time_taken  # No path found
        count = len(path)
        print(f"{algorithm} visited {count} nodes resolving {map_name} in {time_taken} seconds using pushes: {push_count} and pulls: {pull_count}")
        
        return count, time_taken
    
    def plot_multiple_alg_one_heuristic(self, algorithms: List[str], heuristic: str, num_nudes_visited: List[int], time_taken: List[float], map_name: str):
        """
        Plot the number of nodes visited for each algorithm with the same heuristic.
        """
        # create plot
        import matplotlib.pyplot as plt
        import numpy as np
        # create a bar chart with the number of nodes visited for each algorithm
        x = np.arange(len(algorithms))
        fig, ax = plt.subplots()
        bars = ax.bar(x, num_nudes_visited, color=['blue', 'orange', 'green'])
        ax.set_xticks(x)
        ax.set_xticklabels(algorithms)
        ax.set_ylabel('Number of nodes visited')
        ax.set_title(f'Number of nodes visited for {map_name} with {heuristic}')
        # add value to each bar
        for bar in bars:
            yval = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2, yval, int(yval), ha='center', va='bottom')
        plt.show(block=False)

    def plot_one_alg_multiple_heuristics(self, algorithm: str, heuristics: List[str], num_nodes_visited: List[int], time_taken: List[float], map_name: str):
        """
        Plot the number of nodes visited for each heuristic with the same algorithm.
        """
        # create plot
        import matplotlib.pyplot as plt
        import numpy as np
        # create a bar chart with the number of nodes visited for each heuristic
        x = np.arange(len(heuristics))
        fig, ax = plt.subplots()
        bars = ax.bar(x, num_nodes_visited, color=['blue', 'orange', 'green'])
        ax.set_xticks(x)
        ax.set_xticklabels(heuristics)
        ax.set_ylabel('Number of nodes visited')
        ax.set_title(f'Number of nodes visited for {map_name} with {algorithm}')
        # add value to each bar
        for bar in bars:
            yval = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2, yval, int(yval), ha='center', va='bottom')
        # make the window proportional to the number of heuristics
        width = 5 + len(heuristics) * 2
        fig.set_size_inches(width, 5)
        # write the time taken for each heuristic on the x axis
        # use only first 2 decimal digits
        for i in range(len(heuristics)):
            # make the text white
            ax.text(x[i], 74, f"{time_taken[i]:.2f}s", ha='center', va='top', color='white')
        # make background black
        fig.patch.set_facecolor('black')
        ax.set_facecolor('black')
        # make the grid white
        ax.grid(color='white')
        # make the ticks white
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')
        # make the title white
        ax.title.set_color('white')
        # make the labels white
        ax.xaxis.label.set_color('white')
        ax.yaxis.label.set_color('white')
        # make the ticks bigger
        ax.tick_params(axis='x', labelsize=15)
        ax.tick_params(axis='y', labelsize=15)
        # make the title bigger
        ax.title.set_size(20)

        # plot the graph without making the program wait for the user to close it
        plt.show(block=False)

    def plot_one_alg_multiple_maps(self, algorithm: str, heuristic: str, num_nodes_visited: List[int], time_taken: List[float], maps: List[str]):
        """
        Plot the number of nodes visited for each map with the same algorithm and heuristic.
        """
        # create plot
        import matplotlib.pyplot as plt
        import numpy as np
        # create a bar chart with the number of nodes visited for each map
        x = np.arange(len(maps))
        fig, ax = plt.subplots()
        bars = ax.bar(x, num_nodes_visited, color=['blue', 'orange', 'green'])
        ax.set_xticks(x)
        ax.set_xticklabels(maps)
        ax.set_ylabel('Number of nodes visited')
        ax.set_title(f'Number of nodes visited for {algorithm} with {heuristic}')
        # add value to each bar
        for bar in bars:
            yval = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2, yval, int(yval), ha='center', va='bottom')
        # make the window width bigger to fit the text
        width = 5 + len(maps) * 2
        fig.set_size_inches(width, 5)
        # write the time taken for each map on the x axis
        # use only first 2 decimal digits
        for i in range(len(maps)):
            # make the text white
            ax.text(x[i], 74, f"{time_taken[i]:.2f}s", ha='center', va='top', color='white')
        # make background black
        fig.patch.set_facecolor('black')
        ax.set_facecolor('black')
        # make the grid white
        ax.grid(color='white')
        # make the ticks white
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')
        # make the title white
        ax.title.set_color('white')
        # make the labels white
        ax.xaxis.label.set_color('white')
        ax.yaxis.label.set_color('white')
        # make the ticks bigger
        ax.tick_params(axis='x', labelsize=15)
        ax.tick_params(axis='y', labelsize=15)
        # make the title bigger
        ax.title.set_size(20)

        plt.show(block=False)

    def plot_one_alg_one_map_one_heuristic(self, algorithm: str, heuristic: str, num_nudes_visited: int, time_taken: float, map_name: str):
        """
        Plot the number of nodes visited for one map with one algorithm and one heuristic.
        """
        # create plot
        import matplotlib.pyplot as plt
        import numpy as np
        # create a bar chart with the number of nodes visited for each map
        x = np.arange(1)
        fig, ax = plt.subplots()
        bars = ax.bar(x, num_nudes_visited, color=['blue'])
        ax.set_xticks(x)
        ax.set_xticklabels([map_name])
        ax.set_ylabel('Number of nodes visited')
        ax.set_title(f'Number of nodes visited for {algorithm} with {heuristic}')
        # add value to each bar
        for bar in bars:
            yval = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2, yval, int(yval), ha='center', va='bottom')

        # write the time taken for each map on the x axis
        # use only first 2 decimal digits
        for i in range(len(x)):
            # make the text white
            ax.text(x[i], 0, f"{time_taken:.2f}s", ha='center', va='top', color='white')
        # make background black
        fig.patch.set_facecolor('black')
        ax.set_facecolor('black')
        # make the grid white
        ax.grid(color='white')
        # make the ticks white
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')
        # make the title white
        ax.title.set_color('white')
        # make the labels white
        ax.xaxis.label.set_color('white')
        ax.yaxis.label.set_color('white')
        # make the ticks bigger
        ax.tick_params(axis='x', labelsize=15)
        ax.tick_params(axis='y', labelsize=15)
        plt.show(block=False)

    def close_all_plots(self):
        """
        Close all plots.
        """
        import matplotlib.pyplot as plt
        plt.close('all')
