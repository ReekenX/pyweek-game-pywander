class BoardBase(object):
    def update(self, surface, events):
        self.process_inputs(events)
        if self.is_time_to_switch_board():
            return self.get_next_board()
        else:
            self.process_draw_on_surface(surface)
            if self.is_time_to_switch_board():
                return self.get_next_board()
        return self

    def process_inputs(self, events):
        raise Exception('Board has no process_inputs() logic')

    def process_draw_on_surface(self, surface):
        raise Exception('Board has no process_draw_on_surface() logic')

    def is_time_to_switch_board(self):
        raise Exception('Board has no is_time_to_switch() logic')

    def get_next_board(self):
        raise Exception('Board has no get_next_board() logic')
