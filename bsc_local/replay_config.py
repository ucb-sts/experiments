
from config.experiment_config_lib import ControllerConfig
from sts.topology import *
from sts.control_flow import Replayer
from sts.simulation_state import SimulationConfig

simulation_config = SimulationConfig(controller_configs=[ControllerConfig(start_cmd='./bsc_start_vm /home-local/andrewor/work', address='10.10.0.2', port=6633, cwd='experiments/scripts')],
                 topology_class=MeshTopology,
                 topology_params="num_switches=3",
                 patch_panel_class=BufferedPatchPanel,
                 multiplex_sockets=False)

control_flow = Replayer(simulation_config, "experiments/bsc_local/events.trace",
                        wait_on_deterministic_values=False)
# Invariant check: 'InvariantChecker.check_loops'