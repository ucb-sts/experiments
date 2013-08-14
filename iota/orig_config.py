from config.experiment_config_lib import ControllerConfig
from sts.topology import MeshTopology
from sts.control_flow import Fuzzer, Interactive
from sts.input_traces.input_logger import InputLogger
from sts.simulation_state import SimulationConfig

# Work directory must be absolute path
work_directory = "/home-local/andrewor/work"
start_cmd = "./start_vms -d  -h -r" 