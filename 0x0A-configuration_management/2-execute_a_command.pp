#Using Puppet, create a manifest that kills a process named killmenow using the exec and pkill.
exec { 'killmenow_process':
  path    => '/usr/bin/pkill',
  command => 'pkill killmenow',
}
