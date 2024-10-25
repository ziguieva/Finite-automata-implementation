class State:
    def __init__(self, name: str, is_initial: bool = False, is_final: bool = False):
        self.name = name
        self.is_initial = is_initial
        self.is_final = is_final

class Automaton:
    def __init__(self, states: list, alphabet: set, transitions: dict):
        self.states = states  # List of State objects
        self.alphabet = alphabet  # Set of accepted symbols
        self.transitions = transitions  # Dict for transitions {(state, symbol): [next_states]}

    def add_transition(self, state_from: str, symbol: str, state_to: str):
        if (state_from, symbol) in self.transitions:
            self.transitions[(state_from, symbol)].append(state_to)
        else:
            self.transitions[(state_from, symbol)] = [state_to]
