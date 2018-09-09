<?php
  define('BASE_DIR', dirname(__FILE__));
  $command = 'python3 '.BASE_DIR .'/GPIO/irswitch.py';
  exec($command);
  $state = exec("gpio -g read 17");
    if ($state == 1){
	echo "关闭夜视";
    } else {
       echo "开启夜视";
    }
?>
