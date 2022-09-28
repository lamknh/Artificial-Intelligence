# Artificial-Intelligence
2022 ss 인공지능 과제

# Question 1 (3 points) : Finding a Fixed Food Dot using Depth First Search!

### b. Description of DFS Implementation

DFS is implemented using a recursive function, or stack. Therefore, for this project, I used stacks to implement using the given util from the project. After declaring Stack, find the start state and put it in the stack. Then, declare a visited array to check whether to visit or not, and then put a start state/point in the visited array. This is to continue DFS Search thinking that the first starting point has already been visited. It then declares a path dictionary that stores the path that the real Pacman will take. The reason for declaring Paths as a dictionary rather than an array is to use the function getSuccessors to find adjacent nodes of a node, which returns three values (successor, action, stepCost) and uses the dictionary to use these various values.

Proceed with DFS using the While statement. The framework of the existing DFS code has been used and ends when the Goal State is reached. Otherwise, neighboring nodes of the current node are obtained using the getSuccessors function. If there is a neighbor, all of the neighboring nodes are searched using the for statement. If the neighboring node is not visited, it is a path that can be moved, so it is a path that can be moved forward, so it is put in the stack so that it continues to find the next path. And the path is stored in the path, and the corresponding successor is stored in the stack to continue with DFS to find the way to the goal.


### c. Experimental Results

![image](https://user-images.githubusercontent.com/54229039/192667749-1741d009-9f27-4635-b902-6ba7e2464af1.png)

# Question 2 (7 points): A* search!

### - Description of Implementation
The basic principle is the same as DFS, but DFS uses a stack, whereas A* Search uses Priority Queue because it needs to find a case with the largest expected value from the current position to the position of goal. Max Heap can be easily implemented using the Priority Queue. To sort this Max Heap, you need to get Cost. To find the Cost, we need to find the largest distance possible for the heuristic that should be admissible. Like DFS, statements are used to navigate all neighboring nodes, and heuristics are used to find and add the cost from the current position to the goal. Then, put this cost into the Priority Queue and do a Heap Sort to proceed with the A* search.

The difference in performance according to Heuristics depends on how to assume the distance of each vector point. If Manhattan Distance is the sum of the differences between the absolute values on the coordinates of the distance between the two points, Euclidean Distance calculates the linear distance between the two points.

<img width="400" alt="image" src="https://user-images.githubusercontent.com/54229039/192668343-c14234f9-edcf-471b-b33c-72a2dc22747c.png">

### b. New heuristic function
- Method (description of the proposed function)
The first new Heuristic function I tried to make was implemented by referring to Chebyshev Distance.
<img width="400" alt="image" src="https://user-images.githubusercontent.com/54229039/192668196-365f6bb2-2ab4-4028-bde6-40f404a86931.png">

If Manhattan Distance is the sum of the differences between the absolute values on the coordinates of the distance between the two points, Euclidean Distance calculates the linear distance between the two points. On the other hand, Chebyshev Distance differs in processing all eight adjacent cells from one point at the same distance. Since the movement of the Pacman is done in units of compartments while thinking about devising heuristics, I thought that implementing heuristics using Chebyshev Distance would be able to calculate the cost in consideration of the characteristics of the game.

### c. Evaluation of the effectiveness of the heuristic functions!
- Experimental Results (Manhattan vs Euclidean vs new function)
![image](https://user-images.githubusercontent.com/54229039/192667972-f866486f-aa24-4736-9975-1c36b35db91b.png)
![image](https://user-images.githubusercontent.com/54229039/192668035-78fdbfb6-5f03-455a-8571-64af26c0f2ff.png)

