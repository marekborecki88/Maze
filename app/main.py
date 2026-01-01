from tkinter import Tk, Label, Entry, Button, Canvas, mainloop

CELL_SIZE = 30
cells = {}  # Dictionary to store cell rectangles and their colors

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

def build_maze():
    global cells
    cells = {}  # Reset cells dictionary

    height = int(entry_height.get())
    width = int(entry_width.get())

    # Clear previous canvas if exists
    for widget in master.grid_slaves():
        if isinstance(widget, Canvas):
            widget.destroy()

    # Create canvas for the maze grid
    canvas_width = width * CELL_SIZE
    canvas_height = height * CELL_SIZE
    canvas = Canvas(master, width=canvas_width, height=canvas_height, bg='white')
    canvas.grid(row=3, column=0, columnspan=2, pady=10)

    # Bind click event to canvas
    canvas.bind('<Button-1>', on_cell_click)

    # Draw grid
    for row in range(height):
        for col in range(width):
            x1 = col * CELL_SIZE
            y1 = row * CELL_SIZE
            x2 = x1 + CELL_SIZE
            y2 = y1 + CELL_SIZE
            cell_id = canvas.create_rectangle(x1, y1, x2, y2, outline='black', fill='white')
            cells[(row, col)] = (cell_id, 'white')  # Store cell ID and color

master = Tk()
master.title('Maze Generator')

Label(master, text='Height').grid(row=0, sticky='e', padx=5)
Label(master, text='Width').grid(row=1, sticky='e', padx=5)
entry_height = Entry(master)
entry_width = Entry(master)
entry_height.grid(row=0, column=1, padx=5, pady=5)
entry_width.grid(row=1, column=1, padx=5, pady=5)
entry_height.insert(0, '10')
entry_width.insert(0, '10')
Button(master, text='Build Maze', command=build_maze).grid(row=2, columnspan=2, pady=10)
mainloop()
