#Create a file with puppet

fille { "/tmp/school":
	ensure => "directory",
	owner => "www-data",
	group => "www-data",
	mode => 0744,
	content => "I love Puppet",
}
