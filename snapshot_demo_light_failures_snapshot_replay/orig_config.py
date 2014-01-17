
from config.experiment_config_lib import ControllerConfig
from sts.topology import *
from sts.control_flow import Replayer
from sts.simulation_state import SimulationConfig
from sts.input_traces.input_logger import InputLogger
from sts.control_flow.peeker import SnapshotPeeker

simulation_config =SimulationConfig(
  controller_configs=[
    ControllerConfig(
    start_cmd='''./pox.py --verbose openflow.discovery '''
    '''forwarding.l2_multi_synthetic_link_failure_crash '''
    '''sts.util.socket_mux.pox_monkeypatcher --snapshot_address=/tmp/snapshot_address '''
    '''openflow.of_01 --address=__address__ --port=__port__''',
    label='c1', address='127.0.0.1', cwd='pox',
    snapshot_address="/tmp/snapshot_address")
  ],
  topology_class=MeshTopology,
  topology_params="num_switches=3",
  patch_panel_class=BufferedPatchPanel,
  multiplex_sockets=True,
  kill_controllers_on_exit=True)

peeker = SnapshotPeeker(simulation_config, default_dp_permit=True)
# TODO(cs): pass through sends? Add default_dp_permit to Replayer?
control_flow = Replayer(simulation_config, "experiments/snapshot_demo_light_failures/events.trace",
                        input_logger=InputLogger(),
                        wait_on_deterministic_values=False,
                        allow_unexpected_messages=False,
                        delay_flow_mods=True,
                        pass_through_whitelisted_messages=True,
                        invariant_check_name='InvariantChecker.check_liveness',
                        bug_signature="",
                        transform_dag=peeker.peek)
