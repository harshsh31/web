<?php
	if(isset($_POST['verify'])){
		$phone=$_SESSION['phone'];
		$_SESSION['phone']=$phone;
		$query="Select otp from verify where phone='$phone'";
		$res=mysql_query($query);
		if($res==$_POST['otp']){
			echo "You are successfully verified!";
		}
		else
		{
			echo "You are not verified!";
		}
	}
?>
<!DOCTYPE html>
<html>
<head>
	<script
  src="http://code.jquery.com/jquery-3.2.1.min.js"
  integrity="sha256-hwg4gsxgFZhOsEEamdOYGBf13FyQuiTwlAQgxVSNgt4="
  crossorigin="anonymous"></script> 
  <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">

  <!-- Compiled and minified CSS -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/css/materialize.min.css">

  <!-- Compiled and minified JavaScript -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/js/materialize.min.js"></script>
	<title>
		VERIFY YOUR OTP!
	</title>
	<style type="text/css">
		body{
			background-image: url("background.jpg");
			width: 100%;
			height: 80%;
		}
		.page-footer{
			background-color:black;
		}
		h3{
			color: black;
			z-index: 10;
			padding: 15px;
		}
		#align{
			float: right;
			padding-right: 15%;
		}
	</style>
</head>
<body>
	<center><h1>Company's Name</h1></center>
	<div class="col s12 m7" style="margin: 80px;">
    <div class="card horizontal">
      <div class="card-image" style="height: 100%;">
        <img src="img1.jpg">
      </div>
      <div class="card-stacked">
        <div class="card-content">
          <center><h3>Enter your Otp here:</h3></center>
          <form class="col s12" action="">
          	<div class="row">
		        <div class="input-field col s12" style="margin-top: 10%;">
		          <input type="number" id="otp" class="validate" required maxlength="6">
		          <label for="otp">OTP</label>
		        </div>
		    </div>
		  	<div class="row" style="padding-top: 5%;">
		  	  <center><button class="btn waves-effect waves-light" type="submit" name="verify">Verify OTP</button></center>
			</div>
          </form>
        </div>
	    <div class="card-action">
	        <center><button class="btn waves-effect waves-light" id="submit" type="submit">Resend OTP!</button></center>
	    </div>
	    <span id="check" style="color: red; padding: 5%;"></span>
      </div>
    </div>
  </div>
   <footer class="page-footer">
        <div class="container">
            <div class="row">
              <div class="col l6 s12">
                <h5 class="white-text">Footer Content</h5>
                <p class="grey-text text-lighten-4">You can use rows and columns here to organize your footer content.</p>
              </div>
              <div class="col l4 offset-l2 s12">
                <h5 class="white-text">Links</h5>
                <ul>
                  <li><a class="grey-text text-lighten-3" href="#!">Link 1</a></li>
                  <li><a class="grey-text text-lighten-3" href="#!">Link 2</a></li>
                  <li><a class="grey-text text-lighten-3" href="#!">Link 3</a></li>
                  <li><a class="grey-text text-lighten-3" href="#!">Link 4</a></li>
                </ul>
              </div>
            </div>
          </div>
          <div class="footer-copyright">
            <div class="container">
            © 2014 Copyright Text
            <a class="grey-text text-lighten-4 right" href="#!">More Links</a>
            </div>
          </div>
    </footer>
    <script type="text/javascript">
    	$('#submit').click(function()
		{
		    $.ajax({
		        url: test.php,
		        type:'POST',
		        data:
		        {
		            // The key is 'mobile'. This will be the same key in $_POST[] that holds the mobile number value.
		            mobile: $('#mobile').val()
		        },
		        success: function(msg)
		        {
		            $("#check").html(data);
		        }               
		    });
		});
    </script>
</body>
</html>