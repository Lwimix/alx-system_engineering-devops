# This code restarts nginx
service { 'nginx':
  ensure    => stopped,
}

exec { 'restart_nginx':
  command  => '/usr/sbin/nginx',
  provider => 'shell',
  require  => Service['nginx'],
}
