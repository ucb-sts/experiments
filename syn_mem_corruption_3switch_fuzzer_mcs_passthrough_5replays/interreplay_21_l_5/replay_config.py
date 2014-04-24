
from config.experiment_config_lib import ControllerConfig
from sts.topology import *
from sts.control_flow import Replayer
from sts.simulation_state import SimulationConfig
from sts.input_traces.input_logger import InputLogger

simulation_config = SimulationConfig(controller_configs=[ControllerConfig(start_cmd='./pox.py --verbose openflow.of_01 --address=__address__ --port=__port__ openflow.discovery forwarding.l2_multi_syn_mem_corruption', label='c1', address='127.0.0.1', cwd='pox')],
                 topology_class=MeshTopology,
                 topology_params="num_switches=4",
                 patch_panel_class=BufferedPatchPanel,
                 multiplex_sockets=False,
                 kill_controllers_on_exit=True)

control_flow = Replayer(simulation_config, "experiments/syn_mem_corruption_3switch_fuzzer_mcs_passthrough_5replays/interreplay_21_l_5/events.trace",
                        input_logger=InputLogger(),
                        wait_on_deterministic_values=False,
                        allow_unexpected_messages=False,
                        delay_flow_mods=False,
                        default_dp_permit=False,
                        pass_through_whitelisted_messages=False,
                        invariant_check_name='InvariantChecker.check_liveness',
                        bug_signature="c1")
