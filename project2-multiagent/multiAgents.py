# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        score = successorGameState.getScore()
        foodList = newFood.asList()
        if foodList:
            minFood2PacDist = min(manhattanDistance(food, newPos) for food in foodList)
        else:
            minFood2PacDist = 0

        if newGhostStates:
            minGhost2PacDist = min(manhattanDistance(ghost.getPosition(), newPos) for ghost in newGhostStates)
            if any(time > 0 for time in newScaredTimes):    # if Pacman is in the ghost-eating state, go toward ghosts
                minGhost2PacDist = -minGhost2PacDist
        else:
            minGhost2PacDist = 0

        if minFood2PacDist < minGhost2PacDist * 1.5:
            minFood2PacDist *= 1.7

        # Closer to Food is GOOD (so subtract from score)
        # Closer to Ghost is BAD (so add to score)
        score += -minFood2PacDist + minGhost2PacDist
        return score

def scoreEvaluationFunction(currentGameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """
    """
        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """

    def getAction(self, gameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        "*** YOUR CODE HERE ***"
        # Collect legal moves for Pacman
        legalMoves = gameState.getLegalActions(0)

        # Call expectimax function to generate scores of every successor and 
        # return the score for the best expectimax path
        scores = [
            self.expectimax(gameState.generateSuccessor(0, action), 1, 0) 
            for action in legalMoves
        ]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        return legalMoves[chosenIndex]
    

    def expectimax(self, state, agentIndex, depth):
        # Base Case (reaching bottom of tree)
        if (state.isWin() or state.isLose() or depth == self.depth):
            return self.evaluationFunction(state)
        
        numAgents = state.getNumAgents()
        legalMoves = state.getLegalActions(agentIndex)

        # Base Case (when there are no legal moves)
        if not legalMoves:
            return self.evaluationFunction(state)
    
        # Pacman's Turn (Max Node)
        if (agentIndex == 0):
            return max(
                self.expectimax(state.generateSuccessor(agentIndex, action), 1, depth) 
                for action in legalMoves)

        # Ghost's turn (Chance Node)
        else:
            # Loop through all agents until a base case is reached
            nextAgentIndex = (agentIndex + 1) % numAgents

            # Only increase depth when Pacman is the next agent b/c the depth 
            # can only increase once Pacman and all other ghosts have taken a turn
            nextDepth = depth + 1 if nextAgentIndex == 0 else depth

            # expectimax requires that all scores for the ghosts legal moves must
            # be averaged (because the ghosts use chance nodes)
            return sum(
                self.expectimax(state.generateSuccessor(agentIndex, action), nextAgentIndex, nextDepth) 
                for action in legalMoves
                ) / len(legalMoves) 
            




def betterEvaluationFunction(currentGameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: This evaluation function considers the locations of the food, 
    capsules, ghosts, and whether the state is a win or lose state. The manhattan 
    distance is used to calculate the scores of all distance comparisons. The 
    distance from both the food and capsules to Pacman are each subtracted from the 
    overall score to reflect the idea that the closest food/capsule will result in 
    the score decreasing the least. Similarly, the pacman to ghost distance is added
    to the overall score since the closest ghost is going to add the smallest distance
    to the score, however when the ghosts are in a scared state, the calculated distance 
    becomes negative so that it is subtracted from the overall score, encouraging 
    Pacman to move toward the ghosts eat them. Additionally, the current state's win or lose
    conditions are considered so that a very large value is added to the score to
    motivate the Pacman to move toward a winning state versus the losing state 
    subtracting a large amount from the score, discouraging the Pacman from moving 
    toward a losing state. Lastly, when the distance between the Pacman and 
    food/capsules is significantly smaller than the distance between the Pacman and 
    the closest ghost, a positive weight is added to the food/capsule scores to encourage 
    Pacman to prioritize moving toward the nearest food/capsule rather than moving away 
    from the nearest ghost.
    """
    "*** YOUR CODE HERE ***"
    state = currentGameState
    score = state.getScore()
    foodList = state.getFood().asList()
    pacPos = state.getPacmanPosition()
    ghostStates = state.getGhostStates()
    ghostPositions = state.getGhostPositions()
    scaredTimes = [ghostState.scaredTimer for ghostState in ghostStates]
    capsulePositions = state.getCapsules()

    # Score contribution for food positions
    if foodList:
        minFood2PacDist = min(manhattanDistance(food, pacPos) for food in foodList)
    else:
        minFood2PacDist = 0

    # Score contribution for capsule positions
    if capsulePositions:
        minCap2PacDist = min(manhattanDistance(capsule, pacPos) for capsule in capsulePositions)
    else:
        minCap2PacDist = 0

    # Score contribution for ghost positions
    if ghostPositions:
        minGhost2PacDist = min(manhattanDistance(ghostPos, pacPos) for ghostPos in ghostPositions)
        if any(time > 0 for time in scaredTimes):    # if Pacman is in the ghost-eating state, go toward ghosts
            minGhost2PacDist = -minGhost2PacDist
    else:
        minGhost2PacDist = 0

    result = 0
    if state.isWin():
        result = 999999999
    if state.isLose():
        result = -999999999

    # If food is significantly closer than ghost, prioritize moving 
    # toward food rather than away from ghost
    if minFood2PacDist < minGhost2PacDist * 1.5:
        minFood2PacDist *= 1.7

    # If capsule is significantly closer than ghost, prioritize moving 
    # toward capsule rather than away from ghost
    if minCap2PacDist < minGhost2PacDist * 1.5:
        minCap2PacDist *= 1.7

    # Closer to Food is GOOD (so subtract from score since closest food will have the least subtracted from it)
    # Closer to Capsules is GOOD (so subtract from score since closest capsule will have the least subtracted from it)
    # Closer to Ghost is BAD (so add to score since closest ghost will have the least added to it)
    score += -minFood2PacDist - minCap2PacDist + minGhost2PacDist + result
    return score

# Abbreviation
better = betterEvaluationFunction
