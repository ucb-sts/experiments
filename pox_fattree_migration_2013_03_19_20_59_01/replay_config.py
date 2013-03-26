
from config.experiment_config_lib import ControllerConfig
from sts.topology import *
from sts.control_flow import Replayer
from sts.simulation_state import SimulationConfig

simulation_config = SimulationConfig(controller_configs=[ControllerConfig(cmdline='./pox.py --verbose --no-cli sts.syncproto.pox_syncer openflow.discovery openflow.spanning_tree forwarding.l2_multi sts.util.socket_mux.pox_monkeypatcher openflow.of_01 --address=__address__ --port=__port__', address='127.0.0.1', port=6632, cwd='pox', sync='tcp:localhost:18901')],
                 topology_class=FatTree,
                 topology_params="num_pods=10",
                 patch_panel_class=BufferedPatchPanel,
                 dataplane_trace="experiments/pox_fattree_migration_2013_03_19_20_59_01/dataplane.trace",
                 multiplex_sockets=True)

control_flow = Replayer(simulation_config, "experiments/pox_fattree_migration_2013_03_19_20_59_01/events.trace",
                        wait_on_deterministic_values=False)
# Invariant check: 'check_stale_entries'
