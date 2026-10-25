import random
import time


def play_reflex_game():
    print("====================================")
    print("      ⚡ REFLEX LASER TEST ⚡       ")
    print("====================================")
    print("Instructions:")
    print("1. When you see 'FIRE! 🔥', press ENTER as fast as you can.")
    print("2. Don't press early, or you will get a penalty!\n")

    input("Press Enter when you are ready to test your reflexes... ")
    print("Get ready...")

    wait_time = random.uniform(2.0, 5.0)
    time.sleep(wait_time)

    print("\n>>> FIRE! 🔥 <<<")
    reaction_start = time.perf_counter()
    input("")
    reaction_time = (time.perf_counter() - reaction_start) * 1000

    print(f"\n⏱️ Your reaction time: {reaction_time:.2f} ms")

    if reaction_time < 200:
        print("🏆 INCREDIBLE! Are you even human? Lightning fast!")
    elif reaction_time < 350:
        print("🔥 Great reflexes! Well above average.")
    elif reaction_time < 500:
        print("👍 Not bad. Solid human reaction time.")
    else:
        print("🐢 A bit slow! Were you sleeping on the keyboard?")


if __name__ == "__main__":
    while True:
        play_reflex_game()
        again = input("\nTry again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break
