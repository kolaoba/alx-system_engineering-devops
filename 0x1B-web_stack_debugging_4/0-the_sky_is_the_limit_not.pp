# Puppet script will replace a line in a file on a server

$file_to_edit = '/etc/default/nginx'

#replace line containing "phpp" with "php"

exec { 'replace_line':
  command => "sed -i 's/^ULIMIT=.*/ULIMIT=\"-n 15000\"/g' ${file_to_edit}",
  path    => ['/bin','/usr/bin']
}
