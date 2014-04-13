
from config.experiment_config_lib import ControllerConfig
from sts.topology import *
from sts.control_flow import EfficientMCSFinder
from sts.invariant_checker import InvariantChecker
from sts.simulation_state import SimulationConfig

simulation_config = SimulationConfig(controller_configs=[ControllerConfig(start_cmd='./pox.py --verbose openflow.discovery topology host_tracker sts.util.socket_mux.pox_monkeypatcher openflow.of_01 --address=__address__ --port=__port__ --max_connections=15', label='c1', address='127.0.0.1', cwd='pox')],
                 topology_class=MeshTopology,
                 topology_params="num_switches=2",
                 patch_panel_class=BufferedPatchPanel,
                 multiplex_sockets=True,
                 kill_controllers_on_exit=True)

control_flow = EfficientMCSFinder(simulation_config, "experiments/trigger_memory_leak3/events.trace",
                                  wait_on_deterministic_values=False,
                                  default_dp_permit=True,
                                  pass_through_whitelisted_messages=True,
                                  delay_flow_mods=False,
                                  invariant_check_name='InvariantChecker.check_liveness',
                                  bug_signature="")
