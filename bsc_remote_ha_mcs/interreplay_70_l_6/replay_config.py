
from config.experiment_config_lib import ControllerConfig
from sts.topology import *
from sts.control_flow import Replayer
from sts.simulation_state import SimulationConfig
from sts.input_traces.input_logger import InputLogger

simulation_config = SimulationConfig(controller_configs=[ControllerConfig(start_cmd='./start_vms -d /home-local/andrewor/work -h -r', label='c1', address='10.192.5.131', port=6633, cwd='experiments/scripts/bsc', controller_type='bsc', kill_cmd='./stop_process -d /home-local/andrewor/work -i 1 -r', restart_cmd='./start_process -d /home-local/andrewor/work -i 1 -r', check_status_cmd='./check_process -d /home-local/andrewor/work -i 1 -r'), ControllerConfig(start_cmd='sleep 1', label='c2', address='10.192.5.132', port=6633, cwd='experiments/scripts/bsc', controller_type='bsc', kill_cmd='./stop_process -d /home-local/andrewor/work -i 2 -r', restart_cmd='./start_process -d /home-local/andrewor/work -i 2 -r', check_status_cmd='./check_process -d /home-local/andrewor/work -i 2 -r')],
                 topology_class=MeshTopology,
                 topology_params="num_switches=3",
                 patch_panel_class=BufferedPatchPanel,
                 multiplex_sockets=False,
                 kill_controllers_on_exit=False)

control_flow = Replayer(simulation_config, "experiments/bsc_remote_ha_mcs/interreplay_70_l_6/events.trace",
                        input_logger=InputLogger(),
                        wait_on_deterministic_values=False)
# Invariant check: 'None'
