
from config.experiment_config_lib import ControllerConfig
from sts.topology import *
from sts.control_flow import EfficientMCSFinder
from sts.invariant_checker import InvariantChecker
from sts.simulation_state import SimulationConfig

simulation_config = SimulationConfig(controller_configs=[ControllerConfig(start_cmd='./pox.py --verbose openflow.of_01 --address=__address__ --port=__port__ openflow.discovery forwarding.l2_multi', label='c1', address='127.0.0.1', cwd='pox_carp')],
                 topology_class=MeshTopology,
                 topology_params="num_switches=4",
                 patch_panel_class=BufferedPatchPanel,
                 multiplex_sockets=False,
                 kill_controllers_on_exit=True,
                 ignore_interposition=True)

control_flow = EfficientMCSFinder(simulation_config, "experiments/pox_switch_hash_bug_fuzz_fuzzer/events.trace",
                                  wait_on_deterministic_values=False,
                                  default_dp_permit=False,
                                  pass_through_whitelisted_messages=False,
                                  delay_flow_mods=True,
                                  invariant_check_name='InvariantChecker.check_liveness',
                                  bug_signature="")
