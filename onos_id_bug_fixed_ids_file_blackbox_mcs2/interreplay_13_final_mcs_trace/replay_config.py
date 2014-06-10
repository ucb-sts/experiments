
from config.experiment_config_lib import ControllerConfig
from sts.topology import *
from sts.control_flow.replayer import Replayer
from sts.simulation_state import SimulationConfig
from sts.input_traces.input_logger import InputLogger

simulation_config = SimulationConfig(controller_configs=[ControllerConfig(start_cmd='./start-onos.sh start', label='c1', address='192.168.56.11', cwd='/home/mininet/ONOS', controller_type='onos', kill_cmd='./start-onos.sh stop', restart_cmd='./start-onos.sh stop'), ControllerConfig(start_cmd='./start-onos.sh start', label='c2', address='192.168.56.12', cwd='/home/mininet/ONOS', controller_type='onos', kill_cmd='./start-onos.sh stop', restart_cmd='./start-onos.sh stop')],
                 topology_class=MeshTopology,
                 topology_params="num_switches=2",
                 patch_panel_class=BufferedPatchPanel,
                 multiplex_sockets=False,
                 ignore_interposition=True,
                 kill_controllers_on_exit=False)

control_flow = Replayer(simulation_config, "experiments/onos_id_bug_fixed_ids_file_blackbox_mcs2/interreplay_13_final_mcs_trace/events.trace",
                        input_logger=InputLogger(),
                        wait_on_deterministic_values=False,
                        allow_unexpected_messages=False,
                        delay_flow_mods=False,
                        default_dp_permit=False,
                        pass_through_whitelisted_messages=False,
                        invariant_check_name='check_for_file',
                        bug_signature="bug_file_detected")
