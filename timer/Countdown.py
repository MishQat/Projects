#!/usr/bin/env python3
"""
╔══════════════════════════════════════════╗
║  exam_countdown.py                       ║
║  Nothing Phone / Glyph-inspired timer    ║
║  Pixel-art sleeping cat included  ฅ^•ω•^ ║
╚══════════════════════════════════════════╝

NOTE: uses Python's built-in `datetime` not MicroPython's `utime` —
      tkinter only runs in standard Python. Same maths, different module.

Double-click the window to close it.
Click and drag it anywhere on screen.
"""

import tkinter as tk
from datetime import datetime
import time

# ════════════════════════════════════════════════════════════════
#   ✏  TWEAK ZONE — change anything in this block
# ════════════════════════════════════════════════════════════════

EXAM_DATE   = datetime(2026, 5, 20, 9, 45, 0)  # ← your exam date/time

# Window
WINDOW_W    = 300        # width in pixels
MARGIN_R    = 30         # distance from right edge of screen
MARGIN_T    = 60         # distance from top of screen

# Colours — swap these out freely
BG          = "#0a0a0a"  # window background (Nothing black)
FG_DIGIT    = "#f0f0f0"  # countdown numbers
FG_LABEL    = "#3a3a3a"  # "D / H / M / S" labels
FG_SUB      = "#B6ACAC"  # "until exams." subtitle
BORDER_CLR  = "#1c1c1c"  # inner divider line
CAT_CLR     = "#c8c8c8"  # cat body pixels
ZZZ_CLR     = "#2e2e2e"  # z z z sleep text

# Cat pixel art scale (px per "pixel") — bump to 6 for bigger cat
PIXEL_SIZE  = 5

# Refresh rate — 1000 ms = once per second, easy on CPU
TICK_MS     = 1000

# ════════════════════════════════════════════════════════════════


# ── Pixel-art sleeping cat (0 = transparent, 1 = filled) ─────────────────────
# Hand-crafted 15×12 grid. Inspired by lo-fi pixel cat sprites floating
# around GitHub (e.g. github.com/gabrielakoreeda / similar sprite sheets).
# Modify freely — it's just a 2-D list of 0s and 1s.
CAT_ART = [
[0,0,0,0,0,0,1,0,0,0,0,0,1,0],
[0,0,0,0,0,1,1,1,0,0,0,1,1,1],
[0,0,0,0,0,1,3,1,1,1,1,1,3,1],
[0,0,0,0,0,2,2,1,1,1,1,1,2,2],
[0,0,0,0,0,1,1,4,1,1,1,4,1,1],
[0,0,0,0,0,2,2,1,3,5,3,1,2,2],
[0,0,0,0,0,0,1,1,3,3,3,1,1,0],
[0,2,2,0,0,0,2,1,1,1,1,2,0,0],
[2,1,2,0,0,2,1,1,3,3,1,1,0,0],
[1,2,0,0,2,2,2,3,3,3,3,1,0,0],
[2,1,2,1,2,1,2,1,3,3,3,2,2,0],
[0,2,1,2,2,1,1,2,1,3,1,1,2,0]  
]
# ── Cat colour palette ──────────────────────────────────────────
# Key = number in CAT_ART grid, Value = hex colour (0 = transparent)
CAT_PALETTE = {
    0: None,        # trasparent / background
    1: "#a0a0a0",   # l
    3: "#ffffff",   # 
    4: "#000000",   # 
    5: "#ff6fa5",   # 
}
# ─── z z z positions (col offset, row offset, font size) ──────────────────
# These float above the cat's head, shrinking as they rise
ZZZ_OFFSETS = [
    (17, 4, 8),   # closest z  (big)
    (20, 2, 6),   # middle z
    (23, 0, 5),   # far z      (small)
]


class ExamCountdown:
    def __init__(self, root: tk.Tk):
        self.root = root
        self._drag_ox = self._drag_oy = 0
        # Timer state
        self._timer_seconds = 0
        self._timer_running = False
        self._timer_start_time = None
        self._setup_window()
        self._build_ui()
        self._tick()          # kick off the loop

    # ── Window setup ──────────────────────────────────────────────────────────

    def _setup_window(self):
        self.root.title("exam.exe")
        self.root.configure(bg=BG)
        self.root.resizable(False, False)
        self.root.attributes("-topmost", True)   # always on top
        self.root.overrideredirect(True)          # hide OS title bar

        # Park it in the top-right corner
        self.root.update_idletasks()
        sw = self.root.winfo_screenwidth()
        self.root.geometry(f"+{sw - WINDOW_W - MARGIN_R}+{MARGIN_T}")

        # Drag to reposition (since title bar is gone)
        self.root.bind("<ButtonPress-1>",  self._on_drag_start)
        self.root.bind("<B1-Motion>",      self._on_drag_move)
        # Double-click to quit
        self.root.bind("<Double-Button-1>", lambda _e: self.root.destroy())

    def _on_drag_start(self, e):
        self._drag_ox = e.x
        self._drag_oy = e.y

    def _on_drag_move(self, e):
        x = self.root.winfo_x() + (e.x - self._drag_ox)
        y = self.root.winfo_y() + (e.y - self._drag_oy)
        self.root.geometry(f"+{x}+{y}")

    # ── Timer controls ────────────────────────────────────────────────────────

    def _timer_play(self):
        if not self._timer_running:
            self._timer_running = True
            self._timer_start_time = time.time() - self._timer_seconds

    def _timer_pause(self):
        if self._timer_running:
            self._timer_running = False
            self._timer_seconds = int(time.time() - self._timer_start_time)

    def _timer_reset(self):
        self._timer_running = False
        self._timer_seconds = 0
        self._timer_start_time = None
        self._update_timer_display()

    def _update_timer_display(self):
        if self._timer_running:
            self._timer_seconds = int(time.time() - self._timer_start_time)
        
        mins = self._timer_seconds // 60
        secs = self._timer_seconds % 60
        self._timer_label.config(text=f"{mins:02d}:{secs:02d}")

    # ── Build widgets (called once) ────────────────────────────────────────────

    def _build_ui(self):
        pad_x = 20
        pad_y = 14

        # ── Cat canvas ────────────────────────────────────────────────────────
        cat_cols  = len(CAT_ART[0])
        cat_rows  = len(CAT_ART)
        canvas_w  = WINDOW_W                         # full width
        canvas_h  = cat_rows * PIXEL_SIZE + 18       # a little breathing room

        self.cat_canvas = tk.Canvas(
            self.root,
            width=canvas_w, height=canvas_h,
            bg=BG, highlightthickness=0
        )
        self.cat_canvas.pack()

        # Centre the cat horizontally, leave top padding for z's
        self._cat_ox = (canvas_w - cat_cols * PIXEL_SIZE) // 2
        self._cat_oy = 14
        self._draw_cat()

        # ── Hairline divider ──────────────────────────────────────────────────
        tk.Frame(
            self.root, bg=BORDER_CLR, height=1,
            width=WINDOW_W - pad_x * 2
        ).pack(pady=(0, pad_y // 2))

        # ── Countdown segments  D / H / M / S ────────────────────────────────
        row_frame = tk.Frame(self.root, bg=BG)
        row_frame.pack(padx=pad_x)

        self._segs = {}
        keys    = [("d", "D"), ("h", "H"), ("m", "M"), ("s", "S")]
        weights = [1, 1, 1, 1]
        for col, (key, lbl_text) in enumerate(keys):
            row_frame.columnconfigure(col, weight=weights[col])

            cell = tk.Frame(row_frame, bg=BG)
            cell.grid(row=0, column=col, padx=6, pady=0)

            # Big digit
            num_lbl = tk.Label(
                cell, text="00",
                font=("Courier New", 30, "bold"),
                bg=BG, fg=FG_DIGIT,
                width=2, anchor="center"
            )
            num_lbl.pack()

            # Small unit label below
            tk.Label(
                cell, text=lbl_text,
                font=("Courier New", 7),
                bg=BG, fg=FG_LABEL
            ).pack()

            self._segs[key] = num_lbl

        # ── Subtitle ──────────────────────────────────────────────────────────
        tk.Label(
            self.root, text="until exams.",
            font=("Courier New", 8),
            bg=BG, fg=FG_SUB
        ).pack(pady=(pad_y // 2, pad_y))

        # ── Divider ───────────────────────────────────────────────────────────
        tk.Frame(
            self.root, bg=BORDER_CLR, height=1,
            width=WINDOW_W - pad_x * 2
        ).pack(pady=(0, pad_y // 2))

        # ── Timer section ─────────────────────────────────────────────────────
        tk.Label(
            self.root, text="Timer",
            font=("Courier New", 8),
            bg=BG, fg=FG_SUB
        ).pack(pady=(pad_y // 2, pad_y))
        timer_frame = tk.Frame(self.root, bg=BG)
        timer_frame.pack(padx=pad_x, pady=(pad_y // 2, pad_y))

        # Timer display
        self._timer_label = tk.Label(
            timer_frame, text="00:00",
            font=("Courier New", 20, "bold"),
            bg=BG, fg=FG_DIGIT
        )
        self._timer_label.pack(pady=(0, 8))

        # Buttons frame
        btn_frame = tk.Frame(timer_frame, bg=BG)
        btn_frame.pack()

        btn_style = {
            "font": ("Courier New", 8),
            "bg": BORDER_CLR,
            "fg": FG_DIGIT,
            "width": 6,
            "height": 1,
            "relief": "flat",
            "bd": 1,
            "activebackground": "#2a2a2a",
            "activeforeground": FG_DIGIT,
        }

        tk.Button(
            btn_frame, text="▶ Play",
            command=self._timer_play, **btn_style
        ).pack(side="left", padx=2)

        tk.Button(
            btn_frame, text="⏸ Pause",
            command=self._timer_pause, **btn_style
        ).pack(side="left", padx=2)

        tk.Button(
            btn_frame, text="⟲ Reset",
            command=self._timer_reset, **btn_style
        ).pack(side="left", padx=2)

    # ── Draw the pixel cat (static — only called once) ─────────────────────────

    def _draw_cat(self):

        c  = self.cat_canvas
        p  = PIXEL_SIZE
        ox = self._cat_ox
        oy = self._cat_oy

        for r, row in enumerate(CAT_ART):
            for col, px in enumerate(row):
                colour = CAT_PALETTE.get(px)   # look up the colour
                if colour is None:             # 0 = skip (transparent)
                    continue
                x0 = ox + col * p
                y0 = oy + r   * p
                c.create_rectangle(
                    x0, y0, x0 + p, y0 + p,
                    fill=colour, outline=""
                )

        # z z z (unchanged from before)
        for (dc, dr, sz) in ZZZ_OFFSETS:
            c.create_text(
                ox + dc * p, oy + dr * p,
                text="z", font=("Courier New", sz, "bold"),
                fill=ZZZ_CLR, anchor="nw"
            )

    # ── Timer tick — runs every TICK_MS, very light ───────────────────────────

    def _tick(self):
        delta = EXAM_DATE - datetime.now()
        total = int(delta.total_seconds())

        if total <= 0:
            # You're in the exam — good luck!
            for key in self._segs:
                self._segs[key].config(text="GO")
        else:
            d =  total // 86400
            h = (total %  86400) // 3600
            m = (total %   3600) // 60
            s =  total %     60

            self._segs["d"].config(text=f"{d:02d}")
            self._segs["h"].config(text=f"{h:02d}")
            self._segs["m"].config(text=f"{m:02d}")
            self._segs["s"].config(text=f"{s:02d}")

        # Update timer display
        self._update_timer_display()

        # Schedule next update (1 second = low CPU, no spin-loop)
        self.root.after(TICK_MS, self._tick)


# ── Entry point ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    root = tk.Tk()
    ExamCountdown(root)
    root.mainloop()