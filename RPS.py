def player(prev_play, opponent_moves=[], my_moves=[], move_patterns={}, kris_tendency=[0]):
    """
    Rock-Paper-Scissors AI with a hybrid strategy:
    1. If the opponent behaves like Kris (always countering our last move), we switch to a counter-exploit strategy.
    2. Otherwise, we use a Markov chain approach, analyzing the last three moves to predict the next move.
    """

    # Reset tracking data for a new game
    if prev_play == '':
        opponent_moves.clear()
        my_moves.clear()
        move_patterns.clear()
        kris_tendency[0] = 0
        return 'R'  # Start with Rock

    # Store the opponent's move if it's valid
    if prev_play in ['R', 'P', 'S']:
        opponent_moves.append(prev_play)

    # Check if the opponent is exhibiting "Kris-like" behavior
    if my_moves:
        last_move = my_moves[-1]
        counters = {'R': 'P', 'P': 'S', 'S': 'R'}
        if prev_play == counters[last_move]:  # They keep countering our last move
            kris_tendency[0] += 1

    # Determine if we are facing Kris based on behavior
    rounds_played = len(opponent_moves)
    if rounds_played > 5 and (kris_tendency[0] / rounds_played) > 0.45:
        is_kris = True
    else:
        is_kris = False

    if is_kris:
        # Kris counters our last move, so we counter Kris's expected move
        if my_moves:
            last_move = my_moves[-1]
            anti_kris_moves = {'R': 'S', 'P': 'R', 'S': 'P'}
            next_move = anti_kris_moves[last_move]
        else:
            next_move = 'R'  # Default to Rock if no history exists
    else:
        # Use a Markov chain strategy if the opponent isn't Kris
        if not move_patterns:
            sequences = [a + b + c for a in 'RPS' for b in 'RPS' for c in 'RPS']
            move_patterns.update({seq: {'R': 0, 'P': 0, 'S': 0} for seq in sequences})

        # Update frequency of move patterns
        if len(opponent_moves) > 3:
            last_three_moves = ''.join(opponent_moves[-4:-1])  # Get the last three moves (excluding the newest)
            following_move = opponent_moves[-1]  # The move that followed this pattern
            move_patterns[last_three_moves][following_move] += 1

        # Predict the next move and counter it
        next_move = 'R'  # Default choice
        if len(opponent_moves) >= 3:
            last_three_moves = ''.join(opponent_moves[-3:])
            if last_three_moves in move_patterns:
                most_likely = max(move_patterns[last_three_moves], key=move_patterns[last_three_moves].get)
                counter_moves = {'R': 'P', 'P': 'S', 'S': 'R'}
                next_move = counter_moves[most_likely]

    # Store our own move for tracking
    my_moves.append(next_move)
    return next_move
