from sokoban import (
    Box,
    DOWN,
    Map,
    Player
)
from search_methods.solver import Solver
import tkinter as tk
from tkinter import ttk

# Structure where all map names are stored
maps = {
    'easy_map1': 'tests/easy_map1.yaml',
    'easy_map2': 'tests/easy_map2.yaml',
    'medium_map1': 'tests/medium_map1.yaml',
    'medium_map2': 'tests/medium_map2.yaml',
    'large_map1': 'tests/large_map1.yaml',
    'large_map2': 'tests/large_map2.yaml',
    'hard_map1': 'tests/hard_map1.yaml',
    'hard_map2': 'tests/hard_map2.yaml',
    'super_hard_map1': 'tests/super_hard_map1.yaml',
}

heuristics = [
    'manhattan_heuristic',
    'euclidian_heuristic',
    'minimum_euclidian',
    'minimum_manhattan',
    'combined_heuristic',
]

algorithms = ['Beam_Search', 'LRTA_star']

def run_beam_search_all_heuristics(given_map_name):
    """
    Run the beam search algorithm with all heuristics.
    """
    counts = []
    times = []
    for heuristic in heuristics:
        # check if count is 0, then the algorithm failed
        count, time_taken = solver.run_search_algorithm('Beam_Search', heuristic, given_map_name)
        if count == 0:
            print(f"Beam Search with {heuristic} failed on {given_map_name}.")
        counts.append(count)
        times.append(time_taken)
    # plot the results using solver plot_one_alg_multiple_heuristics
    solver.plot_one_alg_multiple_heuristics('Beam_Search', heuristics, counts, times, given_map_name)

def run_lrta_star_all_heuristics(given_map_name):
    """
    Run the LRTA* algorithm with all heuristics.
    """
    counts = []
    times = []
    for heuristic in heuristics:
        count, time_taken = solver.run_search_algorithm('LRTA_star', heuristic, given_map_name)
        counts.append(count)
        times.append(time_taken)
    solver.plot_one_alg_multiple_heuristics('LRTA_star', heuristics, counts, times, given_map_name)

def run_beam_search_all_maps(heuristic):
    """
    Run the beam search algorithm with a specific heuristic and all maps.
    """
    counts = []
    times = []
    for map_name in maps:
        count, time_taken = solver.run_search_algorithm('Beam_Search', heuristic, maps[map_name])
        if count == 0:
            print(f"Beam Search with {heuristic} failed on {map_name}.")
        counts.append(count)
        times.append(time_taken)
    solver.plot_one_alg_multiple_maps('Beam_Search', heuristic, counts, times, maps.keys())

def run_lrta_star_all_maps(heuristic):
    """
    Run the LRTA* algorithm with a specific heuristic and all maps.
    """
    counts = []
    times = []
    for map_name in maps:
        count, time_taken = solver.run_search_algorithm('LRTA_star', heuristic, maps[map_name])
        if count == 0:
            print(f"LRTA* with {heuristic} failed on {map_name}.")
        counts.append(count)
        times.append(time_taken)
    solver.plot_one_alg_multiple_maps('LRTA_star', heuristic, counts, times, maps.keys())

def run_specific_test(map_name, heuristic, algorithm):
    """
    Run a specific test with the given map name, heuristic and algorithm.
    """
    count, time_taken = solver.run_search_algorithm(algorithm, heuristic, maps[map_name])
    solver.plot_one_alg_one_map_one_heuristic(algorithm, heuristic, count, time_taken, map_name)

def open_specific_test_window(root):
    """
    Open a new window to select the specific test parameters.
    """
    # create a new window
    specific_test_window = tk.Toplevel(root)
    specific_test_window.title("Run Specific Test")
    specific_test_window.geometry("400x300")
    specific_test_window.resizable(False, False)

    # create a label for the map name
    map_label = tk.Label(specific_test_window, text="Select Map:", font=("Arial", 12))
    map_label.pack(pady=10)

    # create a combobox for the map names
    map_combobox = ttk.Combobox(specific_test_window, values=list(maps.keys()), state="readonly")
    map_combobox.pack(pady=5)

    # create a label for the heuristic
    heuristic_label = tk.Label(specific_test_window, text="Select Heuristic:", font=("Arial", 12))
    heuristic_label.pack(pady=10)

    # create a combobox for the heuristics
    heuristic_combobox = ttk.Combobox(specific_test_window, values=heuristics, state="readonly")
    heuristic_combobox.pack(pady=5)

    # create a label for the algorithm
    algorithm_label = tk.Label(specific_test_window, text="Select Algorithm:", font=("Arial", 12))
    algorithm_label.pack(pady=10)

    # create a combobox for the algorithms
    algorithm_combobox = ttk.Combobox(specific_test_window, values=algorithms, state="readonly")
    algorithm_combobox.pack(pady=5)

    # preselect the first map, heuristic and algorithm
    map_combobox.current(0)
    heuristic_combobox.current(0)
    algorithm_combobox.current(0)

    # create a button to run the test
    run_button = tk.Button(specific_test_window, text="Run Test", command=lambda: run_specific_test(map_combobox.get(), heuristic_combobox.get(), algorithm_combobox.get()))
    run_button.pack(pady=20)

