# Ensure Python 3 and pip3 are installed 
package {['python3', 'python3-pip']:
 ensure => installed,
}

# Install Flask version 2.1.0 via pip3
exc {'install_flask':
  command => '/usr/bin/pip3 install flask==2.1.0',
  unless  => 'usr/bin/pip3 show flask | grep -q "version: 2.1.0"',
  require => Package['python3-pip'],
}

