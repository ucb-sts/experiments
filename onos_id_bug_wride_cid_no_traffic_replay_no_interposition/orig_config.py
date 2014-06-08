
from config.experiment_config_lib import ControllerConfig
from sts.topology import *
from sts.control_flow.replayer import Replayer
from sts.simulation_state import SimulationConfig
from sts.input_traces.input_logger import InputLogger
from sts.entities.base import LocalEntity


vagrant_dir = "/Users/ahassany/vagrant_onosdev/"


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


setup()

simulation_config = SimulationConfig(controller_configs=[ControllerConfig(start_cmd='./start-onos.sh start', label='c1', address='192.168.56.11', cwd='/home/mininet/ONOS', controller_type='onos', kill_cmd='./start-onos.sh stop', restart_cmd='./start-onos.sh stop'), ControllerConfig(start_cmd='./start-onos.sh start', label='c2', address='192.168.56.12', cwd='/home/mininet/ONOS', controller_type='onos', kill_cmd='./start-onos.sh stop', restart_cmd='./start-onos.sh stop')],
                 topology_class=MeshTopology,
                 topology_params="num_switches=2",
                 patch_panel_class=BufferedPatchPanel,
                 multiplex_sockets=False,
                 ignore_interposition=True,
                 kill_controllers_on_exit=False)

control_flow = Replayer(simulation_config, "experiments/onos_id_bug_wride_cid_no_traffic/events.trace",
                        input_logger=InputLogger(),
                        wait_on_deterministic_values=False,
                        allow_unexpected_messages=False,
                        delay_flow_mods=False,
                        default_dp_permit=True,
                        pass_through_whitelisted_messages=True,
                        end_wait_seconds=3.0,
                        invariant_check_name='InvariantChecker.check_liveness',
                        bug_signature="c2")
