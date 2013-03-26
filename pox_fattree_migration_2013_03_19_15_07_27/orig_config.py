from config.experiment_config_lib import ControllerConfig
from sts.control_flow import Fuzzer
from sts.input_traces.input_logger import InputLogger
from sts.topology import MeshTopology
from sts.simulation_state import SimulationConfig
from sts.invariant_checker import InvariantChecker

# Use POX as our controller
command_line = ('''./pox.py --verbose --no-cli sts.syncproto.pox_syncer '''
                '''openflow.discovery openflow.spanning_tree forwarding.l2_multi '''
                '''sts.util.socket_mux.pox_monkeypatcher '''
                '''openflow.of_01 --address=__address__ --port=__port__''')
controllers = [ControllerConfig(command_line,
                                port=6632,
                                cwd="pox", sync="tcp:localhost:18901")]
topology_params = "num_pods=10"

simulation_config = SimulationConfig(controller_configs=controllers,
                                     topology_params=topology_params,
                                     multiplex_sockets=True)

timestamp_results = True

# Use a Fuzzer (already the default)
control_flow = Fuzzer(simulation_config,
                      #fuzzer_params="exp/config/fuzzer_params_migration_and_switches.py",
                      check_interval=20,
                      halt_on_violation=True,
                      single_hm_wait_rounds=30,
                      initialization_rounds=70,
                      steps=300,
                      input_logger=InputLogger(),
                      invariant_check_name="check_stale_entries")
