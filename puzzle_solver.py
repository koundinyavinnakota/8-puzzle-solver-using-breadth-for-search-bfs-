
"""
  8 - puzzle problem solving using Breadth First Search Algorithm (bfs)

"""

__author__ = "Koundinya Vinnakota"
__version__ = "0.1.0"
__license__ = "MIT"


import numpy as np
class Node:
    def __init__(self,initial_state):
        self.children=0
        self.x=0
        self.node_index=0
        self.parent_index=0
        self.current_config=np.array(initial_state.copy())
        self.stateRows,self.stateColumns=self.current_config.shape
        self.blankPosX,self.blankPosY=np.where(self.current_config==0)
        self.possible_actions=[self.checkUp(),self.checkRight(),self.checkDown(),self.checkLeft()]
        self.queue=[]
        self.possible_configurations()
        
        
    def checkUp(self):
        if self.blankPosX[0]-1 == -1:
            return 0
        else:
            return 1
    def checkRight(self):
        if self.blankPosY[0]+1 >= self.stateColumns:
            
            return 0
        else:
            return 1
        
    def checkDown(self):
        if self.blankPosX[0]+1 >= self.stateRows:
            return 0
        else:
            return 1
    def checkLeft(self):
        if self.blankPosY[0]-1 == -1:
            return 0
        else:
            return 1
        
    def possible_configurations(self):
        self.children=np.count_nonzero(self.possible_actions)
        for a in range(4):
            mat=self.current_config.copy()
            
            if a==0 and self.possible_actions[a] == 1:
                mat[self.blankPosX[0]-1][self.blankPosY[0]], mat[self.blankPosX[0]][self.blankPosY[0]] = mat[self.blankPosX[0]][self.blankPosY[0]], mat[self.blankPosX[0]-1][self.blankPosY[0]] 
                self.queue.append(mat)
                    
            elif a==1 and self.possible_actions[a] == 1:
                mat[self.blankPosX[0]][self.blankPosY[0]+1], mat[self.blankPosX[0]][self.blankPosY[0]] = mat[self.blankPosX[0]][self.blankPosY[0]], mat[self.blankPosX[0]][self.blankPosY[0]+1]
                self.queue.append(mat)
                        
            elif a==2 and self.possible_actions[a] == 1:
                mat[self.blankPosX[0]+1][self.blankPosY[0]], mat[self.blankPosX[0]][self.blankPosY[0]] = mat[self.blankPosX[0]][self.blankPosY[0]], mat[self.blankPosX[0]+1][self.blankPosY[0]]
                self.queue.append(mat)
                        
            elif a==3 and self.possible_actions[a] == 1:
                mat[self.blankPosX[0]][self.blankPosY[0]-1], mat[self.blankPosX[0]][self.blankPosY[0]] = mat[self.blankPosX[0]][self.blankPosY[0]], mat[self.blankPosX[0]][self.blankPosY[0]-1]        
                self.queue.append(mat)
        

        


        
def bfsAlgo(start_node, goal_node):
    visited=[]
    current=[]
    node_index=1
    parent_index=1
    node=Node(start_node)
    node.node_index=node_index
    node.parent_index=parent_index
    current.append(node)
    visited.append(node)
    
    Flag=True
    visited_flag=False
    while Flag:
        element=current.pop(0)
        if np.array_equal(element.current_config,goal_node):
            print("Reached Goal")
            element.node_index=node_index
            visited.append(element)
            break
        else:
            for each in visited:
                if np.array_equal(each.current_config,element.current_config):
                    visited_flag=True
                else:
                    visited_flag=False
            if visited_flag:
                pass
            else:

                element.node_index=node_index
                visited.append(element)
                
        
            for a in range(0,element.children):
                node=Node(element.queue.pop(0))
                node.parent_index=parent_index
                current.append(node)
            node_index+=1
            parent_index+=1
    path=backtracking(initial_config,goal_config,visited)
        
    
    
    return path

def backtracking(start_node,goal_node,visited):
    path=[]
    x=visited[-1].parent_index
    y=visited[0]
    path.append(visited[-1])
    while not np.array_equal(path[-1].current_config,start_node):
        for a in visited:
            if x == a.node_index:
                x=a.parent_index
                path.append( a )
    
    return path[::-1]
   
    
    
    
if __name__=="__main__":
    
    initial_config=np.array([[1,4,7],
                            [5,0,8],
                            [2,3,6]])
    
    goal_config=np.array([[1,4,7],
                          [2,5,8],
                          [3,6,0]])
    
    solution=bfsAlgo(initial_config,goal_config)
    for a in solution:
        print(a.current_config)
    
    

