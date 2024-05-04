#Create a file with puppet

$doc_root = "/tmp"

file { $doc_root:
	ensure => "directory",
	owner => "www-data",
	group => "www-data",
	mode => 0744
}

file { "$doc_root/school":
	ensure => "present",
	content => "I love Puppet",
	require => File[$doc_root]
}
