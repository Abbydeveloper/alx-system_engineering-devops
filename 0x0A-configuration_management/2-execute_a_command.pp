# kill process

exec { 'pkill' :
  command => 'pkill killmenow',
  provier => 'shell'
}
