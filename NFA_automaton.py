class NFA(Automaton):
    def recognize_string(self, input_string: str) -> bool:
        current_states = [state.name for state in self.states if state.is_initial]

        for symbol in input_string:
            next_states = set()
            for state in current_states:
                if (state, symbol) in self.transitions:
                    next_states.update(self.transitions[(state, symbol)])
            current_states = list(next_states)

        return any(state.is_final for state in self.states if state.name in current_states)