def use_graphic_interface():
    """
    Create a graphic interface to run the tests.
    """
    def run_beam_search_all_heuristics_selected_map():
        # create a new window to select the map
        map_window = tk.Toplevel(root)
        map_window.title("Select Map")
        map_window.geometry("300x200")
        map_window.resizable(False, False)
        # create a label for the map
        map_label = tk.Label(map_window, text="Select Map:", font=("Arial", 12))
        map_label.pack(pady=10)
        # create a combobox for the maps
        map_combobox = ttk.Combobox(map_window, values=list(maps.keys()), state="readonly")
        map_combobox.pack(pady=5)
        # preselect the first map
        map_combobox.current(0)
        # create a button to run the test
        run_button = tk.Button(map_window, text="Run Test", command=lambda: [run_beam_search_all_heuristics(maps[map_combobox.get()]), map_window.destroy()])
        run_button.pack(pady=20)
        # close the window when the test is done
        map_window.protocol("WM_DELETE_WINDOW", lambda: map_window.destroy())

    def run_lrta_star_all_heuristics_selected_map():
        # create a new window to select the map
        map_window = tk.Toplevel(root)
        map_window.title("Select Map")
        map_window.geometry("300x200")
        map_window.resizable(False, False)
        # create a label for the map
        map_label = tk.Label(map_window, text="Select Map:", font=("Arial", 12))
        map_label.pack(pady=10)
        # create a combobox for the maps
        map_combobox = ttk.Combobox(map_window, values=list(maps.keys()), state="readonly")
        map_combobox.pack(pady=5)
        # preselect the first map
        map_combobox.current(0)
        # create a button to run the test
        run_button = tk.Button(map_window, text="Run Test", command=lambda: [run_lrta_star_all_heuristics(maps[map_combobox.get()]), map_window.destroy()])
        run_button.pack(pady=20)
        # close the window when the test is done
        map_window.protocol("WM_DELETE_WINDOW", lambda: map_window.destroy())

    def run_beam_search_with_heuristic():
        # create a new window to select the heuristic
        heuristic_window = tk.Toplevel(root)
        heuristic_window.title("Select Heuristic")
        heuristic_window.geometry("300x200")
        heuristic_window.resizable(False, False)
        # create a label for the heuristic
        heuristic_label = tk.Label(heuristic_window, text="Select Heuristic:", font=("Arial", 12))
        heuristic_label.pack(pady=10)
        # create a combobox for the heuristics
        heuristic_combobox = ttk.Combobox(heuristic_window, values=heuristics, state="readonly")
        heuristic_combobox.pack(pady=5)
        # preselect the first heuristic
        heuristic_combobox.current(0)
        # create a button to run the test
        run_button = tk.Button(heuristic_window, text="Run Test", command=lambda: [run_beam_search_all_maps(heuristic_combobox.get()), heuristic_window.destroy()])
        run_button.pack(pady=20)
        # close the window when the test is done
        heuristic_window.protocol("WM_DELETE_WINDOW", lambda: heuristic_window.destroy())

    def run_lrta_star_with_heuristic():
        # create a new window to select the heuristic
        heuristic_window = tk.Toplevel(root)
        heuristic_window.title("Select Heuristic")
        heuristic_window.geometry("300x200")
        heuristic_window.resizable(False, False)
        # create a label for the heuristic
        heuristic_label = tk.Label(heuristic_window, text="Select Heuristic:", font=("Arial", 12))
        heuristic_label.pack(pady=10)
        # create a combobox for the heuristics
        heuristic_combobox = ttk.Combobox(heuristic_window, values=heuristics, state="readonly")
        heuristic_combobox.pack(pady=5)
        # preselect the first heuristic
        heuristic_combobox.current(0)
        # create a button to run the test
        run_button = tk.Button(heuristic_window, text="Run Test", command=lambda: [run_lrta_star_all_maps(heuristic_combobox.get()), heuristic_window.destroy()])
        run_button.pack(pady=20)
        # close the window when the test is done
        heuristic_window.protocol("WM_DELETE_WINDOW", lambda: heuristic_window.destroy())

    # create a window for Sokoban Solver
    root = tk.Tk()
    root.title("Sokoban Solver")
    root.geometry("800x600")
    root.resizable(False, False)

    root.configure(bg="#f0f0f0")
    # create a frame for the title
    title_frame = tk.Frame(root, bg="#4CAF44")
    title_frame.pack(pady=10)
    title_label = tk.Label(title_frame, text="Sokoban Solver", font=("Arial", 24), bg="#f0f0f0")
    title_label.pack()
    # create a frame for the buttons
    button_frame = tk.Frame(root, bg="#f0f0f0")
    button_frame.pack(pady=10)
    # create a button for each test
    beam_search_all_heuristics_button = tk.Button(button_frame, text="Run Beam Search with all heuristics on given map", command=run_beam_search_all_heuristics_selected_map, width=60, height=2, bg="#4CAF50", fg="white", font=("Arial", 14))
    beam_search_all_heuristics_button.pack(pady=5)
    lrta_star_all_heuristics_button = tk.Button(button_frame, text="Run LRTA* with all heuristics on given map", command=run_lrta_star_all_heuristics_selected_map, width=60, height=2, bg="#4CAF50", fg="white", font=("Arial", 14))
    lrta_star_all_heuristics_button.pack(pady=5)
    beam_search_all_maps_button = tk.Button(button_frame, text="Run Beam Search with given heuristic on all maps", command=run_beam_search_with_heuristic, width=60, height=2, bg="#4CAF50", fg="white", font=("Arial", 14))
    beam_search_all_maps_button.pack(pady=5)
    lrta_star_all_maps_button = tk.Button(button_frame, text="Run LRTA* with given heuristic on all maps", command=run_lrta_star_with_heuristic, width=60, height=2, bg="#4CAF50", fg="white", font=("Arial", 14))
    lrta_star_all_maps_button.pack(pady=5)
    # create a button for the specific test
    specific_test_button = tk.Button(button_frame, text="Run specific test", command=lambda: open_specific_test_window(root), width=60, height=2, bg="#4CAF50", fg="white", font=("Arial", 14))
    specific_test_button.pack(pady=5)
    # create close button
    close_button = tk.Button(button_frame, text="Close", command=root.quit, width=60, height=2, bg="#f44336", fg="white", font=("Arial", 14))
    close_button.pack(pady=5)

    # if the window is closed, close all plots
    def on_closing():
        solver.close_all_plots()
        root.destroy()
    
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()
    
