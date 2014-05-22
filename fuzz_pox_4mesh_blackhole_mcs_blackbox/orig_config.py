
from config.experiment_config_lib import ControllerConfig
from sts.topology import *
from sts.control_flow import EfficientMCSFinder
from sts.invariant_checker import InvariantChecker
from sts.simulation_state import SimulationConfig

simulation_config = SimulationConfig(controller_configs=[ControllerConfig(cmdline='./pox.py --verbose --no-cli sts.syncproto.pox_syncer openflow.discovery openflow.spanning_tree forwarding.l2_multi sts.util.socket_mux.pox_monkeypatcher openflow.of_01 --address=__address__ --port=__port__', address='127.0.0.1', port=6632, cwd='pox', sync='tcp:localhost:18901')],
                 topology_class=MeshTopology,
                 topology_params="num_switches=4",
                 patch_panel_class=BufferedPatchPanel,
                 dataplane_trace="experiments/fuzz_pox_4mesh_blackhole/dataplane.trace",
                 multiplex_sockets=True,
                 ignore_interposition=True)

def check_stale_entries(simulation):
  '''Check that the migrated host's old switch has stale entries'''
  dpid = 1 # hardcoding host 1
  port_no = 4

  switch = simulation.topology.get_switch(dpid)

  port_down = port_no in switch.down_port_nos
  old_entries = switch.table.entries_for_port(port_no)

  if port_down and len(old_entries) > 0:
    # we have a violation!
    return old_entries

  return []

control_flow = EfficientMCSFinder(simulation_config, "experiments/fuzz_pox_4mesh_blackhole/events.trace",
                                  invariant_check=check_stale_entries,
                                  wait_on_deterministic_values=False)
