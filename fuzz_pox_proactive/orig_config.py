
from config.experiment_config_lib import ControllerConfig
from sts.topology import FatTree
from sts.control_flow import Fuzzer
from sts.input_traces.input_logger import InputLogger
from sts.simulation_state import SimulationConfig
from sts.util.convenience import backtick

def get_additional_metadata():
  path = "dart_pox"
  return {
    'commit' : backtick("git rev-parse HEAD", cwd=path),
    'branch' : backtick("git rev-parse --abbrev-ref HEAD", cwd=path),
    'remote' : backtick("git remote show origin", cwd=path),
  }


# Use POX as our controller
start_cmd = ('''./pox.py --verbose '''
             #'''sts.syncproto.pox_syncer --blocking=False '''
             '''openflow.discovery forwarding.topo_proactive '''
             #'''sts.util.socket_mux.pox_monkeypatcher '''
             '''openflow.of_01 --address=__address__ --port=__port__''')

controllers = [ControllerConfig(start_cmd, cwd="dart_pox")]
topology_class = FatTree
topology_params = "num_pods=3"

simulation_config = SimulationConfig(controller_configs=controllers,
                                     topology_class=topology_class,
                                     topology_params=topology_params)

control_flow = Fuzzer(simulation_config, check_interval=20,
                      halt_on_violation=True,
                      input_logger=InputLogger(),
                      invariant_check_name="check_for_invalid_ports")

raise RuntimeError("Please add this parameter to Fuzzer: fuzzer_params='experiments/fuzz_pox_proactive/fuzzer_params.py'")