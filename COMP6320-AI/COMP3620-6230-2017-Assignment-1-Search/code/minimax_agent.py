# minimax_agent.py
# --------------
# COMP3620/6320 Artificial Intelligence
# The Australian National University
# For full attributions, see attributions.txt on Wattle at the end of the course

"""
    Enter your details below:

    Name: Longfei Zhao
    Student Code: u5976992
    email: u5976992@anu.edu.au
"""

from agents import Agent
import util

from search_problems import AdversarialSearchProblem

class MinimaxAgent(Agent):
    """ The agent you will implement to compete with the black bird to try and
        save as many yellow birds as possible. """

    def __init__(self, max_player, depth="2"):
        """ Make a new Adversarial agent with the optional depth argument.
            (MinimaxAgent, str) -> None
        """
        self.max_player = max_player
        self.depth = int(depth)

    def evaluation(self, problem, state):
        """
            (MinimaxAgent, AdversarialSearchProblem,
                (int, (int, int), (int, int), ((int, int)), number, number))
                    -> number
        """
        player, red_pos, black_pos, yellow_birds, score, yb_score = state

        numBirds = len(yellow_birds)
        closestDisRed = 0
        closestDisBlack = 0
        sumDisRed = 0
        sumDisBlack = 0
        value = score
        '''
        for bird in yellow_birds:
            disRed = problem.distance[(red_pos, bird)]
            disBlack = problem.distance[(black_pos, bird)]
            sumDisRed += disRed
            sumDisBlack += disBlack
            if closestDisRed == 0 or disRed < closestDisRed:
                closestDisRed = disRed
            if closestDisBlack == 0 or disBlack < closestDisBlack:
                closestDisBlack = disBlack

        if numBirds == 0:
            numBirds = 1

        #yb_score = yb_score - min(closestDisRed, closestDisBlack)
        #if yb_score < 0:
            #yb_score = 0
        value = score + 0.1 * yb_score * (closestDisBlack - closestDisRed) + 0.2 * yb_score * (sumDisBlack - sumDisRed) / numBirds
        '''
        '''
        for bird in yellow_birds:
            disRed = problem.distance[(red_pos, bird)]
            disBlack = problem.distance[(black_pos, bird)]
            if min(disRed, disBlack) >= yb_score:
                continue
            if disRed  > disBlack:
                value -= yb_score - disBlack
            if disBlack > disRed:
                value += yb_score - disRed
        '''
        closestBirdBlack = None
        closestBirdRed = None
        for bird in yellow_birds:
            disRed = problem.distance[(red_pos, bird)]
            disBlack = problem.distance[(black_pos, bird)]
            if disRed  >= disBlack:
                value -= 0.3 * max(yb_score - disBlack, 0)
            else:
                value += 0.3 * max(yb_score - disRed, 0)
            sumDisRed += disRed
            sumDisBlack += disBlack
            if closestDisRed == 0 or disRed < closestDisRed:
                closestDisRed = disRed
                closestBirdRed = bird
            if closestDisBlack == 0 or disBlack < closestDisBlack:
                closestDisBlack = disBlack
                closestBirdBlack = bird
        '''
        if not closestBirdRed and not closestBirdBlack and closestBirdBlack == closestBirdRed:
            if closestDisRed < closestDisBlack:
                value += yb_score - closestDisRed
            else:
                value -= yb_score - closestDisBlack
        else:
            value = value + min(closestDisBlack, yb_score) - min(closestDisRed, yb_score)
        vaule = value + yb_score * numBirds - sumDisRed
        '''
        if numBirds == 0:
            numBirds = 1
        value = value - max(yb_score - closestDisBlack, 0) + max(yb_score - closestDisRed, 0) + 0.25 * yb_score * (sumDisBlack - sumDisRed) / numBirds
        return value


    def maximize(self, problem, state, current_depth):
        """
            This method should return a pair (max_utility, max_action).

             (MinimaxAgent, AdversarialSearchProblem,
                 (int, (int, int), (int, int), ((int, int)), number, number)
                     -> (number, str)
        """

        "*** YOUR CODE GOES HERE ***"
        max_utility = None
        max_action = None
        current_depth = current_depth + 1

        for next_state, action, cost in problem.get_successors(state) :
            if current_depth == self.depth or problem.terminal_test(next_state):
                tempValue = self.evaluation(problem, next_state)
            else:
                tempValue = self.minimize(problem, next_state, current_depth)
            if not max_utility or tempValue > max_utility :
                max_utility = tempValue
                max_action = action
        return max_utility, max_action

    def minimize(self, problem, state, current_depth):
        """
            This function should just return the minimum utility.

            (MinimaxAgent, AdversarialSearchProblem,
                 (int, (int, int), (int, int), ((int, int)), number, number)
                     -> number
        """

        "*** YOUR CODE GOES HERE ***"

        min_utility = None
        current_depth = current_depth + 1

        for next_state, action, cost in problem.get_successors(state) :
            if current_depth == self.depth or problem.terminal_test(next_state):
                tempValue = self.evaluation(problem, next_state)
            else:
                tempValue, tempAction = self.maximize(problem, next_state, current_depth)
            if not min_utility or tempValue < min_utility :
                min_utility = tempValue
        return min_utility

    def get_action(self, game_state):
        """ This method is called by the system to solicit an action from
            MinimaxAgent. It is passed in a State object.

            Like with all of the other search problems, we have abstracted
            away the details of the game state by producing a SearchProblem.
            You will use the states of this AdversarialSearchProblem to
            implement your minimax procedure. The details you need to know
            are explained at the top of this file.
        """
        #We tell the search problem what the current state is and which player
        #is the maximizing player (i.e. who's turn it is now).
        problem = AdversarialSearchProblem(game_state, self.max_player)
        state = problem.get_initial_state()
        utility, max_action = self.maximize(problem, state, 0)
        print("At Root: Utility:", utility, "Action:", max_action, "Expanded:", problem._expanded)
        return max_action
