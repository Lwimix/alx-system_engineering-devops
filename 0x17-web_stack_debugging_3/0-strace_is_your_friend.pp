# This code replaces the extension of the settings file from .phpp to .php
$setting = '/var/www/html/wp-settings.php'
exec { 'replace_extension':
command => "sed -i 's/class-wp-locale.phpp/class-wp-locale.php/g' ${setting}",
path    => ['/bin', '/usr/bin']
}
