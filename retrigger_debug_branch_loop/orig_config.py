from config.experiment_config_lib import ControllerConfig
from sts.topology import MeshTopology
from sts.control_flow.fuzzer import Fuzzer
from sts.input_traces.input_logger import InputLogger
from sts.simulation_state import SimulationConfig
from sts.util.convenience import backtick

def get_additional_metadata():
  return {
    'commit' : backtick("git rev-parse HEAD", cwd="old_pox"),
    'branch' : backtick("git rev-parse --abbrev-ref HEAD", cwd="old_pox")
  }


# Use POX as our controller
command_line = ('''./pox.py --verbose '''
                '''sts.syncproto.pox_syncer --blocking=False '''
                '''openflow.discovery forwarding.l2_multi '''
                '''sts.util.socket_mux.pox_monkeypatcher '''
                '''openflow.of_01 --address=__address__ --port=__port__''')
controllers = [ControllerConfig(command_line, cwd="old_pox", sync="tcp:localhost:18899")]
topology_class = MeshTopology
topology_params = "num_switches=2"
dataplane_trace = "experiments/debug_branch_loop/dataplane.trace"

simulation_config = SimulationConfig(controller_configs=controllers,
                                     topology_class=topology_class,
                                     topology_params=topology_params,
                                     dataplane_trace=dataplane_trace,
                                     violation_persistence_threshold=20,
                                     multiplex_sockets=True)

control_flow = Fuzzer(simulation_config, check_interval=3,
                      halt_on_violation=True,
                      input_logger=InputLogger(),
                      invariant_check_name="check_for_blackholes_or_connectivity",
                      #steps=141,
                      #random_seed=466448715
                      )

raise RuntimeError("Please add this parameter to Fuzzer: fuzzer_params='experiments/retrigger_debug_branch_loop/fuzzer_params.py'")