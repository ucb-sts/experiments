
from config.experiment_config_lib import ControllerConfig
from sts.topology import *
from sts.control_flow import EfficientMCSFinder
from sts.invariant_checker import InvariantChecker
from sts.simulation_state import SimulationConfig

simulation_config = SimulationConfig(controller_configs=[ControllerConfig(start_cmd='java  -server -Xmx512m -Xms512m -Xmn128m -XX:+UseParallelGC -XX:+AggressiveOpts -XX:+UseFastAccessorMethods -XX:MaxInlineSize=8192 -XX:FreqInlineSize=8192 -XX:CompileThreshold=1500 -XX:PreBlockSpin=8 -Dpython.security.respectJavaAccessibility=false -Dlogback.configurationFile=logback.xml -jar target/floodlight.jar -cf __config__', address='127.0.0.1', port=6633, cwd='../floodlight')],
                 topology_class=MeshTopology,
                 topology_params="num_switches=3",
                 patch_panel_class=BufferedPatchPanel,
                 multiplex_sockets=False)

control_flow = EfficientMCSFinder(simulation_config, "experiments/floodlight_test_2014_01_13_19_55_05/events.trace",
                                  wait_on_deterministic_values=False,
                                  invariant_check_name='check_for_loops_blackholes')
