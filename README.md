# Endless Tic-Tac-Toe

**Video Demo:** https://youtu.be/KM_Tcb1YbcI

> Disclaimer: This project is made to fulfill the requirements of CS50P Certificate

## Introduction

Welcome to Endless tic-tac-toe, a twist on the classic tic-tac-toe game where you can only have max of 3 marks on the game board! This game allows players to continuously play by relocating their moves once they have filled their move queue. It's a fun and strategic variation that keeps players engaged and thinking several steps ahead.

## Game Rules

Endless tic-tac-toe follows the basic rules of traditional tic-tac-toe with an added twist. Here’s how it works:

1. **Objective**: The objective of the game is to be the first to get three of your marks in a row (vertically, horizontally, or diagonally).
2. **Turn Order**: The game starts with either the player or the computer, depending on the player's choice of 'X' or 'O'. 'O' always goes first.
3. **Relocation**: Each player has a move queue that can hold up to three moves. When the queue is full, the oldest move is relocated to a new position chosen by the player.
4. **Winning**: The game checks for a win after every move. A win is declared if a player manages to place three of their marks in a row, column, or diagonal.
5. **Camping**: You can't choose to put at the same location of the mark that need to relocate. This is known as camping. Be smart and strategize your move!

## Features

- **Interactive Gameplay**: The game offers an interactive gameplay experience where players can continuously play without restarting.
- **Computer Opponent**: Players can compete against a computer opponent with random move selection.
- **Move Queue**: Players and the computer each have a move queue that adds strategic depth to the game.
- **Win Detection**: The game automatically checks for win conditions after each move and announces the winner.

## How to Play

1. **Start the Game**: Run the main script to start the game.
2. **Choose Your Mark**: When prompted, choose either 'X' or 'O'. 'O' goes first.
3. **Player's Turn**: Input the number of the tile where you want to place your mark.
4. **Computer's Turn**: The computer will randomly select an available tile for its mark.
5. **Relocate Moves**: Once your move queue is full (after three moves), you will need to relocate your oldest move to a new tile.
6. **Win Condition**: The game will automatically check for a win after each move. If you get three of your marks in a row, column, or diagonal, you win!

## Installation

To install and run Endless tic-tac-toe, follow these steps:

1. **Clone the Repository**: Clone the project repository from GitHub to your local machine.

    ```sh
    git clone https://github.com/tasyadew/endless-tic-tac-toe.git
    cd endless-tic-tac-toe
    ```

2. **Dependencies**: Ensure you have Python installed on your machine. The game uses standard libraries such as `random`, `time`, and `queue`.

    ```sh
    pip install -r requirements.txt
    ```

3. **Run the Game**: Execute the main script to start the game.

    ```sh
    python main.py
    ```

## Future Improvements

Here are some potential improvements and additional features that could be added to Endless tic-tac-toe:

1. **Enhanced AI**: Improve the computer opponent’s strategy using more advanced algorithms.
2. **Multiplayer Mode**: Add a multiplayer mode to allow two players to compete against each other.
3. **Graphical Interface**: Develop a graphical user interface (GUI) to make the game more visually appealing and user-friendly.
4. **Difficulty Levels**: Implement different difficulty levels for the computer opponent to cater to players of varying skill levels.
5. **Move History**: Display a history of moves for players to review their strategy.
6. **Sound Effects**: Add sound effects to enhance the gaming experience.

## Conclusion

Endless tic-tac-toe offers an engaging and strategic twist on the classic game. With continuous gameplay and the added challenge of managing a move queue, it provides a fresh and exciting experience for players. Whether you are competing against a computer opponent or strategizing your next move, Endless tic-tac-toe is sure to provide hours of entertainment. Enjoy the game and may the best player win!
