
from config.experiment_config_lib import ControllerConfig
from sts.topology import *
from sts.control_flow import Replayer
from sts.simulation_state import SimulationConfig

simulation_config = SimulationConfig(controller_configs=[ControllerConfig(cmdline='./pox.py --verbose --random-seed=1 openflow.discovery forwarding.l2_multi openflow.of_01 --address=__address__ --port=__port__', address='127.0.0.1', port=6634, cwd='betta')],
                 topology_class=MeshTopology,
                 topology_params="num_switches=2",
                 patch_panel_class=BufferedPatchPanel,
                 dataplane_trace="dataplane_traces/ping_pong_same_subnet.trace",
                 multiplex_sockets=False)

control_flow = Replayer(simulation_config, "exp/pox_l2multi-exp4_2013_01_27_03_05_23/events.trace",
                        wait_on_deterministic_values=False)
