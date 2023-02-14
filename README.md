# Poker Hand Ranking

This repo contains the code in order to create a simple API that returns the poker ranking of a given hand.

## Repo Structure

This repo contains the following:
- `code`, the folder which contains the ranking and API scripts, as well as corresponding tests;
- `requirements.txt`, containing all requirements to run code in the `code` folder.

## Pre-requisites
- Python 3 (Python 3.7.12 was used to create this API)

## Usage

Clone the repo. Create a Python virtual environment and run `pip install -r requirements.txt` to install required dependencies. Then navigate to the `code` folder.

To run the tests, run `python ranking_tests.py` or `python api_tests.py`.

To launch the API, run `python api.py`. Then open a new terminal window and run the following example command to use the API:
`curl --header "Content-Type: application/json" \
       --request POST \
       --data '{"query": "10H KH JH QH AH"}' \
       http://localhost:5000/rank`.

You can modify the `data` field to submit different poker hands for ranking.

## Known Bugs

The API always considers Ace to be a high card, so does not correctly identify straights where the Ace can be used as a low card. This is noted as a TODO in the `ranking.py` script.
