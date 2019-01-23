//
//  1dMaze.cpp
//  COMP8620ASS2
//
//  Created by CaterpieYu on 2017/10/7.
//  Copyright © 2017 CaterpieYu. All rights reserved.
//  Dong Luo, u5319900@anu.edu.au

#include "maze1d.hpp"
/*
 -- 1x4 grid

 --    0   1   3   2

 -- State 3: +1 reward
 --    everything else 0

 -- agent starts at 0, 1 or 2 uniformly at random
 -- agent can move either left or right
*/

const action_t LEFT = 0;
const action_t RIGHT = 1;

const position_t FIRSTCELL = 0;
const position_t SECONDCELL = 1;
const position_t THIRDCELL = 3;
const position_t FOURTHCELL = 2;

const percept_t ZEROREWORD = 0;
const percept_t POSREWORD = 1;

const percept_t NONEPECEPTION = 0;


Maze1d::Maze1d(options_t &options) {
    maze_pos = (percept_t) randRange(FIRSTCELL, FOURTHCELL+1);

    // Set up the initial observation
    m_observation = NONEPECEPTION;
    m_reward = ZEROREWORD;

}



void Maze1d::performAction(action_t action) {

    // observation is constant in a non-informative environment
    m_observation = NONEPECEPTION;
    m_reward = ZEROREWORD;

    if(action!=LEFT && action!= RIGHT){
        std::cerr << "INVALID ACTION ERROR" <<action<<""<<std::endl;
    }

    // Agent makes the move
    switch (maze_pos) {
        case FIRSTCELL:
            if (action == RIGHT){
                maze_pos = SECONDCELL;
            }
            break;
        case SECONDCELL:
            maze_pos = action == LEFT ? FIRSTCELL : THIRDCELL;
            break;
        case FOURTHCELL:
            if (action == LEFT){
                maze_pos = THIRDCELL;
            }
            break;
        default:
            std::cerr << "ERROR" <<action<<""<<std::endl;
    }

    // If goal reached, reset and give the reward
    if (maze_pos == THIRDCELL){
        maze_pos = (percept_t) randRange(FIRSTCELL, FOURTHCELL+1);
        m_reward = POSREWORD;
    }

    // printf("%s%d%s%d", "position :", maze_pos, " reward :", m_reward);

}
