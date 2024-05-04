#Insall flask from pip3

exec { 'flask':
  command => 'usr/bin/pip3 install Flask==2.1.0',
  require => Package['flask-from-pip3']
}

package { 'flask-from-pip3':
  ensure => 'installed'
}