def use_terminal_interface():
    """
    Create a terminal interface to run the tests.
    """
    # read from input what tests to do
    print("1. Run beam search with all heuristics on given map")
    print("2. Run LRTA* with all heuristics on given map")
    print("3. Run beam search with given heuristic on all maps")
    print("4. Run LRTA* with given heuristic on all maps")
    print("5. Run specific algorithm, specific map, specific heuristic")
    number = input("Enter the number of the test you want to run: ")
    if number == '1':
        # print all map names
        print("Available maps:")
        for map_name in maps:
            print(map_name)
        # read from input map name
        map_name = input("Enter the name of the map: ")
        while (map_name not in maps):
            map_name = input("Invalid map name. Try again: ")
        run_beam_search_all_heuristics(maps[map_name])
    elif number == '2':
        # print all map names
        print("Available maps:")
        for map_name in maps:
            print(map_name)
        # read from input map name
        map_name = input("Enter the name of the map: ")
        while (map_name not in maps):
            map_name = input("Invalid map name. Try again: ")
        run_lrta_star_all_heuristics(maps[map_name])
    elif number == '3':
        # print all heuristics
        print("Available heuristics:")
        for heuristic in heuristics:
            print(heuristic)
        # read from input the heuristic to use
        heuristic = input("Enter the heuristic to use: ")
        while (heuristic not in heuristics):
            heuristic = input("Invalid heuristic. Try again: ")
        run_beam_search_all_maps(heuristic)
    elif number == '4':
        # print all heuristics
        print("Available heuristics:")
        for heuristic in heuristics:
            print(heuristic)
        # read from input the heuristic to use
        heuristic = input("Enter the heuristic to use: ")
        while (heuristic not in heuristics):
            heuristic = input("Invalid heuristic. Try again: ")
        run_lrta_star_all_maps(heuristic)
    elif number == '5':
        # print all map names
        print("Available maps:")
        for map_name in maps:
            print(map_name)
        map_name = input("Enter the name of the map: ")
        while (map_name not in maps):
            map_name = input("Invalid map name. Try again: ")
        # print all heuristics
        print("Available heuristics:")
        for heuristic in heuristics:
            print(heuristic)
        heuristic = input("Enter the name of the heuristic: ")
        while (heuristic not in heuristics):
            heuristic = input("Invalid heuristic name. Try again: ")
        # print all algorithms
        print("Available algorithms:")
        for algorithm in algorithms:
            print(algorithm)
        algorithm = input("Enter the name of the algorithm: ")
        while (algorithm not in algorithms):
            algorithm = input("Invalid algorithm name. Try again: ")
        run_specific_test(map_name, heuristic, algorithm)
    else:
        print("Invalid input. Please enter a number between 1 and 6.")

    # wait for enter key to exit
    input("Press enter to exit...")


if __name__ == '__main__':
    solver = Solver()

    # uncomment to use terminal interface
    use_terminal_interface()

    # uncomment to use graphic interface
    # use_graphic_interface()

    