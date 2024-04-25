WHITE = 0
BLACK = 1

KING = 0
QUEEN = 1
ROOK = 2
KNIGHT = 3
BISHOP = 4
PAWN = 5

KING_IMG = '♚'
QUEEN_IMG = '♛'
ROOK_IMG = '♜'
KNIGHT_IMG = '♞'
BISHOP_IMG = '♝'
PAWN_IMG = '♟'

ON = 0
OFF = 1

IMPOSSIBLE_COUNT = 33

translator = {
    "1": "A",
    "2": "B",
    "3": "C",
    "4": "D",
    "5": "E",
    "6": "F",
    "7": "G",
    "8": "H"
}

START_HTML_BOARD = ("\
<!DOCTYPE html> \n\
    <html  lang='ru'> \n\
    <head> \n\
        <title></title> \n\
        <meta charset='UTF-8'> \n\
    <link rel='stylesheet' href='https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/css/bootstrap.min.css' "
                    "integrity='sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T' "
                    "crossorigin='anonymous'> \n\
  <style> \n\
          body { \n\
      font-family: Arial, sans-serif; \n\
      background-color: #f1f1f1; \n\
      margin: 0; \n\
      padding: 0; \n\
      } \n\
      .container { \n\
          max-width: 800px; \n\
          margin: 50px auto; \n\
      } \n\
      #chess-board { \n\
          border-spacing: 0; \n\
          border-collapse: collapse; \n\
          margin: 0 auto; \n\
      } \n\
      #chess-board th, #chess-board td { \n\
          width: 50px; \n\
          height: 50px; \n\
          text-align: center; \n\
      } \n\
      #chess-board th:empty, #chess-board td:empty { \n\
          border: none; \n\
      } \n\
      #chess-board .light { \n\
          background: #f0d9b5; \n\
          color: #774e28; \n\
      } \n\
      #chess-board .dark { \n\
          background: #b58863; \n\
          color: #ffffff; \n\
      } \n\
      #chess-board th:first-child, \n\
      #chess-board td:last-child { \n\
          border-right: 2px solid #774e28; \n\
      } \n\
      #chess-board tr:last-child td { \n\
          border-bottom: 2px solid #774e28; \n\
      } \n\
      #chess-board th + th { \n\
          border-bottom: 2px solid #774e28; \n\
      } \n\
      #chess-board th, #chess-board td { \n\
          width: 100px; \n\
          text-align: center; \n\
      } \n\
      #chess-board th, #chess-board td { \n\
          font-size: 2em; \n\
      } \n\
      #chess-board th.light, #chess-board td.light { \n\
          background: #f0d9b5; \n\
          color: #774e28; \n\
      } \n\
      #chess-board th.dark, #chess-board td.dark { \n\
          background: #b58863; \n\
          color: #ffffff; \n\
      } \n\
      #chess-board th.white, #chess-board td.white { \n\
          color: #ffffff; \n\
      } \n\
      #chess-board th.black, #chess-board td.black { \n\
          color: #000000; \n\
      } \n\
      #chess-board a { \n\
          display: block; \n\
          width: 100%; \n\
          height: 100%; \n\
          text-decoration: none; \n\
          color: inherit; \n\
      } \n\
      .reload-btn { \n\
          display: block; \n\
          margin: 300px 300px; \n\
          padding: 200px; \n\
          background-color: #774e28; \n\
          color: #ffffff; \n\
          text-align: center; \n\
          text-transform: uppercase; \n\
          border-radius: 5px; \n\
          cursor: pointer; \n\
          float: left; \n\
      } \n\
      .reload-btn:hover { \n\
          background-color: #b58863; \n\
      } \n\
  </style> \n\
  <meta http-equiv='refresh' content='30'> \n\
</head> \n\
<body> \n\
  <table id='chess-board'> \n\
      <tbody> \n\
")

