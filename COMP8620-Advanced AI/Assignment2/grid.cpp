//
//  grid.cpp
//  COMP8620ASS2
//
//  Created by CaterpieYu on 2017/10/7.
//  Copyright © 2017 CaterpieYu. All rights reserved.
//  Dong Luo, u5319900

#include "grid.hpp"
#include <stdio.h>
#include <cassert>

#include "util.hpp"

const action_t UP = 0;
const action_t RIGHT = 1;
const action_t DOWN = 2;
const action_t LEFT = 3;


const position_t ZERO_X = 0;
const position_t ONE_X = 1;
const position_t TWO_X = 2;
const position_t THREE_X = 3;

const position_t ZERO_Y = 0;
const position_t ONE_Y = 1;
const position_t TWO_Y = 2;
const position_t THREE_Y = 3;

const percept_t ZEROREWORD = 0;
const percept_t POSREWORD = 1;
const percept_t NONEPECEPTION = 0;

Grid::Grid(options_t &options) {
    // Set up the initial observation
    reset();
    m_observation = NONEPECEPTION;
    m_reward = ZEROREWORD;

}

void Grid::reset(){
    int position = randRange(0,15);
    grid_pos_x = position % 4;
    grid_pos_y = position / 4;
//    printf("NEW LOCATION:(%d, %d)\n",grid_pos_x,grid_pos_y);
}

void Grid::performAction(action_t action) {

    m_observation = NONEPECEPTION;
    m_reward = ZEROREWORD;
    switch (action){
        case UP:
            if (grid_pos_y != ZERO_Y){
                grid_pos_y--;
            }
            break;
        case RIGHT:
            if (grid_pos_x != THREE_X){
                grid_pos_x++;
            }
            break;
        case DOWN:
            if (grid_pos_y != THREE_Y){
                grid_pos_y++;
            }
            break;
        case LEFT:
            if (grid_pos_x != ZERO_X){
                grid_pos_x--;
            }
            break;
        default:
            printf("Error!");
    }

    if(grid_pos_y * 4 + grid_pos_x == 15){
//        printf("CURRENT LOCATION:(%d, %d)\n",grid_pos_x,grid_pos_y);
//        printf("WIN!\n");
        m_reward = POSREWORD;
        reset();
    }


    //   printf("%s%d%d%s%d", "position :", grid_pos_x, grid_pos_y, " reward :", m_reward);
}
