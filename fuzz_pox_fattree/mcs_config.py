
from config.experiment_config_lib import ControllerConfig
from sts.topology import *
from sts.control_flow import EfficientMCSFinder
from sts.invariant_checker import InvariantChecker
from sts.simulation_state import SimulationConfig

simulation_config = SimulationConfig(controller_configs=[ControllerConfig(cmdline='./pox.py --verbose --no-cli sts.syncproto.pox_syncer openflow.discovery openflow.spanning_tree forwarding.l2_multi sts.util.socket_mux.pox_monkeypatcher openflow.of_01 --address=../sts_socket_pipe', address='sts_socket_pipe', cwd='pox', sync='tcp:localhost:18900')],
                 topology_class=FatTree,
                 topology_params="",
                 patch_panel_class=BufferedPatchPanel,
                 dataplane_trace="exp/fuzz_pox_fattree/dataplane.trace",
                 multiplex_sockets=True)

control_flow = EfficientMCSFinder(simulation_config, "exp/fuzz_pox_fattree/events.trace",
                                  wait_on_deterministic_values=False)
