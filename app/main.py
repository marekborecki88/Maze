from tkinter import Tk, Label, Entry, Button, Canvas, mainloop

APP_NAME = 'Maze Generator'
BUILD_MAZE_CAPTION = 'Build Maze'
NEW_MAZE_CAPTION = 'New Maze'
SOLVE_MAZE_CAPTION = 'Solve Maze'

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

def solve_maze():
    """Find and display the shortest path in the maze"""
    print("Solving maze...")
    # TODO: Implement pathfinding algorithm

def new_maze():
    """Reset the view to create a new maze"""
    # Clear canvas and buttons
    for widget in master.grid_slaves():
        if isinstance(widget, Canvas) or (isinstance(widget, Button) and widget.cget('text') in ['Solve Maze', 'New Maze']):
            widget.destroy()

    # Show input fields and Build Maze button again
    label_height.grid()
    label_width.grid()
    entry_height.grid()
    entry_width.grid()
    btn_build.grid()

def build_maze():
    global cells
    cells = {}  # Reset cells dictionary

    height = int(entry_height.get())
    width = int(entry_width.get())

    # Clear previous canvas and solve button if they exist
    for widget in master.grid_slaves():
        if isinstance(widget, Canvas) or (isinstance(widget, Button) and widget.cget('text') == 'Solve Maze'):
            widget.destroy()

    # Hide input fields and Build Maze button
    label_height.grid_remove()
    label_width.grid_remove()
    entry_height.grid_remove()
    entry_width.grid_remove()
    btn_build.grid_remove()

    # Create canvas for the maze grid
    canvas_width = width * CELL_SIZE
    canvas_height = height * CELL_SIZE
    canvas = Canvas(master, width=canvas_width, height=canvas_height, bg='white')
    canvas.grid(row=0, column=0, columnspan=2, pady=10)

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



master = Tk()
master.title(APP_NAME)

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
mainloop()
