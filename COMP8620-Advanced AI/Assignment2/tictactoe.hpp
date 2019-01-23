/**
 * @author Dong Luo
 * @email u5319900@anu.edu.au
 * @create date 2017-10-06 12:03:42
 * @modify date 2017-10-06 12:03:42
 * @desc [description]
*/
#ifndef __TICTACTOE__
#define __TICTACTOE__

#include "environment.hpp"
// tictactoe
class TicTacToe : public Environment {
public:
	// set up the initial environment percept
    explicit TicTacToe(options_t &options);

	// receives the agent's action and calculates the new environment percept
    void performAction(action_t action) override;

    bool isValidAction(int, int) const;

    void encodeO();

    bool isFinished() const override;

    void reset();
    
    percept_t currentStatus() const;
private:

    // Observations...
    // The game board (the observation of the agent)
    percept_t m_board[3][3];

    // The status of cells
    static const percept_t oAvailable;// unfilled places
    static const percept_t oSelf;//occupied by the agent side
    static const percept_t oOppo;//occupied by the opponent

    // rewards
    static const percept_t rWin; // agent wins + 2
    static const percept_t rLose; // agent lose -2
    static const percept_t rDraw; // draws +1
    static const percept_t rIllegal; //illegal move -3
    static const percept_t rLegal; //legal move which does not end the game 0

};
#endif