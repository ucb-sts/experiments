
from config.experiment_config_lib import ControllerConfig
from sts.topology import *
from sts.control_flow import EfficientMCSFinder
from sts.invariant_checker import InvariantChecker
from sts.simulation_state import SimulationConfig

simulation_config = SimulationConfig(controller_configs=[ControllerConfig(start_cmd=' onos stop; zk stop ; cassandra stop; echo "sleeping for 5sec"; sleep 5; /mnt/ahassany/vagrant_onosdev/scripts/conf_setup.sh 2 ; zk start ; cassandra start; echo "sleeping for 10sec"; sleep 10 ; onos start ; echo "sleeping for 40 secs"; sleep 40 ; onos stop; sleep 10; cassandra cleandb; onos start; sleep 40', label='c1', address='192.168.56.11', cwd='/mnt/ahassany/vagrant_onosdev', controller_type='onos', kill_cmd=' ssh onosdev1 "cd ONOS; ./start-onos.sh stop"; echo "killed"; sleep 5', restart_cmd='ssh onosdev1 "cd ONOS; ./start-onos.sh start"; echo "restarted"; sleep 20'), ControllerConfig(start_cmd='echo "DUMMY COMMAND"; sleep 1', label='c2', address='192.168.56.12', cwd='/mnt/ahassany/vagrant_onosdev', controller_type='onos', kill_cmd=' ssh onosdev2 "cd ONOS; ./start-onos.sh stop"; echo "killed"; sleep 5', restart_cmd='ssh onosdev2 "cd ONOS; ./start-onos.sh start"; echo "restarted"; sleep 20')],
                 topology_class=MeshTopology,
                 topology_params="num_switches=2",
                 patch_panel_class=BufferedPatchPanel,
                 multiplex_sockets=False,
                 kill_controllers_on_exit=False)

control_flow = EfficientMCSFinder(simulation_config, "experiments/db_lock_2014_01_31_10_46_33/events.trace",
                                  wait_on_deterministic_values=False,
                                  default_dp_permit=False,
                                  pass_through_whitelisted_messages=False,
                                  delay_flow_mods=False,
                                  invariant_check_name='InvariantChecker.check_liveness',
                                  bug_signature="")
