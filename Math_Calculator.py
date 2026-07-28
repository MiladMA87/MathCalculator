import sympy as sp
import numpy as np
import math
import re
from typing import Union, Dict, List, Any

class UltimateMathCalculator:
    """
    The most comprehensive math calculator with support for:
    - Numeric and symbolic calculations
    - Trigonometric, logarithmic, exponential functions
    - Equation solving (linear, quadratic, nonlinear)
    - Derivatives and integrals (definite and indefinite)
    - Limits
    - Series expansion
    - Matrices
    - Differential equations
    - Plotting graphs
    """
    
    def __init__(self):
        # Symbolic variables
        self.x = sp.symbols('x')
        self.y = sp.symbols('y')
        self.z = sp.symbols('z')
        self.t = sp.symbols('t')
        
        # Numeric variables
        self.variables = {}
        
        # Mathematical constants
        self.constants = {
            'pi': sp.pi,
            'e': sp.E,
            'i': sp.I,
            'inf': sp.oo,
            'nan': sp.nan
        }
        
        # Allowed functions for eval (removed tau to fix error)
        self.allowed_functions = {
            'sin': np.sin, 'cos': np.cos, 'tan': np.tan,
            'asin': np.arcsin, 'acos': np.arccos, 'atan': np.arctan,
            'sinh': np.sinh, 'cosh': np.cosh, 'tanh': np.tanh,
            'asinh': np.arcsinh, 'acosh': np.arccosh, 'atanh': np.arctanh,
            'log': np.log, 'log10': np.log10, 'log2': np.log2,
            'exp': np.exp, 'sqrt': np.sqrt, 'cbrt': np.cbrt,
            'abs': abs, 'round': round, 'floor': math.floor,
            'ceil': math.ceil, 'factorial': math.factorial,
            'pi': np.pi, 'e': np.e,  # removed tau
            'degrees': np.degrees, 'radians': np.radians
        }
        
        # Calculation history
        self.history = []
        
    # ============ Numeric Calculations ============
    
    def numeric_calc(self, expression: str, variables: Dict = None) -> float:
        """
        Fast numeric calculation of expression
        Example: numeric_calc('sin(pi/2) + 3**2') => 10.0
        """
        try:
            if variables is None:
                variables = self.variables
                
            namespace = {**self.allowed_functions, **variables}
            result = eval(expression, {"__builtins__": {}}, namespace)
            
            # Store in history
            self.history.append({
                'type': 'numeric',
                'expression': expression,
                'result': result,
                'variables': variables.copy()
            })
            
            return result
        except Exception as e:
            return f"Error: {e}"
    
    # ============ Symbolic Calculations ============
    
    def symbolic_calc(self, expression: str) -> sp.Expr:
        """
        Symbolic calculation of expression
        Example: symbolic_calc('x**2 + 2*x + 1') => x**2 + 2*x + 1
        """
        try:
            # Replace numeric variables
            expr = sp.sympify(expression)
            
            for var, val in self.variables.items():
                if var in expr.free_symbols:
                    expr = expr.subs(var, val)
            
            # Store in history
            self.history.append({
                'type': 'symbolic',
                'expression': expression,
                'result': expr,
                'variables': self.variables.copy()
            })
            
            return expr
        except Exception as e:
            return f"Error: {e}"
    
    # ============ Equation Solving ============
    
    def solve_equation(self, expression: str, variable: str = 'x', method: str = 'solve') -> List:
        """
        Solve equation with different methods
        
        Parameters:
        - expression: equation like 'x**2 - 4' or 'x**2 - 4 = 0'
        - variable: variable name ('x', 'y', ...)
        - method: 'solve' (exact), 'nsolve' (numeric), 'solveset' (set of solutions)
        
        Example: solve_equation('x**2 - 4') => [-2, 2]
        """
        try:
            # Convert variable to symbol
            var = sp.symbols(variable)
            
            # If equation contains =, split it
            if '=' in expression:
                left, right = expression.split('=')
                expr = sp.sympify(left) - sp.sympify(right)
            else:
                expr = sp.sympify(expression)
            
            # Solve equation
            if method == 'solve':
                solution = sp.solve(expr, var)
            elif method == 'nsolve':
                # Numeric solve (needs initial guess)
                solution = sp.nsolve(expr, var, 0)
            elif method == 'solveset':
                solution = sp.solveset(expr, var, domain=sp.S.Reals)
            else:
                solution = sp.solve(expr, var)
            
            # Store in history
            self.history.append({
                'type': 'solve_equation',
                'expression': expression,
                'result': solution,
                'variable': variable
            })
            
            return solution
        except Exception as e:
            return f"Error: {e}"
    
    # ============ Derivatives ============
    
    def derivative(self, expression: str, variable: str = 'x', order: int = 1) -> sp.Expr:
        """
        Calculate derivative
        
        Example: derivative('x**3', 'x', 2) => 6*x
        """
        try:
            var = sp.symbols(variable)
            expr = sp.sympify(expression)
            result = sp.diff(expr, var, order)
            
            self.history.append({
                'type': 'derivative',
                'expression': expression,
                'result': result,
                'variable': variable,
                'order': order
            })
            
            return result
        except Exception as e:
            return f"Error: {e}"
    
    def partial_derivative(self, expression: str, variables: List[str]) -> sp.Expr:
        """Partial derivative with respect to multiple variables"""
        try:
            vars = [sp.symbols(v) for v in variables]
            expr = sp.sympify(expression)
            result = expr
            for var in vars:
                result = sp.diff(result, var)
            return result
        except Exception as e:
            return f"Error: {e}"
    
    # ============ Integrals ============
    
    def indefinite_integral(self, expression: str, variable: str = 'x') -> sp.Expr:
        """Indefinite integral"""
        try:
            var = sp.symbols(variable)
            expr = sp.sympify(expression)
            result = sp.integrate(expr, var)
            
            self.history.append({
                'type': 'indefinite_integral',
                'expression': expression,
                'result': result,
                'variable': variable
            })
            
            return result
        except Exception as e:
            return f"Error: {e}"
    
    def definite_integral(self, expression: str, variable: str = 'x', 
                         lower_limit: float = 0, upper_limit: float = 1) -> float:
        """Definite integral"""
        try:
            var = sp.symbols(variable)
            expr = sp.sympify(expression)
            result = sp.integrate(expr, (var, lower_limit, upper_limit))
            
            self.history.append({
                'type': 'definite_integral',
                'expression': expression,
                'result': result,
                'variable': variable,
                'lower_limit': lower_limit,
                'upper_limit': upper_limit
            })
            
            return float(result) if result.is_number else result
        except Exception as e:
            return f"Error: {e}"
    
    # ============ Limits ============
    
    def limit(self, expression: str, variable: str = 'x', point: float = 0, 
              direction: str = '+') -> sp.Expr:
        """
        Calculate limit
        
        direction: '+' (right), '-' (left), None (both sides)
        """
        try:
            var = sp.symbols(variable)
            expr = sp.sympify(expression)
            
            if direction == '+':
                result = sp.limit(expr, var, point, dir='+')
            elif direction == '-':
                result = sp.limit(expr, var, point, dir='-')
            else:
                result = sp.limit(expr, var, point)
            
            self.history.append({
                'type': 'limit',
                'expression': expression,
                'result': result,
                'variable': variable,
                'point': point,
                'direction': direction
            })
            
            return result
        except Exception as e:
            return f"Error: {e}"
    
    # ============ Expansion and Simplification ============
    
    def expand(self, expression: str) -> sp.Expr:
        """Expand expression (e.g., (x+1)**2 => x**2 + 2*x + 1)"""
        try:
            expr = sp.sympify(expression)
            return sp.expand(expr)
        except Exception as e:
            return f"Error: {e}"
    
    def simplify(self, expression: str) -> sp.Expr:
        """Simplify expression"""
        try:
            expr = sp.sympify(expression)
            return sp.simplify(expr)
        except Exception as e:
            return f"Error: {e}"
    
    def factor(self, expression: str) -> sp.Expr:
        """Factor expression (x**2 - 4 => (x - 2)*(x + 2))"""
        try:
            expr = sp.sympify(expression)
            return sp.factor(expr)
        except Exception as e:
            return f"Error: {e}"
    
    # ============ Matrices ============
    
    def matrix(self, data: List[List]) -> sp.Matrix:
        """Create matrix"""
        try:
            return sp.Matrix(data)
        except Exception as e:
            return f"Error: {e}"
    
    def solve_matrix(self, A: List[List], b: List) -> List:
        """Solve matrix equation A*x = b"""
        try:
            A_mat = sp.Matrix(A)
            b_vec = sp.Matrix(b)
            return A_mat.solve(b_vec)
        except Exception as e:
            return f"Error: {e}"
    
    # ============ Differential Equations ============
    
    def solve_ode(self, equation: str, function: str = 'f(x)') -> sp.Expr:
        """Solve ordinary differential equation"""
        try:
            f = sp.Function(function.split('(')[0])(self.x)
            expr = sp.sympify(equation.replace(function, str(f)))
            return sp.dsolve(expr, f)
        except Exception as e:
            return f"Error: {e}"
    
    # ============ Plotting ============
    
    def plot_graph(self, expression: str, from_x: float = -10, to_x: float = 10, 
                   num_points: int = 1000, title: str = ""):
        """Plot function graph (requires matplotlib)"""
        try:
            import matplotlib.pyplot as plt
            
            # Convert to numeric function
            x_vals = np.linspace(from_x, to_x, num_points)
            
            # Calculate y values
            y_vals = []
            for x in x_vals:
                try:
                    result = self.numeric_calc(expression, {'x': x})
                    y_vals.append(result if isinstance(result, (int, float)) else np.nan)
                except:
                    y_vals.append(np.nan)
            
            # Plot
            plt.figure(figsize=(10, 6))
            plt.plot(x_vals, y_vals, 'b-', linewidth=2)
            plt.grid(True, alpha=0.3)
            plt.axhline(y=0, color='k', linewidth=0.5)
            plt.axvline(x=0, color='k', linewidth=0.5)
            plt.title(title or f"Graph of {expression}")
            plt.xlabel('x')
            plt.ylabel('y')
            plt.show()
            
            return "Graph plotted successfully"
        except ImportError:
            return "Need matplotlib for plotting: pip install matplotlib"
        except Exception as e:
            return f"Plotting error: {e}"
    
    # ============ Series ============
    
    def taylor_series(self, expression: str, variable: str = 'x', point: float = 0, 
                      order: int = 5) -> sp.Expr:
        """Taylor series expansion"""
        try:
            var = sp.symbols(variable)
            expr = sp.sympify(expression)
            return sp.series(expr, var, point, order + 1)
        except Exception as e:
            return f"Error: {e}"
    
    # ============ History ============
    
    def show_history(self, count: int = 10):
        """Show recent calculations"""
        if not self.history:
            print("History is empty")
            return
        
        for i, item in enumerate(self.history[-count:]):
            print(f"{i+1}. {item['type']}: {item['expression']} = {item['result']}")
    
    # ============ Save and Load ============
    
    def save_variables(self, filename: str = 'variables.txt'):
        """Save variables to file"""
        try:
            with open(filename, 'w') as f:
                for var, val in self.variables.items():
                    f.write(f"{var} = {val}\n")
            return f"Variables saved to {filename}"
        except Exception as e:
            return f"Error: {e}"
    
    def load_variables(self, filename: str = 'variables.txt'):
        """Load variables from file"""
        try:
            with open(filename, 'r') as f:
                for line in f:
                    if '=' in line:
                        var, val = line.split('=')
                        self.variables[var.strip()] = float(val.strip())
            return "Variables loaded successfully"
        except Exception as e:
            return f"Error: {e}"


