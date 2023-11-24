# This script installs flask from pip3
class { 'python':
  pip3 => true,
}

python::pip { 'flask':
  ensure   => '2.1.0',
  provider => '/usr/bin/pip3',
}
