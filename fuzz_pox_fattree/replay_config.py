
from config.experiment_config_lib import ControllerConfig
from sts.topology import *
from sts.control_flow import Replayer
from sts.simulation_state import SimulationConfig

simulation_config = SimulationConfig(controller_configs=[ControllerConfig(cmdline='./pox.py --verbose --no-cli sts.syncproto.pox_syncer openflow.discovery openflow.spanning_tree forwarding.l2_multi sts.util.socket_mux.pox_monkeypatcher openflow.of_01 --address=__address__ --port=__port__', address='127.0.0.1', port=6633, cwd='pox', sync='tcp:localhost:18900')],
                 topology_class=FatTree,
                 topology_params="",
                 patch_panel_class=BufferedPatchPanel,
                 dataplane_trace="exp/fuzz_pox_fattree/dataplane.trace",
                 multiplex_sockets=True)

old_ingress_dpid = 3
def check_stale_entries(simulation):
  access_links = filter(lambda x: x.switch.dpid == old_ingress_dpid,
                        simulation.topology.access_links)
  assert(len(access_links) < 2)
  if len(access_links) == 1:
    link = access_links[0]
    old_switch = link.switch
    old_port = link.switch_port # ofp_phy_port
    old_port_no = old_port.port_no

    # Conjunction of old_port in switch's down ports
    # and old_port still being in routing table
    port_down = old_port_no in old_switch.down_port_nos
    old_entries = old_switch.table.entries_for_port(old_port_no)
    old_old_entries = self.fuzzer.old_routing_entries

    if port_down and len(old_entries) > 0:
      # we have a violation!
      return old_entries

  return []

control_flow = Replayer(simulation_config, "exp/fuzz_pox_fattree/events.trace",
                        invariant_checker=check_stale_entries,
                        wait_on_deterministic_values=False)
