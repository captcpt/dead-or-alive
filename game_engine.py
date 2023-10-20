import random
from datetime import datetime
import time 
from questions import ask_question

def draw_grid(player_position):
    grid = [
        "+---+---+---+",
        "|   |   |   |",
        "+---+---+---+",
        "|   |   |   |",
        "+---+---+---+",
        "|   |   |   |",
        "+---+---+---+"
    ]

    # Player position
    row, col = divmod(player_position, 3)

    # Player Position marking
    grid[2 * row + 1] = grid[2 * row + 1][:4 * col + 1] + "X" + grid[2 * row + 1][4 * col + 2:]

    for row in grid:
        print(row)

def play_dead_or_alive():
    while True:
        description = "In each room, select a door marked Life or Death. One door will let you move on to the next room, and the other door will result in death. You need to make it through all the rooms to survive and stay alive."
        start_prompt = "Ready to Start?"

        title = "Dead or Alive"
        clubs = "♣       ♣       ♣"
        separator = '-' * 13 

        print(separator + title.center(14) + separator)
        print(clubs.center(40))
        print(description.center(5))
        print(start_prompt)


        while True:
            choice = input("Enter 'Yes' to start or 'No' to quit: ").strip().lower()
            if choice == "yes":
                break
            elif choice == "no":
                print("Goodbye!")
                return

        total_time = 120  # 2 minutes in seconds
        current_room = 1
        start_time = datetime.now()
        player_position = 0

        while total_time > 0:
            elapsed_time = (datetime.now() - start_time).total_seconds()
            remaining_time = total_time - elapsed_time

            print("Map:")
            draw_grid(player_position)
            print(f"Time left: {remaining_time} seconds")

            next_room = random.randint(1, 2)

            choice = input("Choose a door (1 for Live, 2 for Death): ")

            if choice == str(next_room):
                print("Correct choice! You move to the next room.")
                current_room += 1
                total_time -= 10
                player_position += 1  # Move to next room automatically
            else:
                print("Wrong choice! Game over.")
                break

            if current_room == 10:
                print("Congratulations! You have reached the final room.")
                break

            # Introduce a random puzzle in 1-3 rooms
            if current_room < 10 and current_room in random.sample(range(1, 11), random.randint(2, 4)):
                print("You've encountered a puzzle room!")
                choice = input("Do you want to solve the puzzle (Yes/No)? ").lower()

                if choice == "yes":
                    start_puzzle_time = time.time()  # Record the start time of the puzzle
                    correct, time_reward = ask_question()
                    if correct:
                        total_time += time_reward  # Add time

                        # Check if there's another puzzle in the next room
                        next_room_has_puzzle = current_room + 1 < 10 and random.random() < 0.5
                        if next_room_has_puzzle:
                            current_room += 1  # Move to the next room
                            player_position += 1  # Update player's position
                    else:
                        total_time -= time_reward  # Deduct time
                        print("You'll remain in the same room.")
                else:
                    print("You've chosen to skip the puzzle.")

        if current_room < 10:
            print("Out of time. Game over.")

        replay = input("Play again? (Yes/No): ").strip().lower()
        if replay != "yes":
            print("♣ Thanks for playing! ♣ ♣")
            break
