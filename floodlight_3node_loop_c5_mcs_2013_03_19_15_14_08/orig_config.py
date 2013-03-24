
from config.experiment_config_lib import ControllerConfig, find_ports
from sts.topology import *
from sts.control_flow import EfficientMCSFinder
from sts.invariant_checker import InvariantChecker
from sts.simulation_state import SimulationConfig

timestamp_results = True
additional_ports = find_ports(of=range(6633,6833), rest=range(8080, 8280), jython=range(7655, 7855))
simulation_config = SimulationConfig(controller_configs=[ControllerConfig(cmdline='java  -server -Xmx512m -Xms512m -Xmn128m -XX:+UseParallelGC -XX:+AggressiveOpts -XX:+UseFastAccessorMethods -XX:MaxInlineSize=8192 -XX:FreqInlineSize=8192 -XX:CompileThreshold=1500 -XX:PreBlockSpin=8 -Dpython.security.respectJavaAccessibility=false -Dlogback.configurationFile=logback.xml -jar target/floodlight.jar -cf __config__', address='127.0.0.1', cwd='floodlight', port=additional_ports['of'], additional_ports = additional_ports, config_template="experiments/config/floodlightconfig.properties.template" )],
                 topology_class=MeshTopology,
                 topology_params="num_switches=3",
                 patch_panel_class=BufferedPatchPanel,
                 dataplane_trace="experiments/floodlight_3node_loop_c5/dataplane.trace",
                 multiplex_sockets=False)

control_flow = EfficientMCSFinder(simulation_config, "experiments/floodlight_3node_loop_c5/events.trace",
                                  wait_on_deterministic_values=False,
				  epsilon_seconds=0.15,
				  no_violation_verification_runs=13,
                                  invariant_check_name='check_for_loops_or_connectivity')
