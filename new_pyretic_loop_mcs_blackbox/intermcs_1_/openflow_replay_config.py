
from config.experiment_config_lib import ControllerConfig
from sts.topology import *
from sts.control_flow import OpenFlowReplayer
from sts.simulation_state import SimulationConfig
from sts.input_traces.input_logger import InputLogger

simulation_config = SimulationConfig(controller_configs=[ControllerConfig(start_cmd='./pyretic.py -m p0 -v high pyretic.modules.hub', label='c1', address='127.0.0.1', cwd='../pyretic', kill_cmd='ps aux | grep -e pox -e pyretic | grep -v simulator | cut -c 9-15 | xargs kill -9')],
                 topology_class=MeshTopology,
                 topology_params="num_switches=3",
                 patch_panel_class=BufferedPatchPanel,
                 multiplex_sockets=False,
                 ignore_interposition=True,
                 kill_controllers_on_exit=True)

control_flow = OpenFlowReplayer(simulation_config, "experiments/t/intermcs_1_/mcs.trace.notimeouts")
# wait_on_deterministic_values=False
# delay_flow_mods=False
# Invariant check: 'InvariantChecker.python_check_loops'
# Bug signature: "{'hs_history': [(x^L) - ([]), (dl_vlan:65535,dl_vlan_pcp:0) - ([]), (dl_vlan:65535,dl_vlan_pcp:0) - ([])], 'hdr': (dl_vlan:65535,dl_vlan_pcp:0) - ([]), 'visits': [100001, 200002, 300001], 'port': 100001}"
