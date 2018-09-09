<?php
  define('BASE_DIR', dirname(__FILE__));
  $command = 'python3 '.BASE_DIR .'/GPIO/temperature.py';
  exec($command);
  sleep(10);
  $contents = file_get_contents("/dev/shm/mjpeg/user_annotate.txt", true);
  echo $contents;
?>
