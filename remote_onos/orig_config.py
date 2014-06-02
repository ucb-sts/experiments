import os
from config.experiment_config_lib import ControllerConfig
from sts.topology import MeshTopology
from sts.control_flow.fuzzer import Fuzzer
from sts.input_traces.input_logger import InputLogger
from sts.simulation_state import SimulationConfig
from sts.entities.base import LocalEntity
from sts.entities.base import SSHEntity
from sts.util.convenience import backtick

vagrant_dir = "/mnt/ahassany/vagrant_onosdev/"

if 'CLUSTER' not in os.environ:
  raise RuntimeError('''Need to set $CLUSTER. See '''
                     '''https://wiki.onlab.us:8443/display/Eng/ONOS+Development+VM.\n'''
                     '''On c5:\n'''
                     '''export CLUSTER=${HOME}/.cluster.hosts\n'''
                     '''export ONOS_CLUSTER_BASENAME="onosdev"\n'''
                     '''export ONOS_CLUSTER_NR_NODES=2\n'''
                     '''export PATH=${HOME}/vagrant_onosdev/ONOS/cluster-mgmt/bin:$PATH''')


def get_additional_metadata():
  path = vagrant_dir + "/ONOS"
  return {
    'commit' : backtick("git rev-parse HEAD", cwd=path),
    'branch' : backtick("git rev-parse --abbrev-ref HEAD", cwd=path)
  }


def get_config(address):
  start_cmd = "./start-onos.sh start"
  kill_cmd = "./start-onos.sh stop"
  restart_cmd = "./start-onos.sh stop"
  check = "./start-onos.sh status"
  address = address
  cwd = "/home/mininet/ONOS"
  config = ControllerConfig(start_cmd, address=address, port=6633,
                            kill_cmd=kill_cmd, restart_cmd=restart_cmd,
                            controller_type="onos", cwd=cwd)
  return config

def get_executor(address, username='mininet', password='mininet', cwd='ONOS'):
  ssh = SSHEntity(address, username=username, password=password, cwd=cwd,
                  label=address, redirect_output=True)
  return ssh


def setup():
  cmd_exec = LocalEntity(redirect_output=True, cwd=vagrant_dir)
  cmd_exec.execute_command("onos stop")
  cmd_exec.execute_command("zk stop")
  cmd_exec.execute_command("cassandra  stop")
  #cmd_exec.execute_command("echo 'sleeping for 10sec'; sleep 10")
  cmd_exec.execute_command("./scripts/conf_setup.sh 2;")
  cmd_exec.execute_command("zk start")
  cmd_exec.execute_command("cassandra  start")
  cmd_exec.execute_command("echo 'sleeping for 10sec'; sleep 10")
  cmd_exec.execute_command("cassandra cleandb;")
  cmd_exec.execute_command("echo 'sleeping for 10sec'; sleep 10")
  #cmd_exec.execute_command("onos start")
  #cmd_exec.execute_command("echo 'sleeping for 40sec'; sleep 40")


controllers = [get_config("192.168.56.11"), get_config("192.168.56.12")]
topology_class = MeshTopology
topology_params = "num_switches=2"


setup()

simulation_config = SimulationConfig(controller_configs=controllers,
                                     topology_class=topology_class,
                                     topology_params=topology_params,
                                     #violation_persistence_threshold=1,
                                     kill_controllers_on_exit=False)

control_flow = Fuzzer(simulation_config, check_interval=50,
                      halt_on_violation=True,
                      input_logger=InputLogger(),
                      #steps=100,
                      delay=3.0,
                      invariant_check_name="InvariantChecker.check_liveness")
                      #invariant_check_name="check_for_flow_entry")
                      #invariant_check_name="InvariantChecker.check_connectivity")
                      #invariant_check_name="check_everything")

raise RuntimeError("Please add this parameter to Fuzzer: fuzzer_params='experiments/remote_onos/fuzzer_params.py'")
