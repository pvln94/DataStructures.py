NO_OF_CHARS = 256

def get_next_state(pattern, pattern_len, current_state, char):
    """
    Calculate the next state for the given character and current state.
    """
    # If the character matches the next character in the pattern, increment the state
    if current_state < pattern_len and char == ord(pattern[current_state]):
        return current_state + 1

    # Otherwise, find the longest prefix which is also a suffix
    for next_state in range(current_state, 0, -1):
        if ord(pattern[next_state - 1]) == char:
            if pattern[:next_state - 1] == pattern[current_state - next_state + 1:current_state]:
                return next_state
    return 0

def build_transition_table(pattern, pattern_len):
    """
    Build the transition table for the finite automaton.
    """
    transition_table = [[0] * NO_OF_CHARS for _ in range(pattern_len + 1)]

    for state in range(pattern_len + 1):
        for char in range(NO_OF_CHARS):
            transition_table[state][char] = get_next_state(pattern, pattern_len, state, char)
    
    return transition_table

def finite_automata_search(pattern, text):
    """
    Search for all occurrences of the pattern in the text using the finite automaton.
    """
    pattern_len = len(pattern)
    text_len = len(text)
    transition_table = build_transition_table(pattern, pattern_len)

    current_state = 0
    for i in range(text_len):
        current_state = transition_table[current_state][ord(text[i])]
        if current_state == pattern_len:
            print(f"Pattern found at index: {i - pattern_len + 1}")

# Driver code to test the function
if __name__ == '__main__':
    text = "AABAACAADAABAAABAA"
    pattern = "AABA"
    finite_automata_search(pattern, text)
