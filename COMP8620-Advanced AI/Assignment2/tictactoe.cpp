/**
 * @author Dong Luo
 * @email u5319900@anu.edu.au
 * @create date 2017-10-06 12:03:20
 * @modify date 2017-10-06 12:03:20
 * @desc [description]
*/

#include "tictactoe.hpp"

const percept_t TicTacToe::rWin = 5; // agent wins + 2
const percept_t TicTacToe::rLose = 1; // agent lose -2
const percept_t TicTacToe::rLegal = 3; // legal move 0
const percept_t TicTacToe::rDraw = 4; // draws +1
const percept_t TicTacToe::rIllegal = 0; //illegal move -3
const percept_t TicTacToe::oAvailable = 0;

const percept_t TicTacToe::oSelf = 1;

const percept_t TicTacToe::oOppo = 2;
TicTacToe::TicTacToe(options_t &options){
    m_reward = 3;
    reset();
};

void TicTacToe::reset() {
    for (auto &i : m_board) {
        for (unsigned int &j : i) {
            j =oAvailable;
        }
    }
    encodeO();
}

bool TicTacToe::isFinished() const {
    // Finishes when the agent wins, loses, draws, or makes illegal moves
    
    return false;
    //return m_reward != rLegal;
}

bool TicTacToe::isValidAction(int row, int col)const{
    if(row<3){
        if(m_board[row][col]==oAvailable){
            return true;
        }
    }
    return false;
}

// Check whether someone has won the game, return rWin, rLose, rLegal (nobody has won), or rDraw.
percept_t TicTacToe::currentStatus() const {
    
    for(int r=0;r<3;r++){
        if(m_board[r][0]==m_board[r][1] && m_board[r][1]==m_board[r][2] && m_board[r][0]!=oAvailable){
            return m_board[r][0]==oSelf?rWin:rLose;
        }
    }
    for(int c=0;c<3;c++){
        if(m_board[0][c]==m_board[1][c] && m_board[1][c]==m_board[2][c] &&
        m_board[0][c]!=oAvailable){
            return m_board[0][c]==oSelf?rWin:rLose;
        }
    }
    if(m_board[1][1]==m_board[2][2] && m_board[1][1]==m_board[0][0] && m_board[0][0]!=oAvailable){
        return m_board[0][0]==oSelf?rWin:rLose;
    }
    if(m_board[0][2]==m_board[1][1] && m_board[1][1]==m_board[2][0] && m_board[1][1]!=oAvailable){
        return m_board[1][1]==oSelf?rWin:rLose;
    }

    bool draw=true;
    for(int r=0;r<3;r++){
        for(int c=0;c<3;c++){
            if(m_board[r][c]==oAvailable){
                draw = false;
                goto stop;
            }
        }
    }
    stop:
    if(draw){
        return rDraw;
    }else{
        return rLegal;
    }
}

void TicTacToe::performAction(action_t action){
    // The row and column where the agent wish to move
    int row = action / 3;
    int col = action % 3;

    //Check whether the action is legal
    if (!isValidAction(row,col)){
        m_reward = rIllegal;
        reset();
        return;
    }

    //Store the action
    m_board[row][col] = oSelf;

    //Check wether the agent side has won
    percept_t status = currentStatus();
    if (status!=rLegal){
        m_reward = status;
        reset();
        return;
    }

    //Opponent randomly moves
    int empties=0; //number of possible options
    for (auto &r : m_board) {
        for (unsigned int c : r) {
            if (c == oAvailable) {
                empties++;
            }
        }
    }
    int move = randRange(1,empties+1);
    for (auto &r : m_board) {
        for (unsigned int &c : r) {
            if (c == oAvailable) {
                move--;
                if(move==0){
                    c = oOppo;
                    goto moved;
                }
            }   
        }
    }
    moved:

    //Check wether the opponent has won
    status = currentStatus();
    if (status!=rLegal){
        m_reward = status;
        reset();
        return;
    }
    //Encode Observation
    m_reward = rLegal;
    encodeO();
}

void TicTacToe::encodeO() {
    m_observation = 0;
    for (auto &r : m_board) {
        for (unsigned int c : r) {
            m_observation = m_observation * 4 + c;
        }
    }
}
