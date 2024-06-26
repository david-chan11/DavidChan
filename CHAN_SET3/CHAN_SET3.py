#!/usr/bin/env python
# coding: utf-8

# In[34]:


def relationship_status(from_member, to_member, social_graph):

    if from_member in social_graph[to_member]["following"] and to_member in social_graph[from_member]["following"]:
        return "friends"
        
    elif from_member in social_graph[to_member]["following"]:
        return "followed by"
        
    elif to_member in social_graph[from_member]["following"]:
        return "follower"
        
    else:
        return "no relationship"
    


# In[38]:


def tic_tac_toe(board):

    for row in board:  
        
        if "" not in row and len(set(row)) == 1:
            return row[0]
            
    for col in range(len(board)): 
        
        if "" not in [row[col] for row in board] and len(set(row[col] for row in board)) == 1:
            return board[0][col]
    
    if "" not in [board[i][i] for i in range(len(board))] and len(set(board[i][i] for i in range(len(board)))) == 1:
        return board[0][0]
   
    if "" not in [board[j][len(board) - 1 - j] for j in range(len(board))] and len(set(board[j][len(board) - 1 - j] for j in range(len(board)))) == 1:
        return board[0][len(board) - 1]
        
    return "NO WINNER"


# In[32]:


def eta(first_stop, second_stop, route_map):

    current_leg = first_stop
    timer = 0
            
    while current_leg != second_stop: 
        
        if (current_leg, second_stop) in route_map: 
            timer = timer + route_map[(current_leg, second_stop)]['travel_time_mins'] 
            break
            
        else: 
            next_stop = None
            
            for leg in route_map:
                
                if leg[0] == current_leg:  
                    next_stop = leg[1]
                    timer += route_map[leg]['travel_time_mins']
                    current_leg = leg[1]
                    break 
                    
        if next_stop is None:
            break 
            
    return timer


# In[ ]:




