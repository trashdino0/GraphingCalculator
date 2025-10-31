# 🧮 Graphing Calculator

An interactive **Python-based Graphing Calculator** built using **Turtle Graphics** and **Tkinter**.  
This calculator allows users to visualize and graph various mathematical equations, including **quadratic**, **trigonometric**, **logarithmic**, and **linear** functions, all within a simple GUI interface.

---

## 🚀 Features

- 📈 **Multiple Equation Types**
  - Quadratic: `y = ax² + bx + c`
  - Linear (Slope): `y = mx + b`
  - Trigonometric: `y = a * sin(fx - h) + v`, `y = a * cos(fx - h) + v`, `y = a * tan(fx - h) + v`
  - Logarithmic: `y = log(x) * a`

- 🎨 **Dynamic Graphing**
  - Randomized graph colors for each new plot  
  - Smooth drawing animations using Turtle Graphics

- 🧰 **Interactive Controls**
  - `Exit` button to close the window  
  - `Restart` button to clear and reinitialize the graph  
  - `Add` button to plot additional graphs  

- 🖥️ **Simple GUI**
  - Built with Tkinter for clean input dialogs and dropdown menus  
  - Select which equation to graph from a menu and input coefficients interactively

---

## 🧩 How It Works

1. Launch the program.
2. Choose a function type from the dropdown menu (Quadratics, Slope, Sin, Cos, Tan, Log).
3. Input the necessary coefficients/parameters (like `a`, `b`, `c`, etc.).
4. Watch your graph appear dynamically in a Turtle Graphics window.

Each function has its own graphing behavior:
- **Quadratic:** Plots parabolas based on `a`, `b`, and `c`.  
- **Slope:** Draws a straight line using slope `m` and intercept `b`.  
- **Sin / Cos / Tan:** Graphs wave functions with adjustable amplitude, frequency, and phase shifts.  
- **Log:** Draws the natural logarithm curve scaled by a multiplier.

---

## ⚙️ Installation

### Requirements
- Python 3.8+
- Tkinter (included in standard Python)
- Turtle (included in standard Python)

### Run the Program
Clone the repository and run the script directly:
```bash
git clone https://github.com/yourusername/GraphingCalculator.git
cd GraphingCalculator
python graphing_calculator.py
