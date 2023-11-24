# This script creates a file in /tmp specifying the owner and permissions
$verbose = nil
file { '/tmp/school':
  ensure  => present,
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love puppet',
}
