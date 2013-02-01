
from config.experiment_config_lib import ControllerConfig
from sts.topology import *
from sts.control_flow import EfficientMCSFinder
from sts.invariant_checker import InvariantChecker
from sts.simulation_state import SimulationConfig

simulation_config = SimulationConfig(controller_configs=[ControllerConfig(cmdline='java  -server -Xmx512m -Xms512m -Xmn128m -XX:+UseParallelGC -XX:+AggressiveOpts -XX:+UseFastAccessorMethods -XX:MaxInlineSize=8192 -XX:FreqInlineSize=8192 -XX:CompileThreshold=1500 -XX:PreBlockSpin=8 -Dpython.security.respectJavaAccessibility=false -Dlogback.configurationFile=logback.xml -jar target/floodlight.jar -cf __config__', address='127.0.0.1', port=6798, cwd='floodlight')],
                 topology_class=MeshTopology,
                 topology_params="num_switches=3",
                 patch_panel_class=BufferedPatchPanel,
                 dataplane_trace="exp/fuzz_floodlight_mesh_3node_2013_01_31_23_33_35/dataplane.trace",
                 multiplex_sockets=False)

control_flow = EfficientMCSFinder(simulation_config, "exp/fuzz_floodlight_mesh_3node_2013_01_31_23_33_35/events.trace",
                                  wait_on_deterministic_values=False)
