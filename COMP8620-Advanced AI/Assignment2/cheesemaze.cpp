/**
 * @author Dong Luo
 * @email u5319900@anu.edu.au
 * @create date 2017-10-07 04:45:01
 * @modify date 2017-10-07 04:45:01
 * @desc [description]
*/
#include "cheesemaze.hpp"

//increment all rewards by 10
const percept_t CheeseMaze::rWall = 0;//-10
const percept_t CheeseMaze::rMove = 10;//-1
const percept_t CheeseMaze::rCheese = 20;//20

const int CheeseMaze::m_cheese = 4;
const percept_t CheeseMaze::wall = 36; //indicate the position for wall
const percept_t CheeseMaze::oCell[11] = {7, 5, 9, 10, 7, 5, 8, 10, 7, 5, 12};
const percept_t CheeseMaze::m_maze[11][4] = {
    {1,wall,wall,wall},//0
    {2,wall,0,wall},//1
    {wall,3,1,wall},//2
    {wall,6,wall,2},//3
    {5,wall,wall,wall},//4
    {6,wall,4,wall},//5
    {wall,7,5,3},//6
    {wall,10,wall,6},//7
    {9,wall,wall,wall},//8
    {10,wall,8,wall},//9
    {wall,wall,9,7}//10
};
CheeseMaze::CheeseMaze(options_t &options){
    //randomly place mouse;
    m_mouse = randRange(11);
    m_observation = oCell[m_mouse];
    m_reward = 0;
}
void CheeseMaze::reset(){
    m_mouse = randRange(11);
    m_observation = oCell[m_mouse];
    m_reward = 0;
}
bool CheeseMaze::isFinished() const {
    return false;
   // return m_reward == rCheese;
}

void CheeseMaze::performAction(action_t action){
    if(m_maze[m_mouse][action]==wall){
        //If the action is invalid, the mouse does not move
        m_reward = rWall;
        return;
    }else{
        m_mouse = m_maze[m_mouse][action];
        m_reward = m_mouse == m_cheese ? rCheese : rMove;
        if (m_reward == rCheese){
            reset();
        }
    }
}