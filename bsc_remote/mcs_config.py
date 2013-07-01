
from config.experiment_config_lib import ControllerConfig
from sts.topology import *
from sts.control_flow import EfficientMCSFinder
from sts.invariant_checker import InvariantChecker
from sts.simulation_state import SimulationConfig

simulation_config = SimulationConfig(controller_configs=[ControllerConfig(start_cmd='./bsc_start_remote_vm /home-local/andrewor/work', address='__address__', cwd='experiments/scripts')],
                 topology_class=MeshTopology,
                 topology_params="num_switches=3",
                 patch_panel_class=BufferedPatchPanel,
                 multiplex_sockets=False)

control_flow = EfficientMCSFinder(simulation_config, "experiments/bsc_remote/events.trace",
                                  wait_on_deterministic_values=False,
                                  invariant_check_name='InvariantChecker.check_loops')
