import matplotlib.pyplot as plt

def create_foundation_diagram(A, B, H, rebar_diameter, grid_x, grid_y):
    fig, ax = plt.subplots(figsize=(10, 6))
    x_lines = int(A / grid_x) + 1
    y_lines = int(B / grid_y) + 1
    for i in range(x_lines):
        x = i * grid_x
        ax.plot([x, x], [0, B], color='black', linewidth=0.5)
    for j in range(y_lines):
        y = j * grid_y
        ax.plot([0, A], [y, y], color='black', linewidth=0.5)
    ax.set_xlim(0, A)
    ax.set_ylim(0, B)
    ax.set_aspect('equal')
    ax.set_title('Схема армирования плиты')
    ax.set_xlabel('Длина (м)')
    ax.set_ylabel('Ширина (м)')
    ax.grid(True)
    img_path = 'static/sketch.png'
    plt.savefig(img_path)
    plt.close()
    return img_path
