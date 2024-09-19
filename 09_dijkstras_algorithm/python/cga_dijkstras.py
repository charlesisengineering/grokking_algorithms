'''
TODO Add types to method prototypes to eliminate bad graphs being used
TODO Add method to check graphs for: non-zero elements, equal-weight loops
TODO Make sure active node is in graph before we start
'''

class Dijkstra():
    # This method takes in a graph and outputs two hash tables where nodes are keys and values are costs and parents
    # we also need to track nodesToSearch in our recursive calls so that we don't search any nodes twice
    def dijSearch(self, graph, costs, parents, activeNode, nodesToSearch):

        # base case is no nodes remaining to search
        if(len(nodesToSearch) == 0):

            return costs, parents
        
        #recursive case is 1 or more nodes still to search
        else:

            print('Active node is ', activeNode)

            # iterate through our activeNode's neighbors to check if we can update costs table for any of the neighbors
            for neighbor in graph[activeNode]:

                print('Checking neighbor ', neighbor)

                # check that we still need to analyze this node
                # TODO check back if we want to move this conditional up to the recursive case else, making it an elif
                if (activeNode in nodesToSearch):
                    # calculate the cost of the new route we've found 
                    newCost = costs[activeNode] + graph[activeNode][neighbor]
                    # update costs dict if the new cost is cheaper than the existing one

                    print('New cost of ', neighbor, 'is ', newCost)
                    if(newCost < costs[neighbor]):
                        costs[neighbor] = newCost
                        # any time we update our cost table we update our parents table
                        parents[neighbor] = activeNode

            #once we've updated our cost table let's pop the activeNode from the nodesToSearch
            nodesToSearch.pop(nodesToSearch.index(activeNode))

            # find the cheapest non-analyzed node
            # create a variable to store our node's cheapest neighbor
            cheapestNeighbor = None
            cheapestEdge = float('inf')
            for node in costs:
                if(node in nodesToSearch and costs[node] < cheapestEdge):
                    cheapestEdge = costs[node]
                    cheapestNeighbor = node

            print('Our costs table is currently ', costs)
            print('Our parents table is currently ', parents)
            print('Our remaining nodes to search are ', nodesToSearch)
            print('Next active node is ', cheapestNeighbor)


            return self.dijSearch(graph, costs, parents, cheapestNeighbor, nodesToSearch)
        
    
    # Take a dijTable as input and calculate the cheapest path
    def cheapestPath(self, costs, parents):
        return None
    
if __name__ == '__main__':
    #import Dijkstra class
    dij = Dijkstra()
    infinity = float('inf')

    # build a test graph to use our Dijkstra's algo implementation on
    # is the smartest graph implementation a nested dict or a dict of linked lists? not considering arrays because of mixed data types (strs and ints)
    graph = {
        "book": {"lp": 5, "poster": 0 },
        "lp": {"bass": 15, "drums": 20},
        "poster": {"bass": 30, "drums": 35},
        "bass": {"piano": 20},
        "drums": {"piano": 10}
    }

    # we'll build this within the algorithm but here's a test costs and parents graph
    # for our algorithm the start node must be included in the costs table
    costsDict = {
        'book': 0,
        'lp':   infinity,
        'poster': infinity,
        'drums': infinity,
        'bass': infinity,
        'piano': infinity 
    }

    parentsDict = {}
    nodesToSearch = list(graph.keys()) 

    newCosts, newParents = dij.dijSearch(graph, costsDict, parentsDict, 'book', nodesToSearch)

    print(newCosts)
    print(newParents)
