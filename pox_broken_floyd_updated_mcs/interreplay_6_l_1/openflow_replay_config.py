
from config.experiment_config_lib import ControllerConfig
from sts.topology import *
from sts.control_flow.openflow_replayer import OpenFlowReplayer
from sts.simulation_state import SimulationConfig
from sts.input_traces.input_logger import InputLogger

simulation_config = SimulationConfig(controller_configs=[ControllerConfig(start_cmd='./pox.py --verbose openflow.discovery forwarding.l2_multi_broken_floyd  sts.util.socket_mux.pox_monkeypatcher openflow.of_01 --address=__address__  --port=__port__', label='c1', address='127.0.0.1', cwd='pox')],
                 topology_class=MeshTopology,
                 topology_params="num_switches=3",
                 patch_panel_class=BufferedPatchPanel,
                 multiplex_sockets=True,
                 ignore_interposition=True,
                 kill_controllers_on_exit=True)

control_flow = OpenFlowReplayer(simulation_config, "experiments/pox_broken_floyd_updated_mcs/interreplay_6_l_1/events.trace")
# wait_on_deterministic_values=False
# delay_flow_mods=False
# Invariant check: 'InvariantChecker.python_check_loops'
# Bug signature: "{'hs_history': [(x^L) - ([]), (dl_src:12:34:56:78:01:03,dl_dst:12:34:56:78:03:03,dl_vlan:65535,dl_vlan_pcp:0,dl_type:2048,nw_tos:0,nw_proto:1,nw_src:123.123.1.3/32,nw_dst:123.123.3.3/32,tp_src:0,tp_dst:0) - ([]), (dl_src:12:34:56:78:01:03,dl_dst:12:34:56:78:03:03,dl_vlan:65535,dl_vlan_pcp:0,dl_type:2048,nw_tos:0,nw_proto:1,nw_src:123.123.1.3/32,nw_dst:123.123.3.3/32,tp_src:0,tp_dst:0) - ([]), (dl_src:12:34:56:78:01:03,dl_dst:12:34:56:78:03:03,dl_vlan:65535,dl_vlan_pcp:0,dl_type:2048,nw_tos:0,nw_proto:1,nw_src:123.123.1.3/32,nw_dst:123.123.3.3/32,tp_src:0,tp_dst:0) - ([])], 'hdr': (dl_src:12:34:56:78:01:03,dl_dst:12:34:56:78:03:03,dl_vlan:65535,dl_vlan_pcp:0,dl_type:2048,nw_tos:0,nw_proto:1,nw_src:123.123.1.3/32,nw_dst:123.123.3.3/32,tp_src:0,tp_dst:0) - ([]), 'visits': [100003, 200002, 300001, 100001], 'port': 200002}"
