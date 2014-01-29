
from config.experiment_config_lib import ControllerConfig
from sts.topology import *
from sts.control_flow import InteractiveReplayer
from sts.simulation_state import SimulationConfig
from sts.input_traces.input_logger import InputLogger

simulation_config = SimulationConfig(controller_configs=[ControllerConfig(start_cmd='./pox.py --verbose openflow.of_01 --address=__address__ --port=__port__ openflow.discovery forwarding.l2_multi', label='c1', address='127.0.0.1', cwd='pox_carp')],
                 topology_class=MeshTopology,
                 topology_params="num_switches=4",
                 patch_panel_class=BufferedPatchPanel,
                 multiplex_sockets=False,
                 kill_controllers_on_exit=True)

control_flow = InteractiveReplayer(simulation_config, "experiments/pox_switch_hash_bug_fuzz_fuzzer_mcs/interreplay_6_l_5/events.trace")
# wait_on_deterministic_values=False
# delay_flow_mods=True
# Invariant check: 'InvariantChecker.check_liveness'
# Bug signature: "c1"
