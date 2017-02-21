from random import choice

from game_state import game_state
from game_objects import Chip, Card, holding_area
from game_actions import TakeChip, TakeCard, Confirm

"""
What's the protocol:
Attach to a player
Player can either be AI or human
If AI, then player has an AI property, otherwise AI is set to None

Flow
    * At the start of a player's turn, if the player has an AI
        * Create list of possible moves
            * What will be gained
            * What is the button's action for this move
                TakeChip(chip, holding_area)
                TakeCard(card, holding_area)
        * Pass list plus current game state to AI
        * AI chooses the move, execute the moves action(s)
            * action.activate(current_player)
            * Moves get shown in the holding area, as usual
        * Normal game flow continues
            * I then confirm the move, so I can see what happened
            * Or I could manually change the move
"""


class AbstractAI(object):
    def __init__(self):
        self.the_game = None
        self.player = None

    def init_ai(self, game, player):
        self.the_game = game
        self.player = player


class RandomAI(AbstractAI):
    def _choose_move(self):
        valid_action_sets = game_state.valid_action_sets

        for action_type in ['card', '3 chips', '2 chips', 'reserve card']:
            if len(valid_action_sets[action_type]):
                return choice(valid_action_sets[action_type])

        return None

    def _action_for_item(self, item):
        for object_type, action in [
            (Chip, TakeChip),
            (Card, TakeCard)
        ]:
            if isinstance(item, object_type):
                return action(item, holding_area)
        return None

    def take_turn(self):
        # TODO: Move this into abstract class's set up code?
        game_state.update(self.the_game)

        my_move = self._choose_move()
        if not my_move:
            return

        actions = [self._action_for_item(item) for item in my_move
                   if self._action_for_item(item)]  # + [Confirm(holding_area)]

        for action in actions:
            action.activate(self.player)


class SimpleAI(AbstractAI):
    pass
