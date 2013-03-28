
from config.experiment_config_lib import ControllerConfig
from sts.topology import *
from sts.control_flow import EfficientMCSFinder
from sts.invariant_checker import InvariantChecker
from sts.simulation_state import SimulationConfig

simulation_config = SimulationConfig(controller_configs=[ControllerConfig(cmdline='./nox_core -v -i ptcp:6635 routing', address='127.0.0.1', port=6635, cwd='nox_classic/build/src')],
                 topology_class=MeshTopology,
                 topology_params="num_switches=4",
                 patch_panel_class=BufferedPatchPanel,
                 dataplane_trace="experiments/nox_mesh_4_loop/dataplane.trace",
                 multiplex_sockets=False)

control_flow = EfficientMCSFinder(simulation_config, "experiments/nox_mesh_4_loop/events.trace",
                                  wait_on_deterministic_values=False,
                                  invariant_check_name='check_for_loops_or_connectivity')
