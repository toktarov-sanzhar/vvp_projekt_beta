"""Vizualizace fraktálů"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
from matplotlib.patches import Rectangle
from .mandelbrot import mandelbrot
from .julia import julia

def run_visualizer():
    width, height = 600, 600
    max_iter_default = 100
    c_re, c_im = -0.4, 0.6
    julia_mode = [False]

    default_window = [[-2.0, 1.0], [-1.5, 1.5]]
    window = [default_window[0][:], default_window[1][:]]

    fig, ax = plt.subplots()
    plt.subplots_adjust(left=0.25, bottom=0.4)

    selection_rect = [None]
    press = [None]

    def draw():
        ax.clear()
        xmin, xmax = window[0]
        ymin, ymax = window[1]

        if julia_mode[0]:
            c = complex(slider_re.val, slider_im.val)
            data = np.array([
                [julia(complex(x, y), c, int(slider_iter.val))
                 for x in np.linspace(xmin, xmax, width)]
                for y in np.linspace(ymin, ymax, height)
            ])
            ax.set_title("Julia")
        else:
            data = np.array([
                [mandelbrot(complex(x, y), int(slider_iter.val))
                 for x in np.linspace(xmin, xmax, width)]
                for y in np.linspace(ymin, ymax, height)
            ])
            ax.set_title("Mandelbrot")
        ax.imshow(data, extent=(xmin, xmax, ymin, ymax), cmap="hot", origin='lower')
        plt.draw()

    def on_press(event):
        if event.inaxes != ax: return
        press[0] = (event.xdata, event.ydata)
        selection_rect[0] = Rectangle((event.xdata, event.ydata), 0, 0,
                                      linewidth=1, edgecolor='cyan', facecolor='none')
        ax.add_patch(selection_rect[0])

    def on_motion(event):
        if not press[0] or event.inaxes != ax: return
        x0, y0 = press[0]
        x1, y1 = event.xdata, event.ydata
        selection_rect[0].set_width(x1 - x0)
        selection_rect[0].set_height(y1 - y0)
        plt.draw()

    def on_release(event):
        if not press[0] or event.inaxes != ax: return
        x0, y0 = press[0]
        x1, y1 = event.xdata, event.ydata
        if abs(x1 - x0) > 0.01 and abs(y1 - y0) > 0.01:
            window[0] = [min(x0, x1), max(x0, x1)]
            window[1] = [min(y0, y1), max(y0, y1)]
        press[0] = None
        selection_rect[0].remove()
        selection_rect[0] = None
        draw()

    fig.canvas.mpl_connect("button_press_event", on_press)
    fig.canvas.mpl_connect("motion_notify_event", on_motion)
    fig.canvas.mpl_connect("button_release_event", on_release)

    ax_re = plt.axes([0.25, 0.25, 0.65, 0.03])
    ax_im = plt.axes([0.25, 0.2, 0.65, 0.03])
    ax_iter = plt.axes([0.25, 0.15, 0.65, 0.03])
    slider_re = Slider(ax_re, 'Re(c)', -1.0, 1.0, valinit=c_re)
    slider_im = Slider(ax_im, 'Im(c)', -1.0, 1.0, valinit=c_im)
    slider_iter = Slider(ax_iter, 'Iterace', 10, 300, valinit=max_iter_default, valstep=10)

    def update(val):
        draw()

    slider_re.on_changed(update)
    slider_im.on_changed(update)
    slider_iter.on_changed(update)

    ax_button = plt.axes([0.025, 0.5, 0.15, 0.04])
    button = Button(ax_button, 'Mandelbrot/Julia')

    def switch(event):
        julia_mode[0] = not julia_mode[0]
        draw()

    button.on_clicked(switch)

    ax_reset = plt.axes([0.025, 0.44, 0.15, 0.04])
    reset_button = Button(ax_reset, 'Reset Zoom')

    def reset_zoom(event):
        window[0][:] = default_window[0][:]
        window[1][:] = default_window[1][:]
        draw()

    reset_button.on_clicked(reset_zoom)

    draw()
    plt.show()
