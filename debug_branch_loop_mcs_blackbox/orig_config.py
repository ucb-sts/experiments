
from config.experiment_config_lib import ControllerConfig
from sts.topology import *
from sts.control_flow import EfficientMCSFinder
from sts.invariant_checker import InvariantChecker
from sts.simulation_state import SimulationConfig

simulation_config = SimulationConfig(controller_configs=[ControllerConfig(cmdline='./pox.py --verbose sts.syncproto.pox_syncer --blocking=False openflow.discovery forwarding.l2_multi sts.util.socket_mux.pox_monkeypatcher openflow.of_01 --address=__address__ --port=6634', address='127.0.0.1', port=6634, cwd='pox', sync='tcp:localhost:19999')],
                 topology_class=MeshTopology,
                 topology_params="num_switches=2",
                 patch_panel_class=BufferedPatchPanel,
                 dataplane_trace="dataplane_traces/ping_pong_same_subnet.trace",
                 multiplex_sockets=True,
                 ignore_interposition=True)

def my_funky_invariant_check(simulation):
  from sts.invariant_checker import InvariantChecker
  result = InvariantChecker.check_loops(simulation)
  if result:
    return result
  return []

results_dir = "experiments/debug_branch_loop_mcs_blackbox/"

control_flow = EfficientMCSFinder(simulation_config, "experiments/debug_branch_loop/events.trace",
                                  invariant_check=my_funky_invariant_check,
                                  wait_on_deterministic_values=False)
