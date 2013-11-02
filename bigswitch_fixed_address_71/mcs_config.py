
from config.experiment_config_lib import ControllerConfig
from sts.topology import *
from sts.control_flow import EfficientMCSFinder
from sts.invariant_checker import InvariantChecker
from sts.simulation_state import SimulationConfig

simulation_config = SimulationConfig(controller_configs=[ControllerConfig(start_cmd='sleep 1', label='c1', address='10.192.5.196', cwd='experiments/scripts/bsc', controller_type='bsc'), ControllerConfig(start_cmd='sleep 1', label='c2', address='10.192.5.197', cwd='experiments/scripts/bsc', controller_type='bsc')],
                 topology_class=MeshTopology,
                 topology_params="num_switches=3",
                 patch_panel_class=BufferedPatchPanel,
                 multiplex_sockets=False,
                 kill_controllers_on_exit=False)

control_flow = EfficientMCSFinder(simulation_config, "experiments/bigswitch_fixed_address_71/events.trace",
                                  wait_on_deterministic_values=False,
                                  delay_flow_mods=False,
                                  invariant_check_name='check_everything')
