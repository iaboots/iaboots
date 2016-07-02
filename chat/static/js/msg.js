
msg_bot1 = "<li class='left clearfix'><span class='chat-img pull-left'><img src='static/img/user/iabots.jpg' alt='User Avatar' class='img-circle' /></span><div class='chat-body clearfix'><div class='header'><strong class='primary-font'>";
msg_bot2 = "</strong><small class='pull-right text-muted'>";
// date  + relleno + message
msg_bot4 = "</p></div></div></li>";

user1 = '<li class="right clearfix"><span class="chat-img pull-right"><img src="static/img/user/avatar';
// image
user2 = '.png" alt="User Avatar" class="img-circle" height=55 width=55 /></span><div class="chat-body clearfix"><div class="header"><small class=" text-muted">';
// time
user3 = '</small><strong class="pull-right primary-font">';
//name
user4='</strong></div><p>';
//message
user5='</p></div></li>';



function ask(inputid, outputid, name_user, user_avatar, nomb_bot, num_bot)
{
	
	var current_time = new Date();
	var month 	= current_time.getMonth() + 1 ;
	var day 	= current_time.getDate();
	var hours 	= current_time.getHours();
	var year	= current_time.getFullYear();
	var min		= current_time.getMinutes();
	var pp		= "AM"
	if (hours > 12){
		hours -= 12; pp = "PM";
	}
	if (hours < 10) hours = "0" + hours;
	if (min < 10) 	min = "0" + min; // put 0 before minutes
	
	var mes_temp = "";
	switch (month){
		case 1: mes_temp = "Enero"; break;
		case 2: mes_temp = "Febrero"; break;
		case 3: mes_temp = "Marzo"; break;
		case 4: mes_temp = "Abril"; break;
		case 5: mes_temp = "Mayo"; break;
		case 6: mes_temp = "Junio"; break;
		case 7: mes_temp = "Julio"; break;
		case 8: mes_temp = "Agosto"; break;
		case 9: mes_temp = "Septiembre"; break;
		case 10: mes_temp = "Octubre"; break;
		case 11: mes_temp = "Noviembre"; break;
		case 12: mes_temp = "Diciembre"; break;
	};
	month = mes_temp;
	var now = month + " " + day + ", " + year + ", " + hours + ":" + min + " " + pp;
	
	var textin = document.getElementById(inputid);
	var query = textin.value;
	if (query == "") return false // chek the query value no None 
  	var url = "/ask?q=" + query + "&n=" + num_bot;
  	var media_list = document.getElementById(outputid);
	// var n_u = name_user.value;

  	media_list.innerHTML += user1 + user_avatar + user2 + now + user3 + name_user + user4 + query + user5;
	textin.value = "Cargando...";
	textin.disabled = true;

	var xmlhttp;
	if (window.XMLHttpRequest){ // code for IE7+, Firefox, Chrome, Opera, Safari
  		xmlhttp=new XMLHttpRequest();
  	}
	else{ // code for IE6, IE5
  		xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
  	}
	xmlhttp.onreadystatechange=function(){
 	 	if (xmlhttp.readyState==4 && xmlhttp.status==200){
		    media_list.innerHTML += msg_bot1 + nomb_bot + msg_bot2 + xmlhttp.responseText + msg_bot4;
			textin.value = "";
			textin.disabled = false;
			panel_body.scrollTop = panel_body.scrollHeight;
		
    	}
  	}
	xmlhttp.open("GET",url,true);
	xmlhttp.send();
	return false;
}