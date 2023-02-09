# Enable the user holberton to login and open files without error.

$file_to_edit = '/etc/security/limits.conf'

# Increase hard file limit for Holberton user.
exec { 'increase-hard-file-limit':
  command => "sed -i '/holberton hard/s/5/60000/' ${file_to_edit}",
  path    => '/usr/local/bin/:/bin/'
}

# Increase soft file limit for Holberton user.
exec { 'increase-soft-file-limit':
  command => "sed -i '/holberton soft/s/4/60000/' ${file_to_edit}",
  path    => '/usr/local/bin/:/bin/'
}
