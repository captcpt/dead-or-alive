# dead-or-alive
Simple text-based game based on the "Dead or Alive" game from Alice in Borderland (Show Adaptation, EP1).

## How to Play
In the folder run the following command, and follow the prompts to play.
```terminal
python main.py
```
![Sample Run of the Game](/images/sample_game.png)

### File Structure
* questions.py: function ask_question() which contains a dictionary of possible questions/answers for puzzles, and returns boolean and randomint for correct/wrong responses (and their subsequent time effects)
  * 2 Basic Questions; can add more and/or provide alternate types of questions in the dictionary
* game_engine.py: main logic structure for the game; Also contains:
  * draw_grid(): Represents map/player position for each turn
  * Title sequence of game
