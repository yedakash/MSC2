var http=require('http');
var url= require('url');
var fs= require('fs');
http.createServer(function(req,res){

var p= url.parse(req.url,true);
var filename="."+p.pathname;
console.log('file received'+filename);
fs.readFile(filename,function(err,data){
    if(err)
    {
        res.writeHead(404,{'content-type':'text/html'});
        res.end('404 page Not found');
    }
    else
    {
        res.writeHead(200,{'content-type':'text/html'});
        res.write(data);
        res.end();

    }
});

}).listen(8000);
console.log('server is running on port 8000');