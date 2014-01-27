from config.experiment_config_lib import ControllerConfig
from sts.topology import MeshTopology
from sts.control_flow import Fuzzer
from sts.input_traces.input_logger import InputLogger
from sts.simulation_state import SimulationConfig

# Use POX as our controller
start_cmd = "./pyretic.py -m p0 -v high pyretic.modules.hub"
controllers = [ControllerConfig(start_cmd, cwd="../pyretic", kill_cmd="ps aux | grep -e pox -e pyretic | grep -v simulator | cut -c 9-15 | xargs kill -9")]

topology_class = MeshTopology
topology_params = "num_switches=3"

simulation_config = SimulationConfig(controller_configs=controllers,
                                     topology_class=topology_class,
                                     topology_params=topology_params)
                            

control_flow = Fuzzer(simulation_config,
                      fuzzer_params='experiments/new_pyretic_loop/fuzzer_params.py',
                      input_logger=InputLogger(),
                      invariant_check_name="InvariantChecker.python_check_loops",
                      check_interval=1,
                      halt_on_violation=True)
