
from config.experiment_config_lib import ControllerConfig
from sts.topology import *
from sts.control_flow import OpenFlowReplayer
from sts.simulation_state import SimulationConfig
from sts.input_traces.input_logger import InputLogger

simulation_config = SimulationConfig(controller_configs=[ControllerConfig(start_cmd='./pox.py --verbose openflow.discovery forwarding.l2_multi forwarding.capabilities_manager sts.util.socket_mux.pox_monkeypatcher openflow.of_01 --address=__address__ --port=__port__', label='c1', address='127.0.0.1', cwd='pox')],
                 topology_class=MeshTopology,
                 topology_params="num_switches=3",
                 patch_panel_class=BufferedPatchPanel,
                 multiplex_sockets=True,
                 kill_controllers_on_exit=True)

control_flow = OpenFlowReplayer(simulation_config, "experiments/trigger_priority_mismatch_mcs/interreplay_10_r_2/events.trace")
# wait_on_deterministic_values=False
# delay_flow_mods=False
# Invariant check: 'check_for_flow_entry'
# Bug signature: "123Found"
