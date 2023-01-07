function validate()                                    
{  
    var fname = document.RegForm.FName; 
    var lname = document.RegForm.LName;  
    var age =document.RegForm.Age;               
    var phone = document.RegForm.Telephone;  
    var what =  document.RegForm.Subject;  
    var address = document.RegForm.Address;  
  function allLetter()
{ 
var letters = /^[A-Za-z]+$/;
//if(letters.test(fname.value))
if(fname.value.match(letters))
{
    fname.focus();
    return true;
}
else{
fname.focus();
return false;
}
}
function allNumeric() 
 {
    var num= /^[0-9]{10}$/;
    if(num.test(phone.value))
    {
        phone.focus();
        return true;
    }
        else
        {
        return false;
    }
    
}  
if(!allLetter())
{
    alert('Username must have alphabet characters only');
 }
 if(!allNumeric())
 window.alert("Enter correct number");
    if(age.value < 18 || age.value > 50)
    { 
        
        window.alert("Please enter correct age."); 
        age.focus(); 
        return false; 
    }
   
   if (address.value == "")                               
    { 
        window.alert("Please enter your address."); 
        address.focus(); 
        return false; 
    } 
}