<html>
<body>
<?php 
echo 'connected';
$item='example';
$tmp = exec("python rcv.py .$item");
echo $tmp;
?>
</body>
</html>