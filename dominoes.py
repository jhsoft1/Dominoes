import random
full_list = []
for i in range(7):
    for j in range(i + 1):
        full_list.append(tuple([j, i]))
full_set = set(full_list)
reshuffle = True
while reshuffle:
    stock = set(random.sample(full_set, 14))
    non_stock = full_set - stock
    computer = random.sample(non_stock, 7)
    player = list(non_stock - set(computer))
    player_highest_double = computer_highest_double = -1
    for i in range(7):
        if tuple([i, i]) in computer: computer_highest_double = i
        if tuple([i, i]) in player: player_highest_double = i
    if computer_highest_double > player_highest_double:
        status = "player"
        domino = [tuple([computer_highest_double, computer_highest_double])]
        computer.remove(domino[0])
        reshuffle = False
    elif computer_highest_double < player_highest_double:
        status = "computer"
        domino = [tuple([player_highest_double, player_highest_double])]
        player.remove(domino[0])
        reshuffle = False
    else: reshuffle = True
game_over = False
while not game_over:
    print(70 * "=")
    print('Stock size:', len(stock))
    print('Computer pieces:', len(computer),'\n')
    if len(domino) > 6:
        d = [list(x) for x in domino]
        print(d[0], d[1], d[2], '...', d[-3], d[-2], d[-1], sep="")
    else:
        for x in domino:
            print(list(x), end='')
    print('\nYour pieces:\n')
    for index, stone in enumerate(player):
        print(index+1, list(stone),sep=':')
    print('\nStatus:',end=' ')
    if status == 'player':
        print("It's your turn to make a move. Enter your command.")
        valid_command = False
        while not valid_command:
            try:
                command = int(input())
                if command > 0:
                    if domino[-1][1] == player[command - 1][0]:
                        domino = domino + [player[command - 1]]
                        del player[command - 1]
                        valid_command = True
                    elif domino[-1][1] == player[command - 1][1]:
                        domino = domino + [(player[command - 1][1], player[command - 1][0])]
                        del player[command - 1]
                        valid_command = True
                    else:
                        print('Illegal move. Please try again.')
                elif command < 0:
                    if domino[0][0] == player[-command - 1][1]:
                        domino = domino + [player[-command - 1]]
                        del player[-command - 1]
                        valid_command = True
                    elif domino[0][0] == player[-command - 1][0]:
                        domino = [(player[-command - 1][1], player[-command - 1][0])] + domino
                        del player[-command - 1]
                        valid_command = True
                    else:
                        print('Illegal move. Please try again.')
                elif len(stock) == 0:
                    print("Status: The game is over. It's a draw!")
                    exit(0)
                else:
                    player.append(stock.pop())
                    valid_command = True
            except (IndexError, ValueError):
                print("Invalid input. Please try again.")
            else:
                if len(player) == 0:
                    status = "player_win"
                else:
                    status = "computer"
    elif status == 'computer':
        input("Computer is about to make a move. Press Enter to continue...")
        command = 1
        computer_single_list = []
        domino_single_list = []
        for piece in computer:
            computer_single_list += [piece[0], piece[1]]
        for piece in domino:
            domino_single_list += [piece[0], piece[1]]
        count = {}
        for i in range(7):
            count[i] = computer_single_list.count(i) + domino_single_list.count(i)
        scores = {}
        for i, piece in enumerate(computer):
            scores[i] = count[piece[0]] + count[piece[1]]
        sorted_scores = dict(sorted(scores.items(), key=lambda item: item[1], reverse=True))
        # print(computer, count, scores, sorted_scores)
        len_computer_old = len(computer)
        for command in sorted_scores:
            if domino[-1][1] == computer[command][0]:
                domino = domino + [computer[command]]
                del computer[command]
                break
            elif domino[-1][1] == computer[command][1]:
                domino = domino + [(computer[command][1], computer[command][0])]
                del computer[command]
                break
            elif domino[0][0] == computer[command][1]:
                domino = domino + [computer[command]]
                del computer[command]
                break
            elif domino[0][0] == computer[command][0]:
                domino = [(computer[command][1], computer[command][0])] + domino
                del computer[command]
                break
        if len_computer_old == len(computer):
            if len(stock) == 0:
                print("Status: The game is over. It's a draw!")
                exit(0)
            else:
                computer.append(stock.pop())
        if len(computer) == 0:
            status = "computer_win"
        else:
            status = "player"
    elif status == 'player_win':
        print('The game is over. You won!')
        exit()
    elif status == 'computer_win':
        print('The game is over. The computer won!')
        exit()
    else:
        print("The game is over. It's a draw!")
        exit()
