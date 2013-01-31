from config.experiment_config_lib import ControllerConfig
from sts.control_flow import Fuzzer
from sts.input_traces.input_logger import InputLogger
from sts.simulation_state import SimulationConfig
from sts.invariant_checker import InvariantChecker

# Use POX as our controller
command_line = ('''./pox.py --verbose --no-cli sts.syncproto.pox_syncer '''
                '''openflow.discovery openflow.spanning_tree forwarding.l2_multi '''
                '''sts.util.socket_mux.pox_monkeypatcher '''
                '''openflow.of_01 --address=../sts_socket_pipe''')
controllers = [ControllerConfig(command_line, address="sts_socket_pipe",
    port=6635, cwd="pox", sync="tcp:localhost:18900")]

simulation_config = SimulationConfig(controller_configs=controllers,
                                     multiplex_sockets=True)

#timestamp_results = True
#exp_name = "fat_tree_migrations_and_switches"

# Use a Fuzzer (already the default)
control_flow = Fuzzer(simulation_config,
                      #fuzzer_params="exp/config/fuzzer_params_migration_and_switches.py",
                      check_interval=20,
                      halt_on_violation=False,
                      initialization_rounds=65,
                      steps=2000,
                      input_logger=InputLogger(),
                      invariant_check=InvariantChecker.python_check_connectivity)

