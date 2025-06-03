from julia import Julia
jl = Julia(compiled_modules=False)  # Optional: helps avoid certain precompile issues

from julia import Main

# Optional: ensure enemy_ship.py is on the Python path
import sys
sys.path.append(".")

# Run the Julia script
Main.include("PyCall.jl")
