import os
import subprocess

# Get the directory of the current script
current_directory = os.path.dirname(os.path.abspath(__file__))

# Specify the Python interpreter path
python_interpreter = "/usr/bin/python3"  # Update this with the correct path

# Execute the first script
subprocess.run([python_interpreter, os.path.join(current_directory, "init_pose.py")])

# Execute the second script
subprocess.run([python_interpreter, os.path.join(current_directory, "goal_pose1.py")])

# Execute the third script
subprocess.run([python_interpreter, os.path.join(current_directory, "manipulator_trajectory_pick.py")])

# Execute the fourth script
subprocess.run([python_interpreter, os.path.join(current_directory, "goal_pose2.py")])

# Execute the fifth script
subprocess.run([python_interpreter, os.path.join(current_directory, "manipulator_trajectory_drop.py")])

