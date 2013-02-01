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

class MigrationChecker(object):
  def __call__(self, simulation):
    '''Check that the migrated host's old switch has stale entries'''
    if self.fuzzer.migrated_link:
      link = self.fuzzer.migrated_link
      old_switch = link.switch
      old_port = link.switch_port # ofp_phy_port
      old_port_no = old_port.port_no

      # Conjunction of old_port in switch's down ports
      # and old_port still being in routing table
      port_down = old_port_no in old_switch.down_port_nos
      old_entries = old_switch.table.entries_for_port(old_port_no)
      if port_down and len(old_entries) > 0:
        # we have a violation!
        return old_entries

    return []

mc = MigrationChecker()

# Use a Fuzzer (already the default)
control_flow = Fuzzer(simulation_config,
                      #fuzzer_params="exp/config/fuzzer_params_migration_and_switches.py",
                      check_interval=20,
                      halt_on_violation=True,
                      single_hm_wait_rounds=50,
                      initialization_rounds=70,
                      steps=2000,
                      input_logger=InputLogger(),
                      invariant_check=mc)

mc.fuzzer = control_flow # HUGE HACK
