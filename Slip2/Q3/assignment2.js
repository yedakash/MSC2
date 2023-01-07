function validate()
{
    var fname=document.empform.fname.value;
    var lname=document.empform.lname.value;
    var dob=document.empform.dob.value;
    var jdate=document.empform.jdate.value;
    var salary=document.empform.salary.value;

    
    var NPattern = /^[a-zA-Z]+$/;
    var dobPattern= /^([0-9]{1,2})([-/.])+([0-9]{1,2})([-/.])+([0-9]{4})$/;
    var JdatePattern= /^([0-9]{2})-([0-9]{2})-([0-9]{4})$/;
    var salaryPattern=/^[0-9]+$/;
    
    if(!NPattern.test(fname)){
        alert('Please Enter valid FirstName');
        return false;
    }  
   
    if(!NPattern.test(lname)){
      alert('Please Enter valid LastName');
      return false;
    }  
 
    
    if (!dobPattern.test(dob)) {
        alert("Invalid date of birth");
        return false;
    }
    if (!JdatePattern.test(jdate)) {
        alert("Invalid date of Joining");
        return false;
    }
    if(salary=="")
    {
      alert("Salary Required");
      return false;
    }
    if(!salaryPattern.test(salary))
    {
      alert("Salary Must be in digits)");
      return false;
      }
     
    
}