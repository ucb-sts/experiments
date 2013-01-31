from config.experiment_config_lib import ControllerConfig
from sts.control_flow import Fuzzer
from sts.input_traces.input_logger import InputLogger
from sts.invariant_checker import InvariantChecker
from sts.simulation_state import SimulationConfig
from sts.topology import MeshTopology, FatTree

# Use NOX as our controller
command_line = "./nox_core -v -i ptcp:6635 routing"
controllers = [ControllerConfig(command_line, cwd="nox_classic/build/src", address="127.0.0.1", port=6635)]


topology_class = MeshTopology
topology_params = "num_switches=4"
# dataplane_trace = "dataplane_traces/ping_pong_same_subnet_4_switches.trace"
# dataplane_trace = "dataplane_traces/ping_pong_fat_tree.trace"

simulation_config = SimulationConfig(controller_configs=controllers,
                                     topology_class=topology_class,
                                     topology_params=topology_params)
           #                          dataplane_trace=dataplane_trace)

#simulation_config = SimulationConfig(controller_configs=controllers,
#                                     dataplane_trace=dataplane_trace)

def fast_die_invariant_check(simulation):
  from sts.invariant_checker import InvariantChecker
  result = InvariantChecker.check_loops(simulation)
  if result:
    return result
  result = InvariantChecker.python_check_connectivity(simulation)
  if not result:
    print "Connectivity established - bailing out"
    import sys
    sys.exit(0)
  return []

# Use a Fuzzer (already the default)
control_flow = Fuzzer(simulation_config, input_logger=InputLogger(),
                      check_interval=20,
                      halt_on_violation=True,
                      steps=300,
                      invariant_check=fast_die_invariant_check)