END_HTML_BOARD = "\
            </tbody> \n\
        </table> \n\
        <script> \n\
            document.getElementById('chess-board').addEventListener('click', function(e) { \n\
                if (e.target.tagName === 'TD') { \n\
                    let cellData = e.target.getAttribute('data-value'); \n\
                    fetch('/chess_move', { \n\
                        method: 'POST', \n\
                        body: JSON.stringify({ data: cellData }), \n\
                        headers: { \n\
                            'Content-Type': 'application/json' \n\
                        } \n\
                    }).then(response => { \n\
                    }); \n\
                } \n\
            }); \n\
        </script> \n\
        <button type='button' class='btn btn-primary btn-lg' onClick='window.location.reload()'>RELOAD</button> \n\
"


class Cell:
    def __init__(self, x, y):
        self.col = x
        self.row = y
        self.figure = None

    def print(self):
        if self.figure is None:
            return "  "

        str = ""
        if self.figure.color == WHITE:
            str += 'W'
        else:
            str += 'B'

        if self.figure.fig == KING:
            str += 'K'
        elif self.figure.fig == QUEEN:
            str += 'Q'
        elif self.figure.fig == ROOK:
            str += 'R'
        elif self.figure.fig == KNIGHT:
            str += 'K'
        elif self.figure.fig == BISHOP:
            str += 'B'
        elif self.figure.fig == PAWN:
            str += 'P'

        return str


