# Puppet script will replace a line in a file on a server

$file_to_edit = '/etc/default/nginx'

# replace ULIMIT line with original default

exec { 'replace_line':
  command => "sed -i 's/^ULIMIT=.*/ULIMIT=\"-n 4096\"/g' ${file_to_edit}",
  path    => ['/bin','/usr/bin']
} ->

exec { 'restart_ngninx':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
