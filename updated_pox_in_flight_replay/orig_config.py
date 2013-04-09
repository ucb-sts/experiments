
from config.experiment_config_lib import ControllerConfig
from sts.topology import *
from sts.control_flow import Replayer
from sts.simulation_state import SimulationConfig

simulation_config = SimulationConfig(controller_configs=[ControllerConfig(cmdline='./pox.py --verbose sts.syncproto.pox_syncer --blocking=False openflow.discovery forwarding.l2_multi sts.util.socket_mux.pox_monkeypatcher openflow.of_01 --address=__address__ --port=__port__', address='127.0.0.1', port=6688, cwd='pox', sync='tcp:localhost:18899')],
                 topology_class=MeshTopology,
                 topology_params="num_switches=2",
                 patch_panel_class=BufferedPatchPanel,
                 multiplex_sockets=True)

control_flow = Replayer(simulation_config, "experiments/updated_pox_in_flight/events.trace",
                        wait_on_deterministic_values=False)
# Invariant check: 'check_for_loops_blackholes_or_connectivity'
