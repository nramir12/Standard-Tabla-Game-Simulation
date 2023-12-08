import random

random_draw_list = random.sample(range(1, 55), 54)

combo_index = []
combo_value = []
def generate_cards():
    card1 = [[1, 2, 3, 4],
             [10, 11, 12, 13],
             [19, 20, 21, 22],
             [28, 29, 30, 31]]

    card2 = [[6, 7, 8, 9],
             [15, 16, 17, 18],
             [24, 25, 26, 27],
             [33, 34, 35, 36]]

    card3 = [[2, 3, 4, 5],
             [7, 8, 9, 10],
             [12, 13, 14, 15],
             [17, 18, 19, 20]]

    card4 = [[25, 26, 27, 41],
             [34, 35, 36, 46],
             [43, 44, 45, 51],
             [52, 53, 54, 32]]

    card5 = [[21, 22, 23, 24],
             [30, 31, 32, 33],
             [39, 40, 41, 42],
             [48, 49, 50, 51]]

    card6 = [[41, 42, 37, 38],
             [50, 51, 46, 47],
             [5, 6, 1, 2],
             [14, 15, 10, 11]]

    card7 = [[39, 40, 19, 20],
             [48, 49, 28, 29],
             [3, 4, 37, 38],
             [12, 13, 46, 47]]

    card8 = [[22, 23, 24, 25],
             [27, 28, 29, 30],
             [32, 33, 34, 35],
             [37, 38, 39, 40]]

    card9 = [[43, 44, 45, 21],
             [52, 53, 54, 26],
             [7, 8, 9, 31],
             [16, 17, 18, 36]]

    card10 = [[42, 43, 44, 45],
              [47, 48, 49, 50],
              [52, 53, 54, 1],
              [40, 10, 19, 20]]

    card11 = [[9, 5, 11, 16],
              [46, 54, 31, 48],
              [6, 35, 39, 14],
              [24, 13, 23, 53]]

    card12 = [[1, 2, 44, 45],
              [10, 11, 49, 13],
              [19, 53, 21, 32],
              [40, 29, 30, 22]]

    card13 = [[36, 7, 45, 21],
              [15, 16, 54, 18],
              [24, 8, 26, 27],
              [9, 17, 35, 6]]

    card14 = [[20, 3, 24, 25],
              [7, 8, 29, 10],
              [12, 33, 14, 15],
              [37, 38, 19, 2]]

    card15 = [[32, 26, 33, 20],
              [34, 35, 28, 46],
              [43, 4, 45, 51],
              [52, 13, 54, 25]]

    card16 = [[51, 22, 37, 38],
              [30, 31, 46, 33],
              [39, 6, 41, 42],
              [14, 15, 50, 21]]

    card17 = [[11, 42, 23, 38],
              [50, 51, 32, 47],
              [5, 40, 1, 2],
              [48, 49, 10, 41]]

    card18 = [[52, 40, 27, 41],
              [48, 49, 36, 29],
              [3, 44, 37, 38],
              [12, 53, 46, 39]]

    card19 = [[40, 23, 4, 5],
              [27, 28, 9, 30],
              [32, 13, 34, 35],
              [37, 18, 39, 22]]

    card20 = [[36, 44, 8, 16],
              [52, 53, 17, 26],
              [7, 25, 9, 31],
              [33, 34, 18, 47]]

    all_cards = [card1, card2, card3, card4, card5, card6, card7, card8, card9, card10, card11, card12, card13, card14,
                 card15, card16, card17, card18, card19, card20]

    combo = random.sample(list(enumerate(all_cards)), 2)
    for idx, val in combo:
        combo_index.append(idx)
        combo_value.append(val)


    return combo_value

ball_list = []


def call_ball():
    number_drawn = random_draw_list.pop()

    ball_list.append(number_drawn)

    return number_drawn

def mark(combo_value):
    ball = call_ball()

    for q in combo_value:  # check if list has number replace number with x
        for i in range(len(q)):
            for j in range(len(q)):
                if q[i][j] == ball:
                    q[i][j] = 'X'

card_num = []
lot_type = []

