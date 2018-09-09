<?php
  exec("python3 /home/pi/GPIO/irswitch.py");
  $state = exec("gpio -g read 17");
    if ($state == 1){
	echo "关闭夜视";
    } else {
       echo "开启夜视";
    }
?>
