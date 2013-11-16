
from config.experiment_config_lib import ControllerConfig
from sts.topology import *
from sts.control_flow import MCSFinder
from sts.invariant_checker import InvariantChecker
from sts.simulation_state import SimulationConfig

simulation_config = SimulationConfig(controller_configs=[ControllerConfig(start_cmd='sleep 1', label='c1', address='10.192.5.101', cwd='experiments/scripts/bsc', controller_type='bsc'), ControllerConfig(start_cmd='sleep 1', label='c2', address='10.192.5.102', cwd='experiments/scripts/bsc', controller_type='bsc')],
                 topology_class=MeshTopology,
                 topology_params="num_switches=3",
                 patch_panel_class=BufferedPatchPanel,
                 multiplex_sockets=False,
                 kill_controllers_on_exit=False)

control_flow = MCSFinder(simulation_config, "experiments/bigswitch_long_apollo/events.trace",
                                  wait_on_deterministic_values=False,
                                  delay_flow_mods=False,
                                  invariant_check_name='check_everything',
                                  no_violation_verification_runs=5)