def check_win(combo_value):
    win = False
    for q in combo_value:
        # col
        if q[0][0] == 'X' and q[1][0] == 'X' and q[2][0] == 'X' and q[3][0] == 'X':
            win = True
            print("WINNER col0")
            index = combo_value.index(q)
            card_num.append(index + 1)
            type = 'Col0'
            lot_type.append(type)
            print(q)
        elif q[0][1] == 'X' and q[1][1] == 'X' and q[2][1] == 'X' and q[3][1] == 'X':
            win = True
            print("WINNER col1")
            index = combo_value.index(q)
            card_num.append(index + 1)
            type = 'Col1'
            lot_type.append(type)
            print(q)
        elif q[0][2] == 'X' and q[1][2] == 'X' and q[2][2] == 'X' and q[3][2] == 'X':
            win = True
            print("WINNER col2")
            index = combo_value.index(q)
            card_num.append(index + 1)
            type = 'Col2'
            lot_type.append(type)
            print(q)
        elif q[0][3] == 'X' and q[1][3] == 'X' and q[2][3] == 'X' and q[3][3] == 'X':
            win = True
            print("WINNER col3")
            index = combo_value.index(q)
            card_num.append(index + 1)
            type = 'Col3'
            lot_type.append(type)
            print(q)
        # row
        elif q[0][0] == 'X' and q[0][1] == 'X' and q[0][2] == 'X' and q[0][3] == 'X':
            win = True
            print("WINNER row0")
            index = combo_value.index(q)
            card_num.append(index + 1)
            type = 'Row0'
            lot_type.append(type)
            print(q)
        elif q[1][0] == 'X' and q[1][1] == 'X' and q[1][2] == 'X' and q[1][3] == 'X':
            win = True
            print("WINNER row1")
            index = combo_value.index(q)
            card_num.append(index + 1)
            type = 'Row1'
            lot_type.append(type)
            print(q)
        elif q[2][0] == 'X' and q[2][1] == 'X' and q[2][2] == 'X' and q[2][3] == 'X':
            win = True
            print("WINNER row2")
            index = combo_value.index(q)
            card_num.append(index + 1)
            type = 'Row2'
            lot_type.append(type)
            print(q)
        elif q[3][0] == 'X' and q[3][1] == 'X' and q[3][2] == 'X' and q[3][3] == 'X':
            win = True
            print("WINNER row3")
            index = combo_value.index(q)
            card_num.append(index + 1)
            type = 'Row3'
            lot_type.append(type)
            print(q)
        # diag
        elif q[0][0] == 'X' and q[1][1] == 'X' and q[2][2] == 'X' and q[3][3] == 'X':
            win = True
            print("WINNER diag1")
            index = combo_value.index(q)
            card_num.append(index + 1)
            type = 'diag1'
            lot_type.append(type)
            print(q)
        elif q[0][3] == 'X' and q[1][2] == 'X' and q[2][1] == 'X' and q[3][0] == 'X':
            win = True
            print("WINNER diag2")
            index = combo_value.index(q)
            card_num.append(index + 1)
            type = 'diag2'
            lot_type.append(type)
            print(q)
        # four corners
        elif q[0][0] == 'X' and q[3][0] == 'X' and q[0][3] == 'X' and q[3][3] == 'X':
            win = True
            print("WINNER outside4")
            index = combo_value.index(q)
            card_num.append(index + 1)
            type = 'outside4'
            lot_type.append(type)
            print(q)
        elif q[1][1] == 'X' and q[1][2] == 'X' and q[2][1] == 'X' and q[2][2] == 'X':
            win = True
            print("WINNER inside4")
            index = combo_value.index(q)
            card_num.append(index + 1)
            type = 'inside4'
            lot_type.append(type)
            print(q)
    return win

def game():
    # print("Let's play bingo!")
    cards = generate_cards()
    # add start game please

    win = check_win(cards)
    balls_till_win = 0

    while win == False:
        mark(cards)
        balls_till_win += 1

        win = check_win(cards)

    if win == True:
        print(f"\nCards Used: {combo_index}")

        print(f"\nCard Winner: {card_num}")
        # print(len(card_num))
        print(f"\nNumbers drawn: {ball_list}")
        # print(len(ball_list))
        print(f"\nBINGO! Total balls to win: {balls_till_win}")
        r = ' '.join(str(y) for y in combo_index)

        s = ' '.join(str(x) for x in card_num)
        # print(s)
        t = ' '.join(str(y) for y in ball_list)
        # print(t)
        u = ' '.join(str(x) for x in lot_type)

        cardsfile = open('hun_cardsused.txt', 'a')
        cardfile = open('hun_cardwinner.txt', 'a')
        ballfile = open('hun_balls_drawn.txt', 'a')
        typefile = open('hun_lot_type.txt', 'a')
        numfile = open('hun_avgnum.txt', 'a')
        cardsfile.write(r + '\n')
        cardfile.write(s + '\n')
        ballfile.write(t + '\n')
        typefile.write(u + '\n')
        numfile.write(str(balls_till_win) + '\n')
        cardsfile.close()
        cardfile.close()
        ballfile.close()
        typefile.close()
        numfile.close()
        print("____________________________________________________________________")

    else:
        print("Goodbye! Thanks for playing")

    reset_game()

def reset_game():
    # print(random_draw_list)
    random_draw_list.extend(ball_list)
    # print(random_draw_list)
    random.shuffle(random_draw_list)
    # print(random_draw_list)

    ball_list.clear()
    card_num.clear()
    lot_type.clear()
    combo_index.clear()
    combo_value.clear()

    number_drawn = random_draw_list.pop()  # removes last element of list
    # print(number_drawn)

    ball_list.append(number_drawn)

def main():
    for g in range(100):
        print(f"GAME: {g + 1}")
        game()


main()
