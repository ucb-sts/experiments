
from config.experiment_config_lib import ControllerConfig
from sts.topology import *
from sts.control_flow import EfficientMCSFinder
from sts.invariant_checker import InvariantChecker
from sts.simulation_state import SimulationConfig

simulation_config = SimulationConfig(controller_configs=[ControllerConfig(start_cmd='./pyretic.py -m p0 -v high pyretic.modules.hub', label='c1', address='127.0.0.1', cwd='../pyretic', kill_cmd='ps aux | grep -e pox -e pyretic | grep -v simulator | cut -c 9-15 | xargs kill -9')],
                 topology_class=MeshTopology,
                 topology_params="num_switches=3",
                 patch_panel_class=BufferedPatchPanel,
                 multiplex_sockets=False,
                 kill_controllers_on_exit=True)

control_flow = EfficientMCSFinder(simulation_config, "experiments/fuzz_pyretic_mesh_flood_check_loop_with_linkfailure/events.trace",
                                  wait_on_deterministic_values=False,
                                  delay_flow_mods=True,
                                  invariant_check_name='InvariantChecker.python_check_loops',
                                  bug_signature="")
