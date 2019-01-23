//
// Created by Ton on 11/10/2017.
//

#include "rockpaperscissor.hpp"

/*
Biased Rock Paper Scissors
*/
// Actions
const action_t RockPaperScissors::aRock = 0;
const action_t RockPaperScissors::aPaper = 1;
const action_t RockPaperScissors::aScissor = 2;

// Rewards
const percept_t RockPaperScissors::rWin = 2;  //1
const percept_t RockPaperScissors::rLose = 0; //-1
const percept_t RockPaperScissors::rDraw = 1; //0

//Observations
const percept_t RockPaperScissors::oRock = 0;
const percept_t RockPaperScissors::oPaper = 1;
const percept_t RockPaperScissors::oScissor = 2;

RockPaperScissors::RockPaperScissors(options_t &options) {

    //Set up the opponent's action
    m_observation = oPaper;
    m_reward = rDraw;
    m_last_action = oPaper;
}

// Opponent choose rock if it rocked and won in the previous trial, other it
// perform randomly(each potential action has equal probability).
// Give a reward 1 if agent wins, 0 if draw, and -1 if agent lose
void RockPaperScissors::performAction(action_t action) {

    // The opponent choose an action
    if (m_reward == rLose && m_last_action == aScissor) {//opponent won in the last trial
        m_observation = oRock;
    } else {
        switch (randRange(3)) {
            case 0:
                m_observation = oRock;
                break;
            case 1:
                m_observation = oPaper;
                break;
            case 2:
                m_observation = oScissor;
                break;
            default:
                break;

        }
    }

    // Compare the actions and give reward
    if (action == m_observation) {
        m_reward = rDraw;
    } else if (action == m_observation + 1 || action == m_observation - 2) {
        m_reward = rWin;
    } else {
        m_reward = rLose;
    }
}

