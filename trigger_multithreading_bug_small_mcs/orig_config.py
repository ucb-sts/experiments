
from config.experiment_config_lib import ControllerConfig
from sts.topology import *
from sts.control_flow import EfficientMCSFinder
from sts.invariant_checker import InvariantChecker
from sts.simulation_state import SimulationConfig

simulation_config = SimulationConfig(controller_configs=[ControllerConfig(start_cmd='./pox.py --verbose openflow.discovery forwarding.topo_proactive sts.util.socket_mux.pox_monkeypatcher openflow.of_01 --address=__address__ --port=6709',
    port=6709, label='c1', address='127.0.0.1', cwd='dart_pox')],
                 topology_class=MeshTopology,
                 topology_params="num_switches=4",
                 patch_panel_class=BufferedPatchPanel,
                 multiplex_sockets=True,
                 kill_controllers_on_exit=True)

control_flow = EfficientMCSFinder(simulation_config, "experiments/trigger_multithreading_bug_small/events.trace",
                                  wait_on_deterministic_values=False,
                                  default_dp_permit=True,
                                  pass_through_whitelisted_messages=True,
                                  delay_flow_mods=False,
                                  max_replays_per_subsequence=2,
                                  invariant_check_name='InvariantChecker.check_liveness',
                                  bug_signature="")
