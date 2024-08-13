# Ensure Apache configuration file is correct

file { '/etc/apache2/sites-available/000-default.conf':
  ensure  => file,
  content => template('0x17-web_stack_debugging_3/templates/000-default.conf.erb'),
  notify  => Service['apache2'],
}

file { '/var/www/html/wp-config.php':
  ensure  => file,
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0644',
  notify  => Service['apache2'],
}

service { 'apache2':
  ensure => running,
  enable => true,
}

