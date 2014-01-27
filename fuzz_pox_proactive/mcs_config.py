
from config.experiment_config_lib import ControllerConfig
from sts.topology import *
from sts.control_flow import EfficientMCSFinder
from sts.invariant_checker import InvariantChecker
from sts.simulation_state import SimulationConfig

simulation_config = SimulationConfig(controller_configs=[ControllerConfig(start_cmd='./pox.py --verbose openflow.discovery forwarding.topo_proactive openflow.of_01 --address=__address__ --port=__port__', label='c1', address='127.0.0.1', cwd='dart_pox')],
                 topology_class=FatTree,
                 topology_params="num_pods=3",
                 patch_panel_class=BufferedPatchPanel,
                 multiplex_sockets=False,
                 kill_controllers_on_exit=True)

control_flow = EfficientMCSFinder(simulation_config, "experiments/fuzz_pox_proactive/events.trace",
                                  wait_on_deterministic_values=False,
                                  delay_flow_mods=False,
                                  default_dp_permit=True,
                                  invariant_check_name='check_for_invalid_ports',
                                  bug_signature="")
