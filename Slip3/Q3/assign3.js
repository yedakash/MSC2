function ValidateEmail()
{
var mailformat = document.getElementById('email').value;
var pattern=/^[a-zA-Z0-9._]+@[a-zA-Z0-9._]+\.[a-zA-Z]{2,3}$/;
// /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
if(pattern.test(mailformat))
{
    alert("welcome");
return true;
}
else
{
alert("You have entered an invalid email address!");
return false;
}
}