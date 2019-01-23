#ifndef __CHEESE__
#define __CHEESE__
#include "environment.hpp"
#include "util.hpp"
// rock-paper-scissors
class CheeseMaze : public Environment {
public:

	// set up the initial environment percept
    explicit CheeseMaze(options_t &options);

	// receives the agent's action and calculates the new environment percept
    void performAction(action_t action) override;

    bool isFinished() const override;
    void reset();
private:


    //Observations
    static const percept_t oCell[11];

    //Reward: for wall, cheese, or movement into free cell
    static const percept_t rWall;
    static const percept_t rCheese;
    static const percept_t rMove;

    //Position of cheese
    static const int m_cheese;

    //Defines how state changes: SxA->S
    static const percept_t m_maze[11][4];

    static const percept_t wall;

    //Position of mouse
    int m_mouse;

};
#endif