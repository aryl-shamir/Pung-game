# Pung-game
Creating a simple pung game, using the turtle graphic library, two paddle, endless fun. 

# 🏓 Pung Game

---

## ✅ Project Milestones

This project was developed by completing the following steps:

### 🎯 TODO.1 - Create the screen
- Initialized the game window using `turtle.Screen()`
- Set screen dimensions, background color, and title
- Disabled auto screen updates to control refresh manually with `screen.update()`

### 🎯 TODO.2 - Create and move a paddle
- Created a `Paddle` class inheriting from `Turtle`
- Used `shapesize()` and `penup()` to form a vertical paddle
- Enabled movement via keyboard input (`Up` and `Down` arrow keys)

### 🎯 TODO.3 - Create another paddle
- Reused the `Paddle` class to instantiate a second paddle on the opposite side
- Controlled using `W` (up) and `S` (down)

### 🎯 TODO.4 - Create the ball and make it move
- Created a `Ball` class to handle ball behavior
- Ball moves diagonally and bounces when hitting the top or bottom wall

### 🎯 TODO.5 - Detect collision with wall and make it bounce
- Ball reverses its vertical direction (`y`) when hitting screen boundaries

### 🎯 TODO.6 - Detect collision with paddle
- When the ball gets close to either paddle and is within range, it bounces in the opposite horizontal direction (`x`)
- Ball speed increases slightly on every successful paddle hit

### 🎯 TODO.7 - Detect when paddle misses
- If the ball crosses the left or right edge without hitting a paddle, the opponent scores a point
- Ball resets to the center and restarts movement

### 🎯 TODO.8 - Keep score
- Implemented a `Scoreboard` class using `Turtle`
- Each time a paddle misses, the opponent’s score increases and is updated on the screen

---

Pung-game/
│
├── main.py # Main game loop
├── paddle.py # Paddle class for player control
├── ball.py # Ball class for movement and collision logic
├── scoreboard.py # Score tracking and display
└── README.md # Project overview and instructions

## 🧠 Game Mechanics

- Right Paddle Controls: `↑` (Up), `↓` (Down)
- Left Paddle Controls: `W` (Up), `S` (Down)
- Ball speed increases after each paddle bounce
- Game runs in a `while` loop, updating the ball position, handling collisions, and tracking score

---

## 📦 Requirements

- No external libraries needed — uses built-in `turtle` and `time`

---

## 🚀 How to Run

1. Download or clone this repository
2. Ensure you have Python installed
3. Run the game:

🐛 Issues Encountered
Bug: Multiple rapid bounces when the ball hits a paddle.

Cause: This happens because the ball still overlaps with the paddle in subsequent frames due to its movement speed and loop delay. The distance condition (ball.distance(paddle) < 50) continues to be True for multiple frames, causing multiple bounces in quick succession.

Fix: A logic condition was added to check the ball’s movement direction (x_move) before bouncing.

🧩 Explanation of the Fix
ball.x_move controls how far the ball moves horizontally per frame.

If x_move > 0, the ball is moving right.

If x_move < 0, the ball is moving left.

Solution logic:
Only bounce if the ball is hitting the paddle in the correct direction:

If the ball is moving right (x_move > 0), only bounce when hitting the right paddle.

If the ball is moving left (x_move < 0), only bounce when hitting the left paddle.

✅ This ensures that the ball only bounces once per paddle hit, not multiple times in a row.

This ensures that the ball only bounces once per paddle hit, not multiple times in quick succession.


 
