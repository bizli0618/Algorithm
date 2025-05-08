def right_set(chess: list) -> list:
    need_chess = [1, 1, 2, 2, 2, 8]
    num_chess = []
    for idx, num in enumerate(need_chess):
        num_chess.append(num - chess[idx])

    return num_chess

if __name__== "__main__":
    white_chess = list(map(int, input().split()))
    num_chessses = right_set(white_chess)
    for chess in num_chessses:
        print(chess, end=" ")
