
from config.experiment_config_lib import ControllerConfig
from sts.topology import *
from sts.control_flow import InteractiveReplayer
from sts.simulation_state import SimulationConfig
from sts.input_traces.input_logger import InputLogger

simulation_config = SimulationConfig(controller_configs=[ControllerConfig(start_cmd='./pox.py --verbose --unthreaded-sh misc.ip_loadbalancer --ip=123.123.1.3 --servers=123.123.2.3,123.123.1.3 sts.util.socket_mux.pox_monkeypatcher   openflow.discovery openflow.of_01 --address=__address__ --port=__port__', label='c1', address='127.0.0.1', cwd='dart_pox')],
                 topology_class=MeshTopology,
                 topology_params="num_switches=3",
                 patch_panel_class=BufferedPatchPanel,
                 multiplex_sockets=True,
                 kill_controllers_on_exit=True)

control_flow = InteractiveReplayer(simulation_config, "experiments/load_balancer_fuzzer_mcs_passthrough/interreplay_5_l_2/events.trace")
# wait_on_deterministic_values=False
# delay_flow_mods=False
# Invariant check: 'check_for_ofp_error'
# Bug signature: "ERROR_SENT"
