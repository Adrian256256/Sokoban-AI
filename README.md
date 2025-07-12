# Sokoban AI Solver: Beam Search & LRTA\*

A project for solving the Sokoban puzzle game using Beam Search and LRTA* algorithms. Includes a customizable test interface (terminal and GUI), various heuristic strategies, and comparative performance analysis.

---

## 📁 Implemented Files

- `lrta_star.py` – LRTA* algorithm implementation.
- `beam_search.py` – Beam Search algorithm implementation.
- `heuristics.py` – Contains all heuristic functions.
- `solver.py` – Functions to run the solvers and generate comparison graphs.
- `main.py` – Provides both terminal and GUI interfaces for running tests.

---

## 🚀 How to Use

### ✅ Run in Terminal

```bash
python3 main.py
```

In `main.py`, comment/uncomment the appropriate function at the bottom:
- `use_graphic_interface()` – for GUI
- `use_terminal_interface()` – for CLI

### 🧪 Terminal Options
You'll see an interactive menu with the following options:

1. Run Beam Search with **all heuristics** on a specified map  
2. Run LRTA* with **all heuristics** on a specified map  
3. Run Beam Search with a **specific heuristic** on **all maps**  
4. Run LRTA* with a **specific heuristic** on **all maps**  
5. Custom test with **chosen map, heuristic, and algorithm**

Input names for maps (e.g., `easy_map1`) and heuristics (e.g., `manhattan_heuristic`) as prompted.

---

### 🖼 GUI Interface

The graphical interface allows the same functionalities via buttons and dropdowns:
- Select map, heuristic, and algorithm
- Run full tests or custom configurations
- Option to close the app

---

## 🔧 Modifications to `apply_move`

The function now counts:
- `push_count` – when the player pushes a box
- `pull_count` – when the player pulls a box

These counters are logged in the terminal during algorithm execution.

---

## 🧠 Implemented Heuristics

1. **Manhattan Distance** (`manhattan_heuristic`)  
2. **Euclidean Distance** (`euclidian_heuristic`)  
3. **Minimum Euclidean Distance** (`minimum_euclidian`)  
4. **Minimum Manhattan Distance** (`minimum_manhattan`)  
5. **Combined Heuristic** (`combined_heuristic`) – Considers player-to-box distances, blockages, and penalties.

---

## 📊 Comparative Analysis

### ✅ LRTA* vs Beam Search

- **Beam Search** generally provides better path quality.
- **LRTA*** performs faster but explores fewer paths.
- Heuristics like `minimum_*` perform poorly in LRTA* but better in Beam Search.
- `combined_heuristic` shows strong performance on large maps in Beam Search.

Performance metrics include:
- Number of visited nodes
- Push/Pull move counts
- Runtime

---
