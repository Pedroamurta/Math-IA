from itertools import product

def is_valid_pattern(pattern):
    """Check if a feedback pattern is logically possible in Wordle."""
    if pattern == "YYYYY":
        return False
    
    return True

def generate_wordle_patterns():
    """Generate all valid Wordle feedback patterns."""
    feedback_states = ['G', 'Y', 'B']
    all_patterns = [''.join(pattern) for pattern in product(feedback_states, repeat=5)]
    
    # Filter out invalid patterns
    valid_patterns = [pattern for pattern in all_patterns if is_valid_pattern(pattern)]
    
    return valid_patterns

# Generate and print valid Wordle patterns
valid_patterns = generate_wordle_patterns()
print(f"Number of valid patterns: {len(valid_patterns)}")
print(valid_patterns)
