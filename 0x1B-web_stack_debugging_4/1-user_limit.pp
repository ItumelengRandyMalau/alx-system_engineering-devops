# Changes the OS configurations so that it enables holberton user to login and
# open a file without any errors

exec {'OS security configurations':
  command => 'sed -i "s/holberton/foo/" /etc/security/limits.conf',
  path    => '/usr/local/bin:/bin/'
}
