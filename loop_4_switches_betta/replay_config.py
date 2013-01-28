
from config.experiment_config_lib import ControllerConfig
from sts.topology import *
from sts.control_flow import Replayer
from sts.simulation_state import SimulationConfig

simulation_config = SimulationConfig(controller_configs=[ControllerConfig(cmdline='./pox.py --verbose openflow.discovery openflow.spanning_tree forwarding.l2_multi openflow.of_01 --address=__address__ --port=__port__', address='127.0.0.1', port=6633, cwd='betta')],
                 topology_class=MeshTopology,
                 topology_params="num_switches=4",
                 patch_panel_class=BufferedPatchPanel,
                 dataplane_trace="exp/loop_4_switches_betta/dataplane.trace",
                 multiplex_sockets=False)

control_flow = Replayer(simulation_config, "exp/loop_4_switches_betta/events.trace",
                        wait_on_deterministic_values=False)
