
from config.experiment_config_lib import ControllerConfig
from sts.topology import *
from sts.control_flow import EfficientMCSFinder
from sts.invariant_checker import InvariantChecker
from sts.simulation_state import SimulationConfig

simulation_config = SimulationConfig(controller_configs=[ControllerConfig(cmdline='./pox.py --verbose --no-cli openflow.discovery openflow.spanning_tree forwarding.l2_multi sts.util.socket_mux.pox_monkeypatcher openflow.of_01 --address=__address__ --port=__port__', address='127.0.0.1', port=6635, cwd='pox')],
                 topology_class=FatTree,
                 topology_params="num_pods=8",
                 patch_panel_class=BufferedPatchPanel,
                 dataplane_trace="experiments/large_pox_fattree_no_logging_2013_03_26_19_45_38/dataplane.trace",
                 multiplex_sockets=True)

control_flow = EfficientMCSFinder(simulation_config, "experiments/large_pox_fattree_no_logging_2013_03_26_19_45_38/events.trace",
                                  wait_on_deterministic_values=False,
                                  invariant_check_name='check_stale_entries')
