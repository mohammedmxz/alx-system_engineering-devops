# configuring a server

$content = ' server {
	listen 80 default_server;
	listen [::]:80 default_server;

	server_name "";
	root /var/www/html;

	location /redirect_me {
		return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
	}
}
'

package { 'nginx':
  name => 'nginx',
  ensure => installed,
  provider => apt,
}

file { '/var/www/html/index.html':
  path => '/var/www/html/index.html',
  ensure => file,
  content => 'Hello World!',
}

file { '/etc/nginx/sites-available/default':
  path => '/etc/nginx/sites-available/default',
  ensure => file,
  content => $content,
}

service { 'nginx':
  name => 'nginx',
  ensure => running,
}