class Board:
    def __init__(self):
        self.last_status = 0
        self.current_color = WHITE
        self.state = ON
        self.width = 8
        self.height = 8
        self.Cells = [[None] * self.height for i in range(self.width)]

        self.last_cell_from = None
        self.last_cell_to = None

        for x in range(self.width):
            for y in range(self.height):
                self.Cells[x][y] = Cell(x, y)

        self.Cells[0][0].figure = Rook(WHITE)
        self.Cells[1][0].figure = Knight(WHITE)
        self.Cells[2][0].figure = Bishop(WHITE)
        self.Cells[3][0].figure = Queen(WHITE)
        self.Cells[4][0].figure = King(WHITE)
        self.Cells[5][0].figure = Bishop(WHITE)
        self.Cells[6][0].figure = Knight(WHITE)
        self.Cells[7][0].figure = Rook(WHITE)

        self.Cells[0][7].figure = Rook(BLACK)
        self.Cells[1][7].figure = Knight(BLACK)
        self.Cells[2][7].figure = Bishop(BLACK)
        self.Cells[3][7].figure = Queen(BLACK)
        self.Cells[4][7].figure = King(BLACK)
        self.Cells[5][7].figure = Bishop(BLACK)
        self.Cells[6][7].figure = Knight(BLACK)
        self.Cells[7][7].figure = Rook(BLACK)

        for i in range(self.width):
            self.Cells[i][1].figure = Pawn(WHITE)
            self.Cells[i][6].figure = Pawn(BLACK)

    def print(self):
        print('     +----+----+----+----+----+----+----+----+')
        for row in range(self.height - 1, -1, -1):
            print(' ', row + 1, end='  ')
            for col in range(self.width):
                print('|', self.Cells[col][row].print(), end=' ')
            print('|')
            print('     +----+----+----+----+----+----+----+----+')

        print(end='        ')
        for col in range(self.width):
            print(chr(ord('A') + col), end='    ')
        print()

    def get_html(self):
        STR = ""
        cur = "БЕЛЫЕ" if self.current_color == WHITE else "ЧЕРНЫЕ"
        if self.last_status == 1:
            STR = "НЕВЕРНЫЙ ХОД, ХОДЯТ " + cur
        elif self.last_status == 2:
            STR = cur + " ВЫИГРАЛИ"
        elif self.last_status == 3:
            STR = "НИЧЬЯ"
        elif self.last_status == 0:
            STR = "ХОДЯТ " + cur

        END_WITH_TEXT = f"\
                <label>{STR}</label>\n\
            </body> \n\
        </html> \n\
        "

        a = START_HTML_BOARD
        a += "<tr>\n"
        a += "<th></th>\n"
        for i in range(8):
            a += f"<th>{chr(i + ord('A'))}</th>\n"
        a += "</tr>\n"
        for row in range(self.height - 1, -1, -1):
            a += "<tr>\n"
            a += f"<th>{row + 1}</th>\n"
            for col in range(self.width):
                v = 'light' if (row + col) % 2 == 1 else 'dark'
                if self.Cells[col][row].figure is None:
                    a += f"<td class = \"{v}\" data-value = \"{str(row) + str(col)}\"></td>\n"
                    continue

                color = 'white' if self.Cells[col][row].figure.color == WHITE else 'black'
                img = self.Cells[col][row].figure.img
                a += f"<td class = \"{v} {color}\" data-value = \"{str(row) + str(col)}\">{img}</td>\n"
            a += "</tr>\n"
        a += END_HTML_BOARD
        a += END_WITH_TEXT
        d = open("templates/chess.html", "w", encoding="utf-8")
        d.write(a)
        d.close()

    def check_castling(self, cell_from: Cell, cell_to: Cell):
        if cell_from.figure.fig != KING or cell_from.figure.init_state != True:
            return False

        if cell_from.row != cell_to.row or abs(cell_from.col - cell_to.col) != 2:
            return False

        rook_col = 0 if cell_from.col > cell_to.col else 7
        row = cell_from.row

        rook_cell = self.Cells[rook_col][row]
        if rook_cell.figure == None or rook_cell.figure.fig != ROOK or rook_cell.figure.init_state != True:
            return False

        if self.count_figures_between_cells(cell_from, rook_cell) != 2:
            return False

        dist_col = abs(cell_from.col - rook_cell.col) + 1

        if dist_col == 5:
            king = cell_from.figure
            cell_from.figure = None

            for col in range(2, 5):
                self.Cells[col][row].figure = king
                ret = self.is_check(self.current_color)
                self.Cells[col][row].figure = None
                if ret == True:
                    cell_from.figure = king
                    return False

            self.Cells[2][row].figure = king
            self.Cells[3][row].figure = rook_cell.figure
            self.Cells[2][row].figure.init_state = False
            self.Cells[3][row].figure.init_state = False
            rook_cell.figure = None
            return True

        if dist_col == 4:
            king = cell_from.figure
            cell_from.figure = None

            for col in range(4, 7):
                self.Cells[col][row].figure = king
                ret = self.is_check(self.current_color)
                self.Cells[col][row].figure = None
                if ret == True:
                    cell_from.figure = king
                    return False

            self.Cells[6][row].figure = king
            self.Cells[5][row].figure = rook_cell.figure
            self.Cells[6][row].figure.init_state = False
            self.Cells[5][row].figure.init_state = False
            rook_cell.figure = None
            return True

        return False

    def check_pawn_prohod(self, cell_from: Cell, cell_to: Cell):
        if cell_from.figure.fig != PAWN or cell_to.figure != None:
            return False

        diff = 1 if self.current_color == WHITE else -1

        if abs(cell_from.col - cell_to.col) != 1 or cell_to.row - cell_from.row != diff:
            return False

        cell_prohod = self.Cells[cell_to.col][cell_from.row]
        if cell_prohod.figure == None or cell_prohod.figure.fig != PAWN or cell_prohod != self.last_cell_to:
            return False

        cell_prohod_prev = self.Cells[cell_to.col][cell_from.row + 2 * diff]
        if cell_prohod_prev != self.last_cell_from:
            return False

        old_cell_prohod_figure = cell_prohod.figure
        old_cell_from_figure = cell_from.figure

        cell_from.figure = None
        cell_to.figure = old_cell_from_figure
        cell_prohod.figure = None

        if self.is_check(self.current_color):
            cell_to.figure = None
            cell_prohod.figure = old_cell_prohod_figure
            cell_from.figure = old_cell_from_figure
            return False

        return True

    def check_pawn_figure(self, cell_from: Cell, cell_to: Cell):
        if cell_from.figure.fig != PAWN:
            return False

        if cell_to.figure != None and cell_to.figure.color == cell_from.figure.color:
            return False

        diff = 1 if self.current_color == WHITE else -1

        if cell_to.row - cell_from.row != diff:
            return False

        if abs(cell_from.col - cell_to.col) > 1:
            return False

        if abs(cell_from.col - cell_to.col) == 0 and cell_to.figure != None:
            return False

        if abs(cell_from.col - cell_to.col) == 1 and cell_to.figure == None:
            return False

        if cell_to.row != 0 and cell_to.row != 7:
            return False

        old_cell_to_figure = cell_to.figure
        old_cell_from_figure = cell_from.figure

        cell_to.figure = old_cell_from_figure
        cell_from.figure = None

        if self.is_check(self.current_color):
            cell_from.figure = old_cell_from_figure
            cell_to.figure = old_cell_to_figure
            return False

        cell_to.figure = Queen(self.current_color)  # АЗАТ
        cell_to.figure.init_state = False
        return True

    def move_cells(self, cell_from: Cell, cell_to: Cell) -> bool:
        if cell_from == cell_to:
            print(0)
            return False

        if cell_from.figure == None:
            print(1)
            return False

        if cell_from.figure.color != self.current_color:
            print(2)
            return False

        if cell_to.figure != None and cell_from.figure.color == cell_to.figure.color:
            print(3)
            return False

        if self.check_castling(cell_from, cell_to):
            pass
        elif self.check_pawn_prohod(cell_from, cell_to):
            pass
        elif self.check_pawn_figure(cell_from, cell_to):
            pass
        else:
            if cell_from.figure.check_move(self, cell_from, cell_to) == False:
                return False

            old_cell_from_figure = cell_from.figure
            old_cell_to_figure = cell_to.figure

            cell_to.figure = cell_from.figure
            cell_from.figure = None

            if self.is_check(self.current_color):
                cell_from.figure = old_cell_from_figure
                cell_to.figure = old_cell_to_figure
                return False

        reverse_color = WHITE if self.current_color == BLACK else BLACK
        if self.is_checkmate(reverse_color):
            self.print()
            if self.current_color == WHITE:
                print("WHITE WIN")
            else:
                print("BLACK WIN")
            self.last_status = 2
            return True

        if self.is_stalemate(reverse_color):
            self.print()
            print("STALEMATE")
            self.last_status = 3
            return True

        self.last_status = 0
        self.last_cell_from = cell_from
        self.last_cell_to = cell_to
        cell_to.figure.init_state = False
        self.current_color = reverse_color
        return True

    def move(self, cells):
        if self.last_status == 2 or self.last_status == 3:
            return False

        self.last_status = 1

        if len(cells) != 2 or len(cells[0]) != 2 or len(cells[1]) != 2:
            return False

        if not (cells[0][0] >= 'A' and cells[0][0] <= 'H' and cells[0][1] >= '1' and cells[0][1] <= '8'):
            return False

        if not (cells[1][0] >= 'A' and cells[1][0] <= 'H' and cells[1][1] >= '1' and cells[1][1] <= '8'):
            return False

        cell_from = self.Cells[ord(cells[0][0]) - ord('A')][ord(cells[0][1]) - ord('1')]
        cell_to = self.Cells[ord(cells[1][0]) - ord('A')][ord(cells[1][1]) - ord('1')]

        print(cell_from, cell_to)

        return self.move_cells(cell_from, cell_to)

    def count_in_col(self, col, row1, row2):
        if row2 < row1:
            row1, row2 = row2, row1
        count = 0
        for row in range(row1, row2 + 1):
            if self.Cells[col][row].figure != None:
                count += 1
        return count

    def count_in_row(self, row, col1, col2):
        if col2 < col1:
            col1, col2 = col2, col1
        count = 0
        for col in range(col1, col2 + 1):
            if self.Cells[col][row].figure != None:
                count += 1
        return count

    def count_in_first_diag(self, col1, row1, col2, row2):
        if col2 < col1:
            col1, col2 = col2, col1
            row1, row2 = row2, row1

        row = row1
        col = col1
        count = 0
        while col <= col2:
            if self.Cells[col][row].figure != None:
                count += 1
            row += 1
            col += 1
        return count

    def count_in_second_diag(self, col1, row1, col2, row2):
        if col2 < col1:
            col1, col2 = col2, col1
            row1, row2 = row2, row1

        row = row1
        col = col1
        count = 0
        while col <= col2:
            if self.Cells[col][row].figure != None:
                count += 1
            row -= 1
            col += 1
        return count

    def count_figures_between_cells(self, cell_from, cell_to):
        # по вертикали
        if cell_from.col == cell_to.col:
            return self.count_in_col(cell_from.col, cell_from.row, cell_to.row)

        # по горизонтали
        if cell_from.row == cell_to.row:
            return self.count_in_row(cell_from.row, cell_from.col, cell_to.col)

        # по обратной диагонали
        if cell_from.col - cell_from.row == cell_to.col - cell_to.row:
            return self.count_in_first_diag(cell_from.col, cell_from.row, cell_to.col, cell_to.row)

        # по главной диагонали
        if cell_from.col + cell_from.row == cell_to.col + cell_to.row:
            return self.count_in_second_diag(cell_from.col, cell_from.row, cell_to.col, cell_to.row)

        # невозможное значение
        return IMPOSSIBLE_COUNT

    def cell_is_correct(self, col, row):
        return (col >= 0 and col < self.width and row >= 0 and row < self.height)

    def get_king(self, color):
        for i in range(self.width):
            for j in range(self.height):
                cell = self.Cells[i][j]
                if cell.figure == None:
                    continue
                if cell.figure.fig == KING and cell.figure.color == color:
                    return cell
        assert 0

    def is_any_move_for_cell(self, cell):
        color = cell.figure.color
        for col in range(self.width):
            for row in range(self.height):
                if col == cell.col and row == cell.row:
                    continue

                cur_cell = self.Cells[col][row]

                if not cell.figure.check_move(self, cell, cur_cell):
                    continue

                old_cell_figure = cell.figure
                old_cur_cell_figure = cur_cell.figure
                cur_cell.figure = cell.figure
                cell.figure = None

                flag = self.is_check(color)

                cell.figure = old_cell_figure
                cur_cell.figure = old_cur_cell_figure

                if not flag:
                    return True
        return False

    def is_any_move(self, color):
        for col in range(self.width):
            for row in range(self.height):
                cell = self.Cells[col][row]
                if cell.figure == None or cell.figure.color != color:
                    continue

                if self.is_any_move_for_cell(cell):
                    return True

        return False

    def is_check(self, color):
        king = self.get_king(color)

        for i in range(self.width):
            for j in range(self.height):
                cell = self.Cells[i][j]
                if cell.figure == None or cell.figure.color == color:
                    continue

                if cell.figure.check_move(self, cell, king):
                    return True
        return False

    def is_checkmate(self, color):
        check_flag = self.is_check(color)
        move_flag = self.is_any_move(color)

        return check_flag and (not move_flag)

    def is_stalemate(self, color):
        check_flag = self.is_check(color)
        move_flag = self.is_any_move(color)

        return (not check_flag) and (not move_flag)


