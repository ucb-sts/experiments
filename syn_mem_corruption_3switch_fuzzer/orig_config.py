from config.experiment_config_lib import ControllerConfig
from sts.topology import MeshTopology, BufferedPatchPanel
from sts.control_flow import Interactive, Fuzzer
from sts.input_traces.input_logger import InputLogger
from sts.simulation_state import SimulationConfig

# Use POX as our controller
start_cmd = "./pox.py --verbose openflow.of_01 --address=__address__ --port=__port__ openflow.discovery forwarding.l2_multi_syn_mem_corruption"
controllers = [ControllerConfig(start_cmd, cwd="pox", address="127.0.0.1", port=8888)]
topology_class = MeshTopology
topology_params = "num_switches=4"

simulation_config = SimulationConfig(controller_configs=controllers,
                                     topology_class=topology_class,
                                     topology_params=topology_params)

control_flow = Fuzzer(simulation_config, check_interval=1,
                      #mock_link_discovery=True,
                      fuzzer_params="experiments/syn_mem_corruption_3switch/fuzzer_params.py",
                      halt_on_violation=True,
                      input_logger=InputLogger(),
                      invariant_check_name="InvariantChecker.check_liveness",
                      steps=5000,
                      #random_seed=466448715
                      )

raise RuntimeError("Please add this parameter to Fuzzer: fuzzer_params='experiments/syn_mem_corruption_3switch_fuzzer/fuzzer_params.py'")