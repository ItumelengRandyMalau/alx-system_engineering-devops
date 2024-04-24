#Using Puppet, create a manifest that kills a process named killmenow using the exec and pkill.
exec { 'killmenow_process':
  command => 'pkill killmenow',
  onlyif  => 'pgrep killmenow',
}
