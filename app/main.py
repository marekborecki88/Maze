from tkinter import Tk, Label, Entry, Button, Canvas, mainloop
from typing import Optional

from app.Path import Path

APP_NAME = 'Maze Generator'
BUILD_MAZE_CAPTION = 'Build Maze'
NEW_MAZE_CAPTION = 'New Maze'
SOLVE_MAZE_CAPTION = 'Solve Maze'

CELL_SIZE = 30
cells = {}  # Dictionary to store cell rectangles and their colors

# Global UI components
master: Optional[Tk] = None
label_height: Optional[Label] = None
label_width: Optional[Label] = None
entry_height: Optional[Entry] = None
entry_width: Optional[Entry] = None
btn_build: Optional[Button] = None

def on_cell_click(event):
    """Handle click events on canvas cells"""
    col = event.x // CELL_SIZE
    row = event.y // CELL_SIZE

    if (row, col) in cells:
        cell_id, current_color = cells[(row, col)]
        # Toggle between white and black
        new_color = 'black' if current_color == 'white' else 'white'
        event.widget.itemconfig(cell_id, fill=new_color)
        cells[(row, col)] = (cell_id, new_color)

def solve_maze():
    paths = {f'${col}:${row}': Path(x=col, y=row) for (row, col), (cell_id, color) in cells.items() if color == 'black'}


def create_form():
    """Create and display the maze configuration form"""
    global label_height, label_width, entry_height, entry_width, btn_build

    label_height = Label(master, text='Height')
    label_width = Label(master, text='Width')
    label_height.grid(row=0, sticky='e', padx=5)
    label_width.grid(row=1, sticky='e', padx=5)
    entry_height = Entry(master)
    entry_width = Entry(master)
    entry_height.grid(row=0, column=1, padx=5, pady=5)
    entry_width.grid(row=1, column=1, padx=5, pady=5)
    entry_height.insert(0, '10')
    entry_width.insert(0, '10')
    btn_build = Button(master, text=BUILD_MAZE_CAPTION, command=build_maze)
    btn_build.grid(row=2, columnspan=2, pady=10)

def destroy_form():
    """Hide the maze configuration form"""
    if label_height:
        label_height.grid_remove()
    if label_width:
        label_width.grid_remove()
    if entry_height:
        entry_height.grid_remove()
    if entry_width:
        entry_width.grid_remove()
    if btn_build:
        btn_build.grid_remove()

def new_maze():
    """Reset the view to create a new maze"""
    # Clear canvas and buttons
    if master:
        for widget in master.grid_slaves():
            if isinstance(widget, Canvas) or (isinstance(widget, Button) and widget.cget('text') in [SOLVE_MAZE_CAPTION, NEW_MAZE_CAPTION]):
                widget.destroy()

    # Show input fields and Build Maze button again
    if label_height:
        label_height.grid()
    if label_width:
        label_width.grid()
    if entry_height:
        entry_height.grid()
    if entry_width:
        entry_width.grid()
    if btn_build:
        btn_build.grid()

def build_maze():
    global cells
    cells = {}  # Reset cells dictionary

    if not entry_height or not entry_width or not master:
        return

    height = int(entry_height.get())
    width = int(entry_width.get())

    # Hide input fields and Build Maze button
    destroy_form()

    # Create canvas for the maze grid
    canvas_width = width * CELL_SIZE
    canvas_height = height * CELL_SIZE
    canvas = Canvas(master, width=canvas_width, height=canvas_height, bg='white', highlightthickness=0)
    canvas.grid(row=0, column=0, columnspan=2)

    # Bind click event to canvas
    canvas.bind('<Button-1>', on_cell_click)

    # Draw grid
    for row in range(height):
        y1 = row * CELL_SIZE
        y2 = y1 + CELL_SIZE
        for col in range(width):
            x1 = col * CELL_SIZE
            x2 = x1 + CELL_SIZE
            cell_id = canvas.create_rectangle(x1, y1, x2, y2, outline='black', fill='white')
            cells[(row, col)] = (cell_id, 'white')  # Store cell ID and color

    # Add Solve Maze and New Maze buttons
    Button(master, text=SOLVE_MAZE_CAPTION, command=solve_maze).grid(row=1, column=0, padx=5, pady=10)
    Button(master, text=NEW_MAZE_CAPTION, command=new_maze).grid(row=1, column=1, padx=5, pady=10)



def main():
    global master

    master = Tk()
    master.title(APP_NAME)
    create_form()
    mainloop()


if __name__ == '__main__':
    main()

