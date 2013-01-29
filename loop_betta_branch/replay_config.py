
from config.experiment_config_lib import ControllerConfig
from sts.topology import *
from sts.control_flow import Replayer
from sts.simulation_state import SimulationConfig

simulation_config = SimulationConfig(controller_configs=[ControllerConfig(cmdline='./pox.py --verbose openflow.discovery forwarding.l2_multi openflow.of_01 --address=__address__ --port=__port__', address='127.0.0.1', port=6633, cwd='betta')],
                 topology_class=MeshTopology,
                 topology_params="num_switches=2",
                 patch_panel_class=BufferedPatchPanel,
                 dataplane_trace="exp/loop_betta_branch/dataplane.trace",
                 multiplex_sockets=False)

control_flow = Replayer(simulation_config, "exp/loop_betta_branch/events.trace",
                        wait_on_deterministic_values=False)