# ============ User Interface ============

def main():
    """Complete and beautiful user interface"""
    calc = UltimateMathCalculator()
    
    print("╔" + "═" * 60 + "╗")
    print("║" + " " * 14 + "ULTIMATE MATH CALCULATOR" + " " * 22 + "║")
    print("║" + " " * 13 + "Created by: Milad Moradpour" + " " * 20 + "║")
    print("╚" + "═" * 60 + "╝")
    print("\nAvailable Commands:")
    print("─" * 60)
    print("  calc <expression>    : Numeric calculation")
    print("  sym <expression>     : Symbolic calculation")
    print("  solve <expression>   : Solve equation")
    print("  diff <expression>    : Derivative")
    print("  int <expression>     : Indefinite integral")
    print("  defint <expr> a b    : Definite integral from a to b")
    print("  limit <expr> a       : Limit at point a")
    print("  expand <expression>  : Expand expression")
    print("  simplify <expr>      : Simplify expression")
    print("  factor <expression>  : Factor expression")
    print("  taylor <expr> n      : Taylor series order n")
    print("  plot <expression>    : Plot graph")
    print("  set <var> <value>    : Set variable")
    print("  vars                 : Show variables")
    print("  clear                : Clear variables")
    print("  history              : Show history")
    print("  save                 : Save variables")
    print("  load                 : Load variables")
    print("  help                 : This help")
    print("  exit                 : Exit")
    print("─" * 60)
    
    while True:
        try:
            user_input = input("\n🔢 > ").strip()
            if not user_input:
                continue
            
            # Check commands
            if user_input.lower() == 'exit':
                print("Goodbye! 👋")
                break
                
            if user_input.lower() == 'help':
                continue
                
            if user_input.lower() == 'vars':
                print(f"Variables: {calc.variables}")
                continue
                
            if user_input.lower() == 'clear':
                calc.variables.clear()
                print("✅ Variables cleared")
                continue
                
            if user_input.lower() == 'history':
                calc.show_history()
                continue
                
            if user_input.lower() == 'save':
                print(calc.save_variables())
                continue
                
            if user_input.lower() == 'load':
                print(calc.load_variables())
                continue
            
            # Set variable
            if user_input.startswith('set '):
                parts = user_input.split()
                if len(parts) == 3:
                    try:
                        calc.variables[parts[1]] = float(parts[2])
                        print(f"✅ {parts[1]} = {parts[2]} set")
                    except:
                        print("❌ Error: Value must be a number")
                continue
            
            # Numeric calculation
            if user_input.startswith('calc '):
                expression = user_input[5:]
                result = calc.numeric_calc(expression)
                print(f"📊 Result: {result}")
                continue
            
            # Symbolic calculation
            if user_input.startswith('sym '):
                expression = user_input[4:]
                result = calc.symbolic_calc(expression)
                print(f"🧮 Result: {result}")
                continue
            
            # Solve equation
            if user_input.startswith('solve '):
                expression = user_input[6:]
                result = calc.solve_equation(expression)
                print(f"✏️ Solutions: {result}")
                continue
            
            # Derivative
            if user_input.startswith('diff '):
                expression = user_input[5:]
                result = calc.derivative(expression)
                print(f"📈 Derivative: {result}")
                continue
            
            # Indefinite integral
            if user_input.startswith('int '):
                expression = user_input[4:]
                result = calc.indefinite_integral(expression)
                print(f"∫ Result: {result} + C")
                continue
            
            # Definite integral
            if user_input.startswith('defint '):
                parts = user_input.split()
                if len(parts) >= 4:
                    expression = parts[1]
                    a = float(parts[2])
                    b = float(parts[3])
                    result = calc.definite_integral(expression, 'x', a, b)
                    print(f"∫ from {a} to {b}: {result}")
                continue
            
            # Limit
            if user_input.startswith('limit '):
                parts = user_input.split()
                if len(parts) >= 3:
                    expression = parts[1]
                    point = float(parts[2])
                    direction = parts[3] if len(parts) > 3 else '+'
                    result = calc.limit(expression, 'x', point, direction)
                    print(f"lim: {result}")
                continue
            
            # Expand
            if user_input.startswith('expand '):
                expression = user_input[7:]
                result = calc.expand(expression)
                print(f"📐 Expanded: {result}")
                continue
            
            # Simplify
            if user_input.startswith('simplify '):
                expression = user_input[9:]
                result = calc.simplify(expression)
                print(f"🔧 Simplified: {result}")
                continue
            
            # Factor
            if user_input.startswith('factor '):
                expression = user_input[7:]
                result = calc.factor(expression)
                print(f"🧩 Factored: {result}")
                continue
            
            # Taylor series
            if user_input.startswith('taylor '):
                parts = user_input.split()
                if len(parts) >= 3:
                    expression = parts[1]
                    n = int(parts[2])
                    result = calc.taylor_series(expression, 'x', 0, n)
                    print(f"📊 Taylor series (order {n}): {result}")
                continue
            
            # Plot graph
            if user_input.startswith('plot '):
                expression = user_input[5:]
                print("📊 Plotting graph...")
                print(calc.plot_graph(expression))
                continue
            
            # If no command, treat as simple expression
            result = calc.numeric_calc(user_input)
            print(f"📊 Result: {result}")
            
        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except Exception as e:
            print(f"❌ Error: {e}")


# Run the program
if __name__ == "__main__":
    main()