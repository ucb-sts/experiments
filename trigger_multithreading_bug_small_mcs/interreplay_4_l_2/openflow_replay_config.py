
from config.experiment_config_lib import ControllerConfig
from sts.topology import *
from sts.control_flow import OpenFlowReplayer
from sts.simulation_state import SimulationConfig
from sts.input_traces.input_logger import InputLogger

simulation_config = SimulationConfig(controller_configs=[ControllerConfig(start_cmd='./pox.py --verbose openflow.discovery forwarding.topo_proactive sts.util.socket_mux.pox_monkeypatcher openflow.of_01 --address=__address__ --port=6709', label='c1', address='127.0.0.1', cwd='dart_pox')],
                 topology_class=MeshTopology,
                 topology_params="num_switches=4",
                 patch_panel_class=BufferedPatchPanel,
                 multiplex_sockets=True,
                 kill_controllers_on_exit=True)

control_flow = OpenFlowReplayer(simulation_config, "experiments/trigger_multithreading_bug_small_mcs/interreplay_4_l_2/events.trace")
# wait_on_deterministic_values=False
# delay_flow_mods=False
# Invariant check: 'InvariantChecker.check_liveness'
# Bug signature: "c1"
