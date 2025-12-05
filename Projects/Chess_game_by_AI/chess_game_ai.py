import pygame
import sys
from typing import List, Tuple, Optional

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 640, 640
BOARD_SIZE = 8
SQUARE_SIZE = WIDTH // BOARD_SIZE
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_SQUARE = (240, 217, 181)
DARK_SQUARE = (181, 136, 99)
HIGHLIGHT = (100, 249, 83, 150)  # Semi-transparent green
MOVE_HIGHLIGHT = (249, 166, 83, 150)  # Semi-transparent orange
CHECK_HIGHLIGHT = (255, 0, 0, 150)  # Semi-transparent red

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Advanced Chess Game")
clock = pygame.time.Clock()

# Load piece images (simplified - using text for pieces in this example)
# In a full implementation, you would load actual images
font = pygame.font.SysFont('Arial', 40)

class Piece:
    def __init__(self, color: str, piece_type: str, position: Tuple[int, int]):
        self.color = color  # 'white' or 'black'
        self.piece_type = piece_type  # 'pawn', 'rook', 'knight', 'bishop', 'queen', 'king'
        self.position = position
        self.has_moved = False
        
    def __str__(self):
        return f"{self.color[0]}{self.piece_type[0].upper()}"
    
    def draw(self, surface):
        x, y = self.position
        rect = pygame.Rect(x * SQUARE_SIZE, y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
        
        # Create a simple text representation
        text_color = WHITE if self.color == 'white' else BLACK
        bg_color = BLACK if self.color == 'white' else WHITE
        
        # Draw piece background
        pygame.draw.rect(surface, bg_color, rect)
        pygame.draw.rect(surface, text_color, rect, 2)
        
        # Draw piece symbol
        symbols = {
            'pawn': 'P', 'rook': 'R', 'knight': 'N', 
            'bishop': 'B', 'queen': 'Q', 'king': 'K'
        }
        text = font.render(symbols[self.piece_type], True, text_color)
        text_rect = text.get_rect(center=rect.center)
        surface.blit(text, text_rect)

class Board:
    def __init__(self):
        self.squares = [[None for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        self.selected_piece = None
        self.valid_moves = []
        self.turn = 'white'
        self.check = False
        self.checkmate = False
        self.stalemate = False
        self.en_passant_target = None
        self.move_history = []
        self.initialize_board()
        
    def initialize_board(self):
        # Initialize pawns
        for x in range(BOARD_SIZE):
            self.squares[x][1] = Piece('white', 'pawn', (x, 1))
            self.squares[x][6] = Piece('black', 'pawn', (x, 6))
        
        # Initialize other pieces
        back_row = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook']
        for x, piece_type in enumerate(back_row):
            self.squares[x][0] = Piece('white', piece_type, (x, 0))
            self.squares[x][7] = Piece('black', piece_type, (x, 7))
    
    def draw(self, surface):
        # Draw board squares
        for y in range(BOARD_SIZE):
            for x in range(BOARD_SIZE):
                color = LIGHT_SQUARE if (x + y) % 2 == 0 else DARK_SQUARE
                rect = pygame.Rect(x * SQUARE_SIZE, y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
                pygame.draw.rect(surface, color, rect)
                
                # Highlight selected piece
                if self.selected_piece and self.selected_piece.position == (x, y):
                    highlight = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE), pygame.SRCALPHA)
                    highlight.fill(HIGHLIGHT)
                    surface.blit(highlight, rect)
                
                # Highlight valid moves
                if (x, y) in self.valid_moves:
                    highlight = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE), pygame.SRCALPHA)
                    highlight.fill(MOVE_HIGHLIGHT)
                    surface.blit(highlight, rect)
                
                # Highlight king in check
                if self.check:
                    king_pos = self.find_king(self.turn)
                    if king_pos == (x, y):
                        highlight = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE), pygame.SRCALPHA)
                        highlight.fill(CHECK_HIGHLIGHT)
                        surface.blit(highlight, rect)
        
        # Draw pieces
        for y in range(BOARD_SIZE):
            for x in range(BOARD_SIZE):
                if self.squares[x][y]:
                    self.squares[x][y].draw(surface)
    
    def select_piece(self, pos: Tuple[int, int]):
        x, y = pos
        if 0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE:
            piece = self.squares[x][y]
            if piece and piece.color == self.turn:
                self.selected_piece = piece
                self.valid_moves = self.get_valid_moves(piece)
                return True
        return False
    
    def move_piece(self, target_pos: Tuple[int, int]) -> bool:
        if not self.selected_piece or target_pos not in self.valid_moves:
            return False
        
        start_x, start_y = self.selected_piece.position
        target_x, target_y = target_pos
        
        # Save move for history
        move_info = {
            'piece': self.selected_piece,
            'start': (start_x, start_y),
            'target': target_pos,
            'captured': self.squares[target_x][target_y]
        }
        
        # Handle en passant capture
        if (self.selected_piece.piece_type == 'pawn' and 
            self.en_passant_target == target_pos and
            start_x != target_x and not self.squares[target_x][target_y]):
            # Remove the captured pawn
            captured_pawn_y = start_y  # The pawn that moved two squares
            self.squares[target_x][captured_pawn_y] = None
            move_info['en_passant_capture'] = (target_x, captured_pawn_y)
        
        # Handle castling
        if (self.selected_piece.piece_type == 'king' and 
            abs(target_x - start_x) == 2):
            # Determine rook position and new rook position
            if target_x > start_x:  # Kingside castling
                rook_start_x, rook_target_x = 7, 5
            else:  # Queenside castling
                rook_start_x, rook_target_x = 0, 3
            
            # Move the rook
            rook = self.squares[rook_start_x][start_y]
            self.squares[rook_start_x][start_y] = None
            self.squares[rook_target_x][start_y] = rook
            rook.position = (rook_target_x, start_y)
            rook.has_moved = True
            move_info['castling'] = (rook_start_x, start_y, rook_target_x, start_y)
        
        # Move the piece
        self.squares[target_x][target_y] = self.selected_piece
        self.squares[start_x][start_y] = None
        self.selected_piece.position = target_pos
        self.selected_piece.has_moved = True
        
        # Handle pawn promotion
        if (self.selected_piece.piece_type == 'pawn' and 
            (target_y == 0 or target_y == 7)):
            # Promote to queen (in a full implementation, you'd let the player choose)
            self.squares[target_x][target_y] = Piece(
                self.selected_piece.color, 'queen', target_pos
            )
            move_info['promotion'] = 'queen'
        
        # Update en passant target
        self.en_passant_target = None
        if (self.selected_piece.piece_type == 'pawn' and 
            abs(target_y - start_y) == 2):
            self.en_passant_target = (target_x, (start_y + target_y) // 2)
        
        # Add move to history
        self.move_history.append(move_info)
        
        # Switch turn
        self.turn = 'black' if self.turn == 'white' else 'white'
        
        # Check for check/checkmate
        self.check = self.is_in_check(self.turn)
        if self.check:
            if self.is_checkmate(self.turn):
                self.checkmate = True
        elif self.is_stalemate(self.turn):
            self.stalemate = True
        
        # Clear selection
        self.selected_piece = None
        self.valid_moves = []
        
        return True
    
    def get_valid_moves(self, piece: Piece) -> List[Tuple[int, int]]:
        moves = []
        x, y = piece.position
        
        if piece.piece_type == 'pawn':
            # Pawn movement
            direction = 1 if piece.color == 'white' else -1
            
            # Move forward one square
            if 0 <= y + direction < BOARD_SIZE and not self.squares[x][y + direction]:
                moves.append((x, y + direction))
                
                # Move forward two squares from starting position
                if ((piece.color == 'white' and y == 1) or 
                    (piece.color == 'black' and y == 6)) and not self.squares[x][y + 2 * direction]:
                    moves.append((x, y + 2 * direction))
            
            # Capture diagonally
            for dx in [-1, 1]:
                if 0 <= x + dx < BOARD_SIZE and 0 <= y + direction < BOARD_SIZE:
                    target = self.squares[x + dx][y + direction]
                    if target and target.color != piece.color:
                        moves.append((x + dx, y + direction))
                    
                    # En passant
                    if (x + dx, y + direction) == self.en_passant_target:
                        moves.append((x + dx, y + direction))
        
        elif piece.piece_type == 'knight':
            # Knight movement (L-shape)
            for dx, dy in [(2, 1), (1, 2), (-1, 2), (-2, 1), 
                          (-2, -1), (-1, -2), (1, -2), (2, -1)]:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < BOARD_SIZE and 0 <= new_y < BOARD_SIZE:
                    target = self.squares[new_x][new_y]
                    if not target or target.color != piece.color:
                        moves.append((new_x, new_y))
        
        elif piece.piece_type == 'bishop':
            # Bishop movement (diagonals)
            for dx, dy in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
                for i in range(1, BOARD_SIZE):
                    new_x, new_y = x + i * dx, y + i * dy
                    if not (0 <= new_x < BOARD_SIZE and 0 <= new_y < BOARD_SIZE):
                        break
                    
                    target = self.squares[new_x][new_y]
                    if not target:
                        moves.append((new_x, new_y))
                    else:
                        if target.color != piece.color:
                            moves.append((new_x, new_y))
                        break
        
        elif piece.piece_type == 'rook':
            # Rook movement (orthogonals)
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                for i in range(1, BOARD_SIZE):
                    new_x, new_y = x + i * dx, y + i * dy
                    if not (0 <= new_x < BOARD_SIZE and 0 <= new_y < BOARD_SIZE):
                        break
                    
                    target = self.squares[new_x][new_y]
                    if not target:
                        moves.append((new_x, new_y))
                    else:
                        if target.color != piece.color:
                            moves.append((new_x, new_y))
                        break
        
        elif piece.piece_type == 'queen':
            # Queen movement (diagonals + orthogonals)
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1),
                          (1, 1), (1, -1), (-1, 1), (-1, -1)]:
                for i in range(1, BOARD_SIZE):
                    new_x, new_y = x + i * dx, y + i * dy
                    if not (0 <= new_x < BOARD_SIZE and 0 <= new_y < BOARD_SIZE):
                        break
                    
                    target = self.squares[new_x][new_y]
                    if not target:
                        moves.append((new_x, new_y))
                    else:
                        if target.color != piece.color:
                            moves.append((new_x, new_y))
                        break
        
        elif piece.piece_type == 'king':
            # King movement (one square in any direction)
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == 0 and dy == 0:
                        continue
                    
                    new_x, new_y = x + dx, y + dy
                    if 0 <= new_x < BOARD_SIZE and 0 <= new_y < BOARD_SIZE:
                        target = self.squares[new_x][new_y]
                        if not target or target.color != piece.color:
                            # Temporarily move king to check if square is safe
                            original_piece = self.squares[new_x][new_y]
                            self.squares[x][y] = None
                            self.squares[new_x][new_y] = piece
                            
                            if not self.is_in_check(piece.color):
                                moves.append((new_x, new_y))
                            
                            # Restore position
                            self.squares[x][y] = piece
                            self.squares[new_x][new_y] = original_piece
            
            # Castling
            if not piece.has_moved and not self.is_in_check(piece.color):
                # Kingside castling
                if (self.squares[7][y] and 
                    self.squares[7][y].piece_type == 'rook' and 
                    not self.squares[7][y].has_moved and
                    not self.squares[5][y] and 
                    not self.squares[6][y] and
                    not self.is_square_attacked((5, y), piece.color) and
                    not self.is_square_attacked((6, y), piece.color)):
                    moves.append((6, y))
                
                # Queenside castling
                if (self.squares[0][y] and 
                    self.squares[0][y].piece_type == 'rook' and 
                    not self.squares[0][y].has_moved and
                    not self.squares[1][y] and 
                    not self.squares[2][y] and 
                    not self.squares[3][y] and
                    not self.is_square_attacked((2, y), piece.color) and
                    not self.is_square_attacked((3, y), piece.color)):
                    moves.append((2, y))
        
        # Filter out moves that would leave the king in check
        valid_moves = []
        for move in moves:
            if self.is_move_safe(piece, move):
                valid_moves.append(move)
        
        return valid_moves
    
    def is_move_safe(self, piece: Piece, target_pos: Tuple[int, int]) -> bool:
        # Simulate the move
        start_x, start_y = piece.position
        target_x, target_y = target_pos
        
        # Save original state
        original_target = self.squares[target_x][target_y]
        self.squares[target_x][target_y] = piece
        self.squares[start_x][start_y] = None
        original_position = piece.position
        piece.position = target_pos
        
        # Check if king is in check after the move
        safe = not self.is_in_check(piece.color)
        
        # Restore original state
        self.squares[start_x][start_y] = piece
        self.squares[target_x][target_y] = original_target
        piece.position = original_position
        
        return safe
    
    def is_in_check(self, color: str) -> bool:
        king_pos = self.find_king(color)
        if not king_pos:
            return False
        
        return self.is_square_attacked(king_pos, color)
    
    def is_square_attacked(self, pos: Tuple[int, int], color: str) -> bool:
        x, y = pos
        opponent_color = 'black' if color == 'white' else 'white'
        
        # Check for attacks from pawns
        pawn_direction = 1 if color == 'black' else -1
        for dx in [-1, 1]:
            if (0 <= x + dx < BOARD_SIZE and 0 <= y + pawn_direction < BOARD_SIZE and
                self.squares[x + dx][y + pawn_direction] and
                self.squares[x + dx][y + pawn_direction].piece_type == 'pawn' and
                self.squares[x + dx][y + pawn_direction].color == opponent_color):
                return True
        
        # Check for attacks from knights
        for dx, dy in [(2, 1), (1, 2), (-1, 2), (-2, 1), 
                      (-2, -1), (-1, -2), (1, -2), (2, -1)]:
            new_x, new_y = x + dx, y + dy
            if (0 <= new_x < BOARD_SIZE and 0 <= new_y < BOARD_SIZE and
                self.squares[new_x][new_y] and
                self.squares[new_x][new_y].piece_type == 'knight' and
                self.squares[new_x][new_y].color == opponent_color):
                return True
        
        # Check for attacks from bishops, rooks, and queens
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1),  # Rook directions
                     (1, 1), (1, -1), (-1, 1), (-1, -1)]  # Bishop directions
        
        for dx, dy in directions:
            for i in range(1, BOARD_SIZE):
                new_x, new_y = x + i * dx, y + i * dy
                if not (0 <= new_x < BOARD_SIZE and 0 <= new_y < BOARD_SIZE):
                    break
                
                target = self.squares[new_x][new_y]
                if not target:
                    continue
                
                if target.color != opponent_color:
                    break
                
                # Check for rook/queen on orthogonal lines
                if (dx == 0 or dy == 0) and target.piece_type in ['rook', 'queen']:
                    return True
                
                # Check for bishop/queen on diagonal lines
                if (dx != 0 and dy != 0) and target.piece_type in ['bishop', 'queen']:
                    return True
                
                # If we encounter any piece, stop checking in this direction
                break
        
        # Check for attacks from the king
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                
                new_x, new_y = x + dx, y + dy
                if (0 <= new_x < BOARD_SIZE and 0 <= new_y < BOARD_SIZE and
                    self.squares[new_x][new_y] and
                    self.squares[new_x][new_y].piece_type == 'king' and
                    self.squares[new_x][new_y].color == opponent_color):
                    return True
        
        return False
    
    def find_king(self, color: str) -> Optional[Tuple[int, int]]:
        for x in range(BOARD_SIZE):
            for y in range(BOARD_SIZE):
                piece = self.squares[x][y]
                if piece and piece.piece_type == 'king' and piece.color == color:
                    return (x, y)
        return None
    
    def is_checkmate(self, color: str) -> bool:
        if not self.is_in_check(color):
            return False
        
        # Check if any piece can make a move that gets out of check
        for x in range(BOARD_SIZE):
            for y in range(BOARD_SIZE):
                piece = self.squares[x][y]
                if piece and piece.color == color:
                    valid_moves = self.get_valid_moves(piece)
                    if valid_moves:
                        return False
        
        return True
    
    def is_stalemate(self, color: str) -> bool:
        if self.is_in_check(color):
            return False
        
        # Check if any piece can make a legal move
        for x in range(BOARD_SIZE):
            for y in range(BOARD_SIZE):
                piece = self.squares[x][y]
                if piece and piece.color == color:
                    valid_moves = self.get_valid_moves(piece)
                    if valid_moves:
                        return False
        
        return True

def main():
    board = Board()
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    x, y = event.pos
                    board_x, board_y = x // SQUARE_SIZE, y // SQUARE_SIZE
                    
                    if board.selected_piece:
                        # Try to move the selected piece
                        if not board.move_piece((board_x, board_y)):
                            # If move failed, try to select a new piece
                            board.select_piece((board_x, board_y))
                    else:
                        # Select a piece
                        board.select_piece((board_x, board_y))
        
        # Draw everything
        screen.fill(BLACK)
        board.draw(screen)
        
        # Display game status
        status_font = pygame.font.SysFont('Arial', 24)
        if board.checkmate:
            winner = 'Black' if board.turn == 'white' else 'White'
            status_text = f"Checkmate! {winner} wins!"
        elif board.stalemate:
            status_text = "Stalemate! Game is a draw."
        elif board.check:
            status_text = f"{board.turn.capitalize()} is in check!"
        else:
            status_text = f"{board.turn.capitalize()}'s turn"
        
        status_surface = status_font.render(status_text, True, WHITE)
        screen.blit(status_surface, (10, 10))
        
        pygame.display.flip()
        clock.tick(FPS)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()