
from config.experiment_config_lib import ControllerConfig
from sts.topology import *
from sts.control_flow import Replayer
from sts.simulation_state import SimulationConfig

simulation_config = SimulationConfig(controller_configs=[ControllerConfig(cmdline='java  -server -Xmx512m -Xms512m -Xmn128m -XX:+UseParallelGC -XX:+AggressiveOpts -XX:+UseFastAccessorMethods -XX:MaxInlineSize=8192 -XX:FreqInlineSize=8192 -XX:CompileThreshold=1500 -XX:PreBlockSpin=8 -Dpython.security.respectJavaAccessibility=false -Dlogback.configurationFile=logback.xml -jar target/floodlight.jar -cf __config__', address='127.0.0.1', port=6633, cwd='floodlight')],
                 topology_class=MeshTopology,
                 topology_params="num_switches=3",
                 patch_panel_class=BufferedPatchPanel,
                 dataplane_trace="exp/floodlight_3node_loop_c3/dataplane.trace",
                 multiplex_sockets=False)

control_flow = Replayer(simulation_config, "exp/floodlight_3node_loop_c3_mcs_2013_02_01_02_15_54/intermcs_9_il.0.l.1.il.2.il.3.il.4.il.5.r.6.l.7/events.trace",
                        wait_on_deterministic_values=False)
