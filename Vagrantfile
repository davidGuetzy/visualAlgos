Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/focal64"
 
  config.vm.provider "virtualbox" do |vb|
  #   # Display the VirtualBox GUI when booting the machine
  # vb.gui = true
  #
  #   # Customize the amount of memory on the VM:
  #  vb.memory = "1024"
  #
    # Disable audio within the VM:
  #  vb.customize ["modifyvm", :id, "--audio", "none"]
  end

  config.vm.provision "shell", inline: <<-SHELL
    apt-get update
    # add-apt-repository ppa:deadsnakes/ppa
    apt install -y software-properties-common
    #apt-get update

    apt-get install -y libcairo2-dev libpango1.0-dev ffmpeg
    apt-get install -y python3-pip
    # apt-get install -y python3.9 python3.9-distutils python3-pip
    apt-get install -y net-tools x11-apps
    apt install -y mplayer
    pip3 install pybind11 manim

    [ -d visualAlgos ] || cp -pr /vagrant/ ./visualAlgos
    [ -d .mplayer ] || mkdir -p .mplayer
    [ -f .mplayer/config ] || cp -p /vagrant/configs/mplayer.config .mplayer/config
    
  SHELL
end
