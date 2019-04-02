Name:nginx		
Version:1.12.2	
Release:	101
Summary:nginx,a web server	
		
License:GPL
URL:www.baidu.com		
Source0:nginx-1.12.2.tar.gz	

#BuildRequires:	
#Requires:	

%description

%post
grep -q 'nginx' /etc/passwd||useradd nginx
echo -e "[Unit]\nDescription=nginx web server\nDocumentation=http://nginx.org/en/docs/\nAfter=network.target remote-fs.target nss-lookup.target\n\n[Service]\nType=forking\nExecStartPre=/usr/local/nginx/sbin/nginx -t -c /usr/local/nginx/conf/nginx.conf\nExecStart=/usr/local/nginx/sbin/nginx -c /usr/local/nginx/conf/nginx.conf\nExecStartPost=/bin/sleep 0.1\nPIDFile=/usr/local/nginx/logs/nginx.pid\nExecReload=/usr/local/nginx/sbin/nginx -s reload\nExecStop=/usr/local/nginx/sbin/nginx -s stop\nPrivateTmp=true\n\n[Install]\nWantedBy=multi-user.target " > /usr/lib/systemd/system/nginx.service
%prep
%setup -q


%build
./configure --with-http_ssl_module --with-http_stub_status_module --with-stream
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files
%doc
/usr/local/nginx/*


%changelog

