from config.experiment_config_lib import ControllerConfig
from sts.control_flow import Fuzzer
from sts.input_traces.input_logger import InputLogger
from sts.simulation_state import SimulationConfig
from sts.invariant_checker import InvariantChecker

# Use POX as our controller
command_line = ('''./pox.py openflow.spanning_tree openflow.discovery '''
                '''forwarding.l2_pairs ''')
controllers = [ControllerConfig(command_line, cwd="carp")]

simulation_config = SimulationConfig(controller_configs=controllers)

# Use a Fuzzer (already the default)
control_flow = Fuzzer(simulation_config,
                      fuzzer_params="experiments/config/fuzzer_params_heavy_failures.py",
                      halt_on_violation=True,
                      input_logger=InputLogger(), invariant_check_name="check_for_loops_blackholes",
                      initialization_rounds=150)
