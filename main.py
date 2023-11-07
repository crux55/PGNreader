import sys
import chess.pgn
import chess.engine

STOCK_ENGINE_PATH = ""

def suggest_next_move(pgn_file_path):

    with open(pgn_file_path) as pgn_file:
        game = chess.pgn.read_game(pgn_file)

        if game is None:
            print("No games found in the PGN file.")
            return

        board = game.board()
        for move in game.mainline_moves():
            board.push(move)

        print("Current position:")
        print(board)

        # Initialize a chess engine
        with chess.engine.SimpleEngine.popen_uci(STOCK_ENGINE_PATH) as engine:
            info = engine.analyse(board, chess.engine.Limit(time=0.1))
            suggested_move = info["pv"][0]

            # Print the suggested move
            print("Suggested move:", board.san(suggested_move))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python suggest_move.py <pgn_file>")
        sys.exit(1)

    pgn_file_path = sys.argv[1]
    suggest_next_move(pgn_file_path)
