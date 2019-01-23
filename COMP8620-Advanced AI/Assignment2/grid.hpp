//
//  grid.hpp
//  COMP8620ASS2
//
//  Created by CaterpieYu on 2017/10/7.
//  Copyright © 2017 CaterpieYu. All rights reserved.
//

#ifndef grid_hpp
#define grid_hpp

#include <stdio.h>

#include "main.hpp"
#include "environment.hpp"

// describe the position of the agent
typedef unsigned int position_t;

class Grid : public Environment {
public:

    // set up the initial environment percept
    Grid(options_t &options);

    // receives the agent's action and calculates the new environment percept
    virtual void performAction(action_t action);

private:
    void reset();
    percept_t grid_pos_x;
    percept_t grid_pos_y;
};
#endif /* grid_hpp */
