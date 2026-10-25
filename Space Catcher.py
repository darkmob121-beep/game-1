import os
import random
import time 

def clear_screen():
    """Clears the terminal screen for smooth animation."""
    os.system('cls' if os.name == 'nt' else 'clear')

def play_space_catcher():
    width = 15
    height = 10
    player_x = width // 2

    score = 0
    lives = 3
    game_speed = 0.18

    items = []

    print("====================================")
    print("      🚀 SPACE CATCHER 🚀           ")
    print("====================================")
    print("Controls:")
    print("  'a' -> Move Left")
    print("  'd' -> Move Right")
    print("  'q' -> Quit Game")
    print("\nCatch stars (⭐) for points!")
    print("Dodge space debris (💥) or lose lives!")
    input("\nPress Enter to Start...")

    while lives > 0:
        clear_screen()

        # 1. Spawn new objects
        if random.random() < 0.4:
            item_type = "star" if random.random() < 0.6 else "debris"
            items.append({"x": random.randint(0, width - 1), "y": 0, "type": item_type})

        # 2. Build grid
        screen = []
        for y in range(height):
            row = [" . "] * width
            screen.append(row)

        for item in items:
            if 0 <= item["y"] < height:
                if item["type"] == "star":
                    screen[item["y"]][item["x"]] = " ⭐"
                else:
                    screen[item["y"]][item["x"]] = " 💥"

        screen[height - 1][player_x] = " 🚀"

        # 3. Print UI
        print(f"Score: {score}   |   Lives: {'❤️ ' * lives}")
        print("=" * (width * 3))
        for row in screen:
            print("".join(row))
        print("=" * (width * 3))

        # 4. Input
        print("Move: [a] left | [d] right  | [q] quit")
        move = input("Action: ").strip().lower()

        if move == "a" and player_x > 0:
            player_x -= 1
        elif move == "d" and player_x < width - 1:
            player_x += 1
        elif move == "q":
            print("Thanks for playing!")
            break 

        # 5. Move items down
        for item in items:
            item["y"] += 1

   
        # 6. Check collisions (handled safely outside single-item loop)
        for item in items[:]:
            if item["y"] == height - 1 and item["x"] == player_x:
                if item["type"] == "star":
                    score += 10
                elif item["type"] == "debris":
                    lives -= 1
                items.remove(item)
            elif item["y"] >= height:
                items.remove(item) 

        time.sleep(game_speed)

    # Game Over Screen (Properly placed outside the while loop)
    clear_screen()
    print("====================================")
    print("            GAME OVER               ")
    print("====================================")
    print(f"Final Score: {score} points!")

if __name__ == "__main__":
    play_space_catcher()