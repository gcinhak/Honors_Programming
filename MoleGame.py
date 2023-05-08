import time # to check the game time
import random # to randomly assign the mole
import curses # to manage  the string in the terminal
import threading # devide into section, display and input


class MoleGame:
    mole = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] #Position of the mole
    score = 0 # reset the score
    game_time = 30 # set the game time in second
    game_over = False # check the game is over


def clear(stdscr):
    stdscr.clear()


def display(stdscr): # show the mole position 0 to '_' and 1 to '&'
    for m in MoleGame.mole:
        if m == 0:
            stdscr.addstr("_ ")
        else:
            stdscr.addstr("& ")


def reset_mole(): #every 1.3 seconds reset the mole position
    for i in range(len(MoleGame.mole)):
        MoleGame.mole[i] = 0


def set_mole(): # randomly assign one mole position
    MoleGame.mole[random.randint(0, 9)] = 1


def show_hit_effect(stdscr, idx): # change the mole '&' to 'X'
    clear(stdscr)
    for i in range(len(MoleGame.mole)):
        if i == idx:
            stdscr.addstr("X ")
        else:
            stdscr.addstr("_ ")
    stdscr.addstr(f"\n\nScore: {MoleGame.score}\nTime: {int(MoleGame.game_time - (time.time() - start_time))}s")
    stdscr.refresh()
    time.sleep(0.1)


def display_loop(stdscr): # threading dislplay
    global start_time
    while not MoleGame.game_over:
        elapsed_time = time.time() - start_time
        if elapsed_time >= MoleGame.game_time:
            MoleGame.game_over = True
            break

        set_mole()
        clear(stdscr)
        display(stdscr)
        stdscr.addstr(f"\n\nScore: {MoleGame.score}\nTime: {int(MoleGame.game_time - elapsed_time)}s")
        stdscr.refresh()
        time.sleep(1.3)
        reset_mole()


def input_loop(stdscr): # threading user's input
    while not MoleGame.game_over:
        player_input = stdscr.getch()
        if player_input != -1 and ord('0') <= player_input <= ord('9'):
            player_input -= ord('0')  # Get input as integer

            if player_input != 0:
                player_input -= 1
            else:
                player_input = 9

            if MoleGame.mole[player_input] == 1:
                MoleGame.score += 1
                show_hit_effect(stdscr, player_input)
                reset_mole()


def main(stdscr): #The main process of the game
    global start_time

    curses.curs_set(0)  # Hide cursor
    stdscr.timeout(100)  # Non-blocking input
    start_time = time.time()

    stdscr.addstr("The mole game begins! Catch as many moles as you can in 30 seconds!\nUse number key on your keyboard!\n")
    stdscr.refresh()
    time.sleep(2)

    display_thread = threading.Thread(target=display_loop, args=(stdscr,))
    input_thread = threading.Thread(target=input_loop, args=(stdscr,))

    display_thread.start()
    input_thread.start()

    display_thread.join()
    input_thread.join()

    clear(stdscr)
    stdscr.addstr(f"The game is over.\nYour score is  {MoleGame.score}\n")
    stdscr.refresh()
    time.sleep(3)


if __name__ == '__main__':
    curses.wrapper(main)