class Actor:
    '''Base class for game actor (a participant or a monster).
    Contains data common to all actors.
    '''

    def __init__(self, actor_type, name, hp, max_hp):

        self.type = actor_type  # { 1: 'Player', 2: 'Monster' }
        self.name = name
        self.hp = hp
        self.max_hp = max_hp
        self.is_alive = 1

    def set_actor_id(self, actor_id):
        ''' Set actor ID.

        Arguments:
        actor_id -- integer, ID of actor.
        '''

        self.id = actor_id

    def decrease_hp(self, diff):
        ''' Decrease actor's HP by diff amount

        Arguments:
        diff -- integer, amoun of HP to be substracted.
        '''

        self.hp -= diff

    def increase_hp(self, diff):
        ''' Increase actor's HP by diff amount, respecting max_hp.

        Arguments:
        diff -- integer, amoun of HP to be added.
        '''

        self.hp += diff
        if self.hp > self.max_hp:
            self.hp = self.max_hp
