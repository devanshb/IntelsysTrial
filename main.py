from collections import deque

import pygame
import random
import math

# Constants
WIDTH = 800  # Width of the grid
HEIGHT = 600  # Height of the grid
GRID_SIZE = 20  # Size of each grid cell
NUM_ROWS = HEIGHT // GRID_SIZE
NUM_COLS = WIDTH // GRID_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


class Rover:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def draw(self):
        pygame.draw.rect(screen, BLUE, (self.x * GRID_SIZE, self.y * GRID_SIZE, GRID_SIZE, GRID_SIZE))


class Obstacle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.rect(screen, RED, (self.x * GRID_SIZE, self.y * GRID_SIZE, GRID_SIZE, GRID_SIZE))


class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.parent = None
        self.g = 0  # Cost from start node to current node
        self.h = 0  # Heuristic (estimated cost from current node to goal node)
        self.f = 0  # Total cost (g + h)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


def heuristic(node, goal):
    return math.sqrt((goal.x - node.x) ** 2 + (goal.y - node.y) ** 2)


def get_neighboring_nodes(node):
    neighbors = []
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            new_x = node.x + dx
            new_y = node.y + dy
            if 0 <= new_x < NUM_COLS and 0 <= new_y < NUM_ROWS:
                neighbors.append(Node(new_x, new_y))
    return neighbors


def a_star_search(start, goal, obstacles):
    open_list = [start]
    closed_list = []

    while open_list:
        current_node = open_list[0]
        current_index = 0

        for index, node in enumerate(open_list):
            if node.f < current_node.f:
                current_node = node
                current_index = index

        open_list.pop(current_index)
        closed_list.append(current_node)

        if current_node == goal:
            path = []
            current = current_node
            while current:
                path.append((current.x, current.y))
                current = current.parent
            return path[::-1]  # Return reversed path

        neighbors = get_neighboring_nodes(current_node)

        for neighbor in neighbors:
            if neighbor in closed_list or Obstacle(neighbor.x, neighbor.y) in obstacles:
                continue

            tentative_g = current_node.g + 1  # Assuming the cost between adjacent nodes is 1

            if neighbor in open_list:
                if tentative_g < neighbor.g:
                    neighbor.g = tentative_g
                    neighbor.parent = current_node
            else:
                neighbor.g = tentative_g
                neighbor.h = heuristic(neighbor, goal)
                neighbor.f = neighbor.g + neighbor.h
                neighbor.parent = current_node
                open_list.append(neighbor)

    return None  # No path found


def draw_grid():
    for x in range(0, WIDTH, GRID_SIZE):
        pygame.draw.line(screen, BLACK, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, BLACK, (0, y), (WIDTH, y))


def generate_obstacles(num_obstacles):
    obstacles = []
    for _ in range(num_obstacles):
        x = random.randint(0, NUM_COLS - 1)
        y = random.randint(0, NUM_ROWS - 1)
        obstacles.append(Obstacle(x, y))
    return obstacles


def is_collision(rover, obstacles):
    for obstacle in obstacles:
        if rover.x == obstacle.x and rover.y == obstacle.y:
            return True
    return False


def main():
    rover = Rover(0, 0)
    obstacles = generate_obstacles(50)

    start_node = Node(rover.x, rover.y)
    goal_node = Node(NUM_COLS - 1, NUM_ROWS - 1)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        keys = pygame.key.get_pressed()
        dx, dy = 0, 0
        if keys[pygame.K_LEFT]:
            dx = -1
        elif keys[pygame.K_RIGHT]:
            dx = 1
        elif keys[pygame.K_UP]:
            dy = -1
        elif keys[pygame.K_DOWN]:
            dy = 1

        new_x = rover.x + dx
        new_y = rover.y + dy
        if 0 <= new_x < NUM_COLS and 0 <= new_y < NUM_ROWS and not is_collision(Rover(new_x, new_y), obstacles):
            rover.move(dx, dy)

        screen.fill(WHITE)
        draw_grid()

        # Run A* search
        path = a_star_search(start_node, goal_node, obstacles)

        for obstacle in obstacles:
            obstacle.draw()
        rover.draw()

        if path:
            # Draw the path
            for node in path:
                pygame.draw.rect(screen, GREEN, (node[0] * GRID_SIZE, node[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

        pygame.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    main()