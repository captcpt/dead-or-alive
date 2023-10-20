# dead-or-alive
Simple text-based game based on the "Dead or Alive" game from Alice in Borderland (show adaptation; EP1).

## How to Play
In the folder run the following command, and follow the prompts to play.
```terminal
python main.py
```

### File Structure
* questions.py: function ask_question() which contains a dictionary of possible questions/answers for puzzles, and returns boolean and randomint for correct/wrong responses (and their subsequent time effects)
* game_engine.py: main logic structure for the game; Also contains:
  * draw_grid(): Represents map/player position for each turn
  * Title sequence of game
