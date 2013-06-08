from config.experiment_config_lib import ControllerConfig
from sts.topology import MeshTopology
from sts.control_flow import Fuzzer, Interactive
from sts.input_traces.input_logger import InputLogger
from sts.simulation_state import SimulationConfig

# Work directory must be absolute path
work_directory = "/home-local/andrewor/work"
start_cmd = ("./bsc_start_vm %s" % work_directory)
kill_cmd = ("./bsc_stop_vm %s" % work_directory)

# Use Floodlight as our controller
controllers = [ ControllerConfig(start_cmd, kill_cmd, cwd="experiments/scripts", address="__address__", port=6633, controller_type="bsc", label="c1") ]
topology_class = MeshTopology
topology_params = "num_switches=3"

simulation_config = SimulationConfig(controller_configs=controllers,
                                     topology_class=topology_class,
                                     topology_params=topology_params,
                                     )

control_flow = Fuzzer(simulation_config, check_interval=20,
                      halt_on_violation=True,
                      input_logger=InputLogger(),
                      invariant_check_name="InvariantChecker.check_loops",
                      steps=999,
                      fuzzer_params="experiments/config/fuzzer_params_heavy_failures.py"
                      )
