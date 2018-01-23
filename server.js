let PythonShell = require('python-shell');
let kill = require('tree-kill');
express = require('express'); //web server
app = express();
var childPid = null;

app.listen(8080, function () { //start the webserver on port 8080
  console.log("server running on port http://localhost:8080");
})

app.use(express.static('./public/')); //tell the server that ./public/ contains the static webpages

app.get('/start/:fileName', function(req, res) {  
  let fileName = req.params.fileName;

  if(childPid) {
    console.log("kill# ", childPid);
    kill(childPid);
  }

  var shell = PythonShell.run(`./python_scripts/${fileName}`, function (err,results) {
    console.log('results ',results);
    if (err) throw err;
    console.log('finished');
  });
  childPid = shell.childProcess.pid
  console.log("open: ", childPid);
});