class Figure:
    color = 0
    fig = 0
    init_state = True
    img = 0


class Pawn(Figure):
    def __init__(self, color):
        self.fig = PAWN
        self.color = color
        self.init_state = True
        self.img = PAWN_IMG

    def check_move(self, board: Board, cell_from: Cell, cell_to: Cell):
        diff = 1 if self.color == WHITE else -1

        # Сдвиг пешки на 1 позицию
        if ((board.count_figures_between_cells(cell_from, cell_to) == 1) and
                (cell_from.col == cell_to.col) and (cell_to.row - cell_from.row == diff)):
            return True

        # Сдвиг пешки на 2 позиции
        if ((board.count_figures_between_cells(cell_from, cell_to) == 1) and (self.init_state == True) and
                (cell_from.col == cell_to.col) and (cell_to.row - cell_from.row == 2 * diff)):
            return True

        # Съесть фигуру рядом
        if ((cell_to.figure != None) and (abs(cell_from.col - cell_to.col) == 1) and
                (cell_to.row - cell_from.row == diff)):
            return True

        return False


class Rook(Figure):
    def __init__(self, color):
        self.fig = ROOK
        self.color = color
        self.init_state = True
        self.img = ROOK_IMG

    def check_move(self, board: Board, cell_from: Cell, cell_to: Cell):
        if cell_from.col != cell_to.col and cell_from.row != cell_to.row:
            return False

        count = board.count_figures_between_cells(cell_from, cell_to)

        # Просто ход
        if count == 1:
            return True

        # Съел
        if count == 2 and cell_to.figure != None and self.color != cell_to.figure.color:
            return True
        return False


