
from config.experiment_config_lib import ControllerConfig
from sts.topology import MeshTopology
from sts.control_flow import Fuzzer
from sts.input_traces.input_logger import InputLogger
from sts.simulation_state import SimulationConfig

# Use POX as our controller
start_cmd = ('''./pox.py --verbose '''
             #'''sts.syncproto.pox_syncer --blocking=False '''
             '''openflow.discovery topology '''
             '''host_tracker '''
             '''sts.util.socket_mux.pox_monkeypatcher '''
             '''openflow.of_01 --address=__address__ --port=__port__ --max_connections=15''')

controllers = [ControllerConfig(start_cmd, cwd="pox")]
topology_class = MeshTopology
topology_params = "num_switches=2"

simulation_config = SimulationConfig(controller_configs=controllers,
                                     topology_class=topology_class,
                                     topology_params=topology_params,
                                     multiplex_sockets=True)

control_flow = Fuzzer(simulation_config, check_interval=150,
fuzzer_params='experiments/trigger_memory_leak2/fuzzer_params.py',
                      halt_on_violation=True,
                      initialization_rounds=30,
                      input_logger=InputLogger(),
                      invariant_check_name="InvariantChecker.check_liveness")

raise RuntimeError("Please add this parameter to Fuzzer: fuzzer_params='experiments/trigger_memory_leak3/fuzzer_params.py'")