# This script executes pkill on process killmenow
exec { 'pkill_killmenow':
command => 'pkill -9 killmenow'
}