class Knight(Figure):
    def __init__(self, color):
        self.fig = KNIGHT
        self.color = color
        self.init_state = True
        self.img = KNIGHT_IMG
        self.delta_col = [1, 1, -1, -1, 2, 2, -2, 2]
        self.delta_row = [2, -2, 2, -2, 1, -1, 1, -1]

    def check_move(self, board: Board, cell_from: Cell, cell_to: Cell):
        for i in range(len(self.delta_col)):
            d_col = self.delta_col[i]
            d_row = self.delta_row[i]

            if cell_from.col + d_col != cell_to.col or cell_from.row + d_row != cell_to.row:
                continue

            if cell_to.figure == None:
                return True

            if self.color != cell_to.figure.color:
                return True

        return False


class Bishop(Figure):
    def __init__(self, color):
        self.fig = BISHOP
        self.color = color
        self.init_state = True
        self.img = BISHOP_IMG

    def check_move(self, board: Board, cell_from: Cell, cell_to: Cell):
        if ((cell_from.col + cell_from.row != cell_to.col + cell_to.row) and
                (cell_from.col - cell_from.row != cell_to.col - cell_to.row)):
            return False

        count = board.count_figures_between_cells(cell_from, cell_to)

        if count == 1:
            return True

        if count == 2 and cell_to.figure != None and self.color != cell_to.figure.color:
            return True
        return False


