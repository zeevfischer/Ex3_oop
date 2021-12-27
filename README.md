# Directed Weighted Graph

### **Explanation**
---

authors: zeev fischer and liav levi.  
following last week's assignment this week was python implementing most of the algorithms from last week such a Dijkstra's algorithm getting paths on a graph and more but in python.  

for more information on the comparison between the tew projects a wiki link is provided  
https://github.com/zeevfischer/Ex3_oop/wiki

For starters, we had tew interfaces to implement the following interfaces  
* GraphInterface – represents the actual Graph 
* GraphAlgoInterface – this interface has all sorts of function that can be implemented on a graph  
A more detailed uml of all the classes will be shown at the bottom 

### **_DirectedWeightedGrapg_**  
#### Complex Functions:  

**removeNode():**    
by removing a Node we also need to remove the Edges that leave this Node and that are directed to it  

### **_DirectedWeightedGrapgAlgo_**  
#### Complex Functions:
**shortstopDist , shortstop:**    
for these functions we first Dijkstra's algorithm (more information will be given via link) basically Dijkstra's algorithm is an algorithm for finding the shortest paths between nodes in a graph and on the way we add a list to represent the shortest path  

**center:**  
for every node we find the longest path that it could go in the graph, and then we return the Node with the smallest longest path (that it is the center)  

**tsp:**  
this is a well known NP hard problem that has no real cost-efficient way to solve for this solution we can pass a given Node more than once so for every Node we will find the shortest path to any node in the list we do this until we reach all the Nodes in the list  


### **Links**
---
more information about DFS:  
https://en.wikipedia.org/wiki/Depth-first_search  

more information about Dijkstra's algorithm:  
https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm  

### **Interface,class,UML**  
---  
**Interface**:  
* GraphAlgoInterface
* GraphInterface

**class**:
* GraphAlgo
* DiGraph
* Node
* Edge
* GUI
* GUI_functions
* location  

**Test**
* TestDiGraph  
* TestGraphAlgo  

![uml_Ex3_oop](https://user-images.githubusercontent.com/92921822/147462180-db6a8ca3-0ad9-4044-a159-36c661ff18fb.jpg)
