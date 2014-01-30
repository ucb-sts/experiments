
from config.experiment_config_lib import ControllerConfig
from sts.topology import *
from sts.control_flow import InteractiveReplayer
from sts.simulation_state import SimulationConfig
from sts.input_traces.input_logger import InputLogger

simulation_config = SimulationConfig(controller_configs=[ControllerConfig(start_cmd='  dsh -g onosdev "cd ~/ONOS; sudo ./reset_iptables.sh";   onos stop; zk stop ; cassandra stop; echo "sleeping for 5sec"; sleep 5; /mnt/ahassany/vagrant_onosdev/scripts/conf_setup.sh 4 ; zk start ; cassandra start; echo "sleeping for 10sec"; sleep 10 ; onos start ; echo "sleeping for 40 secs"; sleep 40 ; onos stop; sleep 10; cassandra cleandb; onos start; sleep 40', label='c1', address='192.168.56.11', cwd='/mnt/ahassany/vagrant_onosdev', controller_type='onos', kill_cmd=' ssh onosdev1 "cd ONOS; ./start-onos.sh stop"; echo "killed"; sleep 10', restart_cmd='ssh onosdev1 "cd ONOS; ./start-onos.sh start"; echo "restarted"; sleep 40'), ControllerConfig(start_cmd='echo "DUMMY COMMAND"; sleep 1', label='c2', address='192.168.56.12', cwd='/mnt/ahassany/vagrant_onosdev', controller_type='onos', kill_cmd=' ssh onosdev2 "cd ONOS; ./start-onos.sh stop"; echo "killed"; sleep 10', restart_cmd='ssh onosdev2 "cd ONOS; ./start-onos.sh start"; echo "restarted"; sleep 40'), ControllerConfig(start_cmd='echo "DUMMY COMMAND"; sleep 1', label='c3', address='192.168.56.13', cwd='/mnt/ahassany/vagrant_onosdev', controller_type='onos', kill_cmd=' ssh onosdev3 "cd ONOS; ./start-onos.sh stop"; echo "killed"; sleep 10', restart_cmd='ssh onosdev3 "cd ONOS; ./start-onos.sh start"; echo "restarted"; sleep 40'), ControllerConfig(start_cmd='echo "DUMMY COMMAND"; sleep 1', label='c4', address='192.168.56.14', cwd='/mnt/ahassany/vagrant_onosdev', controller_type='onos', kill_cmd=' ssh onosdev4 "cd ONOS; ./start-onos.sh stop"; echo "killed"; sleep 10', restart_cmd='ssh onosdev4 "cd ONOS; ./start-onos.sh start"; echo "restarted"; sleep 40')],
                 topology_class=MeshTopology,
                 topology_params="num_switches=2",
                 patch_panel_class=BufferedPatchPanel,
                 multiplex_sockets=False,
                 kill_controllers_on_exit=False)

control_flow = InteractiveReplayer(simulation_config, "experiments/distributed_onos/events.trace")
# wait_on_deterministic_values=False
# delay_flow_mods=False
# Invariant check: 'InvariantChecker.check_connectivity'
# Bug signature: ""
