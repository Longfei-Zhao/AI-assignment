//
//  1dMaze.hpp
//  COMP8620ASS2
//
//  Created by CaterpieYu on 2017/10/7.
//  Copyright © 2017 CaterpieYu. All rights reserved.
//

#ifndef maze1d_hpp
#define maze1d_hpp

#include <stdio.h>

#include "main.hpp"
#include "environment.hpp"

// describe the position of the agent
typedef unsigned int position_t;

class Maze1d : public Environment {
public:
    
    // set up the initial environment percept
    Maze1d(options_t &options);
    
    // receives the agent's action and calculates the new environment percept
    virtual void performAction(action_t action);
    
private:
    percept_t maze_pos;
};

#endif /* maze1d_hpp */
