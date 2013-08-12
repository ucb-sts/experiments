from config.experiment_config_lib import ControllerConfig
from sts.topology import MeshTopology
from sts.control_flow import Fuzzer, Interactive
from sts.input_traces.input_logger import InputLogger
from sts.simulation_state import SimulationConfig

# Work directory must be absolute path
work_directory = "/home-local/andrewor/work"
start_cmd = "./start_vms -d %s -h" % work_directory
kill_cmd = "./stop_process -d %s -i %s" % (work_directory, "%d")
restart_cmd = "./start_process -d %s -i %s" % (work_directory, "%d")
check_status_cmd = "./check_process -d %s -i %s" % (work_directory, "%d")
get_address_cmd = "./show_vms -d %s" % work_directory
dummy_cmd = "sleep 1" 

# Use Floodlight as our controller
controllers = [ ControllerConfig(start_cmd, cwd="experiments/scripts/bsc", address="__address__", port=6633, controller_type="bsc", label="c1", kill_cmd=kill_cmd % 1, restart_cmd=restart_cmd % 1,  check_status_cmd=check_status_cmd % 1, get_address_cmd=get_address_cmd), 
                ControllerConfig(dummy_cmd, cwd="experiments/scripts/bsc", address="__address__", port=6633, controller_type="bsc", label="c2", kill_cmd=kill_cmd % 2, restart_cmd=restart_cmd % 2,  check_status_cmd=check_status_cmd % 2, get_address_cmd=get_address_cmd)]
topology_class = MeshTopology
topology_params = "num_switches=3"

simulation_config = SimulationConfig(controller_configs=controllers,
                                     topology_class=topology_class,
                                     topology_params=topology_params,
                                     kill_controllers_on_exit=False
                                     )

control_flow = Fuzzer(simulation_config,
                      check_interval=5,
                      halt_on_violation=True,
                      input_logger=InputLogger(),
                      invariant_check_name="check_everything",
                      steps=999,
                      fuzzer_params="experiments/config/fuzzer_params_heavy_failures.py"
                      )
