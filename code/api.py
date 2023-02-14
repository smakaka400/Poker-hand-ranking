from flask import Flask, request, jsonify
from ranking import poker_ranking

app = Flask(__name__)

@app.route('/rank', methods=['POST'])
def rank_hand():
    """
    Flask app function to create an API at route /rank, returning the poker hand given an input hand.
    Uses the poker_ranking function to calculate the ranking.
    Args:
        None
    Returns:
        A jsonified string of the ranking of the hand.
    """
    query = request.json['query']
    ranking = poker_ranking(query)
    return jsonify(ranking)

if __name__ == '__main__':
    app.run(debug=True)