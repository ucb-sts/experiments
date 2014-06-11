How to re-run this expirement on c70
=====================================

1. Vagrant and ONOS VMs are already installed on `/mnt/ahassany/vagrant_onosdev/`
2. Load the environment vars: `cd /mnt/ahassany/vagrant_onosdev/; source varsrc`
3. Make sure the VMs are running (only the first two matter): `vagrant status onosdev1 onosdev2` if they're not running use `vagrant up onosdev1 onosdev2`
4. (Optional) clean logs from previous runs: `cd /mnt/ahassany/vagrant_onosdev/; rm cust_log; touch cust_log; rm onos-logs/*`
   * `cust_log`: is the file the keeps track of who claim the link (it's just simpler than following the entire log for ONOS)
   * `cid_onosdev1`, `cid_onosdev2`: keeps track of the previous ONOS ID.
   *  `onosdev1_cids.txt`, `onosdev2_cids.txt`: are the sequence of IDs given to ONOS, once ONOS use one it will mark the link with `X `. The sts Replayer will always add new IDs to the top of the file to make sure the bug is triggered.
5. Run sts from `/mnt/ahassany/sts` then `./simulator.py -c experiments/onos_id_bug_fixed_ids_file/mcs_config.py -n YOUR_EXPERIMENT_NAME`
