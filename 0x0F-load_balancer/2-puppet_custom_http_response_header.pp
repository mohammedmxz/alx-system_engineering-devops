# Configures a brand new Ubuntu

$config = 'server {
	listen 80;
	listen [::]:80;
	server_name _ "";
	add_header X-Served-By "$hostname";
}'

exec { 'apt-get update':
  command => '/usr/bin/apt-get update',
}

exec { 'apt-get upgrade -y':
  command => '/usr/bin/apt-get upgrade -y',
}

package { 'nginx':
  ensure   => installed,
  name     => 'nginx',
  provider => apt,
}

file { '/etc/nginx/sites-available/default':
  ensure  => file,
  path    => '/etc/nginx/sites-available/default',
  content => $config,
}

exec { 'service nginx restart':
  command => '/usr/sbin/service nginx restart',
}
