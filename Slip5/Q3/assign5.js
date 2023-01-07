function validateFile(){
    var file1= document.getElementById("file_1").value;
    var file2 = document.getElementById("'file_2").value;
var fs = require('fs');
    fs.open('file1', 'r+', function (err, fd) {
        if (err) { return console.error(err);     
       }

        var buffr = new Buffer.alloc(24); 
       fs.read(fd, buffr, 0, buffr.length, 0, function (err, bytes) {
            if (err) throw err;
           console.log(buffr.toString()); 
        }); 
        
fs.appendFile('file2', buffr, function (err) {
  if (err) throw err;
  console.log('Saved!');
  fs.close(fd, function (err) { if (err) throw err; }); 
});

});
    //});
}