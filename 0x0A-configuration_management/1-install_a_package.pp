#Using Puppet, install flask from pip3 requirements are: Install flask, version m#ust be 2.1.0
package { 'Flask':
  ensure    => '2.1.0',
  provider  => 'pip3',
}

