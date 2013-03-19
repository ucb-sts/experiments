from config.experiment_config_lib import ControllerConfig, find_ports

from config.experiment_config_lib import ControllerConfig
from sts.topology import *
from sts.control_flow import Replayer
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

additional_ports = find_ports(of=range(6633,6833), rest=range(8080, 8280), jython=range(7655, 7855))
controllers = [ ControllerConfig(command_line, cwd="floodlight", port=additional_ports['of'], additional_ports = additional_ports, uuid=("127.0.0.1", 6633), config_template="exp/config/floodlightconfig.properties.template") ]

simulation_config = SimulationConfig(controller_configs=controllers,
                 topology_class=MeshTopology,
                 topology_params="num_switches=3",
                 patch_panel_class=BufferedPatchPanel,
                 dataplane_trace="exp/floodlight_3node_loop/dataplane.trace",
                 multiplex_sockets=False)

control_flow = Replayer(simulation_config, "exp/floodlight_3node_loop/events.trace", epsilon_seconds=1.,
                        wait_on_deterministic_values=False)