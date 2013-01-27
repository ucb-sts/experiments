""" pox l2_multi loop. old mcs finder algo, powersets ignored, 4 verification runs """
from config.experiment_config_lib import ControllerConfig
from sts.topology import *
from sts.control_flow import MCSFinder
from sts.invariant_checker import InvariantChecker
from sts.simulation_state import SimulationConfig

from config.fuzz_pox_mesh import my_funky_invariant_check

simulation_config = SimulationConfig(controller_configs=[ControllerConfig(cmdline='./pox.py --verbose --random-seed=1 openflow.discovery forwarding.l2_multi openflow.of_01 --address=__address__ --port=__port__', address='127.0.0.1', port=6633, cwd='betta')]),
                 topology_class=MeshTopology,
                 topology_params="num_switches=2",
                 patch_panel_class=BufferedPatchPanel,
                 dataplane_trace="dataplane_traces/ping_pong_same_subnet.trace",
                 multiplex_sockets=False)

control_flow = MCSFinder(simulation_config, "input_traces/2013_01_21_17_41_55.trace",
                         invariant_check=my_funky_invariant_check,
                         wait_on_deterministic_values=False,
			 no_violation_verification_runs=4,
                         ignore_powersets=True)
