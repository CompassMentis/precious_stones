class PlayerStates(object):
    player_waiting = 'waiting_for_turn'
    turn_started = 'turn_started'
    turn_in_progress = 'turn_in_progress'
    turn_valid = 'valid_turn'
    tiles_offered = 'tiles_on_offer'
    tile_selected = 'tile_selected'
    turn_finished = 'turn_finished'


class ComponentStates(object):
    in_supply = 'in_supply'
    in_holding_area = 'in_holding_area'
    in_reserved_area = 'reserved_by_player'
    in_player_area = 'in_player_area'