class Queen(Figure):
    def __init__(self, color):
        self.fig = QUEEN
        self.color = color
        self.init_state = True
        self.img = QUEEN_IMG

    def check_move(self, board: Board, cell_from: Cell, cell_to: Cell):
        count = board.count_figures_between_cells(cell_from, cell_to)

        if count == 1:
            return True

        if count == 2 and cell_to.figure != None and self.color != cell_to.figure.color:
            return True
        return False


class King(Figure):
    def __init__(self, color):
        self.fig = KING
        self.color = color
        self.init_state = True
        self.img = KING_IMG
        self.delta_col = [1, 1, 1, 0, 0, -1, -1, -1]
        self.delta_row = [1, 0, -1, 1, -1, 1, 0, -1]

    def check_move(self, board: Board, cell_from: Cell, cell_to: Cell):
        is_correct = False
        king_is_near = False

        for i in range(len(self.delta_col)):
            d_col = self.delta_col[i]
            d_row = self.delta_row[i]
            if cell_from.col + d_col == cell_to.col and cell_from.row + d_row == cell_to.row:
                is_correct = True

            new_col = cell_to.col + d_col
            new_row = cell_to.row + d_row

            if not board.cell_is_correct(new_col, new_row):
                continue

            figure = board.Cells[new_col][new_row].figure
            if figure != None and figure.fig == KING and figure.color != self.color:
                king_is_near = True

        if is_correct == False or king_is_near == True:
            return False

        if cell_to.figure == None:
            return True

        if self.color != cell_to.figure.color:
            return True
        return False


if __name__ == '__main__':
    board = Board()
    board.print()
    while board.state == ON:
        cells = input().split()
        if board.move(cells) == False:
            print("Incorrect move")
            continue

        board.print()