
from config.experiment_config_lib import ControllerConfig
from sts.topology import *
from sts.control_flow import Replayer
from sts.simulation_state import SimulationConfig
from sts.input_traces.input_logger import InputLogger

simulation_config = SimulationConfig(controller_configs=[ControllerConfig(start_cmd='./pyretic.py -m p0 pyretic.examples.firewall_for_sts_no_close', label='c1', address='127.0.0.1', cwd='../pyretic', kill_cmd='ps aux | grep -e pox -e pyretic | grep -v simulator | cut -c 9-15 | xargs kill -9')],
                 topology_class=MeshTopology,
                 topology_params="num_switches=3",
                 patch_panel_class=BufferedPatchPanel,
                 multiplex_sockets=False,
                 kill_controllers_on_exit=True)

control_flow = Replayer(simulation_config, "experiments/fuzz_pyretic_mesh_proactive_firewall_no_close_check_loop_mcs/intermcs_1_/mcs.trace.notimeouts",
                        input_logger=InputLogger(),
                        wait_on_deterministic_values=False,
                        allow_unexpected_messages=False,
                        delay_flow_mods=False,
                        pass_through_whitelisted_messages=True,
                        invariant_check_name='InvariantChecker.python_check_loops',
                        bug_signature='{'hs_history': [(x^L) - ([]), (dl_vlan:65535,dl_vlan_pcp:0,dl_type:2054,nw_src:123.123.1.3/32,nw_dst:123.123.3.3/32) - ([]), (dl_vlan:65535,dl_vlan_pcp:0,dl_type:2054,nw_src:123.123.1.3/32,nw_dst:123.123.3.3/32) - ([]), (dl_vlan:65535,dl_vlan_pcp:0,dl_type:2054,nw_src:123.123.1.3/32,nw_dst:123.123.3.3/32) - ([])], 'hdr': (dl_vlan:65535,dl_vlan_pcp:0,dl_type:2054,nw_src:123.123.1.3/32,nw_dst:123.123.3.3/32) - ([]), 'visits': [100004, 200002, 300001, 100001], 'port': 200002}')
