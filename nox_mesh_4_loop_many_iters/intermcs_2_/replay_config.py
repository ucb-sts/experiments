
from config.experiment_config_lib import ControllerConfig
from sts.topology import *
from sts.control_flow import Replayer
from sts.simulation_state import SimulationConfig

simulation_config = SimulationConfig(controller_configs=[ControllerConfig(cmdline='./nox_core -v -i ptcp:6635 routing', address='127.0.0.1', port=6635, cwd='nox_classic/build/src')],
                 topology_class=MeshTopology,
                 topology_params="num_switches=4",
                 patch_panel_class=BufferedPatchPanel,
                 multiplex_sockets=False)

control_flow = Replayer(simulation_config, "experiments/nox_mesh_4_loop_many_iters/intermcs_2_/events.trace",
                        wait_on_deterministic_values=False)
# Invariant check: 'None'
