import nginx


c = nginx.Conf()
u = nginx.Upstream('php',
    nginx.Key('server', 'unix:/tmp/php-fcgi.socket')
)
c.add(u)
s = nginx.Server()
s.add(
    nginx.Key('listen', '80'),
    nginx.Comment('Yes, python-nginx can read/write comments!'),
    nginx.Key('server_name', 'localhost 127.0.0.1'),
    nginx.Key('root', '/srv/http'),
    nginx.Key('index', 'index.php'),
    nginx.Location('= /robots.txt',
         nginx.Key('allow', 'all'),
         nginx.Key('log_not_found', 'off'),
         nginx.Key('access_log', 'off')
    ),
    nginx.Location('~ \.php$',
         nginx.Key('include', 'fastcgi.conf'),
         nginx.Key('fastcgi_intercept_errors', 'on'),
         nginx.Key('fastcgi_pass', 'php')
    )
)
c.add(s)
nginx.dumpf(c, '/etc/nginx/sites-available/mysite')
