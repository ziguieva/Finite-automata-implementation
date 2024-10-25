class DFA(Automaton):
    def recognize_string(self, input_string: str) -> bool:
        current_state = next((state for state in self.states if state.is_initial), None)
        if not current_state:
            raise ValueError("DFA must have an initial state.")
        
        for symbol in input_string:
            if (current_state.name, symbol) in self.transitions:
                next_state_name = self.transitions[(current_state.name, symbol)][0]
                current_state = next(state for state in self.states if state.name == next_state_name)
            else:
                return False
        return current_state.is_final
