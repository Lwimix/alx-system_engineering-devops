# This script creates a file in /tmp
$file_mode = '0744'
$file_owner = 'www-data'
$file_group = 'www-data'
$file_content = 'I love puppet'
file { '/tmp/school':
  ensure => present,
  mode   => $file_mode,
  owner  => $file_owner,
  group  => $file_group,
content  => $file_content
}
