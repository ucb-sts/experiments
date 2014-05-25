
from config.experiment_config_lib import ControllerConfig
from sts.topology import *
from sts.control_flow import InteractiveReplayer
from sts.simulation_state import SimulationConfig
from sts.input_traces.input_logger import InputLogger

simulation_config = SimulationConfig(controller_configs=[ControllerConfig(start_cmd='./pox.py --verbose openflow.discovery forwarding.l2_multi forwarding.capabilities_manager sts.util.socket_mux.pox_monkeypatcher openflow.of_01 --address=__address__ --port=__port__', label='c1', address='127.0.0.1', cwd='pox')],
                 topology_class=MeshTopology,
                 topology_params="num_switches=2",
                 patch_panel_class=BufferedPatchPanel,
                 multiplex_sockets=True,
                 ignore_interposition=True,
                 kill_controllers_on_exit=True)

control_flow = InteractiveReplayer(simulation_config, "experiments/trigger_priority_mismatch_small_mcs_blackbox/mcs.trace.notimeouts")
# wait_on_deterministic_values=False
# delay_flow_mods=False
# Invariant check: 'check_for_flow_entry'
# Bug signature: "123Found"
