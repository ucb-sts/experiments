
from config.experiment_config_lib import ControllerConfig
from sts.topology import *
from sts.control_flow import Replayer
from sts.simulation_state import SimulationConfig
from sts.input_traces.input_logger import InputLogger

simulation_config = SimulationConfig(controller_configs=[ControllerConfig(start_cmd='./pox.py --verbose openflow.discovery forwarding.l2_multi_broken_floyd sts.util.socket_mux.pox_monkeypatcher openflow.of_01 --address=__address__ --port=7777', label='c1', address='127.0.0.1', cwd='pox')],
                 topology_class=MeshTopology,
                 topology_params="num_switches=3",
                 patch_panel_class=BufferedPatchPanel,
                 multiplex_sockets=True,
                 kill_controllers_on_exit=True)

control_flow = Replayer(simulation_config, "experiments/pox_broken_floyd_mcs/interreplay_27_final_mcs_trace/events.trace",
                        input_logger=InputLogger(),
                        wait_on_deterministic_values=False,
                        allow_unexpected_messages=False,
                        delay_flow_mods=False,
                        default_dp_permit=False,
                        pass_through_whitelisted_messages=False,
                        invariant_check_name='InvariantChecker.check_loops',
                        bug_signature="(300003, ['-> Port: 300003', '-> Port: 100001', '-> Port: 200002', '-> Port: 300001', '-> Port: 100001'], (dl_src:12:34:56:78:01:03,dl_dst:12:34:56:78:03:03,dl_vlan:65535,dl_vlan_pcp:0,dl_type:2048,nw_tos:0,nw_proto:1,nw_src:10.1.3.2/32,nw_dst:10.3.3.2/32,tp_src:0,tp_dst:0) - ([]))")
