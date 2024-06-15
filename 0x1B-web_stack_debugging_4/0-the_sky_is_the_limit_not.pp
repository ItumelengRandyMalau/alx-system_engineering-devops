# fix nginx to accept and serve more requests by increasing ULIMIT

exec {'modify maximum open files limit setting for nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx && sudo service nginx restart',
  path    => '/usr/local/bin:/bin',
}
