
from config.experiment_config_lib import ControllerConfig
from sts.topology import *
from sts.control_flow import Replayer
from sts.simulation_state import SimulationConfig

simulation_config = SimulationConfig(controller_configs=[ControllerConfig(start_cmd='./nox_core -v -i ptcp:6635 routing', address='127.0.0.1', port=6635, cwd='nox_classic/build/src')],
                 topology_class=MeshTopology,
                 topology_params="num_switches=4",
                 patch_panel_class=BufferedPatchPanel,
                 multiplex_sockets=False)

control_flow = Replayer(simulation_config, "experiments/nox_mesh_4_loop_repro_w_3_retries/interreplay_29_r.4/events.trace",
                        wait_on_deterministic_values=False)
# Invariant check: 'None'
