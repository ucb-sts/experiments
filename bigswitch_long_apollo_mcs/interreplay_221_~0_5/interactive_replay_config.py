
from config.experiment_config_lib import ControllerConfig
from sts.topology import *
from sts.control_flow import InteractiveReplayer
from sts.simulation_state import SimulationConfig
from sts.input_traces.input_logger import InputLogger

simulation_config = SimulationConfig(controller_configs=[ControllerConfig(start_cmd='sleep 1', label='c1', address='10.192.5.101', cwd='experiments/scripts/bsc', controller_type='bsc'), ControllerConfig(start_cmd='sleep 1', label='c2', address='10.192.5.102', cwd='experiments/scripts/bsc', controller_type='bsc')],
                 topology_class=MeshTopology,
                 topology_params="num_switches=3",
                 patch_panel_class=BufferedPatchPanel,
                 multiplex_sockets=False,
                 kill_controllers_on_exit=False)

control_flow = InteractiveReplayer(simulation_config, "experiments/bigswitch_long_apollo_mcs/interreplay_221_~0_5/events.trace")
# wait_on_deterministic_values=False
# delay_flow_mods=False
# Invariant check: 'None'
