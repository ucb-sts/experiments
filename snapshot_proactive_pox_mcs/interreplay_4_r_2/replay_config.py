
from config.experiment_config_lib import ControllerConfig
from sts.topology import *
from sts.control_flow import Replayer
from sts.simulation_state import SimulationConfig
from sts.input_traces.input_logger import InputLogger

simulation_config = SimulationConfig(controller_configs=[ControllerConfig(start_cmd='./pox.py --verbose --unthreaded-sh sts.util.socket_mux.pox_monkeypatcher openflow.discovery forwarding.topo_proactive openflow.of_01 --address=__address__ --port=__port__', label='c1', address='127.0.0.1', cwd='dart_pox')],
                 topology_class=FatTree,
                 topology_params="num_pods=3",
                 patch_panel_class=BufferedPatchPanel,
                 multiplex_sockets=True,
                 kill_controllers_on_exit=True)

control_flow = Replayer(simulation_config, "experiments/snapshot_proactive_pox_mcs/interreplay_4_r_2/events.trace",
                        input_logger=InputLogger(),
                        wait_on_deterministic_values=False,
                        allow_unexpected_messages=False,
                        delay_flow_mods=False,
                        pass_through_whitelisted_messages=True,
                        invariant_check_name='check_for_invalid_ports',
                        bug_signature="(1, 0)")
