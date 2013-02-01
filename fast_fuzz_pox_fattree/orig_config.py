from config.experiment_config_lib import ControllerConfig
from sts.control_flow import Fuzzer
from sts.input_traces.input_logger import InputLogger
from sts.simulation_state import SimulationConfig
from sts.invariant_checker import InvariantChecker

# Use POX as our controller
command_line = ('''./pox.py --verbose --no-cli sts.syncproto.pox_syncer '''
                '''openflow.discovery openflow.spanning_tree forwarding.l2_multi '''
                '''sts.util.socket_mux.pox_monkeypatcher '''
                '''openflow.of_01 --address=__address__ --port=__port__''')
controllers = [ControllerConfig(command_line,
                                cwd="pox", sync="tcp:localhost:18900")]

simulation_config = SimulationConfig(controller_configs=controllers,
                                     multiplex_sockets=True)

#timestamp_results = True
#exp_name = "fat_tree_migrations_and_switches"

def check_stale_entries(simulation):
  '''Check that the migrated host's old switch has stale entries'''
  dpid = 1 # hardcoding host 1
  port_no = 1

  switch = simulation.topology.get_switch(dpid)

  port_down = port_no in switch.down_port_nos
  old_entries = switch.table.entries_for_port(port_no)

  if port_down and len(old_entries) > 0:
    # we have a violation!
    return old_entries

  return []

# Use a Fuzzer (already the default)
control_flow = Fuzzer(simulation_config,
                      #fuzzer_params="exp/config/fuzzer_params_migration_and_switches.py",
                      check_interval=20,
                      halt_on_violation=True,
                     # single_hm_wait_rounds=30,
                      initialization_rounds=70,
                      steps=300,
                      input_logger=InputLogger(),
                      invariant_check=check_stale_entries)
