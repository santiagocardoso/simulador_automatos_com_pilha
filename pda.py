'''
Final work of LFA

Members:
    Santiago Cardoso
    Lucas Gabriel
'''

# Imports
import sys
import json

# Recustion limit
sys.setrecursionlimit(4000)

# Classes
class Transition:
    def __init__(self, symbol_read, symbol_top_pull, symbol_push, state):
        self.symbol_read = symbol_read
        self.symbol_top_pull = symbol_top_pull
        self.symbol_push = symbol_push
        self.state = state

    def __str__(self):
        return f"Transition=('{self.symbol_read}','{self.symbol_top_pull}','{self.symbol_push}',next_state='{self.state}')"


class State:
    def __init__(self, name, transitions, stack):
        self.name = name
        self.transitions = transitions
        self.stack = stack

    def __str__(self):
        transitions_str = ",".join(map(str, self.transitions))
        return f"State=({self.name}=([{transitions_str}],stack={self.stack}))"

    def get_transitions(self):
        return self.transitions
    def get_name(self):
        return self.name

class AutomatonStack:
    def __init__(self, start_state, states, final_state, input, stack):
        self.start_state = start_state
        self.states = states
        self.final_state = final_state
        self.input = input
        self.stack = stack
        self.accept = False

    def __str__(self):
        return f"M=({self.start_state},{self.input},{self.states},{self.final_state},{self.stack})"

    def read_input(self):
        current_transitions = self.start_state.transitions
        count_letters = 0

        for letter in self.input:
            count_letters += 1
            empty_movement = False

            for transition in current_transitions:
                if transition.symbol_read == "":
                    empty_movement = True

            if empty_movement:
                new_input = self.input[count_letters - 1:]
                new_stack = self.stack.copy()

                for state in self.states:
                    if transition.state == state.get_name():
                        new_start_state = state

                new_automaton = AutomatonStack(new_start_state, self.states, self.final_state, new_input, new_stack)
                new_automaton.read_input()

                if new_automaton.accept:
                    self.accept = True
                    return

            for transition in current_transitions:
                # Does not remove anything from the top but puts something on the stack
                if transition.symbol_read == letter and transition.symbol_top_pull == "":
                    self.stack.append(transition.symbol_push)
                    break

                # Neither remove nor add anything, just read the input
                elif transition.symbol_top_pull == "" and transition.symbol_push == "":
                    break

                elif len(self.stack) == 0 and transition.symbol_top_pull != "":
                    return

                # Just remove and don't put anything on the stack
                elif transition.symbol_read == letter and self.stack[-1] == transition.symbol_top_pull and transition.symbol_push == "":
                    self.stack.pop()
                    break

                # Take something out and put something in
                elif transition.symbol_read == letter and self.stack[-1] == transition.symbol_top_pull:
                    self.stack.pop()
                    self.stack.append(transition.symbol_push)
                    break

                elif transition == current_transitions[-1]:
                    return

            next_state = transition.state
            for state in self.states:
                if next_state == state.name:
                    current_transitions = state.transitions

        if next_state == self.final_state.name and len(self.stack) == 0 and count_letters == len(self.input):
            print(f"Word accepted!\nStack = {self.stack}")
            self.accept = True
            return

# Read JSON file
import json

with open('automaton.json', 'r') as file:
    data = json.load(file)
    states_data = data["pda"]["states"]
    stack = []
    states = []

    for state_name, state_data in states_data.items():
        transitions = []

        for transition_data in state_data[0:]:
            label_parts = transition_data["label"].split(',')
            transitions.append(Transition(
                symbol_read     = label_parts[0],
                symbol_top_pull = label_parts[1],
                symbol_push     = label_parts[2],
                state           = transition_data["next"],
            ))
            # print(f"{label_parts[0]},{label_parts[1]},{label_parts[2]}")

        states.append(State(
            name        = state_name,
            transitions = transitions,
            stack       = stack
        ))

    # Define the input
    input_string = data["tests"]["accept"]

    # Define the start state and final state
    for state in states:
        if state.get_name() == data["start"]:
            start_state = state
        if state.get_name() == data["final"]: # Still is only one state, it needs to be a list of final states
            final_states = state

def format_transition(transition):
    symbol_read = "ε" if transition.symbol_read == "" else transition.symbol_read
    symbol_top_pull = "ε" if transition.symbol_top_pull == "" else transition.symbol_top_pull
    symbol_push = "ε" if transition.symbol_push == "" else transition.symbol_push
    return f'{symbol_read},{symbol_top_pull},{symbol_push}'

def generate_dot_format(states, start_state, final_states):
    dot = ['digraph G {', 'rankdir=LR;', 'size = "8.5"', '', f'node [shape = doublecircle];{final_states.get_name()};', 'node [shape = none]; qi', 'node [shape = circle];', '', 'qi-> ' + start_state.get_name() + ';']

    for state in states:
        for transition in state.get_transitions():
            next_state = transition.state
            label = format_transition(transition)

            dot.append(f'{state.get_name()} -> {next_state} [label = "{label}"];')

    dot.append('}')

    return '\n'.join(dot)

# Assuming you have already defined start_state, states, and final_states
dot_format = generate_dot_format(states, start_state, final_states)
print(dot_format)


# Create the automaton
automaton = AutomatonStack(start_state, states, final_states, input_string, stack)
automaton.read_input()
