# Project ReadMe
## 1.	Environment Setup: 
This project will use Ubuntu running on a Virtual Machine. The language used is Python, with emacs as the text editor.
a)	Installing VirtualBox to run Ubuntu was straightforward
b)	Installing Ubuntu was very time consuming since it wouldn’t work at all and be stuck at the loading screen. Tinkering the settings eventually fixed it.
c)	Learning terminal commands was not too hard, and the project does not use a lot of Terminal commands to begin with.
d)	Installing and running the Python package and updated libraries/emacs through Terminal on Ubuntu was a very novel experience but reasonably straightforward.
## 2.	Discovering PyGame
It seemed important to review PyGame documentation before implementing algorithms, since both Python and PyGame are unfamiliar to me. The library already contains comprehensive function sets(modules) like draw, display, Rect that are used in the project.
### Pygame library functions used:
a)	init() : initializes pygame modules(like display.init())
b)	display.set_mode(): initialize window or screen. Size(a,b) takes in a pair of numbers a and b signifying the width and height. 
c)	time.Clock(): creates Clock object to track time
d)	draw.rect: draws a rectangle. Args: surface, color, rect
e)	draw.line: 
f)	key.get_pressed(): get state of keyboard  buttons
## 3.	Deciding the algorithms:
After some research I found that A* algorithm is basically the industry standard so I decided to go with that. Ideally I would implement more and test them out to compare efficiency but due to time constraints I was unable to.
## 4.	Use of ChatGPT: 
AI was used as an enhanced and efficient Google search. It was able to suggest and explain the logic behind established pathfinding algorithms and implement code in the language of my choice(Java). Then I typed a query to implement an example of an A* algorithm in Python, and also an explanation about how to do so. Based on those results, I typed in my code in the project which ultimately I was not able to make work. From ChatGPT:

The A* algorithm is a popular pathfinding algorithm that uses heuristics to find the shortest path between two points in a graph. Here's a step-by-step explanation of how to implement the A* algorithm in Python:
1.	Define a Node class to represent each node in the graph. Each node should have attributes such as its coordinates, the cost to reach it from the start node (g score), the estimated cost to reach the target node (h score), and the total cost (f score) which is the sum of g and h scores. It should also have a list of neighboring nodes.
2.	Implement a heuristic function, often denoted as h(n), which estimates the cost from a given node n to the target node. This function should return a numerical value representing the estimated cost.
3.	Implement a function to reconstruct the path from the start node to the target node once the algorithm has found the target. This function should trace back the previous node attribute starting from the target node until it reaches the start node, and build a list of nodes in reverse order.
4.	Create an empty open set (priority queue) to store the nodes to be evaluated. The nodes in the open set are ordered based on their total cost (f score), with the lowest cost node being the highest priority.
5.	Initialize the g score and f score of all nodes as infinity except for the start node, which is set to 0. Set the h score of all nodes as the heuristic value from each node to the target node.
6.	Add the start node to the open set.
7.	While the open set is not empty, do the following steps:
•	Get the node with the lowest f score from the open set. If there are nodes with equal f scores, use a tiebreaker such as choosing the node with the lowest h score.
•	If the current node is the target node, reconstruct the path and return it.
•	For each neighboring node of the current node:
•	Calculate the tentative g score by adding the cost of moving from the current node to the neighboring node (usually a constant value of 1) to the g score of the current node.
•	If the tentative g score is lower than the g score of the neighboring node, update the g score, f score, and set the previous node of the neighboring node to the current node.
•	If the neighboring node is not in the open set, add it to the open set.
8.	If the open set becomes empty and the target node has not been reached, there is no path from the start node to the target node.
That's the basic outline of implementing the A* algorithm. You can incorporate these steps into your code and customize it based on your specific requirements and graph representation.

The A* algorithm combines elements of both Dijkstra's algorithm and a heuristic search to efficiently find the shortest path between two nodes in a graph. Here's a breakdown of the logic behind the A* algorithm:
1.	The algorithm maintains two main pieces of information for each node:
•	g score: the cost of reaching a particular node from the start node. This value is initialized as infinity for all nodes except the start node, which is set to 0.
•	h score: the estimated cost to reach the target node from a particular node. This is calculated using a heuristic function that provides an optimistic estimate of the remaining cost. The heuristic function should be admissible, meaning it never overestimates the actual cost.
2.	The algorithm uses a priority queue (often implemented as a min-heap) called the open set to keep track of nodes that need to be evaluated. Nodes in the open set are ordered based on their total score, which is the sum of g score and h score.
3.	The A* algorithm starts by adding the start node to the open set with a total score of 0. This node becomes the current node.
4.	While the open set is not empty, the algorithm continues to explore nodes:
•	Select the node with the lowest total score from the open set as the current node.
•	If the current node is the target node, the algorithm terminates as the shortest path has been found. It then reconstructs the path from the target node to the start node using the previous pointers stored in each node.
•	If the current node is not the target node, the algorithm expands its neighboring nodes:
•	For each neighboring node, calculate a tentative g score by adding the cost of moving from the current node to the neighboring node.
•	If the tentative g score is lower than the current g score of the neighboring node, update the g score of the neighboring node to the tentative g score. This means a better path to that neighboring node has been found.
•	Calculate the total score (f score) of the neighboring node by adding its g score and h score.
•	If the neighboring node is not in the open set, add it to the open set. If it is already in the open set, update its position in the priority queue based on the new total score.
•	Once all the neighboring nodes have been evaluated, mark the current node as closed (visited) to avoid revisiting it.
5.	If the open set becomes empty before reaching the target node, it means there is no valid path from the start node to the target node. The algorithm terminates without finding a path.
The A* algorithm's efficiency lies in its ability to prioritize nodes for evaluation based on their total score (f score). By considering both the cost from the start node (g score) and the estimated cost to reach the target node (h score), A* intelligently explores nodes that are likely to lead to the shortest path. The heuristic function plays a crucial role in guiding the search by providing a good estimate of the remaining cost.
By combining the benefits of Dijkstra's algorithm (finding the shortest path) and a heuristic search (guiding the exploration), the A* algorithm can efficiently find optimal paths in various graph-based problems, such as pathfinding in games or route planning in maps.
