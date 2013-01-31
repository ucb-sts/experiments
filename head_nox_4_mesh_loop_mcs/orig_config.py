
from config.experiment_config_lib import ControllerConfig
from sts.topology import *
from sts.control_flow import EfficientMCSFinder
from sts.invariant_checker import InvariantChecker
from sts.simulation_state import SimulationConfig

simulation_config = SimulationConfig(controller_configs=[ControllerConfig(cmdline='./nox_core -v -i ptcp:6635 routing', address='127.0.0.1', port=6635, cwd='nox_classic/build/src')],
                 topology_class=MeshTopology,
                 topology_params="num_switches=4",
                 patch_panel_class=BufferedPatchPanel,
                 dataplane_trace="exp/head_nox_4_mesh_loop/dataplane.trace",
                 multiplex_sockets=False)

def fast_die_invariant_check(simulation):
  from sts.invariant_checker import InvariantChecker
  result = InvariantChecker.check_loops(simulation)
  if result:
    return result
  result = InvariantChecker.python_check_connectivity(simulation)
  if not result:
    print "Connectivity established - bailing out"
    import sys
    sys.exit(0)
  return []

control_flow = EfficientMCSFinder(simulation_config, "exp/head_nox_4_mesh_loop/events.trace",
                                  wait_on_deterministic_values=False,
                                  invariant_check=fast_die_invariant_check
                                  )
