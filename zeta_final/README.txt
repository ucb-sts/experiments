Here are the (fairly straightforward) steps to re-run zeta_final:

1. Prepare STS and dependent repositories with the given git hashes

  git clone git@github.com:ucb-sts/sts
  cd sts
  git clone -b debugger git@github.com:ucb-sts/pox
  git clone -b floodlight git@github.com:ucb-sts/experiments
  
  # Checkout the specific versions of sts and pox
  git checkout 3919638f2d084c55f7b0b457bb64bf176f023ab4
  cd pox
  git checkout cced89df35a07205792deaafc6b0361e5baf7cf7
  cd ..
  
  # Prepare submodules
  git submodule init
  git submodule update

2. Prepare floodlight

  cd ..
  git clone git@github.com:floodlight/floodlight
  cd floodlight
  git checkout ea0c101ba58488db6248e6c0e3f855cfd6368f30
  make all

  # At this point, your directory structure should look like this:
  # 
  # floodlight/
  # sts/
  #   pox/
  #   experiments/

3. Run sts

  ./simulator.py -c experiments/zeta_final/orig_config.py
  ./simulator.py -c experiments/zeta_final/replay_config.py

  # You can expect to run into "org.sdnplatform.sync.error.PersistException: Could not initialize persistent storage"
  # The version of floodlight you checked out does not support persistent storage by default. It is not a fatal error,
  # however, so you can safely continue.

---

Debugging tips:
- If you get a "Connection refused" exception, chances are you are not connecting to floodlight through the default 6633 port.
  Make sure your SimulationConfig is specifying the correct port.
- If you get a "No such file or directory" error while launching floodlight, chances are the working directory is not correct.
  Make sure your SimulationConfig specifies a path that points to an existing floodlight installation.

