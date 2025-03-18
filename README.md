# Hi-Lo Probability Calculator

A simple Python program using Tkinter that calculates the probability of drawing a card higher, lower, or equal to the selected card in a Hi-Lo game. The program helps players understand the probability of their next card in a deck, based on the card they input.

## Features
- Enter a card (2-10, Jack, Queen, King, Ace) to calculate the probability.
- Displays the probability of the next card being:
  - Higher
  - Lower
  - The same value
- User-friendly interface created using Tkinter.

## Requirements
- Python 3.x
- Tkinter (usually comes pre-installed with Python)

## How to Use
1. Run the script.
2. Enter a card value in the input field. You can enter the card as a number (2-10) or as a face card (J, Q, K, A).
3. Click the "Hitung Probabilitas" button to calculate the probabilities.
4. The results will display the chances of the next card being higher, lower, or the same.

## Example
For example:
- If you input "J" (Jack), the program will calculate the probabilities of the next card being higher, lower, or the same value as Jack.
  
## Code Overview
1. **convert_card(card)**: Converts the input card into a numerical value (e.g., "A" becomes 14, "K" becomes 13).
2. **calculate_probability(card, deck)**: Calculates the probability of drawing a higher, lower, or the same card from the deck.
3. **calculate()**: Retrieves the card input from the user, calls the necessary functions, and displays the result.
