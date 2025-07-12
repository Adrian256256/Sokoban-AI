import math
from sokoban.box import Box
from sokoban.map import Map

class Heuristic:
    """
    Base class for heuristics.
    """
    def manhattan_heuristic(map: Map) -> int:
        """
        Heuristic function for Sokoban.
        Calculates the Manhattan distance between boxes and their closest targets.
        """
        total_distance = 0
        for box in map.boxes.values():
            for target in map.targets:
                distance = abs(box.x - target[0]) + abs(box.y - target[1])
                total_distance += distance
        return total_distance
    
    def euclidian_heuristic(map: Map) -> int:
        """
        Heuristic function for Sokoban.
        Calculates the Euclidean distance between boxes and their closest targets.
        """
        total_distance = 0
        for box in map.boxes.values():
            for target in map.targets:
                distance = math.sqrt((box.x - target[0])**2 + (box.y - target[1])**2)
                total_distance += distance
        return total_distance
    
    def minimum_euclidian(map: Map) -> int:
        """
        Heuristic function for Sokoban.
        Calculates the minimum Euclidean distance between boxes and their closest targets.
        """
        minimum_distance = 0
        for box in map.boxes.values():
            for target in map.targets:
                distance = math.sqrt((box.x - target[0])**2 + (box.y - target[1])**2)
                if distance < minimum_distance:
                    minimum_distance = distance
        return minimum_distance
    
    def minimum_manhattan(map: Map) -> int:
        """
        Heuristic function for Sokoban.
        Calculates the minimum Manhattan distance between boxes and their closest targets.
        """
        minimum_distance = 0
        for box in map.boxes.values():
            for target in map.targets:
                distance = abs(box.x - target[0]) + abs(box.y - target[1])
                if distance < minimum_distance:
                    minimum_distance = distance
        return minimum_distance
    
    @staticmethod
    def is_box_blocked(map: Map, box: Box) -> bool:
        """
        Check if a box is blocked (in a corner, not on a target).
        """
        x, y = box.x, box.y
        # Check if the box is in a corner, not on a target
        if (x, y) not in map.targets:
            if ((x - 1, y) in map.obstacles and (x + 1, y) in map.obstacles):
                return True
            if ((x, y - 1) in map.obstacles and (x, y + 1) in map.obstacles):
                return True
        return False
    
    @staticmethod
    def combined_heuristic(map: Map) -> int:
        """
        Improved heuristic function for Sokoban.
        Combines multiple factors:
        - Total Manhattan distance between boxes and targets.
        - Penalization for blocked boxes.
        - Penalization for boxes blocking other boxes.
        - Distance between the player and the closest box.
        """
        total_distance = 0
        blocked_penalty = 50  # penalization for blocked boxes
        blocking_penalty = 50  # penalization for boxes blocking other boxes
        player_distance_weight = 3  # weight the distance between player and closest box

        # Calculate minimum Manhattan distance for each box
        for box in map.boxes.values():
            for target in map.targets:
                distance = abs(box.x - target[0]) + abs(box.y - target[1])
                total_distance += distance

            # Penalize blocked boxes
            if Heuristic.is_box_blocked(map, box):
                total_distance += blocked_penalty

            # Penalize if the box blocking other boxes
            if Heuristic.is_box_blocking_bad_placed(map, box):
                total_distance += blocking_penalty

        # get minimum distance between player and a box
        min_player_distance = float('inf')
        for box in map.boxes.values():
            distance = abs(map.player.x - box.x) + abs(map.player.y - box.y)
            if distance < min_player_distance:
                min_player_distance = distance

        # add the distance between player and box to the total distance
        total_distance += player_distance_weight * min_player_distance

        return total_distance

    @staticmethod
    def is_box_blocking_bad_placed(map: Map, box: Box) -> bool:
        """
        Check if a box is blocking access to other boxes or targets.
        """
        x, y = box.x, box.y
        # Check if the box is adjacent to another box or target and blocks access
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (x + dx, y + dy)
            if neighbor in map.boxes:
                # Check if the neighbour box is on a target
                if (x + dx, y + dy) in map.targets:
                    continue
                # Check if the neighbor box is blocked by this box
                x_neighbor, y_neighbor = map.boxes[neighbor].x, map.boxes[neighbor].y
                # if x and y are on the left of the neighbour, and the neighbour has up or down AND right with an obstacle or other box,
                # then the box is blocking the neighbour
                # if i am on the left
                if (x < x_neighbor and y == y_neighbor):
                    # check if the neighbour has up or down AND right with an obstacle or other box
                    if (x_neighbor, y_neighbor - 1) in map.obstacles or (x_neighbor, y_neighbor - 1) in map.boxes:
                        # check if the right is an obstacle or other box
                        if (x_neighbor + 1, y_neighbor) in map.obstacles or (x_neighbor + 1, y_neighbor) in map.boxes:
                            return True
                # if i am on the right
                if (x > x_neighbor and y == y_neighbor):
                    # check if the neighbour has up or down AND left with an obstacle or other box
                    if (x_neighbor, y_neighbor - 1) in map.obstacles or (x_neighbor, y_neighbor - 1) in map.boxes:
                        # check if the left is an obstacle or other box
                        if (x_neighbor - 1, y_neighbor) in map.obstacles or (x_neighbor - 1, y_neighbor) in map.boxes:
                            return True
                # if i am on the uper side
                if (x == x_neighbor and y < y_neighbor):
                    # check if the neighbour has left or right AND down with an obstacle or other box
                    if (x_neighbor - 1, y_neighbor) in map.obstacles or (x_neighbor - 1, y_neighbor) in map.boxes:
                        # check if the down is an obstacle or other box
                        if (x_neighbor, y_neighbor + 1) in map.obstacles or (x_neighbor, y_neighbor + 1) in map.boxes:
                            return True
                # if i am on the down side
                if (x == x_neighbor and y > y_neighbor):
                    # check if the neighbour has left or right AND up with an obstacle or other box
                    if (x_neighbor - 1, y_neighbor) in map.obstacles or (x_neighbor - 1, y_neighbor) in map.boxes:
                        # check if the up is an obstacle or other box
                        if (x_neighbor, y_neighbor - 1) in map.obstacles or (x_neighbor, y_neighbor - 1) in map.boxes:
                            return True
        return False
