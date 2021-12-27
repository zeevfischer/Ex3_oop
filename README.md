# Directed Weighted Graph

### **Explanation**
---
Written by zeev fischer,eden mor and liav levi.  
This project was all about graphs for starters what we hade to do is implement this following interfaces  
* GeoLocation – the representation of a Node location 
* NodeData – the representation of a Node(point) in the Graph
* EdgeData – represent a directed weighted connection between tew Nodes(points) in the Graph
* DirectedWeightedGrapg – represents the actual Graph 
* DirectedWeightedGraphAlgorithms – this interface has all sorts of function that can be implemented on a graph  
 
for the first three there is not much to explain Now for DirectedWeightedGrapg and DirectedWeightedGraphAlgorithms there is more thought that goes in to implementing these interfaces.  

### **_DirectedWeightedGrapg_**  
#### Complex Functions:  

**removeNode():**    
by removing a Node we also need to remove the Edges that leave this Node and that are directed to it  

### **_DirectedWeightedGrapg_**  
#### Complex Functions:
**shortestpathDist , shortestpath:**    
for these functions we first implemented a fibonacciheap then we ran dijksres algorithm (more information will be given via link) basically dijksres algorithm is an algorithm for finding the shortest paths between nodes in a graph and on the way we add a list to represent the shortest path  

**center:**  
for every node we find the longest path that is has from all the shortest paths it has to every other Node in the Graph then we get the Node with the smallest longest path and it is the center  

**tsp:**  
this is a well known problem that has no real cost efficient way to salve for this solution we can pass an a given Node more then once so for every Node we will find the shortest path to any node in the list we do this until we reach all the Nodes in the list  


### **Links**
---
more infurmation about DFS:  
https://en.wikipedia.org/wiki/Depth-first_search  

more infurmation about Dijkstra's algorithm:  
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
