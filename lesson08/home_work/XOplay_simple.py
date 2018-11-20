

# Ни  классы, ни  ИИ, увы, не сделал -  нет совсем времени на реализацию сейчас.
# решение через функции и без графической оболочки для 2х живых игроков

print ("\n Игра в крестики-нолики \n" )
board = list(range(1,26))

def draw_board(board):
    print ("-" * 26)
    for i in range(5):
        print ("|", board[0+i*5], "|", board[1+i*5], "|", board[2+i*5],"|", board[3+i*5], "|", board[4+i*5], "|")
        print ("-" * 26)

def take_input(player_token):
    valid = False
    while not valid:
        player_answer = input("Куда поставим " + player_token+"? ")
        try:
            player_answer = int(player_answer)
        except:
            print ("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if player_answer >= 1 and player_answer <= 25:
            if (str(board[player_answer-1]) not in "XO"):
                board[player_answer-1] = player_token
                valid = True
            else:
                print ("Эта клетка уже занята")
        else:
            print ("Некорректный ввод. Введите число от 1 до 25 чтобы походить.")

def check_win(board):
    win_coord = ((1,2,3,4,5),(6,7,8,9,10),(11,12,13,14,15),(16,17,18,19,20),(21,22,23,24,25),\
                 (1,6,11,16,21),(2,7,12,17,22),(3,8,13,18,23),(4,9,14,19,24),(5,10,15,20,25),\
                (1,7,13,19,25),(5,9,13,17,21))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]== board[each[3]]== board[each[4]]:
            return board[each[0]]
    return False

def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        if counter > 9:
            tmp = check_win(board)
            if tmp:
                print (tmp, "выиграл!")
                win = True
                break
        if counter == 25:
            print ("Ничья!")
            break
    draw_board(board)

main(board)
