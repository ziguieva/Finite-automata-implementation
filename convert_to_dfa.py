class NFA(Automaton):
    # Existing methods here...

    def convert_to_dfa(self):
        dfa_states = {}
        initial_state = frozenset([state.name for state in self.states if state.is_initial])
        dfa_states[initial_state] = State(name="".join(initial_state), is_initial=True)

        dfa_transitions = {}
        unprocessed_states = [initial_state]

        while unprocessed_states:
            current = unprocessed_states.pop()
            current_dfa_state = "".join(current)

            for symbol in self.alphabet:
                next_state = set()
                for substate in current:
                    if (substate, symbol) in self.transitions:
                        next_state.update(self.transitions[(substate, symbol)])

                next_state = frozenset(next_state)
                if next_state not in dfa_states and next_state:
                    new_state = State(name="".join(next_state), is_final=any(s.is_final for s in self.states if s.name in next_state))
                    dfa_states[next_state] = new_state
                    unprocessed_states.append(next_state)

                if next_state:
                    dfa_transitions[(current_dfa_state, symbol)] = ["".join(next_state)]

        dfa_states_list = list(dfa_states.values())
        return DFA(states=dfa_states_list, alphabet=self.alphabet, transitions=dfa_transitions)
