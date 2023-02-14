def poker_ranking(query: str = None) -> str:
    """
    Function to identify the poker hand given an input query.
    Identifies the correct hand based on a set of rules.
    Args:
        query (str): The input hand. This is a string of the form `VS VS VS VS VS`, 
        where V is the value and S is the suit, and a space denotes a different card.
    Returns:
        A string of the description of the hand.
    """
    # Convert letter values to numbers in order to manipulate more easily
    value_mapping = {"J": "11", "Q": "12", "K": "13", "A": "14"}
    # TODO: INCLUDE FACT THAT "A" CAN ALSO COUNT AS VALUE 1
    suit_mapping = {"H": "hearts", "D": "diamonds", "S": "spades", "C": "clubs"}
    
    try:
        query = query.split(" ")
        values = sorted([int(value_mapping[card[0:-1]]) if card[0:-1] in value_mapping.keys() else int(card[0:-1]) for card in query])
        suits = [card[-1] for card in query]

        # Identify straight and flush conditions
        is_straight = (max(values) - min(values) == 4) and (len(set(values)) == 5)
        is_flush = len(set(suits)) == 1

        # map values back to original
        new_values = ["Ace" if value == 14 else "King" if value == 13 else "Queen" if value == 12 else "Jack" if value == 11 else str(value) for value in values]

        # Run through logic to identify different hands in order of priority
        if (len(set(query)) != 5) or (max(values) > 14) or (min(values) < 2) or (len(suits) != 5) or (set(suits).intersection(suit_mapping.keys()) != set(suits)):
            return "invalid hand: hand should be of the format `VS VS VS VS VS` where V and S are valid values and suits, and cards are distinct"
        elif is_straight and is_flush and "Ace" in new_values:
            return f"royal flush: {suit_mapping[suits[0]]}"
        elif is_straight and is_flush:
            return f"straight flush: {new_values[-1]}-high {suit_mapping[suits[0]]}"
        elif len(set(new_values)) == 2:
            if new_values.count(new_values[0]) in (1, 4):
                return f"four of a kind: {new_values[0]}" if new_values.count(new_values[0])==4 else f"four of a kind: {new_values[-1]}"
            else:
                return f"full house: {new_values[0]} over {new_values[-1]}" if new_values.count(new_values[0])==3 else f"full house: {new_values[-1]} over {new_values[0]}"
        elif is_flush:
            return f"flush: {suit_mapping[suits[0]]}"
        elif is_straight:
            return f"straight: {new_values[-1]}-high"
        elif len(set(new_values)) == 3:
            if new_values.count(new_values[2]) == 3:
                return f"three of a kind: {new_values[2]}"
            else:
                return f"two pair: {new_values[-2]} and {new_values[1]}"
        elif len(set(new_values)) == 4:
            return f"one pair: {new_values[1]}" if new_values.count(new_values[1])==2 else f"one pair: {new_values[3]}"
        else:
            return f"high card: {new_values[-1]}"
    except (KeyError, ValueError):
        # In case of incorrectly inputted hand
        return "invalid hand: hand should be of the format `VS VS VS VS VS` where V and S are valid values and suits, and cards are distinct"