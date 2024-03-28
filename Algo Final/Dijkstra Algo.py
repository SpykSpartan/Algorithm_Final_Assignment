import sys
from heapq import heapify, heappush, heappush

def DijsktraAlgo(graph, source, dest):
    inf = sys.maxsize
   ## holds information for each node, cost to each node from start node and the previous nodes leading up to it
    nodeData = {
    'A':{'cost':inf,'prev':[]},
    'B':{'cost':inf,'prev':[]},
    'C':{'cost':inf,'prev':[]},
    'D':{'cost':inf,'prev':[]},
    'E':{'cost':inf,'prev':[]},
    'F':{'cost':inf,'prev':[]},
    'G':{'cost':inf,'prev':[]},
    'H':{'cost':inf,'prev':[]},
    'I':{'cost':inf,'prev':[]},
    'J':{'cost':inf,'prev':[]},
    'K':{'cost':inf,'prev':[]},
    'L':{'cost':inf,'prev':[]},
    'M':{'cost':inf,'prev':[]},
    'N':{'cost':inf,'prev':[]},
    'O':{'cost':inf,'prev':[]},
    'P':{'cost':inf,'prev':[]},
    'Q':{'cost':inf,'prev':[]},
    'R':{'cost':inf,'prev':[]},
    'S':{'cost':inf,'prev':[]},
    'T':{'cost':inf,'prev':[]},
    'U':{'cost':inf,'prev':[]},
    'V':{'cost':inf,'prev':[]},
    'W':{'cost':inf,'prev':[]},
    }
    ##Sets the source node cost to = becuase it is the first node in the graph
    nodeData[source]['cost'] = 0;
    #Creates an array for vidted nodes, they're only put in here when all of their neighbours have been reached via that node
    visted = []
    ##Temp variable to hold nodes
    temp = source
    ##Runs a for loop for the number of vertices - 1 (23-1 = 22)
    for i in range(22):
        ##If the temp node is not in the visted array add it to the array, this allows us to parse through only the non-visted nodes
        if temp not in visted:
            ##Adds node to visted
            visted.append(temp);
            ## Stores the "Shortest" or minimum elements in the soruce --> Dest
            minHeap = []
            ## runs a for loop for every element in graph
            for j in graph[temp]:
                ##IF the node has node yet been visted run this
                if j not in visted:
                    #Set cost as the source + distance to temp node j
                    cost = nodeData[temp]['cost'] + graph[temp][j]
                    #Checks to see if there is a "Cheaper/Faster" Option
                    if cost < nodeData[j]['cost']:
                        ## Sets the Cot of temp node j to the overall cost
                        nodeData[j]['cost'] = cost
                        ## Adds the temmp node into the list of previous nodes
                        nodeData[j]['prev'] = nodeData[temp]['prev'] + list(temp)
                    ##Element is added to heap 
                    heappush(minHeap,(nodeData[j]['cost'],j))
        #Ensures heap follows the typical heap structure for a min heap
        heapify(minHeap)
        temp = minHeap[0][1]
    print("Shortest Cost: " + str(nodeData[dest]['cost']))
    print("Shortest Path List: " + str(nodeData[dest]['prev'] + list(dest)))

            
    
    
if __name__ == "__main__":
    ##Inputting the graph with weighted vertices
    graph = {
        'A':{'B':6,'F':5},
        'B':{'A':6,'G':6,'C':5},
        'C':{'B':5,'H':5,'D':7},
        'D':{'C':7,'E':7,'I':8},
        'E':{'D':7,'I':6,'N':15},
        'F':{'A':5,'J':7,'G':8},
        'G':{'F':8,'B':6,'K':8,'H':9},
        'H':{'G':9,'C':5,'I':12},
        'I':{'H':12,'D':8,'E':6,'M':10},
        'J':{'F':7,'K':5,'O':7},
        'K':{'J':5,'G':8,'L':7},
        'L':{'K':7,'P':7,'M':7},
        'M':{'L':7,'I':10,'N':9},
        'N':{'M':9,'E':15,'R':7},
        'O':{'J':7,'P':13,'S':9},
        'P':{'O':13,'L':7,'U':11,'Q':8},
        'Q':{'P':8,'R':9},
        'R':{'Q':9,'N':7,'W':10},
        'S':{'O':9,'T':9},
        'T':{'S':9,'U':8},
        'U':{'T':8,'P':11,'V':8},
        'V':{'U':8,'W':5},
        'W':{'V':5,'R':10},

            
        }
        
    ## Trial
    source = 'A';
    dest = 'H';
    DijsktraAlgo(graph,source,dest);
    
    dest = 'K';
    DijsktraAlgo(graph,source,dest);
    
    dest = 'Q';
    DijsktraAlgo(graph,source,dest);
    
    dest = 'T';
    DijsktraAlgo(graph,source,dest);
    
    
    