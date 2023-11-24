# This script executes pkill on process killmenow
exec { 'killmenow':
  command  => '/usr/bin/pkill -9 killmenow',
  provider => 'shell',
  returns  => [0, 1],
}
