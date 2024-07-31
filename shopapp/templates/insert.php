<?php
$sql = "SELECT * FROM `shopapp_registration`;";
$username = $_POST['username'];
$password = $_POST['password'];
$email = $_POST['email'];
$phone = $_POST['phone'];

if(!empty($username) || !empty($password ) || !empty($email) || !empty($phone)){
    $host="localhost";
    $dbUsername="root";
    $dbPassword="";
    $dbname="testdb";

    $conn = new mysqli($host, $dbUsername, $dbPassword, $dbname);

    if(mysqli_connect_error()){
        die('onnect Error('. mysqli_connect_errno().')' . mysqli_connect_error());
    }
}
else{
    $SELECT = "SELECT email From register Where email = ? Limit 1";
    $INSERT = "INSERT Into register (username, password, email, phone) values(?, ?, ?, ?, ?)";

    $stmt = $conn-prepare($SELECT);
    $stmt=bind_param("s",$email);
    $stmt=execute();
    $stmt=bind_result($email);
    $stmt=store_result();
    $rnum = $stmt-num_rows;

    if($rnum==0){
        $stmt=close();
        $stmt = $conn-prepare($INSERT);
        $stmt=bind_param("ssssii", $username, $password, $email, $phone);
        $stmt=execute();
        echo "New record inserted successfully";
    }
    else{
        echo "Someone already registered using this email";
    }
    $stmt=close();
    $conn=close();
}
    
else{
    echo "All fields are required";
    die();
}