from sts.util.convenience import find_ports
from config.experiment_config_lib import ControllerConfig
from sts.topology import *
from sts.control_flow import EfficientMCSFinder
from sts.invariant_checker import InvariantChecker
from sts.simulation_state import SimulationConfig

jvm_opts = ""
jvm_opts += " -server"
#jvm_opts += " -Xmx2g -Xms2g -Xmn800m"
jvm_opts += " -Xmx512m -Xms512m -Xmn128m"
jvm_opts += " -XX:+UseParallelGC -XX:+AggressiveOpts -XX:+UseFastAccessorMethods"
jvm_opts += " -XX:MaxInlineSize=8192 -XX:FreqInlineSize=8192"
jvm_opts += " -XX:CompileThreshold=1500 -XX:PreBlockSpin=8"
jvm_opts += " -Dpython.security.respectJavaAccessibility=false"
log_config = "-Dlogback.configurationFile=logback.xml"
command_line = ("java %s %s -jar target/floodlight.jar -cf __config__" % (jvm_opts, log_config))

timestamp_results = True

# Use Floodlight as our controller
additional_ports = find_ports(of=range(6633,6634), rest=range(8080, 8280), jython=range(7655, 7855))
controllers = [ ControllerConfig(command_line, cwd="../floodlight", port=additional_ports['of'], additional_ports=additional_ports, label="c1", config_template="experiments/config/floodlightconfig.properties.template") ]
topology_class = MeshTopology
topology_params = "num_switches=3"

simulation_config = SimulationConfig(controller_configs=controllers,
                                     topology_class=topology_class,
                                     topology_params=topology_params,
                                     #ignore_interposition=True,
                                     )

control_flow = EfficientMCSFinder(simulation_config, "experiments/zeta/events.trace",
                                  wait_on_deterministic_values=False,
                                  no_violation_verification_runs=10,
                                  invariant_check_name='check_for_loops_or_connectivity')
