import md
from os import path
md.run_md()

assert(path.exists("cu.traj"))

print("The script ran!")
