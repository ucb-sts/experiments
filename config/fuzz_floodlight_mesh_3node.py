from config.experiment_config_lib import ControllerConfig, find_ports
from sts.topology import MeshTopology
from sts.control_flow import Fuzzer, Interactive
from sts.input_traces.input_logger import InputLogger
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

# Use POX as our controller
additional_ports = find_ports(of=range(6633,6833), rest=range(8080, 8280), jython=range(7655, 7855))
controllers = [ ControllerConfig(command_line, cwd="floodlight", port=additional_ports['of'], additional_ports = additional_ports, uuid=("127.0.0.1", 6633), config_template="exp/config/floodlightconfig.properties.template") ]
topology_class = MeshTopology
topology_params = "num_switches=3"
#dataplane_trace = "dataplane_traces/ping_pong_same_subnet.trace"

simulation_config = SimulationConfig(controller_configs=controllers,
                                     topology_class=topology_class,
                                     topology_params=topology_params,
#                                     dataplane_trace=dataplane_trace,
                                     #multiplex_sockets=True
                                     )

def my_funky_invariant_check(simulation):
  from sts.invariant_checker import InvariantChecker
  result = InvariantChecker.check_loops(simulation)
  if result:
    return result
  result = InvariantChecker.check_connectivity(simulation)
  if not result:
    print "Connectivity established - bailing out"
    import sys
    sys.exit(0)
  return []



control_flow = Fuzzer(simulation_config, check_interval=20,
                      #mock_link_discovery=True,
                      halt_on_violation=True,
                      input_logger=InputLogger(),
                      invariant_check=my_funky_invariant_check,
                      steps=999,
                      fuzzer_params="exp/config/fuzzer_params_no_failure.py"
                      #random_seed=466448715
                      )
#control_flow = Interactive(simulation_config, input_logger=InputLogger())
