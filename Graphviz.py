import graphviz

def visualize_automaton(automaton: Automaton, file_name='automaton'):
    dot = graphviz.Digraph()

    for state in automaton.states:
        if state.is_final:
            dot.node(state.name, shape='doublecircle')  # Final state
        else:
            dot.node(state.name, shape='circle')  # Regular state
        if state.is_initial:
            dot.edge("", state.name)  # Initial state indicator

    for (state_from, symbol), states_to in automaton.transitions.items():
        for state_to in states_to:
            dot.edge(state_from, state_to, label=symbol)

    dot.render(file_name, format='png', view=True)
