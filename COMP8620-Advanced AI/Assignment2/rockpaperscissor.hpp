#ifndef __ROCKS__
#define __ROCKS__

#include "environment.hpp"

// rock-paper-scissors
class RockPaperScissors : public Environment {
public:

    // set up the initial environment percept
    explicit RockPaperScissors(options_t &options);

    // receives the agent's action and calculates the new environment percept
    void performAction(action_t action) override;

private:

    //Action: Rock
    static const action_t aRock;

    //Action: Scissor
    static const action_t aScissor;

    //Action: Paper
    static const action_t aPaper;

    //Observation: the most recent action of the opponent is rock
    static const percept_t oRock;

    //Observation: the most recent action of the opponent is scissor
    static const percept_t oScissor;

    //Observation: the most recent action of the opponent is paper
    static const percept_t oPaper;

    //Reward: for win
    static const percept_t rWin;

    //Reward: for lose
    static const percept_t rLose;

    //Reward: for draw
    static const percept_t rDraw;

};

#endif