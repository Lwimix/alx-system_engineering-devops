# This script creates a file in /tmp specifying the owner and permissions
file { '/tmp/school':
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love puppet',
}
